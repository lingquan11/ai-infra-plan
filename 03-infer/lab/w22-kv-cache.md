<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 22 周：KV cache 与 prefill / decode

> 课程：CS336 第 10 讲 ｜ 预计用时：12–15h
> 本周产出：带 KV cache 的推理 + 瓶颈分析

先读：[本周讲义](../lecture/README.md#w22)

## 任务一：KV cache 与 decode 瓶颈分析

**目标**：用数据证明 decode 受限于访存。

**步骤**

1. 给自己的模型写 generate：先写无缓存版本（每一步重算整个序列）
2. 加 KV cache：prefill 一次处理整个 prompt 并填充缓存，decode 每步只计算新 token 并追加 K、V
3. 分别测 prefill 和 decode 的吞吐
4. 算出 decode 一步的 FLOPs 和需要读取的字节数（权重 + KV cache），得出算术强度，对照第 13 周的 roofline
5. 测 batch size 从 1 到 64 时 decode 的吞吐和每 token 延迟

**验收**

- ✅ 数据证明 decode 受限于访存
- ✅ 一条 batch size 与吞吐 / 延迟的曲线

## 自测（周末）

1. 秒答 prefill 为什么快、decode 为什么慢（计算受限 vs 访存受限）
2. 手算 7B 模型（32 层、32 头、head_dim 128）在上下文 4096、batch 16、FP16 下的 KV cache 总量（约 32GB），判断 80GB 显卡还剩多少空间

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w22-kv-cache/`，格式见成果总表。
