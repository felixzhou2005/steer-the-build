# GitHub 建仓后检查表

## 创建仓库

- Repository name：`steer-the-build`
- Description：`A bilingual, open field guide for human-controlled, evidence-driven AI software engineering at scale.`
- Visibility：Public
- Initialize with README：**不要勾选**
- Add `.gitignore`：**不要选择**
- 通过 GitHub 表单添加 License：**不要选择**

下载包中已经包含这些文件。

## 第一次 Push 前的仓库专属信息

- `CITATION.cff`、`mkdocs.yml` 和 Issue 模板配置中的用户名与 URL 已配置为 `felixzhou2005`
- `CITATION.cff` 和 `AUTHORS.md` 中的公开维护者身份已配置为 `Felix Hui Zhou`
- Social 草稿继续保留在本地，不进入公开 v0.1
- `SECURITY.md` 中可选的维护者联系方式

每次发布前，都应在 Git 暂存内容导出的公开副本中检查意外占位符和私有信息。案例证据占位符继续保留在本地，直到真实证据可以公开。

## 仓库设置

启用：

- Issues
- Discussions
- Preserve this repository（首次发布以后可选）
- GitHub Pages → Source: GitHub Actions

建议 Topics：

```text
ai-coding
software-engineering
coding-agents
codex
claude-code
agentic-engineering
testing
observability
ai-code-review
spec-driven-development
human-in-the-loop
bilingual
```

## Label

建立：

- `case-study`
- `experience-report`
- `skill-proposal`
- `content-gap`
- `related-work`
- `translation`
- `evidence-needed`
- `security`
- `good-first-contribution`
- `counterexample`

## `main` 分支保护

建议最低设置：

- 合并前必须 Pull Request；
- 必须通过文档质量 Workflow；
- 必须解决 Review 对话；
- 禁止 Force Push 和删除；
- 只有全部维护者能支持时才要求签名 Commit；
- 初始配置阶段保留管理员通道，稳定后再收紧。

## 首次 Release

- Tag：`v0.1.0`
- Title：`Steer the Build v0.1 — Initial field guide`
- Word 母稿可以作为可选 Release 附件，但 Markdown 仍是规范源。
- 明确说明具体项目的案例证据仍在补充。
- 建立一个 GitHub Discussion，邀请案例、反例和失败经验。

## Social Preview

仓库上线后制作 1280×640 预览图，只放：

- Steer the Build
- AI builds. Humans steer. Evidence decides.
- Human-Controlled, Evidence-Driven AI Software Engineering

不要使用具体模型 Logo，保持工具无关。
