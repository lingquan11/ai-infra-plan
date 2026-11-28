<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 3 章讲义：推理与服务

每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。自己的笔记放在 `lecture/notes/`（手写，脚本不会覆盖）。

<a id="w22"></a>

## 第 22 周 · KV cache 与 prefill / decode

**中文阅读（AIInfraGuide）**

- [LLM 推理基础](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第1章-llm推理基础/11-llm推理基础/)
- [vLLM 快速入门](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第1章-llm推理基础/12-vllm快速入门/)

**课程**

- [CS336 第 10 讲：推理](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)
- [CMU 11-868 第 5 周：生成与投机解码（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)

本周任务：[w22-kv-cache.md](../lab/w22-kv-cache.md)

<a id="w23"></a>

## 第 23 周 · 从静态 batching 到 continuous batching

**中文阅读（AIInfraGuide）**

- [Continuous Batching](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第2章-推理引擎核心技术/22-continuous-batching/)
- [nano-vllm：项目全景与四层架构](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第3章-nano-vllm源码解读/31-项目全景与四层架构/)
- [nano-vllm：配置、入口与一次 generate 的全流程](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第3章-nano-vllm源码解读/32-配置入口与推理主循环/)
- [nano-vllm：Scheduler 与连续批处理](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第3章-nano-vllm源码解读/35-scheduler与连续批处理/)

**课程**

- [论文：Orca（迭代级调度）](https://www.usenix.org/conference/osdi22/presentation/yu)
- [CMU 11-868 第 13 周：LLM serving（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)
- [nano-vllm（约千行的 vLLM 最小实现，作参考）](https://github.com/GeeeekExplorer/nano-vllm)

本周任务：[w23-continuous-batching.md](../lab/w23-continuous-batching.md)

<a id="w24"></a>

## 第 24 周 · PagedAttention：分页管理 KV cache

**中文阅读（AIInfraGuide）**

- [PagedAttention](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第2章-推理引擎核心技术/21-pagedattention/)
- [nano-vllm：KV Cache 与 BlockManager](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第3章-nano-vllm源码解读/34-kvcache与blockmanager/)
- [nano-vllm：模型骨架与核心算子](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第3章-nano-vllm源码解读/33-模型与核心算子/)

**课程**

- [论文：vLLM / PagedAttention](https://arxiv.org/abs/2309.06180)
- [CMU 11-868 第 14 周：PagedAttention 与 vLLM（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)

本周任务：[w24-paged-attention.md](../lab/w24-paged-attention.md)

<a id="w25"></a>

## 第 25 周 · 权重量化

**中文阅读（AIInfraGuide）**

- [量化基础](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第4章-量化/41-量化基础/)
- [W8A8 与 SmoothQuant](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第4章-量化/42-w8a8与smoothquant/)
- [Weight-only INT4](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第4章-量化/43-weight-only-int4/) — 对应本周的 INT4 打包与分组量化
- [KV Cache 量化](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第4章-量化/44-kv-cache量化/)
- [（选读）FP8 与 NVFP4/MXFP4](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第4章-量化/45-fp8与nvfp4-mxfp4/)

**课程**

- [CMU 11-868 第 11–12 周：量化 I、II（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)
- [论文：GPTQ](https://arxiv.org/abs/2210.17323)
- [论文：AWQ](https://arxiv.org/abs/2306.00978)
- [ZOMI AIInfra 05 大模型推理（量化章节）](https://infrasys-ai.github.io/aiinfra-docs/) — 中文

本周任务：[w25-quantization.md](../lab/w25-quantization.md)

<a id="w26"></a>

## 第 26 周 · 投机解码

**中文阅读（AIInfraGuide）**

- [投机解码核心原理](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第5章-speculative-decoding/51-投机解码核心原理/)
- [Draft 模型与无模型方案](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第5章-speculative-decoding/52-draft模型与无模型方案/)
- [Medusa、EAGLE 与 MTP](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第5章-speculative-decoding/53-medusa与eagle/)
- [收益边界与限制](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第5章-speculative-decoding/54-收益边界与限制/)

**课程**

- [CMU 11-868 第 5 周：生成与投机解码（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)
- [论文：Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)

本周任务：[w26-speculative-decoding.md](../lab/w26-speculative-decoding.md)

<a id="w27"></a>

## 第 27 周 · 推理服务化与压测

**中文阅读（AIInfraGuide）**

- [Prefix Cache 与 RadixAttention](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第2章-推理引擎核心技术/23-prefix-cache-与-radixattention/)
- [Chunked Prefill 与统一调度](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第2章-推理引擎核心技术/24-chunked-prefill-与统一调度/)
- [nano-vllm：ModelRunner、CUDA Graph 与性能基准](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第3章-nano-vllm源码解读/36-modelrunner引擎循环与性能/)

**课程**

- [论文：SGLang（RadixAttention 前缀缓存）](https://arxiv.org/abs/2312.07104)
- [CMU 11-868 第 13 周：LLM serving with SGLang（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)

本周任务：[w27-serving-benchmark.md](../lab/w27-serving-benchmark.md)

<a id="w28"></a>

## 第 28 周 · 对标 vLLM，理解 PD 分离

**中文阅读（AIInfraGuide）**

- [Attention 后端与图优化](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第2章-推理引擎核心技术/25-attention-后端与图优化/)
- [量化选型与 vLLM 实战](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第4章-量化/46-量化选型与vllm实战/)
- [vLLM 投机解码实战](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第5章-speculative-decoding/55-vllm投机解码实战/)
- [第 7 章 PD 解耦架构](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第7章-pd解耦架构/第7章-pd解耦架构/) — 目前还是提纲，作者写完后再补读；这周先以课程为准

**课程**

- [论文：DistServe（prefill / decode 分离）](https://arxiv.org/abs/2401.09670)
- [CMU 11-868 第 15 周：DistServe、KV cache（课件）](https://llmsystem.github.io/llmsystem2026spring/docs/Syllabus)
- [vLLM 文档](https://docs.vllm.ai/)
- [Qwen3-0.6B（同量级参照模型）](https://huggingface.co/Qwen/Qwen3-0.6B)

本周任务：[w28-vllm-pd.md](../lab/w28-vllm-pd.md)

<a id="w29"></a>

## 第 29 周 · 缓冲周：第二段复盘

**中文阅读（AIInfraGuide）**

- [推理并行策略总览](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第6章-分布式推理/61-推理并行策略总览/)
- [张量并行推理](https://caomaolufei.github.io/AIInfraGuide/inference/模块四-推理优化/第6章-分布式推理/62-张量并行推理/)

本周任务：[w29-review-infer.md](../lab/w29-review-infer.md)
