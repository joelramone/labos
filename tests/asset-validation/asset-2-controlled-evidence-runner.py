"""Validation-only deterministic runner for LabOS ASSET-2 Phase C evidence."""

from __future__ import annotations

import hashlib
import json
import platform
import sys
from pathlib import Path
from typing import Any

import pandas as pd
import pydantic

import app.research.optimizer.grid_search as optimizer
from app.research.optimizer.grid_search import GridSearchConfig
from app.research.optimizer.leaderboard import LEADERBOARD_COLUMNS, write_leaderboard_csv
from app.research.simulation import BacktestResult, BacktestTrade, calculate_metrics
from app.research.strategies.base import BaseStrategy


EXPECTED_COMBINATIONS = [
    {"take_profit_pct": 0.01, "stop_loss_pct": 0.005},
    {"take_profit_pct": 0.01, "stop_loss_pct": 0.01},
    {"take_profit_pct": 0.02, "stop_loss_pct": 0.005},
    {"take_profit_pct": 0.02, "stop_loss_pct": 0.01},
]

EXPECTED_RANKED = [
    ({"take_profit_pct": 0.02, "stop_loss_pct": 0.005}, 2.0, 0.3),
    ({"take_profit_pct": 0.02, "stop_loss_pct": 0.01}, 2.0, 0.3),
    ({"take_profit_pct": 0.01, "stop_loss_pct": 0.01}, 2.0, 0.1),
    ({"take_profit_pct": 0.01, "stop_loss_pct": 0.005}, 1.5, 0.2),
]


class ControlledGridStrategy(BaseStrategy):
    """Accept the real parameter names while delegating execution to a fixture stub."""

    def __init__(self, take_profit_pct: float, stop_loss_pct: float) -> None:
        self.fixture_take_profit_pct = take_profit_pct
        self.fixture_stop_loss_pct = stop_loss_pct

    def generate_entries(self, df: pd.DataFrame) -> pd.Series:
        return pd.Series([index == 0 for index in range(len(df))], index=df.index)

    def generate_exits(self, df: pd.DataFrame) -> pd.Series:
        return pd.Series(False, index=df.index, dtype=bool)

    def name(self) -> str:
        return "controlled_grid_stub"


def expected_pair(strategy: ControlledGridStrategy) -> tuple[float, float]:
    key = (strategy.fixture_take_profit_pct, strategy.fixture_stop_loss_pct)
    mapping = {
        (0.01, 0.005): (1.5, 0.2),
        (0.01, 0.01): (2.0, 0.1),
        (0.02, 0.005): (2.0, 0.3),
        (0.02, 0.01): (2.0, 0.3),
    }
    return mapping[key]


def controlled_simulation(
    df: pd.DataFrame,
    strategy: ControlledGridStrategy,
    *args: Any,
    **kwargs: Any,
) -> BacktestResult:
    """Return two internally consistent trades with a predeclared PF/expectancy."""
    profit_factor, expectancy = expected_pair(strategy)
    loss = (2.0 * expectancy) / (profit_factor - 1.0)
    win = profit_factor * loss
    trades = [
        BacktestTrade(
            entry_index=0,
            exit_index=1,
            entry_timestamp="2026-01-01T00:00:00Z",
            exit_timestamp="2026-01-01T00:01:00Z",
            entry_price=100.0,
            exit_price=100.0 + win,
            notional=100.0,
            gross_pnl=win,
            fees=0.0,
            net_pnl=win,
            exit_reason="strategy_exit",
        ),
        BacktestTrade(
            entry_index=2,
            exit_index=3,
            entry_timestamp="2026-01-01T00:02:00Z",
            exit_timestamp="2026-01-01T00:03:00Z",
            entry_price=100.0,
            exit_price=100.0 - loss,
            notional=100.0,
            gross_pnl=-loss,
            fees=0.0,
            net_pnl=-loss,
            exit_reason="strategy_exit",
        ),
    ]
    return BacktestResult(trades=trades, metrics=calculate_metrics(trades))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(actual: float, expected: float, tolerance: float = 1e-12) -> None:
    assert abs(actual - expected) <= tolerance, (actual, expected)


