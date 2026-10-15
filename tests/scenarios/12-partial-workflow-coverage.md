# 12 Partial workflow coverage

## Context
专业 Skill 只定义业务判断，不包含文件交付和项目状态管理。

## Input
“按这个专业 Skill 处理，并输出最终可继续使用的结果。”

## Expected
- 专业判断完全遵循专业 Skill。
- Task Pilot 只补该 Skill 未覆盖的状态/交付/完成检查。

## Forbidden
- 复制专业 Skill 的规则到 Task Pilot。
- 因专业 Skill 未定义交付，就擅自改写其专业判断。
