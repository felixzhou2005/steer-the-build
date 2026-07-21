# Glossary

## AI coding agent

A model-driven tool that can inspect a repository, edit multiple files, invoke tools, run commands, and iterate on implementation. The term includes local coding agents and agentic IDE workflows; it does not imply unrestricted autonomy.

## AI-native review

A review process in which AI performs systematic analysis across architecture, requirements, behavior, code, security, performance, and runtime evidence. Human attention is allocated by risk rather than by exhaustive line count.

## AI-readable observability

Logs, traces, metrics, events, and diagnostic artifacts designed so both humans and agents can correlate and retrieve the evidence behind system behavior.

## Control plane

The human-owned artifacts and policies that define intent, constraints, architecture, risk, acceptance, and authority. In this guide, the control plane is primarily textual and version-controlled.

## Evidence plane

The tests, logs, traces, metrics, benchmarks, snapshots, review reports, and runtime observations used to determine whether a system meets its declared requirements.

## First divergence

The earliest observable point at which actual behavior differs from the expected causal chain. Finding it is often more useful than repeatedly patching the final symptom.

## Human-in-control

Humans retain ownership of goals, important trade-offs, risk thresholds, release authority, and consequences. AI may have substantial execution autonomy inside explicitly approved boundaries.

## Independent verification

Validation whose oracle or evidence is not derived solely from the implementation agent's assumptions. Examples include business invariants, golden datasets, differential testing, real-device flows, and independently authored acceptance examples.

## Project AI constitution

A version-controlled set of project-wide rules covering architecture, coding, security, testing, observability, operations, and completion criteria for every agent task.

## Skill

A reusable, versioned instruction package for an agent. A useful skill has a scope, trigger, rules, output contract, verification method, exceptions, and examples—not merely a prompt paragraph.

## Skill hierarchy

The layers through which rules are composed: foundational principles, domain skills, project-specific constraints, and task-level instructions. Narrower layers may specialize but should not silently violate higher-risk foundational rules.

## Software sense

The accumulated ability to recognize useful abstractions, failure patterns, maintainability risks, product trade-offs, and operational consequences before they are fully explicit. AI can amplify this sense but does not automatically give it to a novice.
