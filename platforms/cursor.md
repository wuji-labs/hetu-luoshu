# 平台适配 · Cursor

在 Cursor 中以 Project Rule 形式加载「河图洛书 HeTu LuoShu」推演框架。

## 安装

Cursor 用 `.cursor/rules/*.mdc` 承载规则。新建 `.cursor/rules/hetu-luoshu.mdc`，把本 skill 的核心约定写入（或用 `@` 引用本目录文件）：

```mdc
---
description: HeTu LuoShu — 用易经的阴阳/卦象/变易框架做辩证·系统·动态推演（非占卜）
globs:
alwaysApply: false
---

# 河图洛书推演框架

做判断/系统建模/趋势推演时，遵循 labs/skills/hetu-luoshu/SKILL.md 的四底层原则：
1. 阴阳为体：任何判断先叩两端，阴面阳面都给，不出单值。
2. 卦象为用：系统拆成八卦基本态（健悦丽动入陷止顺），看缺位与相荡。
3. 变易为机：结论必带现态/趋势/临界点/反转条件。
4. 执两用中：落点是"时中"（当下最恰当的度），决定权交还用户。

免责：本框架非占卜、非预测，不作医疗/投资/法律/专业决策依据。
八卦结构化数据见 shared/daotong/data/gua-knowledge.json（只读）。
典源真引用见 labs/skills/hetu-luoshu/reference/yijing.md。
```

## 调用

- 设 `alwaysApply: false` + 在需要时 `@hetu-luoshu` 手动挂载；或对推演类文件设 `globs` 自动应用。
- 也可在 Chat 里 `@SKILL.md`（指向本目录）引入完整框架。

## 加载顺序

1. `.cursor/rules/hetu-luoshu.mdc`（精简规则，常驻/按需）。
2. 需展开时 `@labs/skills/hetu-luoshu/SKILL.md`。
3. 引经据典时 `@labs/skills/hetu-luoshu/reference/yijing.md`。

## 注意

- 只读引用 `gua-knowledge.json`，不修改任何共享 / SSOT 文件。
- 行为与 NoPUA「以道驭术·用信任替代恐惧」一致：框架拓宽视野，不制造压力。
