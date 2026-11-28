<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 9 周：正式版 tokenizer + 资源估算

> 课程：CS336 第 1–2 讲 · 作业 1 ｜ 预计用时：12–15h
> 本周产出：tokenizer 通过测试 + 资源估算笔记

先读：[本周讲义](../lecture/README.md#w09)

## 任务一：[作业 1] 能在大语料上训练的 BPE

**目标**：把第 7 周的 BPE 写成能在几 GB 语料上训练的版本。

**步骤**

1. clone 作业 1 仓库，按 README 用 uv 装环境，下载 TinyStories 数据
2. 实现 BPE 训练：GPT-2 正则预切分、特殊 token 不参与合并、统计字节对并迭代合并
3. 提速一：预切分用多进程并行处理文件的不同分块（在特殊 token 处切块）
4. 提速二：合并时只增量更新受影响的字节对计数，不要每轮全量重算
5. 实现 Tokenizer 类：encode、decode，以及对大文件逐行流式处理的 encode_iterable
6. 在 TinyStories 上训练 1 万的词表，记录耗时、峰值内存和最长的 token

**验收**

- ✅ 仓库测试中 tokenizer 相关部分通过
- ✅ 耗时和内存记入笔记

**提示**：先用 cProfile 找出最慢的函数再优化。

## 任务二：手算模型的资源账

**目标**：建立贯穿全程的「算账」能力。

**步骤**

1. 以 GPT-2 small 规模为例（12 层，d_model 768，词表约 5 万，上下文 1024）
2. 分别算出 embedding、注意力、前馈层的参数量，再求总和
3. 算一次前向中所有矩阵乘的 FLOPs（每次乘加记 2 FLOPs）
4. 训练一步约等于前向的 3 倍，推出训练总 FLOPs ≈ 6 × 参数量 × token 数
5. 算 AdamW 训练的显存：参数、梯度、两份优化器状态，再估算激活
6. 写进 notes/accounting.md

**验收**

- ✅ 参数量与 sum(p.numel() for p in model.parameters()) 一致
- ✅ 能解释 6ND 公式的来历

## 自测（周末）

1. 给定 7B 模型配置（hidden 4096、32 头、32 层、SwiGLU 中间维度 11008、词表 32000），手算总参数量，误差在 20% 以内（约 6.7B）

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w09-tokenizer-estimate/`，格式见成果总表。
