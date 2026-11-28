<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 14 周：CUDA 入门：逐步优化 GEMM

> 课程：11-868 GPU 编程课件 · Simon Boehm ｜ 预计用时：12–15h ｜ 硬件：单卡，需要 CUDA 编译器 nvcc
> 本周产出：GEMM 各版本性能对比表

先读：[本周讲义](../lecture/README.md#w14)

## 任务一：CUDA 编程基础

**目标**：会写、会启动、会调试一个 CUDA kernel。

**步骤**

1. 理解 grid、block、thread 三级结构和线程全局索引的计算
2. 写向量加法：cudaMalloc、cudaMemcpy、启动 kernel、检查错误
3. 写行 softmax：每行一个 block，用 shared memory 做归约，求最大值和求和
4. 用 Nsight Compute（ncu）查看 kernel 耗时和访存吞吐

**验收**

- ✅ 结果与 PyTorch 一致

## 任务二：逐步优化 GEMM

**目标**：体会访存合并、分块和寄存器复用带来的数量级差距。

**步骤**

1. 朴素版：每个线程计算一个输出元素
2. 合并访存版：调整线程到数据的映射，让相邻线程读相邻地址
3. shared memory 分块版
4. 一维、二维 block tiling：每个线程计算多个输出，复用寄存器
5. （选做）向量化访存、Tensor Core（WMMA）
6. 每一版都对 4096×4096 的 FP32 矩阵测 GFLOP/s，与 torch.matmul（cuBLAS）对比

**验收**

- ✅ 一张各版本 GFLOP/s 对比表
- ✅ 最好的版本达到 cuBLAS 的 70% 以上（50% 算及格）

## 自测（周末）

1. 写一个 32×32 矩阵转置 kernel：先做出有 bank conflict 的版本，再加一列 padding 消除冲突，用 Nsight Compute 验证冲突数降到 0

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w14-cuda-gemm/`，格式见成果总表。
