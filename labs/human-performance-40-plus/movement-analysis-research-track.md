# Movement Analysis Research Track

## Working hypothesis

[Hipótesis] A smartphone camera may support useful technical observation, positive validation, comparison over time and understandable feedback for selected movements under controlled capture conditions.

[Decisión] Working names `Movement Analysis` and `Movement Coach` are not brands, Products or canonical Capabilities.

## First technical case

[Decisión] Snatch, clean, jerk, clean & jerk, variants and relevant auxiliaries form the first research case because they expose phase, implement and camera-angle questions. This does not assert they are the best commercial entry point.

## Observation responsibility matrix

The following is a research classification schema, not a conclusion:

| Class | Meaning | Example research target |
|---|---|---|
| Observable | Directly visible under a validated angle and capture condition | Foot contact or visible bar position in a frame |
| Estimable | Derived with uncertainty from visible landmarks over time | Approximate phase timing or 2D trajectory |
| Multi-view required | One view cannot resolve the variable responsibly | Out-of-plane motion or hidden joint relationship |
| Additional sensor required | Video lacks the physical quantity | Force, pressure or load distribution |
| Human review required | Automated confidence/risk insufficient | Ambiguous technical interpretation |
| Not responsible to assess | Claim exceeds evidence or safety boundary | Injury diagnosis or guaranteed safety |

## Research questions

1. What movements can be usefully analyzed with a conventional camera?
2. What technical errors can be identified reliably?
3. What correct components can be recognized?
4. What precision makes feedback useful?
5. When must the system abstain?
6. What camera angle and capture protocol are needed?
7. Is one camera sufficient for each target variable?
8. What roles can pose estimation and computer vision play?
9. How should occlusions be detected and handled?
10. How can bar, plates and joints be detected distinctly?
11. How should a movement be divided into phases?
12. How should uncertainty be represented to users and reviewers?
13. How can false or dangerous feedback be prevented?
14. What feedback requires human review?
15. How can technical improvement be measured longitudinally?
16. How can video be stored with privacy and consent?
17. What trade-offs exist between local and cloud analysis?
18. What latency is acceptable in the relevant training context?
19. What is a technically reasonable research MVP?
20. What evidence is required before claiming “corrects technique”?

## Halterofilia phase research model

[Hipótesis] Candidate phases include setup, first pull, transition, second pull/extension, turnover, receiving, recovery and completion. Clean and jerk may require separate linked phase models.

For each phase, research will evaluate:

- visible starting position;
- bar trajectory and bar-body relationship;
- extension and sequence timing;
- receiving position and depth;
- foot, hip and knee positions visible from the chosen view;
- approximate velocity under known frame rate;
- visible symmetry limits;
- overhead stability and completion;
- uncertainty, occlusion and camera-angle sensitivity.

[Decisión] None of these variables is declared measurable from one camera until validated.

## Positive validation model

Potential feedback categories to test:

- `preserve`: a component appears stable and technically useful;
- `improved`: a validated metric or observation improved versus a comparable attempt;
- `review`: a specific observable warrants attention;
- `insufficient_evidence`: capture or confidence does not support evaluation;
- `human_review`: question exceeds automated scope.

[Hipótesis] Positive, specific feedback may improve learning, motivation and adherence. It must be tested separately from generic praise.

## Future movement expansion

Squat, front squat, deadlift, bench press, overhead press, pull-ups, rows, lunges, kettlebell/dumbbell movements, push-ups, burpees, running drills and mobility exercises remain future research candidates. No implementation or feasibility conclusion exists.

## Technical evidence plan

1. Define a movement-specific question and prohibited claims.
2. Define capture angles, lighting, framing, clothing and equipment conditions.
3. Establish human reference protocol and inter-rater agreement.
4. Build an annotated evaluation sample only after consent/privacy approval.
5. Measure detection, phase segmentation, observation accuracy and abstention performance separately.
6. Report performance by condition and failure mode, not only aggregate accuracy.
7. Run comprehension and behavior tests for feedback wording.
8. Require safety review before any user-facing corrective claim.

## Minimum responsible technical scope hypothesis

[Hipótesis] A first research MVP may be narrower than “technique correction”: guided capture of one movement from one validated angle, phase visualization, a few high-confidence observations, positive validation, comparison with the user's prior attempt and explicit abstention. Technology selection is deferred.

