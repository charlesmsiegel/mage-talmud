# PLAN — Tractate Aliyah

Status, phases, and priorities. SPEC.md is law; this file is the schedule.
Update the status tables here in the same commit as the work.

## Status

| Folio | Title | Type | State |
|---|---|---|---|
| shaar | Title page + ToC | shaar | **built** (phase-3 upgrades pending, see plans/pagetypes.md) |
| 38a/b | Of Gods and Men · The Fragile Path | daf pair | **built** |
| 43a/b | The Avatar · The Seeking | daf pair | **built** |
| 46a/b | The Will to Power · The War | daf pair | **built** — chapter II complete |
| 62a/b | Consensus and Belief · The Zones | daf pair | **built** |
| 78a/b | The Life-Blood · The Wells | daf pair | **built** |
| 82a/b | The Gauntlet · The Crossing | daf pair | **built** — chapter III complete |
| 89a/b | The Penumbra · The Reflection | daf pair | **built** |
| 91a/b | The Three Umbrae · The Courts | daf pair | **built** |
| 109a/b | The Horizon · The Made Countries | daf pair | **built** — chapter IV complete |
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
| 500a/b | Casting · The Long Working | daf pair | **built** |
| 512a/b | Correspondence · The Reach | daf pair | **built** |
| 514a/b | Entropy · Fortune | daf pair | **built** |
| 515a | Forces | daf (Sphere mold) | **built** |
| 515b | Conjunctions | daf | **built** |
| 516a/b | Life · Healing | daf pair | **built** |
| 517a/b | Matter · The Workshop | daf pair | **built** |
| 519a/b | Mind · The Seeming | daf pair | **built** |
| 520a/b | Prime · The Well | daf pair | **built** |
| 521a/b | Spirit · The Crossing | daf pair | **built** |
| 522a/b | Time · The Rewind | daf pair | **built** |
| 384a/b | The Golden Rule · The Contract | daf pair | **built** |
| 250a/b | The Seder of Creation · The Fifteen | seder pair (mold proof) | **built** |
| 409a/b | Combat · The Gun and the Word | daf pair | **built** |
| 423a/b | The Martial Arts and Do · The Eight Limbs | daf pair | **built** |
| 430a/b | Duels, Old Form · The Wager | daf pair | **built** |
| 435a/b | Hazards · The Breaking | luach pair (mold proof) | **built** |
| 385a/b | The Dice · The Count | daf pair | **built** |
| 393a/b | The Rule of One · The Comment | daf pair | **built** |
| 406a/b | Health · The Wound | daf pair | **built** |
| 533a | Paradox | daf | **built** |
| 533b | Witnesses | daf | **built** |
| 554a/b | Quiet · The Three Faces | daf pair | **built** |
| 567a/b | Focus: Belief · The Inheritance | daf pair | **built** |
| 572a/b | Focus: Practice · The Blend | daf pair | **built** |
| 586a/b | Focus: Instruments · The Inventory | daf pair | **built** |
| 607a/b | Rotes and Procedures · The Casebook | daf pair | **built** — chapter XI complete |
| 168a/b | The Precepts · The Clarifications | daf pair (register swap) | **built** |
| 186a/b | Iteration X · The Machine | daf pair | **built** |
| 188a/b | The New World Order · Room 101 | daf pair | **built** |
| 190a/b | The Progenitors · The Vat | daf pair | **built** |
| 192a/b | The Syndicate · The Ledger | daf pair | **built** |
| 194a/b | The Void Engineers · The Unfiled | daf pair | **built** — chapter VI complete |
| 197a/b | The Silent Alliance · The Wise Hearts | daf pair | **built** |
| 224a/b | The Fallen · The Deep Game | daf pair | **built** |
| 234a/b | The Mad · The Weather | daf pair | **built** — chapter VII complete |
| 273a/b | Attributes · The Ladder | luach pair | **built** |
| 275a/b | Abilities · The Knowledges | luach pair | **built** |
| 303a/b | Backgrounds · The Awakened Assets | luach pair | **built** |
| 328a/b | Arete and Will · The Price | daf pair | **built** — chapter VIII complete |
| 143a/b | Certámen · The Stakes | daf pair | **built** — chapter I complete; bound at its number |
| the Sharrim | seven sibling title pages | shaar (skinned) | **built** — see SPEC §3; sources in plans/sharrim/ |
| everything else | — | — | briefed in plans/folio-briefs.md |

