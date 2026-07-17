# CLAUDE.md — Tractate Aliyah

Mage: the Ascension (M20) rendered as a Talmudic tractate: rules as Mishnah,
setting history retold as aggada, interlocking commentaries arguing about
both, bound into a page-turnable HTML codex. Five folios + the shaar exist;
~65 folios are planned.

## Read these, in order, before writing anything
1. `SPEC.md` — the format bible. Binding. §0 has the two inviolable rules.
2. `PLAN.md` — roadmap, status, and what to do next.
3. `plans/folio-briefs.md` — a content brief for every planned folio.
4. `plans/pagetypes.md` — design specs for the unbuilt page types
   (luach, seder, shtar) and the shaar's phase-3 upgrades.
5. Style reference: read `content/f533b_witnesses.py` (a mechanics daf) and
   `content/f003a_judgments.py` (a derivation daf). Between them, the voice.

## The two rules that are never broken (SPEC §0)
1. **No sourcebook text is ever reproduced or closely paraphrased.**
   Mechanics restated as law in original wording; fiction *retold* as aggada.
   Ein Mishpat glosses cite book + page so readers can find the real text;
   the folio never contains it.
2. **All commentary is out of character.** Aggada narration is the one
   bounded exception.

## Commands
```bash
python3 build.py          # content/*.py -> dist/ (standalone folios + codex)
python3 verify.py         # geometry harness; must PASS before a folio is done
# first time only: pip install playwright && playwright install chromium
```

## Producing a folio (the loop)
0. **Fact-check against the wiki.** The `wod-llm-wiki` repo
   (`charlesmsiegel/wod-llm-wiki`; sibling checkout `../wod-llm-wiki` when
   present) is the source of truth for every setting and mechanics claim —
   its pages carry book+page citations. Grep it for the folio's subject
   before and after writing; where memory and the wiki disagree, the wiki
   wins. (SPEC §0 still governs: restate, never reproduce.)
1. Find its brief in `plans/folio-briefs.md`.
2. Copy the nearest content module in `content/` (SPEC §6 naming:
   `f{NNN}{a|b}_{slug}.py`), write the dict per the brief.
3. Register it: `MANIFEST` in `build.py` (keep `'...'` lacuna markers between
   non-adjacent folios) and its ToC line in `content/shaar.py` (set anchor).
4. `python3 build.py && python3 verify.py`.
5. If verify warns a flow "does not wrap beneath": that commentary is too
   short — add a lemma paragraph (real content, never padding). Budgets:
   center 350–520 words; each commentary 1.3–1.6× the center (SPEC §4).
6. Eyeball in a browser at desktop width and ≤860px.

Definition of done: builds clean, verify passes with no warnings on the new
folio, cross-references in Masoret point at real folios (or are phrased as
"wanting"), shaar ToC updated, and the brief's disputes actually appear as
disputes — a folio whose outer commentary merely explains has failed.

## Current state
Built: shaar, all of chapter I (2a/b, 3a/b, and 143 Certámen/Stakes,
bound at its number between chapters IV and V), all of chapter II
(38/43/46, three pairs),
all of chapter III (62/78/82, three pairs), all of chapter IV
(89/91/109, three pairs), all of chapter V
(148–164, nine Tradition pairs), all of chapter VI (168 + the five
Convention pairs 186–194,
in the register swap: inner = procedures-manual deadpan, outer =
Tradition polemic), all of chapter VII (197/224/234, three pairs),
all of chapter VIII (250 seder pair, the three luach pairs 273/275/303,
and 328 Arete/Price), all of chapter IX (384–406, four Middot
pairs), all of chapter X (409–435, three daf pairs + the 435 luach
pair), and all of chapter XI (500 Casting, the nine Sphere pairs
512–522, 533 Paradox/Witnesses, 554 Quiet, the focus trio 567/572/586,
and 607 Rotes) — one hundred and eighteen daf-sides, every bound folio
a complete a/b pair, one shaar ToC row per folio number. All pass verify.
All four page types are proven: daf, luach (f435a/b), seder (f250a),
shaar — conventions in SPEC §3; the six VIII luachs batched against the
luach mold, and the minor tractates batch against it next.
The Sharrim are built: seven sibling-tractate title pages
(dist/tractate-<name>.html), each skinned in its line's interior style
(chrome/sharrim.css; sources and rulings in plans/sharrim/); every shelf
spine is lit and clickable.
Names: classic Tradition names are primary (the renames didn't take),
except Chakravanti and Society of Ether; naming questions appear in-folio
as live debates.
Next: the minor tractates (Kelim K.1–K.2, Bestiary B.1–B.3, shtar);
see PLAN.md. The f143-vs-f430 merge question is decided: both kept,
courthouse/arena division marked in both Masorets.