def main() -> None:
    config_path = Path(sys.argv[1]).resolve()
    config = optimizer.load_grid_search_config(config_path)
    output_path = config.output.resolve()
    frame = pd.DataFrame(
        {
            "timestamp": ["2026-01-01T00:00:00Z"] * 4,
            "open": [100.0] * 4,
            "high": [101.0] * 4,
            "low": [99.0] * 4,
            "close": [100.0] * 4,
            "volume": [1.0] * 4,
        }
    )

    observed_combinations = optimizer.expand_parameter_grid(config.parameters)
    assert observed_combinations == EXPECTED_COMBINATIONS

    original_simulation = optimizer.simulate_strategy
    optimizer.simulate_strategy = controlled_simulation
    try:
        summary = optimizer.run_grid_search(
            df=frame,
            strategy_key=config.strategy,
            timeframe=config.timeframe,
            strategy_class=ControlledGridStrategy,
            parameter_grid=config.parameters,
            min_trades=config.min_trades,
        )
    finally:
        optimizer.simulate_strategy = original_simulation

    assert summary.evaluated_configurations == 4
    assert len(summary.ranked_results) == 4
    assert len(summary.leaderboard_rows) == 4
    for rank, (result, expected) in enumerate(zip(summary.ranked_results, EXPECTED_RANKED, strict=True), start=1):
        expected_parameters, expected_pf, expected_expectancy = expected
        assert result.parameters == expected_parameters
        close(result.metrics.profit_factor, expected_pf)
        close(result.metrics.expectancy, expected_expectancy)
        assert summary.leaderboard_rows[rank - 1].rank == rank
        assert summary.leaderboard_rows[rank - 1].parameters == expected_parameters
        close(summary.leaderboard_rows[rank - 1].profit_factor, expected_pf)
        close(summary.leaderboard_rows[rank - 1].expectancy, expected_expectancy)

    write_leaderboard_csv(summary.leaderboard_rows, output_path)
    with output_path.open(newline="", encoding="utf-8") as csv_file:
        header = csv_file.readline().strip().split(",")
        rows = [line for line in csv_file if line.strip()]
    assert header == LEADERBOARD_COLUMNS
    assert len(rows) == 4

    empty_config_failure: dict[str, str]
    try:
        GridSearchConfig(
            strategy="controlled_stub",
            data=Path("synthetic.csv"),
            output=Path("controlled.csv"),
            parameters={},
        )
    except pydantic.ValidationError as exc:
        empty_config_failure = {"classification": "EXPLICIT", "type": type(exc).__name__}
    else:
        raise AssertionError("empty parameter grid config was accepted")

    def failed_simulation(*args: Any, **kwargs: Any) -> BacktestResult:
        raise RuntimeError("controlled execution failure")

    optimizer.simulate_strategy = failed_simulation
    try:
        try:
            optimizer.run_grid_search(
                df=frame,
                strategy_key=config.strategy,
                timeframe=config.timeframe,
                strategy_class=ControlledGridStrategy,
                parameter_grid={"take_profit_pct": [0.01], "stop_loss_pct": [0.005]},
                min_trades=0,
            )
        except RuntimeError as exc:
            execution_failure = {"classification": "EXPLICIT_PROPAGATED", "message": str(exc)}
        else:
            raise AssertionError("controlled execution failure was swallowed")
    finally:
        optimizer.simulate_strategy = original_simulation

    observed = {
        "config_sha256": sha256(config_path),
        "evaluated_configurations": summary.evaluated_configurations,
        "expected_grid_match": True,
        "expected_ranking_match": True,
        "fixture_kind": "synthetic_in_memory_plus_real_config",
        "leaderboard_columns": len(LEADERBOARD_COLUMNS),
        "leaderboard_rows": len(summary.leaderboard_rows),
        "output_path": str(output_path),
        "output_sha256": sha256(output_path),
        "parameter_combinations": observed_combinations,
        "python": platform.python_version(),
        "pandas": pd.__version__,
        "pydantic": pydantic.__version__,
        "ranked": [
            {
                "parameters": result.parameters,
                "profit_factor": result.metrics.profit_factor,
                "expectancy": result.metrics.expectancy,
                "rank": index,
            }
            for index, result in enumerate(summary.ranked_results, start=1)
        ],
        "tie_behavior": "DETERMINISTIC_UNDOCUMENTED_TIE_BEHAVIOR",
        "empty_grid_failure": empty_config_failure,
        "execution_failure": execution_failure,
    }
    print(json.dumps(observed, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
