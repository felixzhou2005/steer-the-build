# Risk, governance, and anti-patterns

A fast implementation system can accelerate value or accelerate failure. Risk must be designed into the method rather than added after code exists.

## Priority-zero controls

### Product value and requirement validation

Before scaling implementation, verify that the problem exists, that the user and workflow are understood, and that the proposed system changes the desired outcome. Track assumptions and define stop conditions. AI can make an invalid product direction look impressively complete.

### Security, privacy, and compliance

Define data classes, access, consent, retention, deletion, encryption, audit, residency, and incident obligations. Review agent access to repositories, credentials, logs, customer data, browser sessions, devices, and cloud environments. Treat third-party skills and plugins as executable code.

Projects involving scraping, lead generation, automated posting, phone calls, orders, property valuation, and IoT require special attention to platform terms, lawful basis, consent, identity, dangerous actions, human escalation, and disclosure.

### Release, migration, rollback, and incident response

Every high-impact change needs a rollout and recovery plan. Test migrations and rollback. Define blast radius, ownership, monitoring, and emergency stop. Do not let an agent infer production authority from development access.

### Dependencies, supply chain, and licensing

Agents can add packages casually. Require justification, source and maintenance review, license compatibility, version pinning, vulnerability scanning, and a removal plan. For skills and plugins, review instructions, scripts, network access, and secret handling.

### Independent and realistic tests

Prevent the implementer from defining its own truth. Use business invariants, trusted examples, real environments, adversarial cases, separate reviewers, and immutable acceptance criteria.

### Change control and version management

Large generated diffs hide scope expansion. Use small branches, bounded tasks, clean commits, protected main, reviewable artifacts, and explicit document changes. Multiple agents must not modify the same boundary without coordination.

### Maintainability and knowledge ownership

A system is not maintainable merely because an agent can explain it today. Preserve architecture, semantic data documentation, runbooks, tests, and human understanding. Track whether the team can diagnose and recover when a favored model or tool is unavailable.

### End-to-end economics

Measure more than generated lines and apparent speed:

- time from requirement to accepted behavior;
- human attention and coordination time;
- first-pass acceptance and rework;
- escaped defects and rollback;
- mean time to diagnose and recover;
- model, infrastructure, test, and observability cost;
- maintenance effort after one and three months;
- business outcome and adoption.

## Priority-one operating system

As the practice grows, add:

- responsibility mapping for human and AI roles;
- risk-based autonomy levels;
- approved model/tool and data-access policy;
- skill ownership and deprecation;
- documentation freshness controls;
- incident and exception review;
- training for architecture, testing, product, and operations;
- metrics that prevent speed from hiding quality loss.

## Common anti-patterns

| Anti-pattern | Why it fails | Corrective control |
|---|---|---|
| Idea directly to code | Ambiguity becomes structure and later rework | Requirements and plan gate |
| One giant task | Context loss, mixed concerns, delayed feedback | Small independently testable changes |
| Agent chooses the architecture | Generic or over-designed decisions become hard to reverse | Human-led trade-off and ADR |
| Same agent implements and proves | Shared mistake passes shared tests | Independent oracle and reviewer |
| Infinite retry loop | Random edits, weakened assertions, topic drift | Stop condition and reverse diagnosis |
| More logging without design | High cost and low signal | Stable events, correlation, reason codes, retention |
| Skill as a long prompt | No trigger, test, version, or conflict control | Formal skill schema and governance |
| Unrestricted AI operations | High blast radius and weak accountability | Environment and permission tiers |
| Custom feature per customer fork | Short-term delivery creates long-term fragmentation | Configuration, extension points, product-line architecture |
| Productivity measured by lines | Rewards output, not value or reliability | End-to-end outcome metrics |

## Risk-based autonomy

Autonomy should vary by action, not by enthusiasm for a tool.

- **Low risk**: documentation formatting, local analysis, disposable environment setup, focused test generation. Agents may act and report.
- **Medium risk**: bounded code changes, dependency updates, migrations in test, cloud changes in a sandbox. Require plan and automated gates.
- **High risk**: permissions, money, customer communication, data deletion, physical device control, production migration. Require human approval, deterministic procedures, rollback, and audit.
- **Prohibited by default**: exposing secrets, bypassing controls, deleting unbacked-up data, contacting people without approved policy, executing dangerous physical commands, or expanding production access.
