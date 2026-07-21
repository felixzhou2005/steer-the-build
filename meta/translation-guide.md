# Translation guide

## Principle

Chinese and English are two maintained editions of the same method, not a permanently machine-synchronized mirror. Preserve the claim, evidence level, boundary, and structure; adapt wording for the audience.

## Source tracking

For each translated change:

- identify the source file and source commit;
- update the corresponding status in `content-status.md`;
- keep headings stable where practical so links remain comparable;
- record intentional omissions or adaptations in the pull request.

## Terms that should stay consistent

| English | Chinese |
|---|---|
| control plane | 控制面 |
| execution plane | 执行面 |
| evidence plane | 证据面 |
| learning plane | 学习面 |
| AI-native review | AI 原生 Review |
| AI-readable observability | AI 可读可观察性 |
| first divergence | 第一个偏差点 |
| independent verification | 独立验证 |
| human-in-control | 人在控制中 / 以人为控制主体 |
| project AI constitution | 项目 AI 宪法 |
| skill | Skill（保留英文，首次出现可解释） |

## Review checklist

- [ ] No claim became stronger in translation.
- [ ] Personal experience is still marked as personal experience.
- [ ] Safety and boundary statements are preserved.
- [ ] Numbers, units, and status labels match.
- [ ] Links point to the correct language where available.
- [ ] Code, paths, identifiers, and tool names remain technically correct.
- [ ] The translation reads naturally rather than following source word order.
