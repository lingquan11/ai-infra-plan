<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 25 周：权重量化

> 课程：11-868 第 11–12 周 ｜ 预计用时：12–15h
> 本周产出：量化推理

先读：[本周讲义](../lecture/README.md#w25)

## 任务一：INT8 / INT4 权重量化推理

**目标**：用更少的字节读权重，直接缓解 decode 的访存瓶颈。

**步骤**

1. 实现按通道的对称 INT8 权重量化与反量化
2. 写一个 Triton kernel：读取 INT8 权重，在寄存器中反量化后做矩阵乘，激活保持 BF16
3. 扩展到 INT4：两个值打包进一个字节，按组量化（组大小 128）
4. 测量验证集 loss、decode 速度和显存
5. （选读）弄懂 GPTQ、AWQ 为什么比直接四舍五入更准

**验收**

- ✅ 一张精度 / 速度 / 显存对比表

**提示**：第 14–15 周写 GEMM 和 Triton 的经验在这里直接复用。

## 自测（周末）

1. 判断 70B 模型只有 2 张 A100 80GB 时该选 FP16、W8A8 还是 INT4 weight-only，并说明 A100 为什么用不了 FP8
2. 解释为什么小 batch decode 时 INT4 weight-only 往往更快，而大 batch 时 W8A8 可能反超

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w25-quantization/`，格式见成果总表。
