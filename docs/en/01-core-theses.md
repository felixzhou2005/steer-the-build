# Fifteen core theses

1. **AI coding is a reconstruction of engineering roles.** The main benefit is not faster typing. It moves human value toward problem definition, architecture, constraints, validation, and learning.

2. **The complete project lifecycle still matters.** Requirements, design, implementation, testing, release, operations, and retrospective cannot be skipped. AI amplifies good process and bad process alike.

3. **Humans remain accountable for architecture.** Agents can generate options and analyze trade-offs, but they do not carry long-term business context, organizational responsibility, or the consequences of failure.

4. **Review the plan before permitting implementation.** Every meaningful task should first produce an implementation plan, impact analysis, interfaces, risks, and tests. Correcting a plan is cheaper than repairing a generated structure.

5. **Large requests must be decomposed into small, independently verifiable changes.** A task should solve one primary engineering problem, touch a bounded area, and have an observable completion condition.

6. **Tests, logs, traces, and metrics become the primary trust mechanism.** At large code volume, confidence must come from evidence and layered review, not familiarity with every line.

7. **AI-generated systems need deliberate performance governance.** Over-design, redundant fallbacks, complex SQL, repeated transformation, unnecessary abstraction, and accidental network or memory costs are common unless constrained and measured.

8. **Humans control the direction and evaluation of complex algorithms.** AI can search, summarize, compare, derive, and implement. Humans must own the objective, assumptions, data, baseline, error cost, experiment design, and deployment boundary.

9. **Skills turn personal engineering judgment into reusable execution.** Coding style, constraints, anti-patterns, validation, and exceptions should be versioned and tested rather than repeatedly re-explained.

10. **When results diverge, inspect the control system before patching code.** The defect may originate in requirements, architecture, data, plans, tests, observability, or a skill—not only in implementation.

11. **Review itself must scale with AI.** Independent agents can inspect cross-file behavior, boundaries, permissions, concurrency, SQL, performance, and failure paths. Humans focus on high-risk decisions, adversarial questions, and final responsibility.

12. **Documentation is the control plane and external memory.** AI understands the system through text and inspectable artifacts. Missing or stale documentation becomes context drift, inconsistent implementation, and rework.

13. **Observability must serve both humans and AI.** Structured logs, traces, metrics, model and skill versions, decision reasons, and diagnostic maps let an agent retrieve relevant evidence instead of guessing.

14. **Human value moves upward rather than disappearing.** Product taste, visual identity, non-standard architecture, algorithm selection, data modeling, technical judgment, and responsibility become more—not less—important.

15. **Lower implementation cost expands the software market.** Personalized and long-tail software that previously failed an ROI threshold becomes feasible, but teams must prevent customization from turning into unmaintainable forks.

## Operational summary

Humans answer:

- Why should this exist?
- What exactly must be true?
- What is out of scope?
- Which trade-off is acceptable?
- What evidence is sufficient?
- What can fail, and what happens then?
- Who owns the consequence?

AI can answer and execute:

- What options exist?
- What does the repository currently do?
- How can the approved design be implemented?
- Which tests, tools, and logs can verify it?
- Where does the observed execution first diverge?
- Which recurring lesson should become a skill?
