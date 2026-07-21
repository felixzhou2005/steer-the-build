# Architecture and plan-before-code

## Humans lead architecture

Coding agents are strong at familiar patterns. They can draft service boundaries, common API structures, CRUD data models, deployment layouts, and standard mobile or web architecture. Their weaknesses become visible when the system has unusual constraints, competing non-functional goals, long-term migration concerns, expensive failure modes, or domain knowledge absent from the repository.

Architecture therefore remains a human-owned decision process. AI should widen the option space and make trade-offs explicit, not silently choose the system's future.

Human control is especially important for:

- choosing a database or storage model based on real access patterns rather than popularity;
- deciding when denormalization, a wide table, redundancy, or precomputation is justified for performance;
- defining transaction boundaries and consistency expectations;
- separating device, edge, cloud, AI, and safety responsibilities in IoT;
- selecting an ML model family, evaluation method, and fallback;
- determining tenancy, isolation, secrets, and trust boundaries;
- deciding which parts must remain simple even if a generic architecture looks more extensible.

## Product and visual design

AI can generate a competent, conventional Figma design and can implement a functional module layout. It does not reliably create a distinctive visual identity, emotional theme, or artistic coherence without human direction and refinement.

Use AI for:

- component inventories;
- state coverage;
- screen flows;
- accessibility and responsive checks;
- translating approved Figma structures into code.

Use humans for:

- visual theme and hierarchy;
- brand and emotional tone;
- deciding what should feel simple, premium, playful, trustworthy, or calm;
- recognizing when a screen is technically complete but lacks a soul.

When Figma is the source of truth, use a dedicated fidelity skill: require exact component, spacing, typography, color, state, and responsive matching; prohibit “creative improvement” unless explicitly approved; and validate with screenshots or visual comparison.

## The plan gate

Never begin a meaningful implementation with “go build it.” First ask the agent for a detailed plan.

A good implementation plan states:

1. the requirement and acceptance criteria being addressed;
2. current repository behavior and relevant files;
3. the proposed design and why it fits the approved architecture;
4. interfaces, schemas, and state transitions that change;
5. migration and backward-compatibility impact;
6. failure and security considerations;
7. tests and evidence to add;
8. observability changes;
9. documentation updates;
10. rollback or safe abort path;
11. explicit non-goals and files that must not change.

The human reviews the plan, asks for alternatives where needed, and iterates until the approach is acceptable. Only then does the agent implement.

This is one of the strongest controls against black-box code generation. The reviewer can understand and correct a structured proposal without reading every implementation detail. It also forces the agent to retrieve repository context before editing.

## Decompose aggressively

Do not give an agent an entire large design and expect a coherent implementation in one step. Long instructions, many moving boundaries, and delayed validation cause context loss and hidden interactions.

A well-sized task:

- answers one primary engineering question;
- has a bounded file and module surface;
- preserves stable interfaces unless the task is explicitly about changing them;
- can be tested immediately;
- produces a reviewable diff and evidence package;
- can be reverted independently.

Early signals that a task is too large include:

- the plan contains multiple unrelated migrations or features;
- the agent starts “cleaning up” neighboring modules;
- tests are postponed until the end;
- requirements are being reinterpreted during implementation;
- the agent repeatedly re-reads broad parts of the repository without converging;
- a failure cannot be isolated to one change.

## Separation of concerns in the workflow

Separate product design, UI design, architecture, implementation, and verification. For example, do not ask an agent to invent a complete UI and implement it in the same task. Establish the user flow and Figma source first, review them, then implement a bounded screen or component set. The same principle applies to API contracts, database schemas, and algorithms.
