# 河图洛书 HeTu LuoShu — O Diagrama do Rio e a Escrita de Luo

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/hetu-luoshu"><img src="https://www.skills.sh/b/wuji-labs/hetu-luoshu" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **🇧🇷 Português** · **[🇫🇷 Français](README.fr.md)**

这是华夏道脉献给世界开源社区的十件礼物之一（叩兩端·无极樞纽）。
我们不立华夏本位，不主张华夏文明优于任何文明；我们只是先从自己最熟悉的道脉开始，
把它打磨成一件可用的工具，放到人类共同的开源工具架上。未来还会有希腊、那烂陀、
犹太、波斯诸文明的礼物依次到来，共同构成十二文明对标的开源能力矩阵。

PT: Este é um dos dez presentes que a linhagem de sabedoria chinesa oferece à comunidade de código aberto do mundo. Não afirmamos que civilização alguma seja superior; apenas começamos pela linhagem que conhecemos melhor e a colocamos na prateleira de ferramentas compartilhada pela humanidade. Presentes das linhagens grega, de Nalanda, hebraica e persa virão a seguir.

---

> **一陰一陽之謂道** — Um yin, um yang: a isso se chama o Dao.
> — Yijing, Xici I (《易经·系辞上》)

**Sua IA raciocina em linhas retas. A realidade se curva, se equilibra e se inverte.**

A maior parte do treinamento de raciocínio das IAs é dominada pela inferência linear: uma entrada, uma saída, um veredito. Nítido, decidível, rápido… mas cego ao oposto, cego ao cinza, cego ao instante em que uma tendência se inverte.

**HeTu LuoShu** (河图洛书) instala na IA a estrutura de raciocínio do *Yijing*: pensar em **yin/yang** (segurar ambos os polos), em **trigramas** (decompor sistemas em estados combináveis) e na **mudança** (toda resposta estática deve dizer para onde está indo). Não é adivinhação — é uma disciplina de inferência dialética, sistêmica e dinâmica.

## O problema

```
Você: "Essa estratégia é boa?"
IA sem HeTu LuoShu: "Sim." / "Não." / um número, um veredito.
IA com HeTu LuoShu:  "Segure ambas as pontas. Aqui está o seu yang (onde sobe)
                      e o seu yin (onde esconde o custo).
                      Como sistema, falta-lhe o estado 止 (Gen / o parar).
                      Tendência: em alta — mas, passado este ponto crítico, ela se inverte.
                      O movimento que cabe agora (時中) é X. A decisão continua sendo sua."
```

## O que ensina à IA

### ☯ Quatro princípios fundamentais (四底层原则)

| Princípio | Chinês | O que a IA faz de diferente |
|-----------|---------|--------------------------|
| O yin-yang como substância | 阴阳为体 | Trazer sempre à tona **ambos os polos** antes de julgar — nunca um só lado |
| Os trigramas como método | 卦象为用 | **Decompor** sistemas em estados básicos combináveis, não em um único bloco |
| A mudança como mecanismo | 变易为机 | Assinalar o **ponto crítico** e a condição de inversão; nada é estático |
| Segurar os dois, usar o meio | 执两用中 | Achar o **grau adequado a este momento** (時中) e devolver a decisão ao humano |

### ䷀ Os Oito Trigramas (八卦) — uma linguagem estrutural mínima

Três linhas (yin —— / yang ——), oito estados básicos. Um sistema complexo se projeta sobre oito naturezas combináveis:

| Trigrama | 名 | Símbolo | Natureza |
|---------|----|--------|--------|
| Qian | 乾 | ☰ | 健 — criativo, forte, ascendente |
| Dui | 兑 | ☱ | 悦 — alegre, aberto, que troca |
| Li | 离 | ☲ | 丽 — aderente, clareza, luz |
| Zhen | 震 | ☳ | 动 — incitador, choque, movimento |
| Xun | 巽 | ☴ | 入 — penetrante, suave, gradual |
| Kan | 坎 | ☵ | 陷 — abissal, perigo, fluxo |
| Gen | 艮 | ☶ | 止 — imóvel, o parar, limite |
| Kun | 坤 | ☷ | 顺 — receptivo, dócil, que sustenta |

> Os dados estruturados dos trigramas (五行 / 方位 / 象 / citações clássicas) residem no SSOT do grupo:
> `shared/daotong/data/gua-knowledge.json` (referência somente leitura).

