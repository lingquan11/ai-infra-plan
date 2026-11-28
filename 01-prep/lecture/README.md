<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 1 章讲义：预备段

每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。自己的笔记放在 `lecture/notes/`（手写，脚本不会覆盖）。

<a id="w01"></a>

## 第 1 周 · Linux 基础：终端与 shell

**中文阅读（AIInfraGuide）**

- [AI Infra 学习路线](https://caomaolufei.github.io/AIInfraGuide/guides/ai-infra学习路线/) — 先读「全景概览」和「第零层：前置知识」，知道整条路怎么走

**课程**

- [Missing Semester：课程概览与 shell、shell 工具与脚本、编辑器（vim）](https://missing.csail.mit.edu/)
- [中文版：计算机教育中缺失的一课](https://missing-semester-cn.github.io/) — 同一课程的中文翻译
- [安装 WSL2（Windows 用户）](https://learn.microsoft.com/windows/wsl/install)

本周任务：[w01-linux-shell.md](../lab/w01-linux-shell.md)

<a id="w02"></a>

## 第 2 周 · Linux 进阶：远程、Git 与主线仓库

**中文阅读（AIInfraGuide）**

- [编程语言基础](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/第1章-编程语言基础/) — 重点读 Linux 与开发环境、Python 工程化部分

**课程**

- [Missing Semester：数据处理、命令行环境、版本控制（Git）、调试与性能分析](https://missing.csail.mit.edu/)
- [Pro Git 中文版（前三章）](https://git-scm.com/book/zh/v2)

本周任务：[w02-remote-git.md](../lab/w02-remote-git.md)

<a id="w03"></a>

## 第 3 周 · 自动微分与 PyTorch 基础

**中文阅读（AIInfraGuide）**

- [PyTorch 框架快速入门篇](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/pyroch/pytorch框架入门/)
- [数学基础](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/第2章-数学基础/) — 读反向传播、Softmax 与交叉熵部分

**课程**

- [Karpathy：building micrograd（从零讲反向传播）](https://youtu.be/VMj-3S1tku0)
- [PyTorch 官方教程 Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)
- [《动手学深度学习》第 2 章 预备知识](https://zh.d2l.ai/chapter_preliminaries/index.html) — 中文

本周任务：[w03-autograd-pytorch.md](../lab/w03-autograd-pytorch.md)

<a id="w04"></a>

## 第 4 周 · 语言模型入门：bigram 与 MLP

**中文阅读（AIInfraGuide）**

- [AI Infra 工程师为什么必须懂 Transformer](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/31-ai-infra工程师为什么必须懂transformer/)
- [数学基础](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/第2章-数学基础/) — 读线性代数与矩阵维度部分

**课程**

- [Karpathy：building makemore（bigram 语言模型）](https://youtu.be/PaCmpygFfXo)
- [Karpathy：makemore Part 2: MLP](https://youtu.be/TCH_1BHY58I)
- [3Blue1Brown 神经网络系列（前 4 章）](https://www.3blue1brown.com/topics/neural-networks)

本周任务：[w04-bigram-mlp.md](../lab/w04-bigram-mlp.md)

<a id="w05"></a>

## 第 5 周 · 训练动态与手写反向传播

**中文阅读（AIInfraGuide）**

- [LayerNorm 与残差连接深入理解](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/36-layernorm与残差连接深入理解/) — 和本周的 BatchNorm 对照着读

**课程**

- [Karpathy：makemore Part 3: Activations & Gradients, BatchNorm](https://youtu.be/P6sfmUTpUmc)
- [Karpathy：makemore Part 4: Becoming a Backprop Ninja](https://youtu.be/q8SA3rM6ckI)
- [（选看）makemore Part 5: Building a WaveNet](https://youtu.be/t3YJ5hKiMQ0)

本周任务：[w05-backprop.md](../lab/w05-backprop.md)

<a id="w06"></a>

## 第 6 周 · Transformer：从注意力到 GPT

**中文阅读（AIInfraGuide）**

- [Transformer 架构：快速入门篇](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/transformer架构快速入门/)
- [Transformer 全貌及代码实现](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/32-transformer全貌及代码实现/)
- [Self-Attention 机制深入理解](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/33-self-attention机制深入理解/)

**课程**

- [3Blue1Brown：Transformer 与注意力（神经网络系列后几章）](https://www.3blue1brown.com/topics/neural-networks)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [论文：Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [《动手学深度学习》第 10 章 注意力机制](https://zh.d2l.ai/chapter_attention-mechanisms/index.html) — 中文
- [Karpathy：Let's build GPT: from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY)

本周任务：[w06-transformer-gpt.md](../lab/w06-transformer-gpt.md)

<a id="w07"></a>

## 第 7 周 · Tokenizer：从零写 BPE

**中文阅读（AIInfraGuide）**

- [Tokenization 与词嵌入](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/transformer/39-tokenization与词嵌入/)

**课程**

- [Karpathy：Let's build the GPT Tokenizer](https://youtu.be/zduSFxRajkE)
- [minbpe 仓库（含练习说明）](https://github.com/karpathy/minbpe)

本周任务：[w07-bpe-tokenizer.md](../lab/w07-bpe-tokenizer.md)

<a id="w08"></a>

## 第 8 周 · 预览训练优化 + 租卡实操

**中文阅读（AIInfraGuide）**

- [数学基础](https://caomaolufei.github.io/AIInfraGuide/prerequisites/模块一-前置知识/第2章-数学基础/) — 读数值计算与混合精度部分，对应本周打开的 BF16

**课程**

- [Karpathy：Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU)
- [配套代码 build-nanogpt](https://github.com/karpathy/build-nanogpt)

本周任务：[w08-gpt2-preview.md](../lab/w08-gpt2-preview.md)
