# Security and privacy review

> System / change:  
> Risk owner:  
> Reviewers:  
> Status: Draft / Approved / Rejected / Conditional  
> Data classification:

## 1. Assets and consequences

| Asset / capability | Why valuable | Unauthorized consequence | Integrity consequence | Availability consequence |
|---|---|---|---|---|
| | | | | |

Include customer data, credentials, recordings, model context, orders, device control, production commands, and tenant boundaries.

## 2. Actors and trust boundaries

- End users and administrators:
- Internal operators and developers:
- Agents, models, tools, skills, and plugins:
- External APIs and data providers:
- Devices and networks:
- Tenants and environments:

Draw data and command flows across each trust boundary.

## 3. Authorization model

- Authentication mechanism:
- Role/capability/object-level authorization:
- Tenant isolation:
- High-impact command confirmation:
- AI tool permissions and allowlists:
- Production approval boundary:
- Break-glass process and audit:

A model deciding that an action is useful is not authorization to execute it.

## 4. Abuse and failure cases

| Scenario | Preconditions | Detection | Prevention / containment | Residual risk |
|---|---|---|---|---|
| Prompt/tool injection | | | | |
| Cross-tenant access | | | | |
| Secret exfiltration | | | | |
| Unauthorized device/order/action | | | | |
| Malicious or compromised skill/plugin | | | | |
| Sensitive logging | | | | |
| Destructive operations | | | | |

## 5. Data lifecycle and privacy

- Collection purpose and minimum data:
- Consent/notice/contractual basis where applicable:
- Processing locations and subprocessors:
- Prompt, model, and training-data policy:
- Retention and deletion:
- User access/correction/deletion:
- Lower-environment masking:
- Logs, traces, recordings, and test artifacts:

## 6. Supply chain

- Dependency and image pinning:
- Vulnerability and license review:
- Skill/plugin source review:
- Installation/upgrade approval:
- Build provenance and artifact integrity:
- Secret scanning:

## 7. Environment and operations

| Environment | Agent authority | Human approval | Credentials | Network/filesystem limits | Audit |
|---|---|---|---|---|---|
| Development | | | | | |
| Test/staging | | | | | |
| Production | | | | | |

## 8. Verification

- Threat-model review:
- Static/dependency/secret scans:
- Authorization and tenant tests:
- Negative and abuse tests:
- Red-team or penetration test:
- Backup/restore and incident exercise:

## 9. Decision

- Blocking findings:
- Approved exceptions and expiry:
- Residual risk owner:
- Release conditions:
- Approval date:
