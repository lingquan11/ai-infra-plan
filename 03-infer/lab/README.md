<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 3 章动手实践：推理与服务

每周一个任务文件：目标、步骤、✅ 验收、提示和自测。[网页版](https://lingquan11.github.io/ai-infra-plan/)里可以勾选进度，并一键把任务复制给 Muse，让它带你一步步做。

| 周 | 主题 | 课程 | 用时 | 硬件 | 本周产出 |
|---|---|---|---|---|---|
| [22](w22-kv-cache.md) | KV cache 与 prefill / decode | CS336 第 10 讲 | 12–15h | — | 带 KV cache 的推理 + 瓶颈分析 |
| [23](w23-continuous-batching.md) | 从静态 batching 到 continuous batching | Orca · 11-868 第 13 周 | 12–15h | — | continuous batching 调度器 |
| [24](w24-paged-attention.md) | PagedAttention：分页管理 KV cache | vLLM 论文 · 11-868 第 14 周 | 12–15h | — | 分页 KV cache |
| [25](w25-quantization.md) | 权重量化 | 11-868 第 11–12 周 | 12–15h | — | 量化推理 |
| [26](w26-speculative-decoding.md) | 投机解码 | 11-868 第 5 周 | 10–12h | — | 投机解码 + 加速比 |
| [27](w27-serving-benchmark.md) | 推理服务化与压测 | SGLang · 11-868 第 13 周 | 12–15h | — | OpenAI 兼容服务 + 压测报告 |
| [28](w28-vllm-pd.md) | 对标 vLLM，理解 PD 分离 | DistServe · 11-868 第 15 周 | 12–15h | — | 差距分析报告 |
| [29](w29-review-infer.md) | 缓冲周：第二段复盘 | 补完 + 复盘 | 按需 | — | 第二段报告 |
