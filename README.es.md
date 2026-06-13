# 河图洛书 HeTu LuoShu — El Diagrama del Río y la Escritura de Luo

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/hetu-luoshu"><img src="https://www.skills.sh/b/wuji-labs/hetu-luoshu" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **🇪🇸 Español** · **[🇧🇷 Português](README.pt.md)** · **[🇫🇷 Français](README.fr.md)**

这是华夏道脉献给世界开源社区的十件礼物之一（叩兩端·无极樞纽）。
我们不立华夏本位，不主张华夏文明优于任何文明；我们只是先从自己最熟悉的道脉开始，
把它打磨成一件可用的工具，放到人类共同的开源工具架上。未来还会有希腊、那烂陀、
犹太、波斯诸文明的礼物依次到来，共同构成十二文明对标的开源能力矩阵。

ES: Este es uno de los diez regalos que el linaje de sabiduría chino ofrece a la comunidad de código abierto del mundo. No afirmamos que ninguna civilización sea superior; simplemente empezamos por el linaje que mejor conocemos y lo colocamos en el estante de herramientas compartido por la humanidad. Seguirán regalos de los linajes griego, de Nalanda, hebreo y persa.

---

> **一陰一陽之謂道** — Un yin, un yang: a eso se le llama el Dao.
> — Yijing, Xici I (《易经·系辞上》)

**Tu IA razona en líneas rectas. La realidad se curva, se equilibra y se invierte.**

La mayor parte del entrenamiento de razonamiento de las IA está dominado por la inferencia lineal: una entrada, una salida, un veredicto. Nítido, decidible, rápido… pero ciego al opuesto, ciego al gris, ciego al instante en que una tendencia se invierte.

**HeTu LuoShu** (河图洛书) instala en la IA el marco de razonamiento del *Yijing*: pensar en **yin/yang** (sostener ambos polos), en **trigramas** (descomponer los sistemas en estados combinables) y en el **cambio** (toda respuesta estática debe decir hacia dónde se dirige). No es adivinación: es una disciplina de inferencia dialéctica, sistémica y dinámica.

## El problema

```
Tú: «¿Es buena esta estrategia?»
IA sin HeTu LuoShu: «Sí.» / «No.» / un número, un veredicto.
IA con HeTu LuoShu:  «Sostén ambos extremos. Aquí está su yang (dónde asciende)
                      y su yin (dónde oculta su coste).
                      Como sistema, le falta el estado 止 (Gen / detenerse).
                      Tendencia: al alza, pero pasado este punto crítico se invierte.
                      El movimiento que conviene ahora (時中) es X. La decisión sigue siendo tuya.»
```

## Qué le enseña a la IA

### ☯ Cuatro principios fundamentales (四底层原则)

| Principio | Chino | Qué hace distinto la IA |
|-----------|---------|--------------------------|
| El yin-yang como sustancia | 阴阳为体 | Sacar siempre a la luz **ambos polos** antes de juzgar; nunca un solo lado |
| Los trigramas como método | 卦象为用 | **Descomponer** los sistemas en estados básicos combinables, no en una sola masa |
| El cambio como mecanismo | 变易为机 | Señalar el **punto crítico** y la condición de inversión; nada es estático |
| Sostener los dos, usar el medio | 执两用中 | Hallar el **grado que conviene a este momento** (時中) y devolver la decisión al humano |

### ䷀ Los Ocho Trigramas (八卦) — un lenguaje estructural mínimo

Tres líneas (yin —— / yang ——), ocho estados básicos. Un sistema complejo se proyecta sobre ocho naturalezas combinables:

| Trigrama | 名 | Símbolo | Naturaleza |
|---------|----|--------|--------|
| Qian | 乾 | ☰ | 健 — creativo, fuerte, ascendente |
| Dui | 兑 | ☱ | 悦 — gozoso, abierto, intercambiante |
| Li | 离 | ☲ | 丽 — adherente, claridad, luz |
| Zhen | 震 | ☳ | 动 — suscitador, conmoción, movimiento |
| Xun | 巽 | ☴ | 入 — penetrante, suave, gradual |
| Kan | 坎 | ☵ | 陷 — abismal, peligro, flujo |
| Gen | 艮 | ☶ | 止 — quieto, detención, límite |
| Kun | 坤 | ☷ | 顺 — receptivo, dócil, sostenedor |

> Los datos estructurados de los trigramas (五行 / 方位 / 象 / citas clásicas) residen en el SSOT del grupo:
> `shared/daotong/data/gua-knowledge.json` (referencia de solo lectura).

