# 河图洛书 HeTu LuoShu — Le Diagramme du Fleuve et l'Écrit de Luo

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/hetu-luoshu"><img src="https://www.skills.sh/b/wuji-labs/hetu-luoshu" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **[🇧🇷 Português](README.pt.md)** · **🇫🇷 Français**

这是华夏道脉献给世界开源社区的十件礼物之一（叩兩端·无极樞纽）。
我们不立华夏本位，不主张华夏文明优于任何文明；我们只是先从自己最熟悉的道脉开始，
把它打磨成一件可用的工具，放到人类共同的开源工具架上。未来还会有希腊、那烂陀、
犹太、波斯诸文明的礼物依次到来，共同构成十二文明对标的开源能力矩阵。

FR : Voici l'un des dix présents que le courant de sagesse chinois offre à la communauté open source du monde. Nous n'affirmons la supériorité d'aucune civilisation ; nous commençons simplement par le lignage que nous connaissons le mieux, et le déposons sur l'étagère à outils commune de l'humanité. Suivront les présents des courants grec, de Nalanda, hébraïque et perse.

---

> **一陰一陽之謂道** — Un yin, un yang : c'est là ce qu'on nomme le Dao.
> — Yijing, Xici I (《易经·系辞上》)

**Votre IA raisonne en lignes droites. Le réel, lui, se courbe, s'équilibre et s'inverse.**

L'essentiel de l'entraînement au raisonnement des IA est dominé par l'inférence linéaire : une entrée, une sortie, un verdict. Net, décidable, rapide… mais aveugle à l'opposé, aveugle au gris, aveugle à l'instant où une tendance bascule.

**HeTu LuoShu** (河图洛书) installe dans l'IA le cadre de raisonnement du *Yijing* : penser en **yin/yang** (tenir les deux pôles), en **trigrammes** (décomposer les systèmes en états combinables) et en **changement** (toute réponse statique doit dire vers où elle se dirige). Non pas de la divination — une discipline d'inférence dialectique, systémique et dynamique.

## Le problème

```
Vous : « Cette stratégie est-elle bonne ? »
IA sans HeTu LuoShu : « Oui. » / « Non. » / un chiffre, un verdict.
IA avec HeTu LuoShu :  « Tenez les deux bouts. Voici son yang (là où elle s'élève)
                        et son yin (là où elle dissimule son coût).
                        En tant que système, il lui manque l'état 止 (Gen / l'arrêt).
                        Tendance : à la hausse — mais passé ce point critique, elle s'inverse.
                        Le geste qui convient maintenant (時中) est X. La décision reste vôtre. »
```

## Ce qu'elle enseigne à l'IA

### ☯ Quatre principes fondateurs (四底层原则)

| Principe | Chinois | Ce que l'IA fait différemment |
|-----------|---------|--------------------------|
| Le yin-yang comme substance | 阴阳为体 | Faire toujours apparaître **les deux pôles** avant de juger — jamais un seul côté |
| Les trigrammes comme méthode | 卦象为用 | **Décomposer** les systèmes en états de base combinables, et non en un seul bloc |
| Le changement comme mécanisme | 变易为机 | Repérer le **point critique** et la condition d'inversion ; rien n'est statique |
| Tenir les deux, user du milieu | 执两用中 | Trouver le **degré qui convient à cet instant** (時中), puis rendre la décision à l'humain |

### ䷀ Les Huit Trigrammes (八卦) — un langage structurel minimal

Trois traits (yin —— / yang ——), huit états de base. Un système complexe se projette sur huit natures combinables :

| Trigramme | 名 | Symbole | Nature |
|---------|----|--------|--------|
| Qian | 乾 | ☰ | 健 — créateur, fort, ascendant |
| Dui | 兑 | ☱ | 悦 — joyeux, ouvert, échangeant |
| Li | 离 | ☲ | 丽 — adhérent, clarté, lumière |
| Zhen | 震 | ☳ | 动 — éveilleur, ébranlement, mouvement |
| Xun | 巽 | ☴ | 入 — pénétrant, doux, graduel |
| Kan | 坎 | ☵ | 陷 — abyssal, danger, écoulement |
| Gen | 艮 | ☶ | 止 — immobile, arrêt, limite |
| Kun | 坤 | ☷ | 顺 — réceptif, docile, portant |

> Les données structurées des trigrammes (五行 / 方位 / 象 / citations classiques) résident dans le SSOT du groupe :
> `shared/daotong/data/gua-knowledge.json` (référence en lecture seule).

