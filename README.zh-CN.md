# 河图洛书 HeTu LuoShu — 把《易经》推演框架装进 AI

[English](README.md) · 简体中文

> **一陰一陽之謂道。** —《易经·系辞上》

**你的 AI 在走直线，现实却会弯、会平衡、会反转。**

多数 AI 推理被线性推断主导：一输入、一输出、一结论。干脆、可判、快——却看不见对侧、看不见灰度、看不见趋势反转的那一刻。

**HeTu LuoShu** 把《易经》的推演框架装进 AI：用**阴阳**（叩住两端）、**卦象**（把系统拆成可组合的基本态）、**变易**（任何静态结论都要说它正往哪走）来思考。不是占卜——是一套辩证·系统·动态的推演纪律。

这是华夏道脉献给世界开源社区的十件礼物之一。**我们不立华夏本位**，不主张任何文明优于另一文明——只是先从最熟悉的道脉开始，把它打磨成可用工具，放上人类共同的开源工具架。

---

## 结论先行

| 维度 | 没有 HeTu LuoShu | 启用 HeTu LuoShu |
|------|------------------|------------------|
| 判断 | 单值（行/不行、一个数） | 叩两端——同时给出对立面与核心张力 |
| 系统 | 一团 blob 罗列 | 八卦式结构分解，定位**缺位态** |
| 动态 | 静态结论 | 现态/趋势/临界后反态 + 反转条件 + 动之微 |
| 落点 | 折中平均 | 时中——当下最恰当的度，决定权交还你 |

## Before / After 工作流

```
你：「这个上线策略好不好？」
没有本 skill：「好。」/「不好。」——单面、单值、静态。
启用本 skill：「叩两端：阳面在哪升，阴面在哪藏成本。
              作为系统它缺『艮·止』这一态。
              趋势：上行——但过了这个临界点会反转。
              当下最恰当的做法（時中）是 X。决定权仍在你。」
```

## 适用场景（自动激活触发）

- 做一个**非黑即白会出错**的判断（"该不该""行不行""给我个结论"）
- 把复杂系统/团队/架构**结构化分解**，找缺的是哪一态
- 推演**动态走向与临界反转**（"会在哪个点反过来""物极必反"）
- 在两个对立诉求间**权衡取中**（"各退一步对吗""折中一下"）
- 想看到一个判断的**对立面/灰度/盲区**（"别只给我一面""两头都说"）

**反触发红线**：求算吉凶占卜、预测具体未来/命运、为医疗/投资/法律决策背书——本 skill 一律拒绝并转回框架。

## 安装

### 作为 Claude Code plugin（一键）

```
/plugin marketplace add wuji-labs/hetu-luoshu
/plugin install hetu-luoshu
```

### 裸 clone（任意平台）

```bash
# 复制到 skills 目录
cp -r labs/skills/hetu-luoshu ~/.claude/skills/
# 或
cp -r labs/skills/hetu-luoshu ~/.codex/skills/
```

## 调用方式

- **自动**：命中上方触发条件时由模型自动激活。
- **手动**：`/hetu-luoshu <要推演的对象>`（见 [`commands/hetu-luoshu.md`](commands/hetu-luoshu.md)）。
- **subagent**：`hetu-luoshu-deliberator` 辩证推演专员（见 [`agents/`](agents/)）。

## 平台兼容矩阵

| 平台 | 入口 | 说明 |
|------|------|------|
| Claude Code | `/plugin install` 或 `~/.claude/skills/` | [`platforms/claude-code.md`](platforms/claude-code.md) |
| Codex | `~/.codex/skills/` | [`platforms/codex.md`](platforms/codex.md) |
| Cursor | `.cursor/rules/` | [`platforms/cursor.md`](platforms/cursor.md) |

## 方法论背书与溯源

四步推演法（叩两端·立卦象·观变易·求时中）由《易经》核心概念体系萃取，所有引文**注明书·篇、出处可核**，不确信者只述概念不杜撰——见 [`reference/yijing.md`](reference/yijing.md)。结构化八卦语义引用集团 SSOT `shared/daotong/data/gua-knowledge.json`（只读）。

与 **NoPUA**（以道驭术·用信任替代恐惧）同源：框架是为让人/AI 看得更全、判断更稳，而非制造焦虑或恐惧式说服。

## 工件一览

| 工件 | 路径 |
|------|------|
| 内核 | [`SKILL.md`](SKILL.md) |
| 典源弹药 | [`reference/yijing.md`](reference/yijing.md) |
| 手动入口 | [`commands/hetu-luoshu.md`](commands/hetu-luoshu.md) |
| 范例 | [`examples/`](examples/) |
| 推演专员 | [`agents/hetu-luoshu-deliberator.md`](agents/hetu-luoshu-deliberator.md) |
| 评测设计 | [`benchmark/`](benchmark/)（结果待真实运行） |

## 免责声明

本 skill 仅提供**思维框架**（辩证·系统·动态），**不**预测吉凶祸福、未来事件或命运，**不**构成医疗、投资、法律或任何专业决策依据。引经据典仅作概念与方法说明。最终判断与责任归于使用者本人（执两用中——决定权在你）。

## 基本信息

| 项 | 值 |
|----|----|
| 归属 | WUJI Labs |
| 许可证 | MIT |
| 上游 | github.com/wuji-labs/hetu-luoshu |
| 版本 | v1.1.0 · 2026-06-02 |

---

*河图洛书 HeTu LuoShu — by [WUJI](https://github.com/wuji-labs)*
*一陰一陽之謂道。叩兩端，观其变，求其中 —— gift to the world.*
