# 翻译指南

## 原则

中英文是同一方法的两个持续维护版本，不是永久机械同步的镜像。翻译必须保留结论、证据层级、边界和结构，同时根据读者调整表达。

## 源版本追踪

每次翻译修改：

- 标明源文件和源 commit；
- 更新 `content-status.md` 中的状态；
- 在可行时保持标题稳定，使深层链接可比较；
- 在 Pull Request 中记录有意省略或适配的地方。

## 需要保持稳定的术语

| English | 中文 |
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

## Review 检查

- [ ] 翻译没有加强原文结论。
- [ ] 个人经验仍明确是个人经验。
- [ ] 安全和边界说明完整保留。
- [ ] 数字、单位和状态一致。
- [ ] 有对应语言页面时，链接指向正确版本。
- [ ] 代码、路径、标识符和工具名技术上正确。
- [ ] 译文符合本地语言表达，而不是照搬语序。
