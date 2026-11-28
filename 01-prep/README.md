<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 1 章：预备段

> Linux、PyTorch、Transformer 入门（第 1–8 周）

## 本章收获
第 8 周的出口检查，进入下一章之前逐条确认：
- 能 ssh 到远程机器，用 tmux 挂训练任务，用 git 提交代码
- 不看资料写出完整的 PyTorch 训练循环（数据加载、前向、loss、反向、更新、保存 checkpoint）
- 讲清注意力中 (B, T, C) 的形状变化和因果掩码的作用
- 讲清 BPE 是怎样一步步合并出词表的

## 知识点地图
1. 第 1 周 · Linux 基础：终端与 shell（MIT Missing Semester）
2. 第 2 周 · Linux 进阶：远程、Git 与主线仓库（MIT Missing Semester）
3. 第 3 周 · 自动微分与 PyTorch 基础（Karpathy Zero to Hero 第 1 集）
4. 第 4 周 · 语言模型入门：bigram 与 MLP（Karpathy makemore 第 1–2 集）
5. 第 5 周 · 训练动态与手写反向传播（Karpathy makemore 第 3–4 集）
6. 第 6 周 · Transformer：从注意力到 GPT（Karpathy Let's build GPT）
7. 第 7 周 · Tokenizer：从零写 BPE（Karpathy Let's build the GPT Tokenizer）
8. 第 8 周 · 预览训练优化 + 租卡实操（Karpathy Let's reproduce GPT-2）

## 讲义
每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。

| 周 | 主题 | 中文阅读 | 课程 |
|---|---|---|---|
| [1](lecture/README.md#w01) | Linux 基础：终端与 shell | 1 篇 | 3 项 |
| [2](lecture/README.md#w02) | Linux 进阶：远程、Git 与主线仓库 | 1 篇 | 2 项 |
| [3](lecture/README.md#w03) | 自动微分与 PyTorch 基础 | 2 篇 | 3 项 |
| [4](lecture/README.md#w04) | 语言模型入门：bigram 与 MLP | 2 篇 | 3 项 |
| [5](lecture/README.md#w05) | 训练动态与手写反向传播 | 1 篇 | 3 项 |
| [6](lecture/README.md#w06) | Transformer：从注意力到 GPT | 3 篇 | 5 项 |
| [7](lecture/README.md#w07) | Tokenizer：从零写 BPE | 1 篇 | 2 项 |
| [8](lecture/README.md#w08) | 预览训练优化 + 租卡实操 | 1 篇 | 2 项 |

## 动手实践
每周一个任务文件：目标、步骤、✅ 验收、提示和自测。在[网页版](https://lingquan11.github.io/ai-infra-plan/)里可以勾选进度，并一键把任务复制给 Muse，让它带你一步步做。

| 周 | 主题 | 课程 | 用时 | 硬件 | 本周产出 |
|---|---|---|---|---|---|
| [1](lab/w01-linux-shell.md) | Linux 基础：终端与 shell | MIT Missing Semester | 10–12h | — | 可用的终端环境 + 第一个 bash 脚本 |
| [2](lab/w02-remote-git.md) | Linux 进阶：远程、Git 与主线仓库 | MIT Missing Semester | 10–12h | — | 主线仓库 + 性能日志模板 |
| [3](lab/w03-autograd-pytorch.md) | 自动微分与 PyTorch 基础 | Karpathy Zero to Hero 第 1 集 | 12–15h | — | micrograd + FashionMNIST 分类器 |
| [4](lab/w04-bigram-mlp.md) | 语言模型入门：bigram 与 MLP | Karpathy makemore 第 1–2 集 | 10–12h | — | 能生成名字的 MLP 语言模型 |
| [5](lab/w05-backprop.md) | 训练动态与手写反向传播 | Karpathy makemore 第 3–4 集 | 12–15h | — | 对反向传播计算量和激活显存的直观理解 |
| [6](lab/w06-transformer-gpt.md) | Transformer：从注意力到 GPT | Karpathy Let's build GPT | 12–15h | — | 字符级 GPT |
| [7](lab/w07-bpe-tokenizer.md) | Tokenizer：从零写 BPE | Karpathy Let's build the GPT Tokenizer | 10–12h | — | 自己写的 BPE（第 9 周会写正式版） |
| [8](lab/w08-gpt2-preview.md) | 预览训练优化 + 租卡实操 | Karpathy Let's reproduce GPT-2 | 12–15h | 按小时租一张云 GPU | 第一批性能日志 + 优化清单 |

## 成果展示
已产出 0 / 8 周，见[本章成果总表](showcase/README.md)。

还没有成果。每完成一周，按[成果总表](showcase/README.md)里的格式加一个目录。

## 与后续章节的关系
第 8 周的出口检查通过后进入第 2 章。

过渡问题：这些优化你已经会用了，可它们内部是怎么工作的？主线会逐个拆开。

下一章：[第 2 章 训练主线](../02-train/)（CS336 作业 1、2：一个模型从手写到分布式）
