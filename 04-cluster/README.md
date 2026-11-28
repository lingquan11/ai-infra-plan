<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 4 章：集群与平台

> ZOMI AIInfra：通信、存储、调度、监控（第 30–34 周）

## 本章收获
本章结束时你会有：
- 通信实测报告
- checkpoint 开销分析
- 运行在 K8s 上的推理服务
- 可调度的训练与推理
- 全链路平台

## 知识点地图
1. 第 30 周 · AI 集群与网络通信（ZOMI AIInfra 01–02）
2. 第 31 周 · 集合通信与 checkpoint 存储（ZOMI AIInfra 02）
3. 第 32 周 · 容器与 Kubernetes 基础（ZOMI AIInfra 03）
4. 第 33 周 · GPU 调度与分布式训练任务（ZOMI AIInfra 03）
5. 第 34 周 · 监控、故障恢复与全链路（ZOMI AIInfra 03）

## 讲义
每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。

| 周 | 主题 | 中文阅读 | 课程 |
|---|---|---|---|
| [30](lecture/README.md#w30) | AI 集群与网络通信 | 2 篇 | 4 项 |
| [31](lecture/README.md#w31) | 集合通信与 checkpoint 存储 | 0 篇 | 2 项 |
| [32](lecture/README.md#w32) | 容器与 Kubernetes 基础 | 1 篇 | 3 项 |
| [33](lecture/README.md#w33) | GPU 调度与分布式训练任务 | 1 篇 | 6 项 |
| [34](lecture/README.md#w34) | 监控、故障恢复与全链路 | 2 篇 | 4 项 |

## 动手实践
每周一个任务文件：目标、步骤、✅ 验收、提示和自测。在[网页版](https://lingquan11.github.io/ai-infra-plan/)里可以勾选进度，并一键把任务复制给 Muse，让它带你一步步做。

| 周 | 主题 | 课程 | 用时 | 硬件 | 本周产出 |
|---|---|---|---|---|---|
| [30](lab/w30-cluster-network.md) | AI 集群与网络通信 | ZOMI AIInfra 01–02 | 10–12h | 短期租一台多卡机器 | 通信实测报告 |
| [31](lab/w31-checkpoint-storage.md) | 集合通信与 checkpoint 存储 | ZOMI AIInfra 02 | 10–12h | — | checkpoint 开销分析 |
| [32](lab/w32-k8s-basics.md) | 容器与 Kubernetes 基础 | ZOMI AIInfra 03 | 10–12h | 本地 kind 集群即可，不需要 GPU | 运行在 K8s 上的推理服务 |
| [33](lab/w33-gpu-scheduling.md) | GPU 调度与分布式训练任务 | ZOMI AIInfra 03 | 12–15h | kind 上可以不用 GPU 练调度；验证 GPU 调度需要短期租一个带 GPU 的云 K8s | 可调度的训练与推理 |
| [34](lab/w34-monitoring.md) | 监控、故障恢复与全链路 | ZOMI AIInfra 03 | 12–15h | — | 全链路平台 |

## 成果展示
已产出 0 / 5 周，见[本章成果总表](showcase/README.md)。

还没有成果。每完成一周，按[成果总表](showcase/README.md)里的格式加一个目录。

## 与后续章节的关系
第 2–4 章的性能日志汇成第 5 章的技术报告。

下一章：[第 5 章 毕业项目](../05-capstone/)（技术报告 + 第一个开源 PR）