### 🔄 Le changement est le premier sens de 易 (Yi)

```
物极必反   Ce qui culmine s'inverse.
否极泰来   Au fond de la stagnation, l'aisance revient.
幾者動之微 Le germe du changement est ténu — saisissez-le tôt.
時中       Le milieu n'est pas le point médian ; c'est le degré juste pour CET instant.
```

## Installation

### En tant que plugin Claude Code (en un clic)
```
/plugin marketplace add wuji-labs/hetu-luoshu
/plugin install hetu-luoshu
```

### Clone brut (toute plateforme)
```bash
# Copiez dans votre répertoire de skills
cp -r labs/skills/hetu-luoshu ~/.claude/skills/
# ou
cp -r labs/skills/hetu-luoshu ~/.codex/skills/
```
Points d'entrée par plateforme : [`platforms/claude-code.md`](platforms/claude-code.md) · [`platforms/codex.md`](platforms/codex.md) · [`platforms/cursor.md`](platforms/cursor.md)

### Cursor
Voir [`platforms/cursor.md`](platforms/cursor.md) — copiez la règle dans votre répertoire `.cursor/rules/`.

## Comment elle est invoquée

- **Automatique** — le modèle active la skill lorsque votre requête correspond aux déclencheurs (verdicts binaires, décomposition de systèmes, raisonnement de tendance/inversion, pesée de deux extrêmes).
- **Manuel** — `/hetu-luoshu <sujet>` (voir [`commands/hetu-luoshu.md`](commands/hetu-luoshu.md)).
- **Sous-agent** — `hetu-luoshu-deliberator` pour une passe dialectique dédiée (voir [`agents/`](agents/)).

## Compatibilité des plateformes

| Plateforme | Entrée | Guide |
|----------|-------|-------|
| Claude Code | `/plugin install` ou `~/.claude/skills/` | [`platforms/claude-code.md`](platforms/claude-code.md) |
| Codex | `~/.codex/skills/` | [`platforms/codex.md`](platforms/codex.md) |
| Cursor | `.cursor/rules/` | [`platforms/cursor.md`](platforms/cursor.md) |

## Exemples travaillés et benchmark

- Exemples entrée→sortie (décision / système / ligne rouge) : [`examples/`](examples/)
- Conception de l'évaluation (8 scénarios, grille de notation, référence vs skill — **les résultats sont en attente d'une exécution réelle ; aucun chiffre n'est publié**) : [`benchmark/`](benchmark/)

## Les lignes droites rencontrent un réel courbe

HeTu LuoShu ne remplace pas la logique formelle. Elle la **parachève**.

| Par défaut linéaire / occidental | + HeTu LuoShu | = Raisonnement parachevé |
|--------------------------|---------------|------------------------|
| Un verdict (oui/non) | 阴阳 : tenir les deux pôles | Un jugement qui voit son propre opposé |
| Décomposition plate | 八卦 : états combinables | Une structure que l'on peut recombiner |
| Conclusion statique | 变易 : tendance + point critique | Des réponses qui savent vers où elles vont |
| Moyenne / compromis | 時中 : le degré juste pour l'instant | Un équilibre ajusté à la situation |

> **叩其兩端而竭焉。**
> Frappe aux deux bouts, et épuise la question depuis là.
> — Lunyu, Zihan (《论语·子罕》)

## Pas de la divination — Avertissement

Cette skill ne fournit **qu'un cadre de raisonnement** (dialectique · systémique · dynamique). Elle **ne** prédit **aucunement** la fortune, les événements à venir ou le destin, et ne constitue **pas** un fondement pour quelque décision médicale, financière, juridique ou professionnelle que ce soit. Les classiques sont cités pour expliquer des concepts et une méthode. Le jugement final — et la responsabilité — vous reste (执两用中 : la décision vous appartient).

## De la même famille

- **NoPUA** — conduit l'IA par la sagesse plutôt que par la peur (以道驭术·用信任替代恐惧). HeTu LuoShu en partage le principe racine : un cadre élargit la vue, il ne fabrique jamais de pression.

## Informations de base

| Champ | Valeur |
|----|----|
| Appartenance | WUJI Labs |
| Répertoire | `labs/skills/hetu-luoshu/` |
| Licence | MIT |
| Amont | github.com/wuji-labs/hetu-luoshu |
| Version | v1.1.0 · 2026-06-02 |

---

*河图洛书 HeTu LuoShu — by [WUJI](https://github.com/wuji-labs)*
*一陰一陽之謂道。叩兩端，观其变，求其中 —— gift to the world.*
