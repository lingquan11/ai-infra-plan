<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 2 章动手实践：训练主线

每周一个任务文件：目标、步骤、✅ 验收、提示和自测。[网页版](https://lingquan11.github.io/ai-infra-plan/)里可以勾选进度，并一键把任务复制给 Muse，让它带你一步步做。

| 周 | 主题 | 课程 | 用时 | 硬件 | 本周产出 |
|---|---|---|---|---|---|
| [9](w09-tokenizer-estimate.md) | 正式版 tokenizer + 资源估算 | CS336 第 1–2 讲 · 作业 1 | 12–15h | — | tokenizer 通过测试 + 资源估算笔记 |
| [10](w10-transformer-lm.md) | 从零实现 Transformer 组件 | CS336 第 3 讲 · 作业 1 | 12–15h | — | 完整的 Transformer LM |
| [11](w11-training-baseline.md) | 训练基础设施 + 性能基线 | CS336 第 4 讲（选看）· 作业 1 | 12–15h | — | 会讲故事的小模型 + 主线性能基线 |
| [12](w12-ablation-baseline.md) | 实验与消融，冻结基线 | CS336 作业 1 | 10–12h | — | tag v0-baseline |
| [可选](w12x-minitorch.md) | （可选 +2 周）手写深度学习框架 | CMU 11-868 作业 2 · miniTorch | 10–15h，共 2 周 | — | 迷你框架 |
| [13](w13-profiling-roofline.md) | GPU 硬件、profiling 与 roofline | CS336 第 5 讲 · 作业 2 §2 | 12–15h | 单卡；先在 CPU 上调通正确性 | profiling 报告 + roofline 图 |
| [14](w14-cuda-gemm.md) | CUDA 入门：逐步优化 GEMM | 11-868 GPU 编程课件 · Simon Boehm | 12–15h | 单卡，需要 CUDA 编译器 nvcc | GEMM 各版本性能对比表 |
| [15](w15-triton-memory.md) | Triton 与单卡显存优化 | CS336 第 6 讲 · 作业 2 §3 | 12–15h | — | Triton RMSNorm + 显存优化对比 |
| [16](w16-flashattn-forward.md) | FlashAttention-2：前向 | 作业 2 §4 | 12–15h | — | FA2 前向 + 速度 / 显存对比 |
| [17](w17-flashattn-backward.md) | FlashAttention-2：反向并接入模型 | 作业 2 §4 | 12–15h | — | 用上自写 FlashAttention 的训练 |
| [18](w18-collectives-ddp.md) | 集合通信与手写 DDP | CS336 第 7 讲 · 作业 2 §5 | 12–15h | 需要 2–4 张卡；正确性可先用 CPU 的 gloo 后端验证 | 手写 DDP + 通信基准 |
| [19](w19-fsdp.md) | 优化器分片、FSDP 与并行策略 | CS336 第 8 讲 · 作业 2 §6–8 | 12–15h | 2–4 张卡 | 分片训练 + 并行策略分析 |
| [20](w20-tp-pp.md) | 张量并行与流水线并行 | picotron · Playbook · 11-868 第 10 周 | 12–15h | 2–4 张卡 | 1 → N 卡扩展效率曲线 |
| [21](w21-review-train.md) | 缓冲周：第一段复盘 | 补完 + 复盘 | 按需 | — | 第一段报告 |
