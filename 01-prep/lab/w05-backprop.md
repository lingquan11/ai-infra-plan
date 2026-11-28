<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 5 周：训练动态与手写反向传播

> 课程：Karpathy makemore 第 3–4 集 ｜ 预计用时：12–15h
> 本周产出：对反向传播计算量和激活显存的直观理解

先读：[本周讲义](../lecture/README.md#w05)

## 任务一：激活值、梯度与 BatchNorm

**目标**：看懂训练为什么会不稳定，以及初始化和归一化如何解决它。

**步骤**

1. 在上周的 MLP 上观察：初始 loss 偏高、tanh 大量饱和
2. 修正输出层初始化，让初始 loss 接近 -ln(1/27)
3. 用 Kaiming 初始化缩放隐藏层权重
4. 加入 BatchNorm，理解训练模式与推理模式（running mean / var）的区别
5. 画出各层激活值和梯度的直方图，对比修改前后

**验收**

- ✅ 能解释初始 loss 为什么应约为 3.3
- ✅ 修正后训练曲线开头不再有陡降

## 任务二：不用 autograd 手写反向传播

**目标**：弄清每一步反向传播算什么、需要哪些前向结果。

**步骤**

1. 对网络 embedding → linear → BatchNorm → tanh → linear → cross-entropy，逐步手写每个中间张量的梯度
2. 每算出一个梯度，就和 autograd 的结果比对
3. 把 cross-entropy 的反向化简成一个式子：softmax 概率减去 one-hot
4. 把 BatchNorm 的反向化简成一个融合公式
5. 列一张表：每一步反向需要保存哪些前向张量

**验收**

- ✅ 所有中间梯度与 autograd 一致
- ✅ 这张表能说明训练时的激活显存从哪里来

**提示**：这张表第 15 周讲激活重计算时会再用到。

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w05-backprop/`，格式见成果总表。
