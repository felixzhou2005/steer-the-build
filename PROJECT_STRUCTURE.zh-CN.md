# 仓库结构

```text
steer-the-build/
├── README.md / README.zh-CN.md       # 对外首页
├── QUICKSTART.md / QUICKSTART.zh-CN.md
├── docs/
│   ├── en/                           # 20 个英文方法章节
│   └── zh-CN/                        # 20 个中文章节和完整长文版
├── templates/
│   ├── en/                           # 20 个英文可执行模板
│   └── zh-CN/                        # 20 个对应中文模板
├── research/                         # 相关工作、差异化和术语
├── meta/                             # 编辑、翻译、维护和发布指南
├── scripts/                          # 链接、双语和网站构建验证
├── .github/
│   ├── ISSUE_TEMPLATE/               # 以证据为核心的贡献表单
│   └── workflows/                    # 质量检查和 GitHub Pages 部署
├── mkdocs.yml                        # 文档网站配置
├── requirements-docs.txt
├── CONTRIBUTING*.md
├── GOVERNANCE.md / CODE_OF_CONDUCT.md / SECURITY.md
├── ROADMAP.md / CHANGELOG.md / CITATION.cff
└── LICENSE / LICENSE-CODE / LICENSES.md
```

## 本地保留、后续发布的内容

`case-studies/`、`skills/` 和 `social/` 继续保留在维护者本地工作区，但有意不进入公开 v0.1。案例只有在完成脱敏证据后发布；Skill 只有在与实际使用版本一致并经过验证后发布；Social 草稿在对应公开内容稳定后再发布。

## 规范源原则

仓库中的 Markdown 是可编辑规范源。Word 和 PDF 可以作为 Release、演讲或离线阅读产物生成，但公开修改应先进入 Markdown，再生成其他格式。

## 内容演化闭环

```text
现场经验
  → 案例证据
  → 方法修订
  → 回归测试或质量门
  → Skill / 模板更新
  → 双语 Review
  → 版本发布
  → 聚焦的 LinkedIn 帖子
```

## 增加一个真实项目

1. 复制 `templates/en/case-study.md` 或 `templates/zh-CN/case-study.md`。
2. 区分已知事实、解释、指标和未知项。
3. 加入脱敏证据，而不只是功能清单。
4. 至少识别一项由人拥有的决定和一套由 AI 执行的工作。
5. 记录一个失败、第一个偏差点、修复，以及长期流程或 Skill 变化。
6. 把案例链接到对应方法章节，并在具备条件时链接到经过验证的 Skill。
