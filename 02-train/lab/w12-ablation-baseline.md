<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 12 周：实验与消融，冻结基线

> 课程：CS336 作业 1 ｜ 预计用时：10–12h
> 本周产出：tag v0-baseline

先读：[本周讲义](../lecture/README.md#w12)

## 任务一：[作业 1] 实验与消融

**目标**：学会用实验回答「这个设计为什么存在」。

**步骤**

1. 学习率扫描：找到最佳值和开始发散的边界
2. 改变 batch size，观察对效果和吞吐的影响
3. 消融：去掉 RMSNorm、改成 post-norm、去掉 RoPE、把 SwiGLU 换成参数量相当的 SiLU 前馈
4. 在 OpenWebText 子集上训练，与 TinyStories 对比
5. 每个实验画 loss 曲线并写一句结论

**验收**

- ✅ 每个实验都有曲线和结论
- ✅ 打 git tag v0-baseline，作为整个计划的基线

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w12-ablation-baseline/`，格式见成果总表。
