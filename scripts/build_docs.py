#!/usr/bin/env python3
"""从 plan.json 和各章 showcase/ 生成仓库里的全部文档。

用法（仓库根目录）：
    python scripts/build_docs.py          # 重新生成文档
    python scripts/build_docs.py --check  # 只检查，不写文件（CI 用）

数据源（唯一）：
    学习路线 ← plan.json（网页 index.html 也读它）
    成果     ← <章>/showcase/wNN-<英文短名>/README.md（目录存在，就表示这一周的产出已完成）

生成的文件第一行带 GENERATED 标记，不要手动修改。
手写、不会被覆盖的内容：<章>/showcase/wNN-*/ 和 <章>/lecture/notes/。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://lingquan11.github.io/ai-infra-plan/"
GENERATED = "<!-- 由 scripts/build_docs.py 生成，不要手动修改；改路线请改 plan.json，加成果请在 showcase/ 下建目录 -->"
CN_NUM = "一二三四五六七八九十"
BAR_WIDTH = 10

# 每章的补充信息：plan.json 里没有、首页和学习地图要用的内容。
CHAPTERS = {
    "prep": {
        "dir": "01-prep",
        "stars": "★☆☆",
        "prereq": "会用命令行，能读懂 Python",
        "learn": "Linux 与远程开发、自动微分与 PyTorch、从 bigram 到 GPT、BPE tokenizer",
        "gain": "字符级 GPT、自己写的 BPE、第一批性能日志",
        "next": "第 8 周的出口检查通过后进入第 2 章",
    },
    "train": {
        "dir": "02-train",
        "stars": "★★★",
        "prereq": "第 1 章出口检查",
        "learn": "从零实现并训练 Transformer LM，profiling 与 roofline，CUDA / Triton / FlashAttention-2，DDP、FSDP、张量并行与流水线并行",
        "gain": "完整的 Transformer LM、自写 FlashAttention、手写 DDP、1 → N 卡扩展效率曲线",
        "next": "本章训练的模型，就是第 3 章推理引擎的对象",
    },
    "infer": {
        "dir": "03-infer",
        "stars": "★★★",
        "prereq": "第 2 章",
        "learn": "KV cache 与 prefill / decode、continuous batching、PagedAttention、量化、投机解码、推理服务与压测",
        "gain": "带 KV cache、continuous batching 和分页 KV cache 的推理引擎，压测报告",
        "next": "本章的推理服务在第 4 章部署到集群上",
    },
    "cluster": {
        "dir": "04-cluster",
        "stars": "★★☆",
        "prereq": "第 2、3 章",
        "learn": "集群网络与集合通信、checkpoint 存储、容器与 Kubernetes、GPU 调度、监控与故障恢复",
        "gain": "运行在 K8s 上的推理服务、可调度的训练与推理、全链路平台",
        "next": "第 2–4 章的性能日志汇成第 5 章的技术报告",
    },
    "cap": {
        "dir": "05-capstone",
        "stars": "★★☆",
        "prereq": "第 1–4 章",
        "learn": "把性能日志整理成技术报告，选定方向并提交第一个开源 PR",
        "gain": "技术报告、第一个开源 PR",
        "next": "—",
    },
}

# 每周任务文件的英文短名（文件名：wNN-<短名>.md）。plan.json 加了新周而这里没有时，文件名只用 wNN。
SLUGS = {
    "w01": "linux-shell", "w02": "remote-git", "w03": "autograd-pytorch", "w04": "bigram-mlp",
    "w05": "backprop", "w06": "transformer-gpt", "w07": "bpe-tokenizer", "w08": "gpt2-preview",
    "w09": "tokenizer-estimate", "w10": "transformer-lm", "w11": "training-baseline",
    "w12": "ablation-baseline", "w12x": "minitorch", "w13": "profiling-roofline", "w14": "cuda-gemm",
    "w15": "triton-memory", "w16": "flashattn-forward", "w17": "flashattn-backward",
    "w18": "collectives-ddp", "w19": "fsdp", "w20": "tp-pp", "w21": "review-train",
    "w22": "kv-cache", "w23": "continuous-batching", "w24": "paged-attention", "w25": "quantization",
    "w26": "speculative-decoding", "w27": "serving-benchmark", "w28": "vllm-pd", "w29": "review-infer",
    "w30": "cluster-network", "w31": "checkpoint-storage", "w32": "k8s-basics",
    "w33": "gpu-scheduling", "w34": "monitoring", "w35": "tech-report", "w36": "open-source-pr",
}


# ---------- 小工具 ----------

def key_of(w: dict) -> str:
    return w.get("k") or f"w{int(w['n']):02d}"


def label(w: dict) -> str:
    """表格里的周号：可选周写"可选"。"""
    return "可选" if w.get("opt") else str(int(w["n"]))


def week_name(w: dict) -> str:
    return "可选周" if w.get("opt") else f"第 {int(w['n'])} 周"


def heading(w: dict, sep: str) -> str:
    """周标题：可选周的标题里已经写了"（可选 +2 周）"，不再加周号。"""
    return w["title"] if w.get("opt") else f"{week_name(w)}{sep}{w['title']}"


def fmt_hours(h: str | None) -> str | None:
    """"12–15" → "12–15h"，"10–15，共 2 周" → "10–15h，共 2 周"，"按需" 不变。"""
    return re.sub(r"^(\d+–\d+)(?=，|$)", r"\1h", h) if h else h


def lab_file(w: dict) -> str:
    k = key_of(w)
    return f"{k}-{SLUGS[k]}.md" if k in SLUGS else f"{k}.md"


def cell(text) -> str:
    return str(text if text not in (None, "") else "—").replace("|", "\\|").replace("\n", " ")


def link_item(x: dict) -> str:
    s = f"[{x['t']}]({x['u']})" if x.get("u") else x["t"]
    return s + (f" — {x['d']}" if x.get("d") else "")


def hours_range(weeks: list[dict]) -> str:
    lo = hi = 0
    extra = []
    for w in weeks:
        m = re.fullmatch(r"(\d+)–(\d+)", w.get("hours", ""))
        if m and not w.get("opt"):
            lo, hi = lo + int(m[1]), hi + int(m[2])
        elif w.get("opt"):
            extra.append("可选周另计")
        else:
            extra.append("缓冲周按需")
    s = f"{lo}–{hi}h"
    return s + (f"（{'，'.join(dict.fromkeys(extra))}）" if extra else "")


def compress(nums: list[int]) -> str:
    """[13, 14, 18, 19, 20] → 第 13–14、18–20 周"""
    if not nums:
        return "—"
    runs, start, prev = [], nums[0], nums[0]
    for n in nums[1:] + [None]:
        if n is not None and n == prev + 1:
            prev = n
            continue
        runs.append(str(start) if start == prev else f"{start}–{prev}")
        if n is not None:
            start = prev = n
    return f"第 {'、'.join(runs)} 周"


def bar(done: int, total: int) -> str:
    filled = round(BAR_WIDTH * done / total) if total else 0
    return "█" * filled + "░" * (BAR_WIDTH - filled)


# ---------- 读数据 ----------

def load() -> tuple[list[dict], dict]:
    plan = json.loads((ROOT / "plan.json").read_text(encoding="utf-8"))
    chapters = []
    for i, s in enumerate(plan["segments"], 1):
        if s["id"] not in CHAPTERS:
            sys.exit(f"plan.json 的阶段 {s['id']} 在 build_docs.py 的 CHAPTERS 里没有对应设置")
        meta = CHAPTERS[s["id"]]
        weeks = [w for w in plan["weeks"] if w["seg"] == s["id"]]
        chapters.append({**s, **meta, "no": i, "weeks": weeks})
    for i, c in enumerate(chapters):
        c["next_ch"] = chapters[i + 1] if i + 1 < len(chapters) else None
        c["bridge"] = next((w["bridge"] for w in reversed(c["weeks"]) if w.get("bridge")), None)
        c["gate"] = next((w["gate"] for w in reversed(c["weeks"]) if w.get("gate")), None)
    return chapters, plan


def scan_showcase(chapters: list[dict]) -> tuple[dict, list[str]]:
    """返回 {周 key: 成果信息} 和问题列表。"""
    found, problems = {}, []
    for c in chapters:
        keys = {key_of(w): w for w in c["weeks"]}
        sc = ROOT / c["dir"] / "showcase"
        if not sc.is_dir():
            continue
        for d in sorted(p for p in sc.iterdir() if p.is_dir()):
            m = re.match(r"(w\d{2}x?)(?:-|$)", d.name)
            if not m or m[1] not in keys:
                problems.append(f"{c['dir']}/showcase/{d.name}：目录名要以本章某一周的编号开头（如 {next(iter(keys))}-xxx）")
                continue
            readme = d / "README.md"
            if not readme.exists():
                problems.append(f"{c['dir']}/showcase/{d.name}：缺少 README.md")
                continue
            text = readme.read_text(encoding="utf-8")
            title = next((ln[2:].strip() for ln in text.splitlines() if ln.startswith("# ")), d.name)
            summary = next((re.sub(r"^\*\*结论\*\*[：:]\s*", "", ln).strip()
                            for ln in text.splitlines() if ln.startswith("**结论**")), "")
            found[m[1]] = {"dir": d.name, "title": title, "summary": summary,
                           "chapter": c, "week": keys[m[1]]}
    return found, problems


# ---------- 生成 ----------

def chapter_readme(c: dict, shows: dict) -> str:
    L = [GENERATED, f"# 第 {c['no']} 章：{c['name']}", "",
         f"> {c['desc']}（第 {c['from']}–{c['to']} 周）", ""]
    L += ["## 本章收获"]
    if c["gate"]:
        L += [f"第 {c['to']} 周的出口检查，进入下一章之前逐条确认："]
        L += [f"- {g}" for g in c["gate"]]
    else:
        L += ["本章结束时你会有："]
        L += [f"- {w['out']}" + ("（可选）" if w.get("opt") else "") for w in c["weeks"] if w.get("out")]
    L += ["", "## 知识点地图"]
    L += [f"{i}. {heading(w, ' · ')}" + (f"（{w['src']}）" if w.get("src") else "")
          for i, w in enumerate(c["weeks"], 1)]
    L += ["", "## 讲义", "每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。", "",
          "| 周 | 主题 | 中文阅读 | 课程 |", "|---|---|---|---|"]
    for w in c["weeks"]:
        L.append(f"| [{label(w)}](lecture/README.md#{key_of(w)}) | {cell(w['title'])} | "
                 f"{len(w.get('read', []))} 篇 | {len(w.get('theory', []))} 项 |")
    L += ["", "## 动手实践", "每周一个任务文件：目标、步骤、✅ 验收、提示和自测。"
          f"在[网页版]({SITE})里可以勾选进度，并一键把任务复制给 Muse，让它带你一步步做。", ""]
    L += lab_table(c, prefix="lab/")
    done = [shows[key_of(w)] for w in c["weeks"] if key_of(w) in shows]
    L += ["", "## 成果展示", f"已产出 {len(done)} / {len(c['weeks'])} 周，"
          f"见[本章成果总表](showcase/README.md)。", ""]
    if done:
        L += [f"- {week_name(s['week'])} · [{s['title']}](showcase/{s['dir']}/)"
              + (f"：{s['summary']}" if s["summary"] else "") for s in done]
    else:
        L += ["还没有成果。每完成一周，按[成果总表](showcase/README.md)里的格式加一个目录。"]
    L += ["", "## 与后续章节的关系"]
    nxt = c["next_ch"]
    if nxt:
        L += [f"{c['next']}。", ""]
        if c["bridge"]:
            L += [f"过渡问题：{c['bridge']}", ""]
        L += [f"下一章：[第 {nxt['no']} 章 {nxt['name']}](../{nxt['dir']}/)（{nxt['desc']}）"]
    else:
        L += ["这是最后一章。"]
    return "\n".join(L) + "\n"


def lab_table(c: dict, prefix: str) -> list[str]:
    L = ["| 周 | 主题 | 课程 | 用时 | 硬件 | 本周产出 |", "|---|---|---|---|---|---|"]
    for w in c["weeks"]:
        L.append(f"| [{label(w)}]({prefix}{lab_file(w)}) | {cell(w['title'])} | {cell(w.get('src'))} | "
                 f"{cell(fmt_hours(w.get('hours')))} | {cell(w.get('gpu'))} | {cell(w.get('out'))} |")
    return L


def lecture_readme(c: dict) -> str:
    L = [GENERATED, f"# 第 {c['no']} 章讲义：{c['name']}", "",
         "每周先读 AIInfraGuide 的中文文章建立直觉，再看课程补深度。"
         "自己的笔记放在 `lecture/notes/`（手写，脚本不会覆盖）。", ""]
    for w in c["weeks"]:
        L += [f'<a id="{key_of(w)}"></a>', "", f"## {heading(w, ' · ')}", ""]
        if w.get("read"):
            L += ["**中文阅读（AIInfraGuide）**", ""] + [f"- {link_item(x)}" for x in w["read"]] + [""]
        if w.get("theory"):
            L += ["**课程**", ""] + [f"- {link_item(x)}" for x in w["theory"]] + [""]
        L += [f"本周任务：[{lab_file(w)}](../lab/{lab_file(w)})", ""]
    return "\n".join(L)


def lab_index(c: dict) -> str:
    L = [GENERATED, f"# 第 {c['no']} 章动手实践：{c['name']}", "",
         "每周一个任务文件：目标、步骤、✅ 验收、提示和自测。"
         f"[网页版]({SITE})里可以勾选进度，并一键把任务复制给 Muse，让它带你一步步做。", ""]
    return "\n".join(L + lab_table(c, prefix="")) + "\n"


def lab_week(c: dict, w: dict, shows: dict) -> str:
    k = key_of(w)
    meta = [f"课程：{w['src']}" if w.get("src") else "", f"预计用时：{fmt_hours(w['hours'])}" if w.get("hours") else ""]
    if w.get("gpu"):
        meta.append(f"硬件：{w['gpu']}")
    L = [GENERATED, f"# {heading(w, '：')}", "", "> " + " ｜ ".join(m for m in meta if m)]
    if w.get("out"):
        L += [f"> 本周产出：{w['out']}"]
    L += ["", f"先读：[本周讲义](../lecture/README.md#{k})", ""]
    for i, t in enumerate(w.get("tasks", [])):
        L += [f"## 任务{CN_NUM[i]}：{t['t']}", ""]
        if t.get("goal"):
            L += [f"**目标**：{t['goal']}", ""]
        if t.get("steps"):
            L += ["**步骤**", ""] + [f"{j}. {s}" for j, s in enumerate(t["steps"], 1)] + [""]
        if t.get("done"):
            L += ["**验收**", ""] + [f"- ✅ {d}" for d in t["done"]] + [""]
        if t.get("hint"):
            L += [f"**提示**：{t['hint']}", ""]
    if w.get("check"):
        L += ["## 自测（周末）", ""] + [f"{j}. {s}" for j, s in enumerate(w["check"], 1)] + [""]
    if w.get("gate"):
        L += [f"## {c['name']}出口检查", "", "进入下一章之前逐条确认：", ""]
        L += [f"- {g}" for g in w["gate"]] + [""]
    if w.get("bridge"):
        L += ["## 过渡问题", "", w["bridge"], ""]
    L += ["## 成果", ""]
    if k in shows:
        s = shows[k]
        L += [f"已产出：[{s['title']}](../showcase/{s['dir']}/)" + (f"：{s['summary']}" if s["summary"] else "")]
    else:
        slug = SLUGS.get(k)
        L += [f"完成后在本章的 [showcase/](../showcase/README.md) 下新建 `{k}-{slug or '<英文短名>'}/`，"
              "格式见成果总表。"]
    return "\n".join(L) + "\n"


def showcase_readme(c: dict, shows: dict) -> str:
    done = sum(1 for w in c["weeks"] if key_of(w) in shows)
    L = [GENERATED, f"# 第 {c['no']} 章成果展示：{c['name']}", "",
         f"已产出 {done} / {len(c['weeks'])} 周。", "",
         "| 周 | 计划产出 | 成果 | 结论 |", "|---|---|---|---|"]
    for w in c["weeks"]:
        s = shows.get(key_of(w))
        got = f"[{cell(s['title'])}]({s['dir']}/)" if s else "未开始"
        L.append(f"| {label(w)} | {cell(w.get('out'))} | {got} | {cell(s['summary'] if s else '')} |")
    L += ["", "## 怎么加一项成果", "",
          "1. 在本目录新建 `wNN-<英文短名>/`，编号和 lab 里的文件一致（例如 `w13-profiling-roofline/`）",
          "2. 写 `README.md`（≤ 30 行），按这个顺序：",
          "   - `# 标题`",
          "   - **问题**：这一周想回答什么",
          "   - **做法**：环境、规模、测量方法",
          "   - 结果：表或图",
          "   - `**结论**：一句话`（这一行会被收进成果总表和首页）",
          "   - 边界：这次结果能说明什么、不能说明什么",
          "   - 数据与复现：原始数据放在同一目录；代码链接到主线仓库的具体 commit",
          "3. 在仓库根目录运行 `python scripts/build_docs.py`，本表、章节 README 和首页会自动更新", ""]
    return "\n".join(L)


def root_readme(chapters: list[dict], plan: dict, shows: dict) -> str:
    total = len(plan["weeks"])
    L = [GENERATED, "# AI Infra 36 周学习计划", "",
         "> 从 Linux 和 PyTorch 入门，一路做到算子、分布式训练、推理服务和集群平台。", "",
         f"[打开网页版]({SITE})：可以勾选进度、写笔记，每个实践任务都能一键复制给 Muse，让它带你一步步做。", "",
         "## 课程简介", "",
         f"36 周分 {len(chapters)} 章（另有一个可选的 2 周）。每周四步：先读 AIInfraGuide 的中文文章建立直觉，"
         "再看课程补深度，然后在同一个模型上动手实践，周末用自测题检查。"
         "每章由讲义（`lecture/`）、动手实践（`lab/`）和成果展示（`showcase/`）三部分组成。", "",
         "## 章节总览", "", "| 章节 | 周次 | 主题 | 你将学到 | 你的收获 |", "|---|---|---|---|---|"]
    for c in chapters:
        L.append(f"| [第 {c['no']} 章 {c['name']}]({c['dir']}/) | {c['from']}–{c['to']} | {cell(c['desc'])} | "
                 f"{cell(c['learn'])} | {cell(c['gain'])} |")
    L += ["", "## 学习路径", ""]
    for c in chapters:
        L.append(f"{c['no']}. **[{c['name']}]({c['dir']}/)**（第 {c['from']}–{c['to']} 周）：{c['desc']}")
        if c["gate"]:
            L.append(f"   - 出口检查：第 {c['to']} 周，见[第 {c['no']} 章](./{c['dir']}/)的「本章收获」")
        if c["bridge"] and c["next_ch"]:
            L.append(f"   - 过渡问题：{c['bridge']}")
    L += ["", "## 学习地图：时长与难度", "",
          "| 章节 | 周数 | 预计时长 | 难度 | 前置 | 需要 GPU 的周 | 与后续章节的关系 |",
          "|---|---|---|---|---|---|---|"]
    lo = hi = 0
    for c in chapters:
        gpu = [int(w["n"]) for w in c["weeks"] if w.get("gpu") and not w.get("opt")]
        regular = [w for w in c["weeks"] if not w.get("opt")]
        L.append(f"| 第 {c['no']} 章 | {len(regular)} | {hours_range(c['weeks'])} | {c['stars']} | "
                 f"{cell(c['prereq'])} | {compress(gpu)} | {cell(c['next'])} |")
        m = re.match(r"(\d+)–(\d+)h", hours_range(c["weeks"]))
        lo, hi = lo + int(m[1]), hi + int(m[2])
    L += ["", f"> 时长按每周计划用时加总，合计约 {lo}–{hi} 小时；缓冲周（按需）和可选周不计入。"
          "每周的硬件需求写在任务文件开头。", ""]
    done_total = len(shows)
    L += ["## 成果展示", "", f"已产出 {done_total} / {total} 周。", "", "```"]
    width = max(len(f"第 {c['no']} 章 {c['name']}") for c in chapters)
    for c in chapters:
        d = sum(1 for w in c["weeks"] if key_of(w) in shows)
        name = f"第 {c['no']} 章 {c['name']}"
        L.append(f"{name}{'　' * (width - len(name))}  {bar(d, len(c['weeks']))}  {d}/{len(c['weeks'])}")
    L += ["```", ""]
    order = {key_of(w): i for i, w in enumerate(plan["weeks"])}
    recent = sorted(shows.items(), key=lambda kv: order[kv[0]], reverse=True)[:5]
    if recent:
        L += ["最近的成果：", ""]
        for _, s in recent:
            c = s["chapter"]
            L.append(f"- {week_name(s['week'])} · [{s['title']}]({c['dir']}/showcase/{s['dir']}/)"
                     + (f"：{s['summary']}" if s["summary"] else ""))
        L.append("")
    else:
        first = chapters[0]
        L += [f"还没有成果。每完成一周，在对应章节的 `showcase/` 下建一个目录，"
              f"格式见[第 1 章成果展示]({first['dir']}/showcase/README.md)。", ""]
    L += ["## 如何开始", "",
          f"1. 打开[网页版]({SITE})从第 1 周开始，或者在仓库里读[第 1 章]({chapters[0]['dir']}/)",
          "2. 每周四步：读本章 `lecture/` 里的中文阅读 → 看课程 → 做 `lab/` 里的任务（可以在网页上点「复制给 Muse」让它带你做）→ 周末用自测题检查",
          "3. 第 2 周建好主线仓库，之后的代码都放在那里",
          "4. 每完成一周，把成果放进该章的 `showcase/`，然后运行 `python scripts/build_docs.py`", "",
          "## 先修要求", "",
          "- 一台能联网的电脑；Windows 用 WSL2 + Ubuntu（第 1 周会装好）",
          "- 能读写基本的 Python",
          "- 第 8 周开始需要按小时租用云 GPU，每周的硬件需求写在任务文件开头", "",
          "## 维护", "",
          "- 改路线只改 `plan.json`（网页也读它），然后运行 `python scripts/build_docs.py` 重新生成全部文档；"
          "CI 会运行 `--check`，忘了重新生成会报错",
          "- 手写的只有各章 `showcase/` 下的成果目录和 `lecture/notes/` 里的笔记", "",
          "## 目录结构", "", "```text",
          "ai-infra-plan/",
          "├── README.md               # 课程首页（生成）",
          "├── index.html              # 网页版：勾选进度、写笔记、复制给 Muse",
          "├── plan.json               # 学习路线的唯一数据源",
          "├── 01-prep/ … 05-capstone/ # 一章一个目录",
          "│   ├── README.md           # 章节导读（生成）",
          "│   ├── lecture/README.md   # 逐周的中文阅读和课程（生成）",
          "│   ├── lab/                # 每周一个任务文件（生成）",
          "│   └── showcase/           # 成果展示：README 总表（生成）+ 每周一个成果目录（手写）",
          "└── scripts/build_docs.py   # 从 plan.json 和 showcase/ 生成以上文档",
          "```", "",
          "> 课程信息按 2025–2026 学年的版本整理，2026 年 11 月核对过链接；各课程每年改版，以官网为准。"
          "实践任务的说明是按课程作业要求改写的等效描述，不是原作业文本。"
          "中文阅读来自 AIInfraGuide（caomaolufei/AIInfraGuide），它还在持续更新，标着「提纲」的章节暂时只有大纲；"
          "术语或写法与课程不一致时，写代码以课程为准。"]
    return "\n".join(L) + "\n"


def build() -> tuple[dict[Path, str], list[str]]:
    chapters, plan = load()
    shows, problems = scan_showcase(chapters)
    files = {ROOT / "README.md": root_readme(chapters, plan, shows)}
    for c in chapters:
        d = ROOT / c["dir"]
        files[d / "README.md"] = chapter_readme(c, shows)
        files[d / "lecture" / "README.md"] = lecture_readme(c)
        files[d / "lab" / "README.md"] = lab_index(c)
        files[d / "showcase" / "README.md"] = showcase_readme(c, shows)
        for w in c["weeks"]:
            files[d / "lab" / lab_file(w)] = lab_week(c, w, shows)
    return files, problems


def stale_generated(files: dict[Path, str]) -> list[Path]:
    """以前生成、现在不再生成的文件（比如改了短名）。"""
    out = []
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts or p in files:
            continue
        with p.open(encoding="utf-8") as f:
            if f.readline().rstrip("\n") == GENERATED:
                out.append(p)
    return sorted(out)


def broken_links(files: dict[Path, str]) -> list[str]:
    problems = []
    texts = {p: t for p, t in files.items()}
    for p in ROOT.rglob("*.md"):
        if ".git" not in p.parts and p not in texts:
            texts[p] = p.read_text(encoding="utf-8")
    for p, text in sorted(texts.items()):
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = urllib.parse.unquote(target.split("#")[0])
            if not (p.parent / path).exists() and (p.parent / path) not in files:
                problems.append(f"{p.relative_to(ROOT).as_posix()}：失效链接 {target}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="只检查，不写文件")
    args = parser.parse_args()
    files, problems = build()
    stale = stale_generated(files)
    changed = [p for p, t in files.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
    if args.check:
        problems += [f"{p.relative_to(ROOT).as_posix()}：和 plan.json / showcase 不同步" for p in changed]
        problems += [f"{p.relative_to(ROOT).as_posix()}：已不再生成，应删除" for p in stale]
    else:
        for p in changed:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(files[p], encoding="utf-8")
        for p in stale:
            p.unlink()
        print(f"已生成 {len(files)} 个文件（更新 {len(changed)} 个，删除 {len(stale)} 个）")
    problems += broken_links(files)
    for p in problems:
        print("✗ " + p)
    if not problems:
        print("✓ 文档与 plan.json、showcase/ 同步，相对链接全部有效")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
