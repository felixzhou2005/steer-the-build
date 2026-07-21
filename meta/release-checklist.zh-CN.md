# 发布检查表

## 内容完整性

- [ ] 所有修改结论都有明确证据层级。
- [ ] 项目指标已实测、有来源，或明确标为估计。
- [ ] 没有暴露客户、用户、凭据、Endpoint 或私有数据细节。
- [ ] 中英文状态已记录。
- [ ] 相关工作和工具版本敏感结论已复核。
- [ ] 案例明确区分事实、解释和未知项。

## 仓库质量

- [ ] `python scripts/check_links.py` 通过。
- [ ] `python scripts/check_bilingual.py` 通过。
- [ ] `python scripts/prepare_site.py && mkdocs build --strict` 通过。
- [ ] 发布 Commit 上的 GitHub Actions 通过。
- [ ] 已人工审查占位符，而不是机械清空。
- [ ] `CHANGELOG.md`、`CITATION.cff` 和版本号已更新。

## 治理

- [ ] 安全敏感贡献在必要时经过私下 Review。
- [ ] 贡献者署名正确。
- [ ] 文字与可复用资产之间的许可证边界保持清楚。
- [ ] 模板或 Skill 契约的破坏性变化已说明。

## 发布

- [ ] 创建签名或 annotated Tag `vX.Y.Z`。
- [ ] 从 Changelog 生成 Release Notes。
- [ ] 部署后检查 GitHub Pages。
- [ ] 路径变化时更新 LinkedIn 排期中的深层链接。
- [ ] 建立 Release Discussion 收集反馈和反例。
