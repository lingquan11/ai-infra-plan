<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 16 周：FlashAttention-2：前向

> 课程：作业 2 §4 ｜ 预计用时：12–15h
> 本周产出：FA2 前向 + 速度 / 显存对比

先读：[本周讲义](../lecture/README.md#w16)

## 任务一：[作业 2 §4] 注意力基准与 FA2 前向

**目标**：实现一个分块计算、不保存整张注意力矩阵的注意力 kernel。

**步骤**

1. 测朴素 PyTorch 注意力在不同序列长度和 head 维度下的耗时和显存，找到 OOM 的位置
2. 用 torch.compile 编译注意力再测一遍
3. 弄懂 online softmax：分块计算时维护每行的最大值 m 和归一化因子 l，最后统一缩放
4. 先用纯 PyTorch 写分块版 FA2 前向，方便调试
5. 再用 Triton 写 kernel：每个 program 负责一个 Q 块，循环加载 K、V 块，支持因果掩码
6. 输出注意力结果，同时保存每行的 logsumexp 供反向使用

**验收**

- ✅ 与朴素注意力的输出在容差内一致
- ✅ 长序列下显存不再随 T² 增长

## 自测（周末）

1. 不看论文推导 online softmax：分块时怎样维护行最大值和归一化因子，最后怎样统一缩放

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w16-flashattn-forward/`，格式见成果总表。
