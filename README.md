# Task Pilot / 任务总控

`task-pilot` 是一个长期通用任务控制 Skill。它不替代专业工作流，而是负责：

- 识别并遵循用户当前指定的 Workflow / Skill / 项目规则；
- 在没有更具体流程时提供最小必要的通用任务处理；
- 控制关键未知、执行范围和已有成果继承；
- 防止重复实现、无关重构、擅自扩范围和未验证完成；
- 在任务结束时同时检查“漏做”和“多做”。

## 核心原则

> 用户决定做什么；专业流程决定具体怎么做；Task Pilot 负责找到正确路径、守住边界并确认真正完成。

## 使用方式

平时直接正常描述任务即可。兼容自动 Skill 匹配的 Agent 可以隐式调用它。

需要明确调用时：

- `用任务总控处理这个任务：...`
- `用任务总控检查当前状态并继续未完成内容。`
- `用任务总控做最终验收，不要扩大任务范围。`
- `用任务总控检查方案，但不要执行。`

Task Pilot 的自动判断只负责路由和执行深度，不负责改变目标或扩大范围。

## 目录

- `skills/task-pilot/SKILL.md`：核心入口、优先级、路由和停止条件。
- `skills/task-pilot/references/`：按需加载的详细规则。
- `skills/task-pilot/templates/`：仅在需要时使用的决策和交接模板。
- `tests/scenarios/`：回归场景，包含正向与“过度行为”检查。
- `docs/decisions/`：Task Pilot 自身的重要设计决策。
- `MAINTENANCE.md`：长期内容治理规则。
- `CHANGELOG.md`：版本变化。

## 安装思路

本仓库同时保留标准 Skill 源码和 Agent Plugins 1.0 `plugin.json`。

发布到 GitHub 后，可在支持 `skills` CLI 的环境中使用仓库安装方式；也可以将 `skills/task-pilot` 放入兼容的 Agent Skills 目录。

ChatGPT / Codex 等支持 Agent Plugin 的环境可使用单独生成的 plugin ZIP。平台安装入口会变化，因此核心 Skill 不依赖某个固定 UI 路径。

## 长期维护原则

不限制文件规模，限制冗余。

不追求短，追求收敛。大型工程需要更多规则时可以增加，但每条规则都必须有明确职责、适用条件和长期价值。

## 仓库自检

提交或发布前运行：

```bash
python scripts/validate_repo.py
```

它检查 manifest、版本一致性、Skill frontmatter、本地 Markdown 引用和明显的敏感文件风险。GitHub Actions 会在 push / pull request 时运行同一检查。
