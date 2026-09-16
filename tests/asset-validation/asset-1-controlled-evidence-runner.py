"""Validation-only deterministic runner for LabOS ASSET-1 Phase C evidence."""

from __future__ import annotations

import hashlib
import json
import platform
import sys
from pathlib import Path

import pandas as pd
import pydantic

from app.research.backtester import load_ohlcv_csv
from app.research.simulation import simulate_strategy
from app.research.strategies.base import BaseStrategy


EXPECTED = {
    "signals": 1,
    "entries": 1,
    "exits": 1,
    "position_count": 1,
    "entry_price": 100.0,
    "exit_price": 101.0,
    "gross_pnl": 1.0,
    "fees": 0.0804,
    "net_pnl": 0.9196,
    "wins": 1,
    "losses": 0,
    "final_equity": 0.9196,
    "win_rate": 1.0,
    "expectancy": 0.9196,
    "average_win": 0.9196,
    "average_loss": 0.0,
    "max_drawdown": 0.0,
    "exit_reason": "take_profit",
}


class ControlledStrategy(BaseStrategy):
    """Enter once at row zero and use fixed, manually-derived exit limits."""

    def take_profit_pct(self) -> float:
        return 0.01

    def stop_loss_pct(self) -> float:
        return 0.005

    def max_holding_candles(self) -> int:
        return 2

    def generate_entries(self, df: pd.DataFrame) -> pd.Series:
        return pd.Series([index == 0 for index in range(len(df))], index=df.index)

    def generate_exits(self, df: pd.DataFrame) -> pd.Series:
        return pd.Series(False, index=df.index, dtype=bool)

    def name(self) -> str:
        return "controlled_phase_c_stub"


def close(actual: float, expected: float, tolerance: float = 1e-12) -> None:
    assert abs(actual - expected) <= tolerance, (actual, expected)


def main() -> None:
    fixture_path = Path(sys.argv[1]).resolve()
    fixture_bytes = fixture_path.read_bytes()
    fixture_hash = hashlib.sha256(fixture_bytes).hexdigest()

    frame = load_ohlcv_csv(fixture_path)
    assert list(frame.columns) == ["timestamp", "open", "high", "low", "close", "volume"]
    assert len(frame) == 3

    result = simulate_strategy(frame, ControlledStrategy())
    assert len(result.trades) == EXPECTED["position_count"]
    trade = result.trades[0]
    metrics = result.metrics
    assert trade.entry_index == 0
    assert trade.exit_index == 1
    assert trade.exit_reason == EXPECTED["exit_reason"]
    close(trade.entry_price, EXPECTED["entry_price"])
    close(trade.exit_price, EXPECTED["exit_price"])
    close(trade.gross_pnl, EXPECTED["gross_pnl"])
    close(trade.fees, EXPECTED["fees"])
    close(trade.net_pnl, EXPECTED["net_pnl"])
    assert metrics.total_trades == 1
    assert metrics.wins == EXPECTED["wins"]
    assert metrics.losses == EXPECTED["losses"]
    close(metrics.win_rate, EXPECTED["win_rate"])
    close(metrics.gross_pnl, EXPECTED["gross_pnl"])
    close(metrics.estimated_fees, EXPECTED["fees"])
    close(metrics.net_pnl, EXPECTED["net_pnl"])
    close(metrics.expectancy, EXPECTED["expectancy"])
    close(metrics.average_win, EXPECTED["average_win"])
    close(metrics.average_loss, EXPECTED["average_loss"])
    close(metrics.max_drawdown, EXPECTED["max_drawdown"])

    missing_volume = frame.drop(columns=["volume"])
    missing_path = fixture_path.with_name("asset-1-controlled-fixture.missing-volume.tmp.csv")
    try:
        missing_volume.to_csv(missing_path, index=False)
        try:
            load_ohlcv_csv(missing_path)
        except ValueError as exc:
            missing_column = {"classification": "EXPLICIT", "message": str(exc)}
        else:
            raise AssertionError("missing volume was accepted")
    finally:
        missing_path.unlink(missing_ok=True)

    empty = frame.iloc[0:0]
    empty_result = simulate_strategy(empty, ControlledStrategy())
    assert empty_result.metrics.total_trades == 0
    empty_behavior = "GRACEFUL_AT_SIMULATOR_BOUNDARY"

    reverse_order = frame.iloc[::-1].reset_index(drop=True)
    reverse_result = simulate_strategy(reverse_order, ControlledStrategy())
    ordering_behavior = {
        "classification": "IMPLICIT",
        "loader_reorders": False,
        "simulator_uses_positional_order": True,
        "observed_trade_count": reverse_result.metrics.total_trades,
    }

    observed = {
        "fixture_sha256": fixture_hash,
        "fixture_rows": len(frame),
        "python": platform.python_version(),
        "pandas": pd.__version__,
        "pydantic": pydantic.__version__,
        "trade": trade.model_dump(mode="json"),
        "metrics": metrics.model_dump(mode="json"),
        "final_equity": metrics.net_pnl,
        "missing_column": missing_column,
        "empty_behavior": empty_behavior,
        "ordering_behavior": ordering_behavior,
        "expected_match": True,
        "temporary_file_cleanup": not missing_path.exists(),
    }
    print(json.dumps(observed, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
