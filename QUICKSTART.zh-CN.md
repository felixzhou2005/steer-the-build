# 快速开始

## 用这个下载包创建 GitHub 仓库

1. 创建一个名为 `steer-the-build` 的 **Public 空仓库**。
2. 不要初始化 README、`.gitignore` 或 License。
3. 解压下载包，进入 `steer-the-build` 目录。
4. 核对已经配置的仓库地址，再补充公开作者和维护者信息。
5. 验证并 Push：

```bash
python scripts/check_links.py
python scripts/check_bilingual.py
python -m pip install -r requirements-docs.txt
python scripts/prepare_site.py
mkdocs build --strict

git init
git add .
git commit -m "docs: launch Steer the Build v0.1.0"
git branch -M main
git remote add origin git@github.com:<YOUR_GITHUB_USERNAME>/steer-the-build.git
git push -u origin main
```

6. 按[建仓后检查表](meta/post-create-checklist.zh-CN.md)完成设置。

## 在另一个软件项目中使用方法

优先复制：

- `templates/zh-CN/project-ai-constitution.md`
- `templates/zh-CN/product-requirements.md`
- `templates/zh-CN/architecture-design.md`
- `templates/zh-CN/implementation-plan.md`
- `templates/zh-CN/test-strategy.md`
- `templates/zh-CN/observability-spec.md`
- `templates/zh-CN/skill-spec.md`，用于把已经重复验证的经验整理成 Skill
