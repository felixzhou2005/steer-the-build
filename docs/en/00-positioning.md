# Positioning

## What this is

Steer the Build is a practitioner-led method for building real software with coding agents while retaining human control over intent, architecture, algorithms, product quality, risk, evidence, and release decisions.

It grew out of nearly one year of intensive use of Claude, Codex, and ChatGPT Pro across business applications, mobile software, machine-learning systems, voice systems, IoT and hardware-adjacent work, cloud deployment, and reusable agent skills. A common workflow was to use a stronger general reasoning model for difficult research or algorithm design, then give the resulting approach and key code to a local coding agent for repository-aware review, adaptation, testing, and implementation.

Based on the maintainer's current cross-project estimate, the underlying practice produced more than 300,000 lines of AI-generated application code without the maintainer hand-writing that code. The counting method has not yet been independently audited, so the figure is a personal practice estimate rather than a benchmark or universal performance claim. Its importance is structural: once implementation volume exceeds what a person can read line by line, the engineering method must move from manual production and exhaustive inspection to explicit control, independent evidence, risk-based review, and runtime diagnosis.

## What this is not

This is not:

- a prompt collection;
- a comparison of which model is “best”;
- a claim that a non-technical person can automatically build any complex system;
- a proposal to remove humans from architecture, algorithms, design, production, or accountability;
- a rejection of code review, testing, or standard software process;
- a promise that generated code is correct because an agent says it is done.

## The key distinction

“Not hand-writing code” does not mean “not doing engineering.” It shifts engineering effort upward:

- from typing syntax to defining complete intent;
- from local implementation choices to system boundaries and trade-offs;
- from reading every line to reviewing architecture, behavior, evidence, and risk;
- from debugging by intuition to querying logs, traces, metrics, and controlled experiments;
- from one-off corrections to persistent tests, templates, and skills.

## Intended audience

The guide is most useful to experienced engineers, technical founders, architects, product-technical leaders, ML practitioners, and small teams using coding agents on systems that must remain maintainable. Beginners can still benefit, but AI does not manufacture software sense. A person who cannot recognize architectural drift, ambiguous requirements, weak tests, unsafe operations, or invalid algorithmic assumptions will have difficulty controlling a large generated system.

## Working definitions

**Coding agent**: an AI system that can inspect a repository, edit files, run commands, execute tests, and iterate on results.

**AI-native review**: review designed for code volume that exceeds exhaustive manual inspection. Agents analyze architecture, requirements coverage, implementation paths, security, performance, and evidence; humans own review questions, risk classification, sampling, exceptions, and release authority.

**Evidence**: an artifact that supports a claim about behavior. Examples include independent tests, traces, logs, metrics, benchmarks, screenshots, recordings, hardware results, migrations exercised in a disposable environment, and explicit acceptance records.

**Skill**: a versioned set of instructions, constraints, examples, anti-patterns, and validation rules that makes a repeated engineering preference executable by an agent.

## A scoped claim

The project makes a strong but bounded claim:

> It is possible to delegate nearly all coding actions in some complex projects, provided that the human control system becomes more complete, not less complete.

Whether that works in a particular environment depends on domain expertise, risk, tool access, testability, data, architecture, and the cost of failure. High-stakes systems require stronger controls and may retain direct human implementation or inspection in critical areas.
