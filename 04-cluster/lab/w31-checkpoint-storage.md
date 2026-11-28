<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 31 周：集合通信与 checkpoint 存储

> 课程：ZOMI AIInfra 02 ｜ 预计用时：10–12h
> 本周产出：checkpoint 开销分析

先读：[本周讲义](../lecture/README.md#w31)

## 任务一：量化 checkpoint 开销

**目标**：让保存 checkpoint 不再拖慢训练。

**步骤**

1. 测量第 19 周分片训练的 checkpoint 保存和加载耗时
2. 改用 torch.distributed.checkpoint，每个 rank 只写自己的分片
3. 尝试异步保存，让训练不中断
4. 计算不同保存间隔下，checkpoint 开销占训练时间的比例

**验收**

- ✅ 一张开销比例表

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w31-checkpoint-storage/`，格式见成果总表。
