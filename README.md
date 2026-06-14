# 河图洛书 HeTu LuoShu — River Chart and Luo Script

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/hetu-luoshu"><img src="https://www.skills.sh/b/wuji-labs/hetu-luoshu" alt="skills.sh"></a>
  <a href="https://github.com/wuji-labs/hetu-luoshu/actions/workflows/validate.yml"><img src="https://github.com/wuji-labs/hetu-luoshu/actions/workflows/validate.yml/badge.svg" alt="Validate"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **[🇧🇷 Português](README.pt.md)** · **[🇫🇷 Français](README.fr.md)**

English · [简体中文](README.zh-CN.md)

这是华夏道脉献给世界开源社区的十件礼物之一（叩兩端·无极樞纽）。
我们不立华夏本位，不主张华夏文明优于任何文明；我们只是先从自己最熟悉的道脉开始，
把它打磨成一件可用的工具，放到人类共同的开源工具架上。未来还会有希腊、那烂陀、
犹太、波斯诸文明的礼物依次到来，共同构成十二文明对标的开源能力矩阵。

EN: This is one of ten gifts the Chinese stream of wisdom offers to the world's
open-source community. We make no claim that any civilization is superior; we
simply begin with the lineage we know best, and place it on humanity's shared
toolshelf. Gifts from the Greek, Nalanda, Hebrew, and Persian streams will follow.

---

> **一陰一陽之謂道** — One yin, one yang: that is called the Dao.
> — Yi Jing, Xici I (《易经·系辞上》)

**Your AI reasons in straight lines. Reality bends, balances, and reverses.**

Most AI reasoning training is dominated by linear inference: one input, one output, one verdict. Crisp, decidable, fast... but blind to the opposite, blind to the gray, blind to the moment a trend flips.

**HeTu LuoShu** (河图洛书) installs the *Yi Jing*'s reasoning framework into AI: think in **yin/yang** (hold both poles), in **trigrams** (decompose systems into composable states), and in **change** (every static answer must say where it is heading). Not divination — a discipline of dialectical, systemic, dynamic inference.

## The Problem

```
You: "Is this strategy good?"
AI without HeTu LuoShu: "Yes." / "No." / one number, one verdict.
AI with HeTu LuoShu:    "Hold both ends. Here is its yang (where it rises)
                         and its yin (where it hides cost).
                         As a system it lacks the 止 (Gen / stopping) state.
                         Trend: rising — but past this critical point it reverses.
                         The fitting move now (時中) is X. The call stays yours."
```

## What It Teaches AI

### ☯ Four Foundational Principles (四底层原则)

| Principle | Chinese | What AI Does Differently |
|-----------|---------|--------------------------|
| Yin-Yang as substance | 阴阳为体 | Always surface **both poles** before judging — never one-sided |
| Trigrams as method | 卦象为用 | **Decompose** systems into composable basic states, not one blob |
| Change as mechanism | 变易为机 | Mark the **critical point** and reversal condition; nothing is static |
| Hold-two, use-the-mean | 执两用中 | Find the **fitting degree for this moment** (時中), then return the call to the human |

### ䷀ The Eight Trigrams (八卦) — a minimal structural language

Three lines (yin —— / yang ——), eight basic states. A complex system maps onto eight composable natures:

| Trigram | 名 | Symbol | Nature |
|---------|----|--------|--------|
| Qian | 乾 | ☰ | 健 — creative, strong, rising |
| Dui | 兑 | ☱ | 悦 — joyous, open, exchanging |
| Li | 离 | ☲ | 丽 — clinging, clarity, light |
| Zhen | 震 | ☳ | 动 — arousing, shock, motion |
| Xun | 巽 | ☴ | 入 — penetrating, gentle, gradual |
| Kan | 坎 | ☵ | 陷 — abysmal, danger, flow |
| Gen | 艮 | ☶ | 止 — keeping still, stopping, limit |
| Kun | 坤 | ☷ | 顺 — receptive, yielding, supporting |

