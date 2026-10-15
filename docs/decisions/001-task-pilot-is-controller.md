# 001 — Task Pilot 是控制层，不是万能工作流

## Decision
Task Pilot 负责路由、边界、状态和完成检查，不复制专业工作流的专业规则。

## Reason
避免与现有 Workflow / Skill 产生重复流程、冲突和长期规则膨胀。