## Phase 1 — Template proofs (do these first, in this order)

Each proves a mold the rest of production reuses. Definition of done is in
CLAUDE.md.

1. ~~**f515 Forces** (Sphere daf)~~ **done** — the Sphere mold is proven;
   folios 512–524 batch against `content/f515a_forces.py`.
2. ~~**f148 Akashic Brotherhood** (Avot daf)~~ **done** — the Avot mold is proven;
   chapter V batches against `content/f148a_akashayana.py`.
3. ~~**f435 Hazards** (luach)~~ **done** — the chart mold is proven
   (f435a/b, `render_luach`, table CSS); 273/275/303 batched against it
   (since built), the minor tractates next. Conventions recorded in SPEC §3.
4. ~~**f250 The Seder of Creation** (seder)~~ **done** — the
   ordered-procedure mold is proven (f250a + its Fifteen verso,
   `render_seder`, step CSS); conventions in SPEC §3. All four page types
   are now implemented.

After each proof: extract anything reusable you learned into SPEC.md (new
conventions get written down, same commit).

## Phase 2 — Chapters, in dependency order

Rationale: mechanics folios get cited by everything, so they go early; the
faction chapters batch cleanly once their molds exist.

1. ~~**IX Middot** (384, 385, 393, 406)~~ **done** — the dice; four a/b pairs,
   chapter complete.
2. ~~**X Strife** (409, 423, 430, 435)~~ **done** — four pairs, the last two
   sides the luach proof; chapter complete.
3. ~~**XI The Book of Magick**~~ **done** — Sphere pairs 512–522, 500 Casting,
   554 Quiet, the focus trio 567/572/586, and 607 Rotes; chapter complete.
4. ~~**V Avot** (150–164 batch vs the f148 mold)~~ **done** — chapter V complete, every folio an a/b pair.
5. ~~**VI The Union** (168, 186–194)~~ **done** — register swap trialed on 168
   and adopted for the whole chapter (see Standing decisions); six a/b pairs.
6. ~~**II The Awakening** (38, 43, 46) and **III The World** (62, 78, 82)~~
   **done** — both chapters complete, every folio an a/b pair.
7. ~~**IV The Worlds Beyond** (89, 91, 109)~~ **done** — three a/b pairs;
   chapter complete.
8. ~~**VII The Unseated and the Fallen** (3b✓, 197, 224, 234)~~ **done** —
   three a/b pairs; chapter complete.
9. ~~**VIII The Order of Making** (250, 273, 275, 303, 328)~~ **done** —
   the seder pair, three luach pairs (the six VIII luachs batched against
   the f435 mold), and the f328 Arete/Price daf pair; chapter complete.
10. ~~**I remainder**: f143 Certámen~~ **done** — the f143a/b pair
    (institution + stakes), bound at its number between chapters IV
    and V; chapter I complete.
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
- Chapter VI runs the register swap: inner commentary in procedures-manual
  deadpan ("Standard Commentary … per the manual"), outer as the Traditions'
  polemic with the Union answering ("The Council's Objections"). Trialed on
  f168, adopted for 186–194. Both registers stay out of character per SPEC §0.

## Open questions (decide during the relevant folio)

- ~~f143 vs f430: keep both or merge?~~ **Decided: keep both.** f143 owns
  the institution (the courthouse), f430 the old-form mechanics (the
  arena); both Masorets mark the division as standing. The bound folios
  already reserved 143 "the institution's full trial," and the material
  splits cleanly (TBOoH Rev pp.26/37/43-45 vs. M20 pp.430-433).
- Whether the Digital Web deserves one luach after all (currently cut).
