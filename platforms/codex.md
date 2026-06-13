# 平台适配 · Codex

在 Codex（OpenAI Codex / codex CLI）中加载与调用「河图洛书 HeTu LuoShu」推演框架。

## 安装

```bash
cp -r labs/skills/hetu-luoshu ~/.codex/skills/
```

若你的 Codex 配置用集中式 prompt/skill 目录，把本目录纳入其 skills 检索路径即可。

## 调用

- 在系统提示 / AGENTS.md 中加入一行指针：
  「推演类任务先读 `skills/hetu-luoshu/SKILL.md`，按四底层原则（阴阳/卦象/变易/时中）作答。」
- 或在单次请求中显式要求：「用河图洛书框架（叩两端·观其变·求其中）推演」。

## 加载顺序

1. `SKILL.md` —— 框架主规范。
2. `reference/yijing.md` —— 典源真引用与四步推演法（需引经据典时）。
3. `shared/daotong/data/gua-knowledge.json` —— 八卦结构化数据（只读引用）。

## 行为约定

- 判断必含阴阳两面；系统必做八卦分解；结论必带趋势+临界点。
- 落「时中」，决定权归用户。
- 严守免责：框架非占卜、非预测、非医疗/投资/法律依据。

## 注意

- 只读引用 `gua-knowledge.json`，不修改任何共享 / SSOT 文件。
- 输出风格遵循 SKILL.md，与 NoPUA「以道驭术·用信任替代恐惧」不冲突。
