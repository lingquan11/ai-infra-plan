<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 10 周：从零实现 Transformer 组件

> 课程：CS336 第 3 讲 · 作业 1 ｜ 预计用时：12–15h
> 本周产出：完整的 Transformer LM

先读：[本周讲义](../lecture/README.md#w10)

## 任务一：[作业 1] 从零实现 Transformer LM

**目标**：不用现成的层，从参数开始写出一个现代 Transformer。

**步骤**

1. 用 nn.Parameter 实现无偏置的 Linear（截断正态初始化）和 Embedding
2. 实现 RMSNorm：计算时先转成 float32，最后转回原 dtype
3. 实现 SwiGLU 前馈层
4. 实现 RoPE 旋转位置编码，预先计算并缓存 cos、sin
5. 实现数值稳定的 softmax（减去最大值）和支持掩码的缩放点积注意力
6. 实现带因果掩码和 RoPE 的多头自注意力
7. 组装 pre-norm Transformer block 和完整的 Transformer LM，通过 adapters.py 接上测试

**验收**

- ✅ 组件相关测试全部通过

**提示**：einops 能让形状变换更清楚，不容易写错。

## 自测（周末）

1. 不看资料画出 Pre-Norm Decoder Block：RMSNorm → 带掩码的自注意力 → 残差 → RMSNorm → FFN → 残差，标出每一步的张量形状，说清 Q、K、V 怎么由线性投影得到

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w10-transformer-lm/`，格式见成果总表。
