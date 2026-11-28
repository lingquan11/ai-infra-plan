<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 29 周：缓冲周：第二段复盘

> 课程：补完 + 复盘 ｜ 预计用时：按需
> 本周产出：第二段报告

先读：[本周讲义](../lecture/README.md#w29)

## 任务一：第二段复盘报告

**目标**：把推理部分的工作整理成报告。

**步骤**

1. 补完没做完的任务
2. 整理推理部分的 perf-log，画出关键指标的变化
3. 写 notes/segment2-report.md

**验收**

- ✅ 报告完成
- ✅ 打 git tag v2-inference

## 自测（周末）

1. 给定 70B 稠密模型和一台 8 卡 H100，说清 TP=8 与 TP=4 + DP=2 在单请求延迟、总吞吐和 KV cache 容量上的差别

## 过渡问题

训练任务和多个推理服务要共用一个集群时，资源该怎么分？

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w29-review-infer/`，格式见成果总表。
