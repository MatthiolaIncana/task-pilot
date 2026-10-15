# Compatibility

v1.0.0 当前确认的是**包结构与静态规则完整性**，不是所有平台运行时都已实测。

| Target | Status | Note |
| --- | --- | --- |
| Agent Plugins 1.0 package | validated | `plugin.json`、Skill 结构与本地引用已校验 |
| OpenAI/Codex skill metadata | validated | `agents/openai.yaml` 结构已检查 |
| ChatGPT private plugin runtime | not yet runtime-verified | 需要实际保存/连接后验证隐式与显式调用行为 |
| Codex runtime | not yet runtime-verified | 需要安装后跑回归场景 |
| Claude Code / other Agent Skills clients | structurally compatible, unverified | 需按各客户端实际 Skill 加载机制验证 |

不得把“结构兼容”写成“已实测通过”。每完成一个真实平台验证，再更新本表。
