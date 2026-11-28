<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->
# 第 1 周：Linux 基础：终端与 shell

> 课程：MIT Missing Semester ｜ 预计用时：10–12h
> 本周产出：可用的终端环境 + 第一个 bash 脚本

先读：[本周讲义](../lecture/README.md#w01)

## 任务一：搭建 Linux 环境并熟悉文件操作

**目标**：拥有一个日常可用的 Linux 终端，不靠图形界面完成常见文件操作。

**步骤**

1. Windows 安装 WSL2 + Ubuntu；macOS 可先用自带终端练习，另准备一个 Linux 云主机或虚拟机
2. 理解目录结构：/、~、/etc、/tmp、/usr，以及绝对路径和相对路径
3. 用 ls、cd、pwd、mkdir、cp、mv、rm、cat、less、head、tail 完成一组文件整理练习
4. 用 find 按名称和大小找文件，用 grep 在文件中搜索文本，用管道 | 组合命令
5. 理解文件权限 rwx、chmod、sudo，用 apt 安装一个软件（如 htop）

**验收**

- ✅ 不用图形界面完成：建目录、移动文件、找到指定文件、查看日志末尾 20 行
- ✅ 能解释 ls -l 输出中每一列的含义

**提示**：遇到不认识的命令，先用 man 命令名 或 命令名 --help 自己查。

## 任务二：写第一个 bash 脚本并学会 vim

**目标**：能用脚本把重复操作自动化，能在服务器上用 vim 改文件。

**步骤**

1. 运行 vimtutor，完成全部练习
2. 写脚本 count_ext.sh：接收一个目录参数，统计其中各扩展名的文件数量，按数量从多到少输出
3. 脚本中用到变量、if 判断（目录不存在时报错退出）、find、sort、uniq -c
4. chmod +x 后直接运行；把脚本放进 ~/bin 并加入 PATH，理解环境变量和 ~/.bashrc

**验收**

- ✅ 对不存在的目录给出错误提示并返回非 0 退出码
- ✅ 在任意目录下都能直接用 count_ext.sh 调用

**提示**：echo $? 可以查看上一条命令的退出码。

## 成果

完成后在本章的 [showcase/](../showcase/README.md) 下新建 `w01-linux-shell/`，格式见成果总表。
