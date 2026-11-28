<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 32 周：容器与 Kubernetes 基础

> 课程：ZOMI AIInfra 03 ｜ 预计用时：10–12h ｜ 硬件：本地 kind 集群即可，不需要 GPU
> 本周产出：运行在 K8s 上的推理服务

先读：[本周讲义](../lecture/README.md#w32)

## 任务一：容器化并部署到本地 K8s

**目标**：让训练和推理都能以容器方式运行。

**步骤**

1. 为训练脚本和推理服务分别写 Dockerfile（基于 PyTorch 官方镜像，用多阶段构建控制体积）
2. 用 kind 起一个本地集群，熟悉 kubectl get、describe、logs、exec
3. 用 Deployment + Service 部署推理服务（CPU 模式或小模型），配置就绪和存活探针、资源 requests / limits
4. 用 ConfigMap 传配置，从集群外调用服务
5. 滚动更新镜像，观察服务是否中断

**验收**

- ✅ 推理服务在 kind 集群中可以访问
- ✅ 滚动更新时服务不中断

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w32-k8s-basics/`，格式见成果总表。
