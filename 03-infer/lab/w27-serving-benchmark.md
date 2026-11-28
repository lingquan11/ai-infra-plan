<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 27 周：推理服务化与压测

> 课程：SGLang · 11-868 第 13 周 ｜ 预计用时：12–15h
> 本周产出：OpenAI 兼容服务 + 压测报告

先读：[本周讲义](../lecture/README.md#w27)

## 任务一：OpenAI 兼容服务 + 压测

**目标**：把引擎变成能被真实流量调用的服务，并用指标衡量它。

**步骤**

1. 用 FastAPI 实现兼容 OpenAI 的 /v1/completions 和 /v1/chat/completions，支持流式输出（SSE）
2. 引擎在独立循环中运行，请求通过异步队列进出
3. 前缀缓存：对 prompt 前缀对应的 KV 块做哈希复用
4. chunked prefill：把长 prompt 分块，与 decode 混合调度
5. 写压测脚本：按泊松到达率发送请求，统计 TTFT、TPOT、吞吐和 P50 / P99
6. 画出 QPS-延迟曲线

**验收**

- ✅ 能用 OpenAI 官方 SDK 调用你的服务
- ✅ 一份压测报告

## 自测（周末）

1. 你的压测报告至少包含 QPS、TTFT（P50/P95）、TPOT（P50/P95）、吞吐、显存峰值、GPU 利用率；所有压测配置写在一个文件里，两次测试之间只改一个变量

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w27-serving-benchmark/`，格式见成果总表。
