<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 28 周：对标 vLLM，理解 PD 分离

> 课程：DistServe · 11-868 第 15 周 ｜ 预计用时：12–15h
> 本周产出：差距分析报告

先读：[本周讲义](../lecture/README.md#w28)

## 任务一：与 vLLM 对比并分析差距

**目标**：找到自己的实现和工业系统差在哪里。

**步骤**

1. 用 vLLM 部署一个参数量相近的开源模型（如 Qwen3-0.6B），用同一套压测脚本测试
2. 精读 vLLM 调度器：请求状态流转、抢占策略、chunked prefill
3. 对比你的实现，逐项找差距来源：kernel、调度、CUDA Graph、采样等
4. 读 DistServe，写出 prefill / decode 分离部署在什么负载下有收益

**验收**

- ✅ 一份差距分析报告

## 自测（周末）

1. 解释 goodput：为什么 QPS 很高用户仍嫌慢，满足 SLO 的请求占比才是真正的服务质量
2. 给出推理框架选型的结构化回答：什么场景选 vLLM、什么场景选 SGLang、什么场景值得上 TensorRT-LLM

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w28-vllm-pd/`，格式见成果总表。