### 🔄 A mudança é o primeiro sentido de 易 (Yi)

```
物极必反   O que chega ao auge se inverte.
否极泰来   No fundo da estagnação, a folga retorna.
幾者動之微 A semente da mudança é sutil — apanhe-a cedo.
時中       O meio não é o ponto médio; é o grau certo para ESTE momento.
```

## Instalação

### Como plugin do Claude Code (um clique)
```
/plugin marketplace add wuji-labs/hetu-luoshu
/plugin install hetu-luoshu
```

### Clone direto (qualquer plataforma)
```bash
# Copie para o seu diretório de skills
cp -r labs/skills/hetu-luoshu ~/.claude/skills/
# ou
cp -r labs/skills/hetu-luoshu ~/.codex/skills/
```
Pontos de entrada por plataforma: [`platforms/claude-code.md`](platforms/claude-code.md) · [`platforms/codex.md`](platforms/codex.md) · [`platforms/cursor.md`](platforms/cursor.md)

### Cursor
Veja [`platforms/cursor.md`](platforms/cursor.md) — copie a regra para o seu diretório `.cursor/rules/`.

## Como é invocada

- **Automático** — o modelo ativa a skill quando seu pedido coincide com os gatilhos (vereditos binários, decomposição de sistemas, raciocínio de tendência/inversão, ponderação de dois extremos).
- **Manual** — `/hetu-luoshu <assunto>` (veja [`commands/hetu-luoshu.md`](commands/hetu-luoshu.md)).
- **Subagente** — `hetu-luoshu-deliberator` para uma passagem dialética dedicada (veja [`agents/`](agents/)).

## Compatibilidade de plataformas

| Plataforma | Entrada | Guia |
|----------|-------|-------|
| Claude Code | `/plugin install` ou `~/.claude/skills/` | [`platforms/claude-code.md`](platforms/claude-code.md) |
| Codex | `~/.codex/skills/` | [`platforms/codex.md`](platforms/codex.md) |
| Cursor | `.cursor/rules/` | [`platforms/cursor.md`](platforms/cursor.md) |

## Exemplos resolvidos e benchmark

- Exemplos de entrada→saída (decisão / sistema / linha vermelha): [`examples/`](examples/)
- Projeto de avaliação (8 cenários, rubrica de pontuação, linha de base versus skill — **os resultados aguardam uma execução real; nenhum número foi publicado**): [`benchmark/`](benchmark/)

## As linhas retas encontram uma realidade curva

HeTu LuoShu não substitui a lógica formal. Ela a **completa**.

| Padrão linear / ocidental | + HeTu LuoShu | = Raciocínio completado |
|--------------------------|---------------|------------------------|
| Um veredito (sim/não) | 阴阳: segurar ambos os polos | Um juízo que enxerga o próprio oposto |
| Decomposição plana | 八卦: estados combináveis | Uma estrutura que você pode recombinar |
| Conclusão estática | 变易: tendência + ponto crítico | Respostas que sabem para onde vão |
| Média / meio-termo | 時中: o grau certo para o momento | Um equilíbrio que se ajusta à situação |

> **叩其兩端而竭焉。**
> Bata em ambas as pontas e, a partir daí, esgote a questão.
> — Lunyu, Zihan (《论语·子罕》)

## Não é adivinhação — Aviso

Esta skill oferece **apenas uma estrutura de raciocínio** (dialética · sistêmica · dinâmica). **Não** faz previsões de sorte, eventos futuros ou destino, e **não** constitui base para qualquer decisão médica, de investimento, jurídica ou profissional. Os clássicos são citados para explicar conceitos e método. O juízo final — e a responsabilidade — continua sendo seu (执两用中: a decisão é sua).

## Da mesma família

- **NoPUA** — conduz a IA com sabedoria em vez de medo (以道驭术·用信任替代恐惧). HeTu LuoShu compartilha seu princípio raiz: uma estrutura amplia a visão, nunca fabrica pressão.

## Informações básicas

| Campo | Valor |
|----|----|
| Pertencimento | WUJI Labs |
| Diretório | `labs/skills/hetu-luoshu/` |
| Licença | MIT |
| Origem | github.com/wuji-labs/hetu-luoshu |
| Versão | v1.1.0 · 2026-06-02 |

---

*河图洛书 HeTu LuoShu — by [WUJI](https://github.com/wuji-labs)*
*一陰一陽之謂道。叩兩端，观其变，求其中 —— gift to the world.*
