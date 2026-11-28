<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 17 周：FlashAttention-2：反向并接入模型

> 课程：作业 2 §4 ｜ 预计用时：12–15h
> 本周产出：用上自写 FlashAttention 的训练

先读：[本周讲义](../lecture/README.md#w17)

## 任务一：[作业 2 §4] FA2 反向 + 端到端接入

**目标**：让自己写的注意力真正用在训练里。

**步骤**

1. 推导注意力的反向：dV、dP、dS、dQ、dK
2. 利用保存的 logsumexp 重新计算 P，避免存储整张注意力矩阵
3. 先用 PyTorch（可加 torch.compile）实现反向
4. （选做）用 Triton 写反向 kernel
5. 用 torch.autograd.Function 包装前向和反向，与朴素实现比对梯度
6. 替换进自己的 Transformer，端到端训练，对比吞吐和显存

**验收**

- ✅ 梯度与朴素实现一致
- ✅ perf-log 记录端到端提速

## 自测（周末）

1. 在白板上画出 FlashAttention 的分块过程（V1 与 V2 的内外层循环有何不同），说清额外显存为什么从 O(N²) 降到 O(N)

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w17-flashattn-backward/`，格式见成果总表。
