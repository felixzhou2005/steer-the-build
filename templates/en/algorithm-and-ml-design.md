# Algorithm and ML design

> Problem / model:  
> Human algorithm owner:  
> Status: Research / Proposed / Approved / Experiment / Production  
> Data snapshot:  
> Last reviewed:

## 1. Decision problem

State the real decision or prediction, who acts on it, the cost of different errors, and why an algorithm is needed. Do not begin with a preferred model.

## 2. Output contract

- Output and unit:
- Confidence or uncertainty representation:
- Explanation requirement:
- Validity window:
- Human override / appeal:
- Abstention and fallback behavior:
- Actions the output is not permitted to trigger automatically:

## 3. Baseline

Define the simplest useful baseline: rule, average, existing workflow, linear model, prior system, or human process.

| Baseline | Metric | Result | Cost / latency | Limitation |
|---|---|---:|---:|---|
| | | | | |

A complex model must outperform a relevant baseline on the dimensions that matter, not only on one aggregate metric.

## 4. Data design

- Sources, ownership, and collection period:
- Label definition and who/what produced it:
- Leakage risks:
- Missingness and selection bias:
- Temporal and geographic representativeness:
- Train/validation/test split rationale:
- Privacy and retention:
- Golden cases and known hard slices:

## 5. Evaluation design

| Metric | Why it matters | Target | Slice | Decision threshold |
|---|---|---:|---|---:|
| | | | | |

Include error distribution and business cost, not only averages. Define segment, time, location, device, language, or property-type slices that can hide failure.

## 6. Candidate approaches

| Approach | Assumptions | Advantages | Risks | Compute / latency | Evidence |
|---|---|---|---|---|---|
| | | | | | |

Record the human reasoning behind selection. AI may research papers and compare options, but it does not own the final problem framing, evaluation standard, or trade-off.

## 7. Experiment plan

- Hypothesis:
- Fixed data/version/configuration:
- Variables changed:
- Repetition and statistical uncertainty:
- Ablation or sensitivity analysis:
- Stopping rule:
- Artifact and result registry:

## 8. Error analysis and reverse diagnosis

When a result is wrong:

1. preserve the exact input, model/data/config versions, and output;
2. decompose the pipeline into observable stages;
3. identify the first stage whose intermediate result diverges from expectation;
4. compare competing hypotheses: data, label, preprocessing, feature, model, threshold, integration, or metric;
5. run the smallest discriminating experiment;
6. update the design before broad retraining or repeated code changes.

Maintain an error taxonomy and representative examples.

## 9. Production architecture

- Online/offline flow:
- Feature or input consistency:
- Model registry and versioning:
- Serving latency and capacity:
- Fallback and rollback:
- Shadow/canary strategy:
- Monitoring and alerting:
- Feedback-loop risks:

## 10. Monitoring

- Input/data drift:
- Output distribution:
- Accuracy proxy and delayed ground truth:
- Slice performance:
- Confidence/abstention rate:
- Business outcome and harmful error rate:
- Model, prompt, feature, and data version correlation:

## 11. Model card summary

Document intended use, out-of-scope use, training/evaluation data, metrics, limitations, ethical/privacy considerations, and responsible owner.

## 12. Approval gates

- Problem framing approved by:
- Data/label review:
- Evaluation design review:
- Production risk review:
- Release criteria:
- Revisit date:
