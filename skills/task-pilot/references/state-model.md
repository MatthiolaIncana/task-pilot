# State Model / 状态模型

仅在长期项目、复杂接续或明确需要状态传递时使用统一状态。

- `CONFIRMED`：已经明确决定，但不等于已经实现。
- `VERIFIED`：已经实现并通过与任务相称的验证。
- `IMPLEMENTED_UNVERIFIED`：已经实现，但验证不足或尚未执行。
- `PENDING`：尚未完成。
- `DEPRECATED`：已经废弃，不应继续作为当前方案使用。
- `REVIEW_REQUIRED`：出现新情况，需要重新评估；在评估前不要把旧状态当成仍然有效。

## 使用规则

状态描述必须对应具体对象或能力，避免“整个项目已完成”这类过度概括。

从 `IMPLEMENTED_UNVERIFIED` 进入 `VERIFIED` 必须有实际验证证据。

`CONFIRMED` 不自动升级为 `IMPLEMENTED_UNVERIFIED`。

出现失败或新改动后，只把受影响部分降级，不无依据重置整个项目。
