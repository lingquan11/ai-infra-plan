<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 3 章：推理与服务

> 11-868 课件 + 给自己的模型写推理引擎（第 22–29 周）

## 本章收获
本章结束时你会有：
- 带 KV cache 的推理 + 瓶颈分析
- continuous batching 调度器
- 分页 KV cache
- 量化推理
- 投机解码 + 加速比
- OpenAI 兼容服务 + 压测报告
- 差距分析报告
- 第二段报告

## 知识点地图
1. 第 22 周 · KV cache 与 prefill / decode（CS336 第 10 讲）
2. 第 23 周 · 从静态 batching 到 continuous batching（Orca · 11-868 第 13 周）
3. 第 24 周 · PagedAttention：分页管理 KV cache（vLLM 论文 · 11-868 第 14 周）
4. 第 25 周 · 权重量化（11-868 第 11–12 周）
5. 第 26 周 · 投机解码（11-868 第 5 周）
6. 第 27 周 · 推理服务化与压测（SGLang · 11-868 第 13 周）
7. 第 28 周 · 对标 vLLM，理解 PD 分离（DistServe · 11-868 第 15 周）
8. 第 29 周 · 缓冲周：第二段复盘（补完 + 复盘）

## 讲义
每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。

| 周 | 主题 | 中文阅读 | 课程 |
|---|---|---|---|
| [22](lecture/README.md#w22) | KV cache 与 prefill / decode | 2 篇 | 2 项 |
| [23](lecture/README.md#w23) | 从静态 batching 到 continuous batching | 4 篇 | 3 项 |
| [24](lecture/README.md#w24) | PagedAttention：分页管理 KV cache | 3 篇 | 2 项 |
| [25](lecture/README.md#w25) | 权重量化 | 5 篇 | 4 项 |
| [26](lecture/README.md#w26) | 投机解码 | 4 篇 | 2 项 |
| [27](lecture/README.md#w27) | 推理服务化与压测 | 3 篇 | 2 项 |
| [28](lecture/README.md#w28) | 对标 vLLM，理解 PD 分离 | 4 篇 | 4 项 |
| [29](lecture/README.md#w29) | 缓冲周：第二段复盘 | 2 篇 | 0 项 |

## 动手实践
每周一个任务文件：目标、步骤、✅ 验收、提示和自测。在[网页版](https://lingquan11.github.io/ai-infra-plan/)里可以勾选进度，并一键把任务复制给 Muse，让它带你一步步做。

| 周 | 主题 | 课程 | 用时 | 硬件 | 本周产出 |
|---|---|---|---|---|---|
| [22](lab/w22-kv-cache.md) | KV cache 与 prefill / decode | CS336 第 10 讲 | 12–15h | — | 带 KV cache 的推理 + 瓶颈分析 |
| [23](lab/w23-continuous-batching.md) | 从静态 batching 到 continuous batching | Orca · 11-868 第 13 周 | 12–15h | — | continuous batching 调度器 |
| [24](lab/w24-paged-attention.md) | PagedAttention：分页管理 KV cache | vLLM 论文 · 11-868 第 14 周 | 12–15h | — | 分页 KV cache |
| [25](lab/w25-quantization.md) | 权重量化 | 11-868 第 11–12 周 | 12–15h | — | 量化推理 |
| [26](lab/w26-speculative-decoding.md) | 投机解码 | 11-868 第 5 周 | 10–12h | — | 投机解码 + 加速比 |
| [27](lab/w27-serving-benchmark.md) | 推理服务化与压测 | SGLang · 11-868 第 13 周 | 12–15h | — | OpenAI 兼容服务 + 压测报告 |
| [28](lab/w28-vllm-pd.md) | 对标 vLLM，理解 PD 分离 | DistServe · 11-868 第 15 周 | 12–15h | — | 差距分析报告 |
| [29](lab/w29-review-infer.md) | 缓冲周：第二段复盘 | 补完 + 复盘 | 按需 | — | 第二段报告 |

## 成果展示
已产出 0 / 8 周，见[本章成果总表](showcase/README.md)。

还没有成果。每完成一周，按[成果总表](showcase/README.md)里的格式加一个目录。

## 与后续章节的关系
本章的推理服务在第 4 章部署到集群上。

过渡问题：训练任务和多个推理服务要共用一个集群时，资源该怎么分？

下一章：[第 4 章 集群与平台](../04-cluster/)（ZOMI AIInfra：通信、存储、调度、监控）
