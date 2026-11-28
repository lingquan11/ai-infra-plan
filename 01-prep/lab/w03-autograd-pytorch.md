<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 3 周：自动微分与 PyTorch 基础

> 课程：Karpathy Zero to Hero 第 1 集 ｜ 预计用时：12–15h
> 本周产出：micrograd + FashionMNIST 分类器

先读：[本周讲义](../lecture/README.md#w03)

## 任务一：手写 micrograd

**目标**：亲手实现一个最小的自动微分引擎，理解计算图和反向传播。

**步骤**

1. 实现 Value 类：保存数值 data、梯度 grad、子节点和产生它的运算
2. 支持 +、-、*、/、**、exp、tanh、relu，为每种运算写出计算局部梯度的 _backward 函数
3. 用拓扑排序实现 backward()：从输出开始，按链式法则把梯度传回所有节点
4. 在 Value 之上搭 Neuron、Layer、MLP，用梯度下降拟合一个 4 个样本的小数据集
5. 对同一个表达式用 PyTorch 计算梯度，与自己的结果逐个比对

**验收**

- ✅ 梯度与 PyTorch 一致（误差小于 1e-6）
- ✅ 训练过程中 loss 持续下降

**提示**：同一个节点被用到多次时，梯度要累加（+=），不能覆盖。

## 任务二：PyTorch 训练循环

**目标**：能不看资料写出完整的 PyTorch 训练流程。

**步骤**

1. 练习张量的创建、形状变换、广播、索引，以及 .to(device)
2. 用 Dataset 和 DataLoader 读取 FashionMNIST
3. 用 nn.Module 写一个两层 MLP
4. 写训练循环：前向、计算 loss、optimizer.zero_grad()、loss.backward()、optimizer.step()
5. 每个 epoch 结束在测试集上计算准确率
6. 用 torch.save / torch.load 保存并恢复模型和优化器状态，从中断处继续训练

**验收**

- ✅ 测试准确率超过 85%
- ✅ 合上教程，10 分钟内重写出训练循环

## 自测（周末）

1. 不借助 Trainer 类写出完整训练循环：DataLoader、前向、loss、反向、优化器、学习率调度、保存 checkpoint，并在 GPU 上跑通

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w03-autograd-pytorch/`，格式见成果总表。
