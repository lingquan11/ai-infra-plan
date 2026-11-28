<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 6 周：Transformer：从注意力到 GPT

> 课程：Karpathy Let's build GPT ｜ 预计用时：12–15h
> 本周产出：字符级 GPT

先读：[本周讲义](../lecture/README.md#w06)

## 任务一：从零写字符级 GPT

**目标**：亲手搭出一个 decoder-only Transformer 并训练它。

**步骤**

1. 下载 tiny shakespeare（约 1MB 文本），做字符级编码和 90/10 的训练、验证划分
2. 先写 bigram 基线，搭好训练和采样框架
3. 实现单头自注意力：Q、K、V 投影，缩放点积，下三角因果掩码，softmax
4. 扩展为多头注意力，加上前馈层、残差连接和 LayerNorm（pre-norm），组成 block
5. 堆叠多个 block，加入位置嵌入和 dropout，训练并采样生成文本
6. 每加一个部件，就记录一次验证集 loss

**验收**

- ✅ 生成的文本有莎士比亚剧本的格式和词汇
- ✅ 能画出一个 block 内张量形状 (B, T, C) 的变化，并讲清因果掩码的作用

**提示**：先用很小的配置（2 层、64 维）在 CPU 上调通，再放大。

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w06-transformer-gpt/`，格式见成果总表。
