<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 4 章讲义：集群与平台

每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。自己的笔记放在 `lecture/notes/`（手写，脚本不会覆盖）。

<a id="w30"></a>

## 第 30 周 · AI 集群与网络通信

**中文阅读（AIInfraGuide）**

- [多节点部署](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第6章-分布式推理/65-多节点部署/) — 看多机网络与拓扑部分
- [集群通信网络与 NCCL（复读）](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/communication/collective-communication-primer/) — 带着实测数据再读一遍

**课程**

- [ZOMI AIInfra 01 AI 计算集群](https://infrasys-ai.github.io/aiinfra-docs/) — 中文
- [ZOMI AIInfra 02 通信与存储：网络、RDMA / RoCE、拓扑](https://infrasys-ai.github.io/aiinfra-docs/) — 中文
- [ZOMI 酱 B 站视频](https://space.bilibili.com/517221395)
- [nccl-tests](https://github.com/NVIDIA/nccl-tests)

本周任务：[w30-cluster-network.md](../lab/w30-cluster-network.md)

<a id="w31"></a>

## 第 31 周 · 集合通信与 checkpoint 存储

**课程**

- [ZOMI AIInfra 02：集合通信、NCCL、checkpoint 存储](https://infrasys-ai.github.io/aiinfra-docs/) — 中文
- [PyTorch 分布式 checkpoint 文档](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html)

本周任务：[w31-checkpoint-storage.md](../lab/w31-checkpoint-storage.md)

<a id="w32"></a>

## 第 32 周 · 容器与 Kubernetes 基础

**中文阅读（AIInfraGuide）**

- [第 8 章 生产部署与运维](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第8章-生产部署与运维/第8章-生产部署与运维/) — 目前还是提纲，作者写完后再补读；这周先以课程为准

**课程**

- [ZOMI AIInfra 03 集群容器与云原生：Docker、K8s 基础](https://infrasys-ai.github.io/aiinfra-docs/) — 中文
- [Kubernetes 官方教程](https://kubernetes.io/zh-cn/docs/tutorials/)
- [kind（在本地运行 K8s 集群）](https://kind.sigs.k8s.io/)

本周任务：[w32-k8s-basics.md](../lab/w32-k8s-basics.md)

<a id="w33"></a>

## 第 33 周 · GPU 调度与分布式训练任务

**中文阅读（AIInfraGuide）**

- [vLLM 分布式部署实战](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第6章-分布式推理/66-vllm分布式部署实战/)

**课程**

- [ZOMI AIInfra 03：K8s 调度、AI 云平台](https://infrasys-ai.github.io/aiinfra-docs/) — 中文
- [Kueue](https://kueue.sigs.k8s.io/)
- [Volcano](https://volcano.sh/)
- [Kubeflow Trainer](https://www.kubeflow.org/docs/components/trainer/)
- [NVIDIA k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)
- [KEDA（事件驱动的自动扩缩容）](https://keda.sh/)

本周任务：[w33-gpu-scheduling.md](../lab/w33-gpu-scheduling.md)

<a id="w34"></a>

## 第 34 周 · 监控、故障恢复与全链路

**中文阅读（AIInfraGuide）**

- [流水线并行推理](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第6章-分布式推理/63-流水线并行推理/)
- [数据并行与专家并行](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第6章-分布式推理/64-数据并行与专家并行/)

**课程**

- [ZOMI AIInfra 03：监控](https://infrasys-ai.github.io/aiinfra-docs/) — 中文
- [dcgm-exporter](https://github.com/NVIDIA/dcgm-exporter)
- [Prometheus 入门](https://prometheus.io/docs/introduction/overview/)
- [Grafana 文档](https://grafana.com/docs/grafana/latest/)

本周任务：[w34-monitoring.md](../lab/w34-monitoring.md)
