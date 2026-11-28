<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 33 周：GPU 调度与分布式训练任务

> 课程：ZOMI AIInfra 03 ｜ 预计用时：12–15h ｜ 硬件：kind 上可以不用 GPU 练调度；验证 GPU 调度需要短期租一个带 GPU 的云 K8s
> 本周产出：可调度的训练与推理

先读：[本周讲义](../lecture/README.md#w33)

## 任务一：调度训练任务，自动扩缩容推理

**目标**：让集群自动给训练和推理分配资源。

**步骤**

1. 了解 device plugin 如何把 nvidia.com/gpu 暴露为可调度资源
2. 安装 Kueue（或 Volcano），配置队列和配额
3. 理解 gang 调度为什么对分布式训练必不可少（避免一部分 worker 拿到资源、其余在等，造成死锁）
4. 安装 Kubeflow Trainer，把第 18–19 周的分布式训练打包提交（kind 上用 CPU + gloo）
5. 用 KEDA 或 HPA，按推理服务的请求队列长度自动扩缩容副本

**验收**

- ✅ 一条命令提交训练任务
- ✅ 压测时推理副本自动扩容

## 自测（周末）

1. 解释为什么 LLM 服务不能只按 GPU 利用率扩缩容，而要结合排队请求数、KV cache 使用率和 TTFT

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w33-gpu-scheduling/`，格式见成果总表。
