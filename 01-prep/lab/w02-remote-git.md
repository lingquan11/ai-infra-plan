<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 2 周：Linux 进阶：远程、Git 与主线仓库

> 课程：MIT Missing Semester ｜ 预计用时：10–12h
> 本周产出：主线仓库 + 性能日志模板

先读：[本周讲义](../lecture/README.md#w02)

## 任务一：ssh、tmux 与资源查看

**目标**：能远程登录服务器，让任务在断开连接后继续运行。

**步骤**

1. 用 ssh-keygen 生成密钥，用密钥登录一台远程机器（云主机，或在 WSL 里开 sshd 练习）
2. 在 ~/.ssh/config 中给机器配别名，之后用 ssh 别名 登录
3. 用 scp 或 rsync 双向传文件
4. tmux：新建会话、分屏、detach 后重新 attach；在里面运行一个每秒打印时间的脚本，断开 ssh 再连回，确认仍在运行
5. 用 htop、free -h、df -h、du -sh 查看资源；有 GPU 时用 nvidia-smi

**验收**

- ✅ 断开 ssh 再连上，tmux 中的任务仍在运行
- ✅ 能用一条 rsync 命令把本地目录同步到服务器

**提示**：tmux 的前缀键默认是 Ctrl-b，按完前缀再按 d 就是 detach。

## 任务二：Python 环境与主线仓库

**目标**：建好后面 34 周都在用的代码仓库和性能日志。

**步骤**

1. 安装 uv（或 conda），为本计划建一个虚拟环境
2. 在 GitHub 新建仓库（例如 ai-infra-journey），目录：notes/、labs/、perf-log.md
3. 练习 git 基本流程：add、commit、push、branch、merge、log、diff
4. 写 .gitignore，排除数据集、checkpoint 和虚拟环境
5. 在 perf-log.md 写好表头：日期 | 改动 | 硬件 | tokens/s | 显存峰值 | MFU | 备注

**验收**

- ✅ 仓库已推送到 GitHub，能在另一台机器 clone 下来
- ✅ perf-log.md 表头已就位

**提示**：uv 文档：https://docs.astral.sh/uv/

## 自测（周末）

1. 在服务器上独立完成：ssh 登录、tmux 管理会话、用 uv 或 conda 管环境、nvidia-smi 看 GPU、git 管代码、写 bash 脚本批量跑任务

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w02-remote-git/`，格式见成果总表。
