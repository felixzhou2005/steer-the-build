# AI-readable observability and reverse diagnosis

## Observability is a design requirement

Large AI-generated systems contain more code than a person can memorize. When behavior is wrong, reading the entire implementation is neither necessary nor efficient. The system should expose enough structured runtime evidence for a human and an agent to reconstruct what happened.

Observability includes logs, traces, metrics, profiles, model and data versions, events, and diagnostic tools. “Write many logs” is not sufficient. Logs must be searchable, correlated, privacy-aware, and connected to decisions.

## Design telemetry for retrieval

Useful correlation fields include:

- `request_id` and `trace_id`;
- anonymized user, tenant, session, order, device, or job identifier;
- service, module, operation, and state;
- model, prompt, data, configuration, and skill versions;
- prior and next state for important transitions;
- external dependency, latency, status, and retry reason;
- decision outcome and reason code;
- fallback, degradation, or circuit-breaker path;
- error category, severity, and candidate root-cause domain;
- source revision and deployment version.

Prefer structured events with stable names and fields over unstructured paragraphs. Record the reason for important decisions, not only the result. A message such as “lead rejected” is far less useful than an event containing the scoring inputs, threshold version, rule path, and redacted reason codes.

## Protect privacy and cost

Observability can become a security and privacy problem. Do not log secrets, raw credentials, unnecessary personal data, complete phone recordings, unrestricted prompts, or customer content by default. Define redaction, sampling, retention, access, and deletion rules. High-volume logging also has performance and financial cost; every event should support an operational or diagnostic question.

## Reverse diagnosis from result to first divergence

Complex algorithms and distributed workflows often fail as a large final result: an estimate is implausible, a translated call loses meaning, an order does not synchronize, or a device ends in the wrong state. Repeatedly asking an agent to “fix the result” encourages random changes.

Use a reverse diagnostic method:

1. Freeze the input, source revision, model/data/config versions, and environment.
2. Describe the expected result precisely.
3. Break the final result into smaller observable stages.
4. Compare expected and actual values at each stage.
5. Find the earliest stage where they diverge.
6. Ask the agent to explain the exact code, data, state, and external calls that produce that stage.
7. Form a small set of competing hypotheses.
8. Design the cheapest discriminating experiment or additional instrumentation.
9. Fix the root cause, add a regression test, and update the relevant document or skill.

For ML, the stages may be data selection, feature computation, normalization, model input, inference, calibration, post-processing, and business rule application. For a voice system, they may be audio capture, segmentation, ASR, language detection, translation, intent recognition, action, and confirmation.

## Stop blind retries

A coding agent can enter a dead end when it repeatedly modifies code, reruns the same weak test, invents new explanations, or drifts away from the original requirement. Continuing the loop can make the system harder to understand.

Stop and reset when:

- the same failure survives several materially different attempts;
- the agent cannot state which hypothesis the latest change tests;
- acceptance criteria or assertions are being weakened;
- unrelated files and abstractions expand;
- the explanation changes without new evidence;
- the agent no longer references the original requirement or frozen input;
- the result improves locally but regresses another invariant;
- no new telemetry or experiment is produced.

A reset means returning to the last known-good revision, restating the problem, reducing the test case, adding observability, and possibly using a fresh model or reviewer context. Do not preserve a long conversation's accidental assumptions merely because time has already been spent.

## A diagnostic record

For every significant failure, capture:

- symptom and impact;
- exact input and environment;
- expected versus actual result;
- timeline and correlated identifiers;
- first divergent stage;
- hypotheses considered and evidence for/against each;
- root cause;
- code, data, test, document, and skill changes;
- how recurrence will be detected earlier.

This record becomes both human knowledge and high-quality context for future agents.
