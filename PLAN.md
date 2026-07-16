# PLAN — Tractate Aliyah

Status, phases, and priorities. SPEC.md is law; this file is the schedule.
Update the status tables here in the same commit as the work.

## Status

| Folio | Title | Type | State |
|---|---|---|---|
| shaar | Title page + ToC | shaar | **built** (phase-3 upgrades pending, see plans/pagetypes.md) |
| 2a | Convocation | daf | **built** |
| 2b | The Betrayal | daf | **built** |
| 3a | Judgments | daf | **built** |
| 3b | The Unseated Answer | daf | **built** |
| 148a | The Akashic Brotherhood | daf (Avot mold) | **built** |
| 148b | The Wheel | daf | **built** |
| 150a/b | The Celestial Chorus · The Reformation | daf pair | **built** |
| 152a/b | The Cult of Ecstasy · The Burden | daf pair | **built** |
| 154a/b | The Dreamspeakers · The People | daf pair | **built** |
| 156a/b | The Chakravanti · Jhor | daf pair | **built** |
| 158a/b | The Order of Hermes · The Houses | daf pair | **built** |
| 160a/b | The Society of Ether · Paradigma | daf pair | **built** |
| 162a/b | The Verbena · The Garden | daf pair | **built** |
| 164a/b | The Virtual Adepts · The Web | daf pair | **built** |
| 515a | Forces | daf (Sphere mold) | **built** |
| 515b | Conjunctions | daf | **built** |
| 533a | Paradox | daf | **built** |
| 533b | Witnesses | daf | **built** |
| everything else | — | — | briefed in plans/folio-briefs.md |

## Phase 1 — Template proofs (do these first, in this order)

Each proves a mold the rest of production reuses. Definition of done is in
CLAUDE.md.

1. ~~**f515 Forces** (Sphere daf)~~ **done** — the Sphere mold is proven;
   folios 512–524 batch against `content/f515a_forces.py`.
2. ~~**f148 Akashic Brotherhood** (Avot daf)~~ **done** — the Avot mold is proven;
   chapter V batches against `content/f148a_akashayana.py`.
3. **f435 Hazards** (luach). Requires `render_luach` in build.py + table CSS
   in chrome/daf.css. Spec: plans/pagetypes.md. Proves the chart mold used by
   273/275/303/435 and the minor tractates.
4. **f250 The Seder of Creation** (seder). Requires `render_seder` + CSS.
   Spec: plans/pagetypes.md.

After each proof: extract anything reusable you learned into SPEC.md (new
conventions get written down, same commit).

## Phase 2 — Chapters, in dependency order

Rationale: mechanics folios get cited by everything, so they go early; the
faction chapters batch cleanly once their molds exist.

1. **IX Middot** (384, 385, 393, 406) — the dice; everything cites these.
2. **X Strife** (409, 423, 430, 435✓) — combat; 435 already done in Phase 1.
3. **XI The Book of Magick** (500, 512–524 batch vs the f515 mold, 554,
   567/572/586, 607) — the heart; largest chapter, ~16 remaining after proofs.
4. ~~**V Avot** (150–164 batch vs the f148 mold)~~ **done** — chapter V complete, every folio an a/b pair.
5. **VI The Union** (168, 186–194) — decide the register-swap question on 168
   before batching the Conventions (see chapter VI brief).
6. **II The Awakening** (38, 43, 46) and **III The World** (62, 78, 82).
7. **IV The Worlds Beyond** (89, 91, 109).
8. **VII The Unseated and the Fallen** (3b, 197, 224, 234) — 3b pays the debt
   the Masoret of 2a promised.
9. **VIII The Order of Making** (250✓, 273, 275, 303, 328) — luachs + Arete.
10. **I remainder**: f143 Certámen.
11. **Minor tractates**: Kelim (K.1–K.2), Bestiary (B.1–B.3), shtar.

## Phase 3 — Bindery (when folio count makes the flat tab bar absurd, ~15+)

- Navigation at scale: the codex is deliberately tab-less (pages turn via
  arrows/keys/swipe; the shaar ToC deep-links by hash). When the folio count
  grows, invest in the shaar ToC (and perhaps per-chapter half-title leaves),
  not a tab bar.
- Auto-generate the shaar ToC from build.py's MANIFEST + brief titles
  (single source of truth; today shaar.py is hand-kept).
- Print stylesheet (each leaf a print page; binder hidden).
- Optional: client-side search across leaves; per-folio deep links already
  work (#515 etc.).

## Standing decisions (made; do not relitigate without cause)

- Folio numbers are M20 page numbers; Chapter I keeps 2a–3b by printers'
  custom (SPEC §1).
- Fiction never excerpted, only retold; mechanics restated (SPEC §0).
- Edition differences are variant manuscripts in the outer commentary, never
  silently harmonized.
- Storyteller advice lives in the Later Authorities of the folio it concerns;
  there is no "storytelling chapter."
- Every chapter owns at least one honest TEYKU.

## Open questions (decide during the relevant folio)

- Chapter VI register swap: do Convention folios flip the commentary voices
  (inner = procedures-manual deadpan, outer = Tradition polemic)? Trial it on
  f168 and decide before batching 186–194.
- f143 vs f430 (Certámen the institution vs. old-form duel mechanics): keep
  both or merge into 430 with a Masoret note at 143? Decide when writing 143.
- Whether the Digital Web deserves one luach after all (currently cut).
