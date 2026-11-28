<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 2 章讲义：训练主线

每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。自己的笔记放在 `lecture/notes/`（手写，脚本不会覆盖）。

<a id="w09"></a>

## 第 9 周 · 正式版 tokenizer + 资源估算

**中文阅读（AIInfraGuide）**

- [分布式训练总论：显存账本与五大并行策略全景](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/11-分布式训练总论/) — 先读显存账本部分，配合本周的资源估算

**课程**

- [CS336 第 1 讲：课程概览与分词](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)
- [CS336 第 2 讲：PyTorch 与资源估算（FLOPs、显存、算术强度）](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)
- [CS336 课程主页](https://cs336.stanford.edu/)
- [CS336 作业 1 仓库与 handout](https://github.com/stanford-cs336/assignment1-basics)

本周任务：[w09-tokenizer-estimate.md](../lab/w09-tokenizer-estimate.md)

<a id="w10"></a>

## 第 10 周 · 从零实现 Transformer 组件

**中文阅读（AIInfraGuide）**

- [Transformer 前馈网络 FFN 深入理解](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/34-transformer前馈网络ffn深入理解/) — 对应 SwiGLU
- [Transformer 位置编码深入理解](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/35-transformer位置编码深入理解/) — 对应 RoPE
- [Transformer Decoder Block 完整解析](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/37-transformer-decoder-block完整解析/)

**课程**

- [CS336 第 3 讲：模型结构与超参数](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)

本周任务：[w10-transformer-lm.md](../lab/w10-transformer-lm.md)

<a id="w11"></a>

## 第 11 周 · 训练基础设施 + 性能基线

**中文阅读（AIInfraGuide）**

- [从 Transformer 到 LLM 自回归生成深入理解](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/38-从transformer到llm自回归生成深入理解/) — 对应本周的解码与采样
- [优化器：从 SGD 到 AdamW 与显存开销分析](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/31-优化器原理与显存开销分析/) — 对应本周手写 AdamW

**课程**

- [CS336 第 4 讲：注意力变体与 MoE（选看）](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)

本周任务：[w11-training-baseline.md](../lab/w11-training-baseline.md)

<a id="w12"></a>

## 第 12 周 · 实验与消融，冻结基线

**中文阅读（AIInfraGuide）**

- [AI Infra 学习路线](https://caomaolufei.github.io/AIInfraGuide/guides/ai-infra学习路线/) — 读「第一层：CUDA 编程与算子优化」，预习下一阶段

**课程**

- [CS336 作业 1 handout 的实验部分](https://github.com/stanford-cs336/assignment1-basics)

本周任务：[w12-ablation-baseline.md](../lab/w12-ablation-baseline.md)

<a id="w12x"></a>

## （可选 +2 周）手写深度学习框架

**课程**

- [CMU 11-868 第 3 周：深度学习框架与自动微分（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)
- [CMU 11-868 作业页](https://llmsystem.github.io/llmsystemhomework/)
- [另一个选择：CMU 10-414/714 Deep Learning Systems（Needle 框架）](https://dlsyscourse.org/) — 在线评测已关闭，只能用本地测试

本周任务：[w12x-minitorch.md](../lab/w12x-minitorch.md)

<a id="w13"></a>

## 第 13 周 · GPU 硬件、profiling 与 roofline

**中文阅读（AIInfraGuide）**

- [GPU 基础知识：从硬件架构到 AI 计算](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/gpu/gpu-basics/)
- [NVIDIA GPU 架构演进：从 Volta 到 Blackwell](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/gpu/nvidia-gpu-evolution/)

**课程**

- [CS336 第 5 讲：GPU 与 TPU](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)
- [CS336 作业 2 仓库与 handout](https://github.com/stanford-cs336/assignment2-systems)
- [How to Scale Your Model（roofline 章节）](https://jax-ml.github.io/scaling-book/)
- [ZOMI AISystem：AI 芯片与 GPU 架构](https://github.com/Infrasys-AI/AISystem) — 中文，配 B 站视频

本周任务：[w13-profiling-roofline.md](../lab/w13-profiling-roofline.md)

<a id="w14"></a>

## 第 14 周 · CUDA 入门：逐步优化 GEMM

**中文阅读（AIInfraGuide）**

- [CUDA 开发环境搭建](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/11-cuda开发环境搭建/)
- [CUDA 编程模型](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/12-cuda编程模型/)
- [CUDA 内存模型](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/13-cuda内存模型/)
- [第一个实用 Kernel：向量加法](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/14-第一个实用kernel/)
- [Warp 与执行模型](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/21-warp与执行模型/)
- [内存访问优化](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/22-内存访问优化/)
- [CUDA GEMM 算子性能优化](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/41-cuda-gemm算子性能优化/) — 和本周的 GEMM 逐步优化对照

**课程**

- [CMU 11-868 第 1–2 周：GPU 编程基础（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)
- [How to Optimize a CUDA Matmul Kernel（Simon Boehm）](https://siboehm.com/articles/22/CUDA-MMM)
- [配套代码 SGEMM_CUDA](https://github.com/siboehm/SGEMM_CUDA)
- 参考书：Programming Massively Parallel Processors（前 6 章） — 纸质书或电子书

本周任务：[w14-cuda-gemm.md](../lab/w14-cuda-gemm.md)

<a id="w15"></a>

## 第 15 周 · Triton 与单卡显存优化

**中文阅读（AIInfraGuide）**

- [Occupancy 与资源分配](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/23-occupancy与资源分配/)
- [同步与原子操作](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/24-同步与原子操作/)
- [CUDA Reduce 算子优化](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/31-cuda-reduce算子优化/)
- [Triton 编程模型](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/71-triton编程框架/)

**课程**

- [CS336 第 6 讲：算子与 Triton](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)
- [Triton 官方教程](https://triton-lang.org/main/getting-started/tutorials/index.html)

本周任务：[w15-triton-memory.md](../lab/w15-triton-memory.md)

<a id="w16"></a>

## 第 16 周 · FlashAttention-2：前向

**中文阅读（AIInfraGuide）**

- [CUDA Softmax 朴素实现优化](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/51-cuda-softmax朴素实现优化/)
- [CUDA Online Softmax 实现优化](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/52-cuda-online-softmax实现/) — 本周 FA2 前向的核心
- [FlashAttention V1 详解](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/61-flashattention-v1详解/)

**课程**

- [论文：FlashAttention](https://arxiv.org/abs/2205.14135)
- [论文：FlashAttention-2](https://arxiv.org/abs/2307.08691)
- [CS336 作业 2 handout §4](https://github.com/stanford-cs336/assignment2-systems)

本周任务：[w16-flashattn-forward.md](../lab/w16-flashattn-forward.md)

<a id="w17"></a>

## 第 17 周 · FlashAttention-2：反向并接入模型

**中文阅读（AIInfraGuide）**

- [FlashAttention V2 详解](https://caomaolufei.github.io/AIInfraGuide/cuda/模块二-cuda编程与算子优化/62-flashattention-v2详解/)
- [集群通信网络与 NCCL：分布式训练的通信骨架](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/communication/collective-communication-primer/) — 为下周分布式训练预习

**课程**

- [FlashAttention-2 论文中的反向推导](https://arxiv.org/abs/2307.08691)

本周任务：[w17-flashattn-backward.md](../lab/w17-flashattn-backward.md)

<a id="w18"></a>

## 第 18 周 · 集合通信与手写 DDP

**中文阅读（AIInfraGuide）**

- [集合通信原语详解](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/21-集合通信原语详解/)
- [环境搭建与分布式启动](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/12-环境搭建与分布式启动/)
- [数据并行详解](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/41-数据并行详解/)

**课程**

- [CS336 第 7 讲：并行（上）](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)
- [Ultra-Scale Playbook：数据并行部分](https://huggingface.co/spaces/nanotron/ultrascale-playbook)

本周任务：[w18-collectives-ddp.md](../lab/w18-collectives-ddp.md)

<a id="w19"></a>

## 第 19 周 · 优化器分片、FSDP 与并行策略

**中文阅读（AIInfraGuide）**

- [PyTorch 数据并行从原理到实战](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/42-pytorch-数据并行从原理到实战/)
- [第 5 章 ZeRO 系列](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/第5章-zero系列/) — 目前还是提纲，作者写完后再补读；这周先以课程为准

**课程**

- [CS336 第 8 讲：并行（下）](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)
- [Ultra-Scale Playbook：ZeRO 部分](https://huggingface.co/spaces/nanotron/ultrascale-playbook)
- [论文：ZeRO](https://arxiv.org/abs/1910.02054)

本周任务：[w19-fsdp.md](../lab/w19-fsdp.md)

<a id="w20"></a>

## 第 20 周 · 张量并行与流水线并行

**中文阅读（AIInfraGuide）**

- [第 6 章 张量并行与序列并行](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/第6章-张量并行与序列并行/) — 目前还是提纲，作者写完后再补读；这周先以课程为准
- [第 7 章 流水线并行](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/第7章-流水线并行/) — 目前还是提纲，作者写完后再补读；这周先以课程为准
- [第 11 章 3D 并行与混合并行策略](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/第11章-3d并行与混合并行策略/) — 目前还是提纲，作者写完后再补读；这周先以课程为准

**课程**

- [Ultra-Scale Playbook：张量并行与流水线并行部分](https://huggingface.co/spaces/nanotron/ultrascale-playbook)
- [CMU 11-868 第 10 周：GPipe、Megatron-LM（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)
- [picotron（最小的 4D 并行训练框架）](https://github.com/huggingface/picotron)
- [picotron 逐步教程视频](https://www.youtube.com/playlist?list=PL-_armZiJvAnhcRr6yTJ0__f3Oi-LLi9S)
- [ZOMI AIInfra 04 大模型训练（并行章节）](https://github.com/Infrasys-AI/AIInfra) — 中文，配 B 站视频

本周任务：[w20-tp-pp.md](../lab/w20-tp-pp.md)

<a id="w21"></a>

## 第 21 周 · 缓冲周：第一段复盘

**中文阅读（AIInfraGuide）**

- [AI Infra 学习路线](https://caomaolufei.github.io/AIInfraGuide/guides/ai-infra学习路线/) — 读「新人破局指南」和「核心思维模型」，对照自己的复盘
- [第 8 章 混合精度与显存优化](https://caomaolufei.github.io/AIInfraGuide/distributed/模块三-分布式训练/第8章-混合精度与显存优化/) — 目前还是提纲，作者写完后再补读；这周先以课程为准

本周任务：[w21-review-train.md](../lab/w21-review-train.md)
