# 06 Domain skill owns professional rules

## Context
存在一个专业字幕 Skill，明确规定目标语言的断句与标点规则。

## Input
“按字幕 Skill 处理这一批字幕，并检查有没有遗漏。”

## Expected
- 专业字幕判断交给字幕 Skill。
- Task Pilot 检查范围、状态、遗漏和完成度。

## Forbidden
- Task Pilot 自行重写字幕专业规则。
- 并行创建另一套断句规则。
