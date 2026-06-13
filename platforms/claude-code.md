# 平台适配 · Claude Code

在 Claude Code 中加载与调用「河图洛书 HeTu LuoShu」推演框架。

## 安装

把本 skill 目录拷到 Claude Code 的 skills 目录：

```bash
cp -r labs/skills/hetu-luoshu ~/.claude/skills/
```

或在项目内通过 `.claude/` 引用（monorepo 内本目录即 `labs/skills/hetu-luoshu/`，可直接路径引用）。

## 调用

Claude Code 会按 `SKILL.md` frontmatter 的 `description` 自动匹配触发。也可显式唤起：

- 直接说明意图，例如：「用河图洛书的框架帮我推演这个策略」「叩两端分析一下这个判断」。
- 或在对话中要求：「读 `labs/skills/hetu-luoshu/SKILL.md` 再回答」。

## 加载顺序（推荐）

1. 先读 `SKILL.md`（四底层原则 + 四步工作流）。
2. 需要典源/真引用时读 `reference/yijing.md`。
3. 需要八卦结构化语义时只读引用 `shared/daotong/data/gua-knowledge.json`（集团 SSOT，勿改）。

## 触发后的行为约定

- 任何判断先「叩两端」（阴阳两面都给）。
- 系统问题用八卦做结构化分解。
- 结论必带动态（趋势 + 临界点 + 反转条件）。
- 落点是「时中」，并把最终决定权交还用户。
- 严守免责声明：不占卜、不预测、不作专业决策依据。

## 注意

- 本 skill 只读引用 `gua-knowledge.json`，**不写**该文件，也不碰任何共享/SSOT 文件。
- 框架用于辅助思考与结构化表达，不替代用户判断（以道驭术·用信任替代恐惧）。
