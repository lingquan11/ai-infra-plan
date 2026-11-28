<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 7 周：Tokenizer：从零写 BPE

> 课程：Karpathy Let's build the GPT Tokenizer ｜ 预计用时：10–12h
> 本周产出：自己写的 BPE（第 9 周会写正式版）

先读：[本周讲义](../lecture/README.md#w07)

## 任务一：实现字节级 BPE tokenizer

**目标**：理解大模型如何把文本切成 token，为第 9 周的正式版打基础。

**步骤**

1. 理解 Unicode 码点和 UTF-8 编码，把文本转成字节序列（0–255）
2. 统计相邻字节对的频次，把最频繁的一对合并成新 token 并记录合并规则，重复到目标词表大小
3. 实现 encode：按学到的合并顺序把字节序列压缩成 token
4. 实现 decode：把 token 还原为字节，再解码为文本
5. 加入 GPT-2 风格的正则预切分：先把文本切成词块，再在块内做 BPE
6. 支持特殊 token（例如 <|endoftext|>），它不参与合并
7. 在几 MB 的文本上训练一个约 1000 的词表

**验收**

- ✅ 任意文本都满足 decode(encode(x)) == x
- ✅ 能解释为什么需要预切分

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w07-bpe-tokenizer/`，格式见成果总表。
