<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 15 周：Triton 与单卡显存优化

> 课程：CS336 第 6 讲 · 作业 2 §3 ｜ 预计用时：12–15h
> 本周产出：Triton RMSNorm + 显存优化对比

先读：[本周讲义](../lecture/README.md#w15)

## 任务一：Triton 入门 + 读编译器生成的代码

**目标**：掌握块级 GPU 编程，并看懂 torch.compile 做了什么。

**步骤**

1. 跟官方教程实现 vector add、fused softmax、matrix multiplication
2. 理解 program_id、块内偏移、mask 和 autotune
3. 写一个 Triton 版 RMSNorm 前向，和 PyTorch 版对比速度
4. 用 torch.compile 编译模型中的 RMSNorm，设置环境变量 TORCH_LOGS=output_code 查看生成的 Triton 代码，和自己写的对比

**验收**

- ✅ 自写 RMSNorm 比未编译的 PyTorch 版快
- ✅ 能指出编译器生成的代码融合了哪些操作

## 任务二：[作业 2 §3] 单卡显存优化

**目标**：理解激活显存的来源，学会用算力换显存。

**步骤**

1. 分析 autograd 为反向保存了哪些中间张量，哪些可以通过算子融合省掉
2. 用 torch.utils.checkpoint 实现激活重计算
3. 测量重计算前后的显存和速度
4. 在固定显存下，比较能跑的最大 batch size 和上下文长度

**验收**

- ✅ 一张显存与速度的取舍表，记入 perf-log

**提示**：第 5 周那张「反向要保存哪些张量」的表这里正好用上。

## 自测（周末）

1. Reduce 三个版本：全局内存原子加 → 共享内存树形归约 → warp shuffle，用 Nsight Compute 比较吞吐，说清每一步省在哪里

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w15-triton-memory/`，格式见成果总表。
