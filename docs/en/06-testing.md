# Automated testing as the trust infrastructure

AI-generated code should be assumed plausible, not correct. A strong test system is therefore not an optional cleanup phase; it is the main infrastructure that makes high implementation throughput usable.

## Use many test tools, not one test label

Different layers answer different questions:

| Layer | Main question | Typical evidence |
|---|---|---|
| Static analysis | Does the change violate types, lint rules, security patterns, or architectural constraints? | Compiler/linter/static-analysis report |
| Unit tests | Does a small function or object satisfy local rules and edge cases? | Fast deterministic test report |
| Property tests | Do invariants hold across generated input ranges? | Seeded runs and minimized counterexamples |
| Contract tests | Do services and clients agree on schemas, errors, and compatibility? | Provider/consumer contract result |
| Integration tests | Do real components work together with databases, queues, APIs, or devices? | Environment-bound test report |
| End-to-end tests | Can a user or external system complete the critical workflow? | Browser/device trace, video, screenshots |
| Performance tests | Does the system meet latency, throughput, memory, battery, or resource budgets? | Benchmark and profile |
| Resilience tests | What happens under timeout, partial failure, disconnect, retry, or degraded dependency? | Fault-injection evidence |
| Acceptance tests | Does the result satisfy business and product expectations? | Signed criteria, reviewed artifacts |

## Tool examples

**pytest** is a natural default for Python unit, integration, regression, property, and data-driven testing. It is especially effective when agents can run focused tests after each change and return the exact failing case.

**Playwright** exercises web applications in real browsers and produces traces, screenshots, videos, console output, network detail, and DOM state. These artifacts are highly useful to an agent diagnosing UI and flow failures.

**Maestro** describes mobile UI flows in readable YAML and can drive iOS and Android journeys. It is valuable when an agent writes a large amount of mobile UI code that a person cannot manually exercise across every state and device path.

Hardware and IoT projects should add simulators, protocol tests, hardware-in-the-loop runs, network fault tests, command authorization tests, and physical safety checks.

## Tests must be independent

The test system must not merely encode the same assumption as the implementation. Strong oracles come from:

- explicit requirement examples;
- business invariants;
- trusted historical outputs;
- golden datasets reviewed by domain experts;
- differential comparison with another implementation;
- metamorphic or property relations;
- real-device, real-browser, or real-service behavior;
- deliberately adversarial cases;
- production telemetry replay after privacy review.

A separate agent can generate tests, but agent separation alone is insufficient if both agents receive the same incomplete specification. The source of truth must be independently grounded.

## Test the tests

Agents sometimes weaken assertions, remove difficult cases, broaden tolerances, mock away the real behavior, or change acceptance criteria in order to make a test suite pass. Guard against this by:

- reviewing assertion changes separately from implementation changes;
- requiring a failing test before the fix for defects;
- using mutation testing where practical;
- preserving golden cases and locked invariants;
- preventing implementation tasks from editing acceptance criteria without approval;
- reporting skipped, flaky, quarantined, or unexecuted tests explicitly;
- storing failure artifacts, not only a green summary.

## A completion claim needs an evidence bundle

“Done” should mean more than “tests passed.” A useful evidence bundle may contain:

- exact source revision;
- requirement and plan links;
- static and unit results;
- integration and end-to-end results;
- screenshots, videos, traces, or hardware logs;
- performance comparison against budget;
- migration and rollback result;
- known gaps and accepted residual risk;
- reviewer and human approval for the risk class.

## Keep the suite economically healthy

More tests are not automatically better. Tests can become over-designed, flaky, slow, coupled to implementation detail, or expensive to maintain. Measure detection value, execution time, stability, and diagnosis quality. Delete or redesign tests that produce noise without protecting behavior.
