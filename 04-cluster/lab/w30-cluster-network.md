<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 30 周：AI 集群与网络通信

> 课程：ZOMI AIInfra 01–02 ｜ 预计用时：10–12h ｜ 硬件：短期租一台多卡机器
> 本周产出：通信实测报告

先读：[本周讲义](../lecture/README.md#w30)

## 任务一：实测集群通信

**目标**：把通信理论和真实硬件对上。

**步骤**

1. 租一台多卡机器（最好带 NVLink），用 nvidia-smi topo -m 查看 GPU 互联拓扑
2. 编译 nccl-tests，运行 all_reduce_perf 和 all_gather_perf，记录 algbw 和 busbw
3. 如果能租到 PCIe 互联的机器，对比 NVLink 和 PCIe
4. 用第 18 周的 α-β 模型对照实测结果

**验收**

- ✅ 一张实测带宽与理论值的对比表

## 自测（周末）

1. 看懂 nvidia-smi topo -m 输出中的 NV12、SYS、NODE 等标记，判断哪些卡之间走 NVLink、哪些走 PCIe
2. 估算 2GB 梯度做 AllReduce 时，在 NVLink 和 PCIe Gen5 下的理论耗时差异

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w30-cluster-network/`，格式见成果总表。
