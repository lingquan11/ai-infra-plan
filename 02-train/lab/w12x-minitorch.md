<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# （可选 +2 周）手写深度学习框架

> 课程：CMU 11-868 作业 2 · miniTorch ｜ 预计用时：10–15h，共 2 周
> 本周产出：迷你框架

先读：[本周讲义](../lecture/README.md#w12x)

## 任务一：实现一个迷你张量框架

**目标**：弄懂 PyTorch 这类框架内部怎么存张量、怎么调度运算、怎么做自动微分。

**步骤**

1. 张量存储：一维 buffer + shape + strides，实现索引，以及不复制数据的转置
2. 实现广播规则
3. 实现 map、zip、reduce 三类基础运算，在其上构建常用算子
4. 实现自动微分：记录计算历史，拓扑排序后按链式法则反向传播
5. 用自己的框架训练一个小网络，与 PyTorch 对比结果

**验收**

- ✅ 作业自带的测试通过
- ✅ 能解释 stride 如何让 transpose、view 不复制数据

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w12x-minitorch/`，格式见成果总表。
