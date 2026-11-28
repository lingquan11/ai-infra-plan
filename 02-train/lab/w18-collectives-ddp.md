<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 18 周：集合通信与手写 DDP

> 课程：CS336 第 7 讲 · 作业 2 §5 ｜ 预计用时：12–15h ｜ 硬件：需要 2–4 张卡；正确性可先用 CPU 的 gloo 后端验证
> 本周产出：手写 DDP + 通信基准

先读：[本周讲义](../lecture/README.md#w18)

## 任务一：集合通信基准

**目标**：用数据认识通信的代价。

**步骤**

1. 用 torchrun 或 mp.spawn 起多个进程，分别用 gloo（CPU）和 NCCL（GPU）后端
2. 测 all-reduce 在不同数据量和进程数下的耗时，算出有效带宽
3. 用 α-β 模型拟合：耗时 = 延迟 α + 数据量 / 带宽
4. 解释小消息和大消息的差别

**验收**

- ✅ 一条带宽随数据量变化的曲线

## 任务二：[作业 2 §5] 手写 DDP

**目标**：从最朴素的版本一步步做到计算与通信重叠。

**步骤**

1. 朴素版：反向结束后，对每个参数的梯度单独 all-reduce 并取平均
2. 验证与单卡训练的结果一致（相同的全局 batch 和初始化）
3. 改进一：把所有梯度展平拼接，一次 all-reduce，减少通信调用次数
4. 改进二：用 register_post_accumulate_grad_hook，在每个参数的梯度就绪时立即发起异步 all-reduce，与剩余的反向计算重叠
5. （进阶）按大小把参数分桶通信
6. 对比各版本每一步的耗时和通信占比

**验收**

- ✅ 各版本结果都与单卡一致
- ✅ 一张各版本耗时对比表

## 自测（周末）

1. 拿到一个单卡训练脚本，30 分钟内改成 DDP 多卡版本并跑通（init_process_group、DistributedSampler、包装模型）
2. 画出 AllReduce、AllGather、ReduceScatter 的数据流，写出 Ring AllReduce 的通信量约为 2(N−1)/N × 数据量

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w18-collectives-ddp/`，格式见成果总表。