> Structured trigram data (五行 / 方位 / 象 / classic quotes) lives in the group SSOT:
> `shared/daotong/data/gua-knowledge.json` (read-only reference).

### 🔄 Change is the first meaning of 易 (Yi)

```
物极必反   What peaks, reverses.
否极泰来   At the depth of stagnation, ease returns.
幾者動之微 The seed of change is subtle — catch it early.
時中       The mean is not the midpoint; it is the right degree for THIS moment.
```

## Installation

### As a Claude Code plugin (one-click)
```
/plugin marketplace add wuji-labs/hetu-luoshu
/plugin install hetu-luoshu
```

### Bare clone (any platform)
```bash
# Copy to your skills directory
cp -r labs/skills/hetu-luoshu ~/.claude/skills/
# or
cp -r labs/skills/hetu-luoshu ~/.codex/skills/
```
Platform entry points: [`platforms/claude-code.md`](platforms/claude-code.md) · [`platforms/codex.md`](platforms/codex.md) · [`platforms/cursor.md`](platforms/cursor.md)

### Cursor
See [`platforms/cursor.md`](platforms/cursor.md) — copy the rule into your `.cursor/rules/` directory.

## How It's Invoked

- **Automatic** — the model activates the skill when your request matches the triggers (binary verdicts, system decomposition, trend/reversal reasoning, weighing two extremes).
- **Manual** — `/hetu-luoshu <subject>` (see [`commands/hetu-luoshu.md`](commands/hetu-luoshu.md)).
- **Subagent** — `hetu-luoshu-deliberator` for a dedicated dialectical pass (see [`agents/`](agents/)).

## Platform Compatibility

| Platform | Entry | Guide |
|----------|-------|-------|
| Claude Code | `/plugin install` or `~/.claude/skills/` | [`platforms/claude-code.md`](platforms/claude-code.md) |
| Codex | `~/.codex/skills/` | [`platforms/codex.md`](platforms/codex.md) |
| Cursor | `.cursor/rules/` | [`platforms/cursor.md`](platforms/cursor.md) |

## Worked Examples & Benchmark

- Input→output examples (decision / system / red-line): [`examples/`](examples/)
- Evaluation design (8 scenarios, scoring rubric, baseline-vs-skill — **results pending a real run, no numbers shipped**): [`benchmark/`](benchmark/)

## Straight Lines Meet Bent Reality

HeTu LuoShu does not replace formal logic. It **completes** it.

| Linear / Western default | + HeTu LuoShu | = Completed reasoning |
|--------------------------|---------------|------------------------|
| One verdict (yes/no) | 阴阳: hold both poles | Judgment that sees its own opposite |
| Flat decomposition | 八卦: composable states | Structure you can recombine |
| Static conclusion | 变易: trend + critical point | Answers that know where they head |
| Average / compromise | 時中: right degree for the moment | Balance that fits the situation |

> **叩其兩端而竭焉。**
> Knock on both ends, and exhaust the question from there.
> — Lunyu, Zihan (《论语·子罕》)

## Not Divination — a Disclaimer

This skill provides a **reasoning framework only** (dialectical · systemic · dynamic). It makes **no** predictions of fortune, future events, or fate, and is **not** a basis for medical, investment, legal, or any professional decision. Classics are cited to explain concepts and method. The final judgment — and the responsibility — stays with you (执两用中: the call is yours).

## From the Same Family

- **NoPUA** — drives AI with wisdom instead of fear (以道驭术·用信任替代恐惧). HeTu LuoShu shares its root principle: a framework widens sight, it never manufactures pressure.

## 基本信息

| 项 | 值 |
|----|----|
| 归属 | WUJI Labs |
| 目录 | `labs/skills/hetu-luoshu/` |
| 许可证 | MIT |
| 上游 | github.com/wuji-labs/hetu-luoshu |
| 版本 | v1.1.0 · 2026-06-02 |

---

*河图洛书 HeTu LuoShu — by [WUJI](https://github.com/wuji-labs)*
*一陰一陽之謂道。叩兩端，观其变，求其中 —— gift to the world.*
