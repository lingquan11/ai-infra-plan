<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 21 周：缓冲周：第一段复盘

> 课程：补完 + 复盘 ｜ 预计用时：按需
> 本周产出：第一段报告

先读：[本周讲义](../lecture/README.md#w21)

## 任务一：第一段复盘报告

**目标**：把 13 周的工作沉淀成一份可以展示的报告。

**步骤**

1. 补完没做完的任务
2. 根据 perf-log 画出从 v0-baseline 到现在的吞吐、显存、MFU 变化
3. 每项优化写一句它为什么有效
4. 写下你预期推理阶段会遇到哪些不同的瓶颈

**验收**

- ✅ notes/segment1-report.md 完成
- ✅ 打 git tag v1-training

## 过渡问题

为什么推理时 decode 阶段的瓶颈和训练完全不同？

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w21-review-train/`，格式见成果总表。
