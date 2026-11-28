<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 23 周：从静态 batching 到 continuous batching

> 课程：Orca · 11-868 第 13 周 ｜ 预计用时：12–15h
> 本周产出：continuous batching 调度器

先读：[本周讲义](../lecture/README.md#w23)

## 任务一：continuous batching 调度器

**目标**：让 GPU 不再等最慢的那个请求。

**步骤**

1. 读 nano-vllm 的整体结构（引擎、调度器、模型执行、采样）作参考，但给自己的模型实现
2. 静态 batching：一批请求左填充后一起生成，测量短请求等待长请求造成的浪费
3. continuous batching：每个 decode 步结束后移出已完成的请求，从等待队列补入新请求
4. 用一组长度随机的请求，对比逐条生成、静态 batching、continuous batching 的吞吐

**验收**

- ✅ 三种方式的吞吐对比表
- ✅ 能解释迭代级调度为什么能提高 GPU 利用率

## 自测（周末）

1. 向不懂技术的人讲清 static batching 和 continuous batching 的区别，以及后者为什么能大幅提高 GPU 利用率

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w23-continuous-batching/`，格式见成果总表。
