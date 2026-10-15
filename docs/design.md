# Task Pilot v1.0 Design

## Product definition

Task Pilot 是跨项目、跨专业、跨 Agent 的通用任务控制 Skill。

它优先识别并遵循用户指定的工作流、项目规则和专业 Skill；只有没有适用流程时才使用自身的通用处理规则。

## Non-goals

v1.0 不包含：

- GUI / Dashboard；
- 数据库；
- 遥测；
- 云端服务；
- 自动经验收集；
- 固定复杂度评分；
- 大量 slash commands；
- 用 Task Pilot 替代专业 Workflow。

## Stable behavior

- 自动判断 = 路由，不是做主。
- 不限制规则文件规模，限制冗余和职责混乱。
- 现有专业流程优先，Task Pilot 不建立平行流程。
- 完成检查同时防“漏做”和“多做”。
