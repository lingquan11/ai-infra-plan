<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 24 周：PagedAttention：分页管理 KV cache

> 课程：vLLM 论文 · 11-868 第 14 周 ｜ 预计用时：12–15h
> 本周产出：分页 KV cache

先读：[本周讲义](../lecture/README.md#w24)

## 任务一：block 管理器与分页注意力

**目标**：解决 KV cache 的碎片问题，提高并发数。

**步骤**

1. 先观察：按最大长度连续预分配 KV cache 会浪费多少显存
2. 实现 block 管理器：把 KV cache 切成固定大小的块（如 16 个 token），每个请求维护一张逻辑块到物理块的块表
3. 实现分配、释放，以及显存不足时的抢占（重算或换出）
4. 修改注意力，按块表读取 K、V（先用 PyTorch 索引实现，选做 Triton kernel）
5. 测量同样显存下可以同时服务的请求数

**验收**

- ✅ 输出与不分页的版本一致
- ✅ 最大并发数的前后对比

## 自测（周末）

1. 画出 KV cache 管理全链路：分配、碎片化、PagedAttention 的逻辑块到物理块映射、前缀缓存如何靠哈希复用已有的块

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w24-paged-attention/`，格式见成果总表。
