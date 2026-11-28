<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 13 周：GPU 硬件、profiling 与 roofline

> 课程：CS336 第 5 讲 · 作业 2 §2 ｜ 预计用时：12–15h ｜ 硬件：单卡；先在 CPU 上调通正确性
> 本周产出：profiling 报告 + roofline 图

先读：[本周讲义](../lecture/README.md#w13)

## 任务一：[作业 2 §2] 基准测试与 profiling

**目标**：会测量，才能知道时间和显存花在哪里。

**步骤**

1. clone 作业 2 仓库，接上作业 1 的模型
2. 写端到端 benchmark：先预热几步，再计时前向、反向；每次计时前后调用 torch.cuda.synchronize()
3. 对不同模型规模做一张耗时表
4. 用 Nsight Systems（nsys profile）抓一次训练步，用 NVTX 标注前向、反向、优化器阶段，找出最耗时的 kernel
5. 开启 BF16 混合精度（torch.autocast），对比速度和 loss
6. 用 PyTorch 显存快照画出显存时间线，找出峰值出现在哪里

**验收**

- ✅ 一张「模型规模 × 前向 / 反向耗时」表
- ✅ 能指出最耗时的三类 kernel

## 任务二：画出模型的 roofline

**目标**：判断每个算子受限于算力还是访存。

**步骤**

1. 查出你的 GPU 的 BF16 Tensor Core 峰值算力和 HBM 带宽，算出拐点（FLOPs / 字节）
2. 分别估算矩阵乘、softmax、RMSNorm、逐元素激活的算术强度
3. 把它们画到 roofline 图上
4. 用 profiler 的实测时间验证你的判断

**验收**

- ✅ 一张 roofline 图
- ✅ 说清哪些算子受限于访存，以及原因

## 自测（周末）

1. 不查资料说出 H100 的 HBM 容量、HBM 带宽、L2 大小、每个 SM 的共享内存上限的量级，并解释为什么显存带宽常常先于算力成为瓶颈
2. 用 Nsight Systems 抓一次训练迭代，指出 GPU 空闲是来自数据预处理、通信等待还是 kernel 启动开销；用 Nsight Compute 的 SOL 面板判断一个 kernel 受限于访存还是算力

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w13-profiling-roofline/`，格式见成果总表。