### 🔄 El cambio es el primer sentido de 易 (Yi)

```
物极必反   Lo que llega a su cúspide, se invierte.
否极泰来   En lo más hondo del estancamiento, regresa la holgura.
幾者動之微 La semilla del cambio es sutil: cógela temprano.
時中       El medio no es el punto intermedio; es el grado justo para ESTE momento.
```

## Instalación

### Como plugin de Claude Code (un clic)
```
/plugin marketplace add wuji-labs/hetu-luoshu
/plugin install hetu-luoshu
```

### Clon directo (cualquier plataforma)
```bash
# Copiar a tu directorio de skills
cp -r labs/skills/hetu-luoshu ~/.claude/skills/
# o
cp -r labs/skills/hetu-luoshu ~/.codex/skills/
```
Puntos de entrada por plataforma: [`platforms/claude-code.md`](platforms/claude-code.md) · [`platforms/codex.md`](platforms/codex.md) · [`platforms/cursor.md`](platforms/cursor.md)

### Cursor
Consulta [`platforms/cursor.md`](platforms/cursor.md): copia la regla en tu directorio `.cursor/rules/`.

## Cómo se invoca

- **Automático** — el modelo activa la skill cuando tu petición coincide con los disparadores (veredictos binarios, descomposición de sistemas, razonamiento de tendencia/inversión, ponderación de dos extremos).
- **Manual** — `/hetu-luoshu <asunto>` (véase [`commands/hetu-luoshu.md`](commands/hetu-luoshu.md)).
- **Subagente** — `hetu-luoshu-deliberator` para una pasada dialéctica dedicada (véase [`agents/`](agents/)).

## Compatibilidad de plataformas

| Plataforma | Entrada | Guía |
|----------|-------|-------|
| Claude Code | `/plugin install` o `~/.claude/skills/` | [`platforms/claude-code.md`](platforms/claude-code.md) |
| Codex | `~/.codex/skills/` | [`platforms/codex.md`](platforms/codex.md) |
| Cursor | `.cursor/rules/` | [`platforms/cursor.md`](platforms/cursor.md) |

## Ejemplos resueltos y benchmark

- Ejemplos de entrada→salida (decisión / sistema / línea roja): [`examples/`](examples/)
- Diseño de evaluación (8 escenarios, rúbrica de puntuación, base de referencia frente a skill — **los resultados quedan pendientes de una ejecución real; no se publican cifras**): [`benchmark/`](benchmark/)

## Las líneas rectas se encuentran con una realidad curva

HeTu LuoShu no reemplaza la lógica formal. La **completa**.

| Predeterminado lineal / occidental | + HeTu LuoShu | = Razonamiento completado |
|--------------------------|---------------|------------------------|
| Un veredicto (sí/no) | 阴阳: sostener ambos polos | Un juicio que ve su propio opuesto |
| Descomposición plana | 八卦: estados combinables | Una estructura que puedes recombinar |
| Conclusión estática | 变易: tendencia + punto crítico | Respuestas que saben hacia dónde van |
| Promedio / componenda | 時中: el grado justo para el momento | Un equilibrio que se ajusta a la situación |

> **叩其兩端而竭焉。**
> Golpea ambos extremos y agota desde ahí la cuestión.
> — Lunyu, Zihan (《论语·子罕》)

## No es adivinación — Aviso legal

Esta skill ofrece **únicamente un marco de razonamiento** (dialéctico · sistémico · dinámico). **No** hace predicciones de fortuna, sucesos futuros ni destino, y **no** constituye base para ninguna decisión médica, de inversión, legal o profesional. Los clásicos se citan para explicar conceptos y método. El juicio final —y la responsabilidad— sigue siendo tuyo (执两用中: la decisión es tuya).

## De la misma familia

- **NoPUA** — conduce la IA con sabiduría en lugar de con miedo (以道驭术·用信任替代恐惧). HeTu LuoShu comparte su principio raíz: un marco amplía la mirada, nunca fabrica presión.

## Información básica

| Campo | Valor |
|----|----|
| Pertenencia | WUJI Labs |
| Directorio | `labs/skills/hetu-luoshu/` |
| Licencia | MIT |
| Origen | github.com/wuji-labs/hetu-luoshu |
| Versión | v1.1.0 · 2026-06-02 |

---

*河图洛书 HeTu LuoShu — by [WUJI](https://github.com/wuji-labs)*
*一陰一陽之謂道。叩兩端，观其变，求其中 —— gift to the world.*
