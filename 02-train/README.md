<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 2 章：训练主线

> CS336 作业 1、2：一个模型从手写到分布式（第 9–21 周）

## 本章收获
本章结束时你会有：
- tokenizer 通过测试 + 资源估算笔记
- 完整的 Transformer LM
- 会讲故事的小模型 + 主线性能基线
- tag v0-baseline
- 迷你框架（可选）
- profiling 报告 + roofline 图
- GEMM 各版本性能对比表
- Triton RMSNorm + 显存优化对比
- FA2 前向 + 速度 / 显存对比
- 用上自写 FlashAttention 的训练
- 手写 DDP + 通信基准
- 分片训练 + 并行策略分析
- 1 → N 卡扩展效率曲线
- 第一段报告

## 知识点地图
1. 第 9 周 · 正式版 tokenizer + 资源估算（CS336 第 1–2 讲 · 作业 1）
2. 第 10 周 · 从零实现 Transformer 组件（CS336 第 3 讲 · 作业 1）
3. 第 11 周 · 训练基础设施 + 性能基线（CS336 第 4 讲（选看）· 作业 1）
4. 第 12 周 · 实验与消融，冻结基线（CS336 作业 1）
5. （可选 +2 周）手写深度学习框架（CMU 11-868 作业 2 · miniTorch）
6. 第 13 周 · GPU 硬件、profiling 与 roofline（CS336 第 5 讲 · 作业 2 §2）
7. 第 14 周 · CUDA 入门：逐步优化 GEMM（11-868 GPU 编程课件 · Simon Boehm）
8. 第 15 周 · Triton 与单卡显存优化（CS336 第 6 讲 · 作业 2 §3）
9. 第 16 周 · FlashAttention-2：前向（作业 2 §4）
10. 第 17 周 · FlashAttention-2：反向并接入模型（作业 2 §4）
11. 第 18 周 · 集合通信与手写 DDP（CS336 第 7 讲 · 作业 2 §5）
12. 第 19 周 · 优化器分片、FSDP 与并行策略（CS336 第 8 讲 · 作业 2 §6–8）
13. 第 20 周 · 张量并行与流水线并行（picotron · Playbook · 11-868 第 10 周）
14. 第 21 周 · 缓冲周：第一段复盘（补完 + 复盘）

## 讲义
每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。

