<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 34 周：监控、故障恢复与全链路

> 课程：ZOMI AIInfra 03 ｜ 预计用时：12–15h
> 本周产出：全链路平台

先读：[本周讲义](../lecture/README.md#w34)

## 任务一：监控、故障注入和全链路演示

**目标**：把训练到上线串成一条可观测、能自动恢复的流水线。

**步骤**

1. 用 kube-prometheus-stack 部署 Prometheus + Grafana
2. 在 GPU 节点部署 dcgm-exporter，做 GPU 利用率、显存、功耗面板
3. 让推理服务暴露自定义指标：TTFT、队列长度、吞吐
4. 故障注入：训练中删除一个 worker pod，确认任务能从最近的 checkpoint 恢复
5. 串起全链路：提交训练 → 保存 checkpoint → 部署为推理服务 → 监控面板

**验收**

- ✅ 一份全链路演示文档或录屏
- ✅ 恢复过程有日志为证

## 自测（周末）

1. 某次提交后 TPOT P95 退化了 15%：说出你会怎样用 git bisect 定位提交，再用 Nsight Systems 对比前后的 trace 找原因

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w34-monitoring/`，格式见成果总表。
