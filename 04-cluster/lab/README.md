<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 4 章动手实践：集群与平台

每周一个任务文件：目标、步骤、✅ 验收、提示和自测。[网页版](https://lingquan11.github.io/ai-infra-plan/)里可以勾选进度，并一键把任务复制给 Muse，让它带你一步步做。

| 周 | 主题 | 课程 | 用时 | 硬件 | 本周产出 |
|---|---|---|---|---|---|
| [30](w30-cluster-network.md) | AI 集群与网络通信 | ZOMI AIInfra 01–02 | 10–12h | 短期租一台多卡机器 | 通信实测报告 |
| [31](w31-checkpoint-storage.md) | 集合通信与 checkpoint 存储 | ZOMI AIInfra 02 | 10–12h | — | checkpoint 开销分析 |
| [32](w32-k8s-basics.md) | 容器与 Kubernetes 基础 | ZOMI AIInfra 03 | 10–12h | 本地 kind 集群即可，不需要 GPU | 运行在 K8s 上的推理服务 |
| [33](w33-gpu-scheduling.md) | GPU 调度与分布式训练任务 | ZOMI AIInfra 03 | 12–15h | kind 上可以不用 GPU 练调度；验证 GPU 调度需要短期租一个带 GPU 的云 K8s | 可调度的训练与推理 |
| [34](w34-monitoring.md) | 监控、故障恢复与全链路 | ZOMI AIInfra 03 | 12–15h | — | 全链路平台 |