| 周 | 主题 | 中文阅读 | 课程 |
|---|---|---|---|
| [9](lecture/README.md#w09) | 正式版 tokenizer + 资源估算 | 1 篇 | 4 项 |
| [10](lecture/README.md#w10) | 从零实现 Transformer 组件 | 3 篇 | 1 项 |
| [11](lecture/README.md#w11) | 训练基础设施 + 性能基线 | 2 篇 | 1 项 |
| [12](lecture/README.md#w12) | 实验与消融，冻结基线 | 1 篇 | 1 项 |
| [可选](lecture/README.md#w12x) | （可选 +2 周）手写深度学习框架 | 0 篇 | 3 项 |
| [13](lecture/README.md#w13) | GPU 硬件、profiling 与 roofline | 2 篇 | 4 项 |
| [14](lecture/README.md#w14) | CUDA 入门：逐步优化 GEMM | 7 篇 | 4 项 |
| [15](lecture/README.md#w15) | Triton 与单卡显存优化 | 4 篇 | 2 项 |
| [16](lecture/README.md#w16) | FlashAttention-2：前向 | 3 篇 | 3 项 |
| [17](lecture/README.md#w17) | FlashAttention-2：反向并接入模型 | 2 篇 | 1 项 |
| [18](lecture/README.md#w18) | 集合通信与手写 DDP | 3 篇 | 2 项 |
| [19](lecture/README.md#w19) | 优化器分片、FSDP 与并行策略 | 2 篇 | 3 项 |
| [20](lecture/README.md#w20) | 张量并行与流水线并行 | 3 篇 | 5 项 |
| [21](lecture/README.md#w21) | 缓冲周：第一段复盘 | 2 篇 | 0 项 |

## 动手实践
每周一个任务文件：目标、步骤、✅ 验收、提示和自测。在[网页版](https://lingquan11.github.io/ai-infra-plan/)里可以勾选进度，并一键把任务复制给 Muse，让它带你一步步做。

| 周 | 主题 | 课程 | 用时 | 硬件 | 本周产出 |
|---|---|---|---|---|---|
| [9](lab/w09-tokenizer-estimate.md) | 正式版 tokenizer + 资源估算 | CS336 第 1–2 讲 · 作业 1 | 12–15h | — | tokenizer 通过测试 + 资源估算笔记 |
| [10](lab/w10-transformer-lm.md) | 从零实现 Transformer 组件 | CS336 第 3 讲 · 作业 1 | 12–15h | — | 完整的 Transformer LM |
| [11](lab/w11-training-baseline.md) | 训练基础设施 + 性能基线 | CS336 第 4 讲（选看）· 作业 1 | 12–15h | — | 会讲故事的小模型 + 主线性能基线 |
| [12](lab/w12-ablation-baseline.md) | 实验与消融，冻结基线 | CS336 作业 1 | 10–12h | — | tag v0-baseline |
| [可选](lab/w12x-minitorch.md) | （可选 +2 周）手写深度学习框架 | CMU 11-868 作业 2 · miniTorch | 10–15h，共 2 周 | — | 迷你框架 |
| [13](lab/w13-profiling-roofline.md) | GPU 硬件、profiling 与 roofline | CS336 第 5 讲 · 作业 2 §2 | 12–15h | 单卡；先在 CPU 上调通正确性 | profiling 报告 + roofline 图 |
| [14](lab/w14-cuda-gemm.md) | CUDA 入门：逐步优化 GEMM | 11-868 GPU 编程课件 · Simon Boehm | 12–15h | 单卡，需要 CUDA 编译器 nvcc | GEMM 各版本性能对比表 |
| [15](lab/w15-triton-memory.md) | Triton 与单卡显存优化 | CS336 第 6 讲 · 作业 2 §3 | 12–15h | — | Triton RMSNorm + 显存优化对比 |
| [16](lab/w16-flashattn-forward.md) | FlashAttention-2：前向 | 作业 2 §4 | 12–15h | — | FA2 前向 + 速度 / 显存对比 |
| [17](lab/w17-flashattn-backward.md) | FlashAttention-2：反向并接入模型 | 作业 2 §4 | 12–15h | — | 用上自写 FlashAttention 的训练 |
| [18](lab/w18-collectives-ddp.md) | 集合通信与手写 DDP | CS336 第 7 讲 · 作业 2 §5 | 12–15h | 需要 2–4 张卡；正确性可先用 CPU 的 gloo 后端验证 | 手写 DDP + 通信基准 |
| [19](lab/w19-fsdp.md) | 优化器分片、FSDP 与并行策略 | CS336 第 8 讲 · 作业 2 §6–8 | 12–15h | 2–4 张卡 | 分片训练 + 并行策略分析 |
| [20](lab/w20-tp-pp.md) | 张量并行与流水线并行 | picotron · Playbook · 11-868 第 10 周 | 12–15h | 2–4 张卡 | 1 → N 卡扩展效率曲线 |
| [21](lab/w21-review-train.md) | 缓冲周：第一段复盘 | 补完 + 复盘 | 按需 | — | 第一段报告 |

## 成果展示
已产出 0 / 14 周，见[本章成果总表](showcase/README.md)。

还没有成果。每完成一周，按[成果总表](showcase/README.md)里的格式加一个目录。

## 与后续章节的关系
本章训练的模型，就是第 3 章推理引擎的对象。

过渡问题：为什么推理时 decode 阶段的瓶颈和训练完全不同？

下一章：[第 3 章 推理与服务](../03-infer/)（11-868 课件 + 给自己的模型写推理引擎）
