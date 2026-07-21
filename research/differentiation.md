# Differentiation and positioning

## The category

Steer the Build belongs to a broader category that may be described as **AI-native software engineering governance**: the methods used to preserve intent, quality, explainability, and accountability when agents perform a large share of implementation, review, testing, and development operations.

## The distinctive combination

No single component below should be treated as an isolated novelty claim. The project is differentiated by how the components work together:

1. **Scale-aware control.** The method starts from the practical condition that generated code volume may exceed what a person can reasonably read line by line.
2. **Documentation as a control plane.** Requirements, architecture, contracts, algorithms, UI specifications, plans, and acceptance criteria externalize the human reasoning process before implementation.
3. **Plan approval before execution.** Agents must propose a detailed implementation plan that can be corrected before code becomes a black box.
4. **AI-native multi-layer review.** AI analyzes architecture, functional coverage, cross-file implementation, security, performance, concurrency, and failure paths; humans review the highest-risk decisions and evidence.
5. **Independent evidence.** Test oracles come from requirements, invariants, real examples, golden data, differential behavior, devices, and production-like environments—not only from the same agent that wrote the code.
6. **AI-readable observability.** Logs, metrics, and traces are structured so that an agent can retrieve the evidence for one request, user, device, model, skill, or state transition.
7. **Reverse diagnosis.** When a complex result is wrong, the method seeks the first observable divergence and works backward rather than permitting uncontrolled retry loops.
8. **Defect-to-skill learning.** Repeated mistakes become versioned skills, regression tests, templates, and quality gates.
9. **Explicit human value.** Product taste, visual character, architecture trade-offs, algorithmic direction, technical selection, business value, and risk remain human-owned.
10. **Cross-domain proof.** The case program covers business software, mobile, machine learning, voice, IoT, hardware-adjacent systems, agent automation, and cloud service delivery.
11. **Controlled AI DevOps.** AI may exercise broad authority in development and test environments; production changes remain bounded by permissions, approvals, backups, rollback, and audit.
12. **Software economics.** The guide examines how lower implementation cost changes which customized systems become economically rational, without confusing lower coding cost with zero lifecycle cost.

## The primary reader

The primary reader is an experienced engineer, architect, technical founder, product-technical lead, or AI engineering leader who:

- is building more than a small prototype;
- delegates substantial implementation to agents;
- needs maintainable systems rather than one-time demos;
- cannot inspect all generated code manually;
- is prepared to own design, evidence, and consequences.

## Boundaries

This repository is not:

- a beginner tutorial for one programming language;
- a collection of “magic prompts”;
- a benchmark comparing Claude, Codex, or other agents;
- a declaration that humans should never read code;
- a production-autonomy recipe;
- a substitute for domain expertise or safety review.

## One-sentence positioning

> Steer the Build is a bilingual field guide for controlling large-scale AI-generated software through explicit intent, approved design, independent evidence, AI-native review, observable runtime behavior, and human accountability.
