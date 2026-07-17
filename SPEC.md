# SPEC — Tractate Aliyah

The house style for rendering Mage: the Ascension (M20) as a Talmudic tractate.
Every folio produced for this project must conform to this document. When a
convention here conflicts with convenience, the convention wins; when a new
convention is invented, it gets written into this file in the same commit.

## 0. The two inviolable rules

1. **No text of any sourcebook is ever reproduced.** Mechanics are restated as
   law in original wording (game mechanics themselves are not protected; their
   expression is — so ours is always our own). Fiction and history are *retold*
   as aggada, never excerpted, never closely paraphrased. Ein Mishpat cites
   page numbers so readers can find the real text; the folio never contains it.
   Character names, dates, and events of the setting are facts of the fiction
   and fine to use; sentences of the books are not.
2. **All commentary is out of character.** The one bounded exception is aggada:
   the narrative portions of the Gemara are told in a storyteller's voice. The
   commentaries around them discuss rules, sources, editions, and play — never
   pretending to be written by mages.

## 1. The conceit

- The corpus is **Seder Chashak** (חשך, "to be dark, hidden, obscured") — the
  World of Darkness as an order of tractates. This volume is **Tractate
  Aliyah** (עלייה, "ascension"): Mage. The sibling tractates carry Hebrew
  names chosen for the connotations of each line's subtitle, and exist as
  **Sharrim** — title pages with all-wanting ToCs (see §3) — plus Masoret
  cross-references, until someone writes their folios:
  - **Masekha** (מסכה, "mask" — and, pointedly, "molten idol"): Vampire,
    the Masquerade. The pun on *masechet* is intentional and citable.
  - **Acharit** (אחרית, "the end of days," *acharit ha-yamim*): Werewolf,
    the Apocalypse.
  - **Neshiyah** (נשייה, "oblivion, the land of forgetting," Ps. 88's
    *eretz neshiyah* — where the dead are forgotten): Wraith, the Oblivion.
  - **Chalom** (חלום, "dream"; Ps. 126's "we were like dreamers" — exile
    remembered as a dream): Changeling, the Dreaming.
  - **Din** (דין, "judgment"; *Yom ha-Din*, the Day of Reckoning): Hunter,
    the Reckoning.
  - **Techiyah** (תחייה, "resurrection," *techiyat ha-metim*): Mummy, the
    Resurrection.
  - **Nefilim** (נפילים, "the fallen ones," Gen. 6): Demon, the Fallen.
  In-folio references use the Hebrew name (e.g. "Tractate Masekha's
  breach"); the shelf shows Hebrew script on the spine-head and the
  transliteration on the spine.
- **Folio numbers are M20 page numbers.** Folio 148 is the Akashayana because
  that is their page in the book; the Spheres run 511–527; Paradox is 533.
  This makes Ein Mishpat citations and folio numbers one concordance, and
  makes every gap ("the folios between are wanting") honest structure.
  Exception, by printers' custom: tractates open at folio 2, so Chapter the
  First (the founding) holds folios 2a–3b regardless of M20 pagination. A
  hagahah may wink at this.
- Folio sides: `a` recto, `b` verso. Recto/verso pairs should be thematically
  paired when possible (2a founding / 2b betrayal; 533a Paradox / 533b
  Witnesses).

## 2. Apparatus — what goes in which layer

| Layer | Function | Source material it absorbs |
|---|---|---|
| **Mishnah** (center, top) | Binding mechanics as terse law, original wording | The rule itself |
| **Gemara** (center, below the dotted rule) | Derivations, worked examples ("Come and hear:…"), and **aggada** — fiction and history retold | M20's fiction, preludes, history chapters |
| **Inner commentary** ("On the Law" / named voice) | The plain sense: how the rule runs at the table; lemma-by-lemma | M20's explanatory body text, as function not text |
| **Outer commentary** ("On the Story" / "The Disputants") | Dialectic: difficulties, named camps, edition variances as variant manuscripts, community debates, optional rules | Sidebars, optional rules, 30 years of arguments |
| **Ein Mishpat** (left gloss) | Citations *outward*: book, edition, page | — |
| **Masoret** (right gloss) | Citations *inward*: cross-folio and cross-tractate references | — |
| **The Later Authorities** (bottom band) | Storyteller advice attached to the rule it advises about; genre consequences of rulings; procedure ("declare it in session zero") | **All of M20 Chapter Seven distributes here, folio by folio** |
| **Hagahah** (dark strip) | Errata, in-jokes, one-liners that earn their place | — |
| **Colophon** | Page's self-description + forward/backward hand-off | — |

Register conventions:
- Commentary voices are **named schools**, not people: The Bystander, The
  Census, The Disputants, On the Law, On the Story. New folios may coin new
  voices when the topic warrants (a Sphere folio might oppose "The Ladder"
  and "The Gradient").
- Talmudic formulas, used sparingly and in English: "Some say… and some say",
  "An objection: … Answer:", "Come and hear:", "OUR TEACHERS TOLD:" and
  "IT HAPPENED THAT" (aggada openers, set in `.kw`), and **TEYKU** ("let it
  stand") for genuinely unresolved questions. Every chapter should own at
  least one teyku; do not manufacture false resolutions.
- Lemmas: outer/inner commentary paragraphs open with a bold small-caps
  quotation of the center text (`<span class="lemma">…</span>`), then comment.
- Edition variance: the Mishnah states the M20 baseline. Revised/2nd/1st
  readings appear in the outer commentary as variant manuscripts ("the first
  recension reads…"), never silently harmonized. "One does not harmonize what
  the sources left rough. The roughness is data."
- The Acher rule: where the setting refuses a name (Thoabath), the apparatus
  enacts the refusal formally rather than merely describing it.

## 3. Page types

- **daf** — the standard interlocking page (implemented). Regions: running
  head, subtitle, glosses, title box, center (Mishnah+Gemara), two commentary
  flows, bottom band, hagahah, colophon.
- **shaar** — ornate title page + table of contents (implemented). Folio 1 of
  the codex; ToC anchors navigate the codex by hash.
- **the shelf** — the site's home page (implemented; `dist/index.html`, not a
  folio). The eight tractates of Seder Chashak stand spine-out on a shelf in
  publication order of their game lines. Every spine is lit and clickable:
  Aliyah (tallest, maroon and gold) opens the bound codex, which has no tab
  bar — pages are turned with the side arrows, arrow keys, swipe, or a
  `#folio` hash; the seven siblings, each in its own line's spine colors,
  open their Sharrim.
- **the Sharrim** — sibling-tractate title pages (implemented;
  `dist/tractate-<name>.html`, one per line). Each is the shaar structure
  re-skinned in its source book's interior language: display face and
  palette per `plans/sharrim/style-notes.md`, ToC drawn from the core
  book's structure (`plans/sharrim/*-toc.md`) with **every row wanting**,
  the same imprint discipline (fan work, no text reproduced, folio = source
  page number), Dark Pack notice, and a colophon that says plainly the
  volume is unbound. Content modules `content/shaar_<name>.py` (type
  `shaar` + a `skin` key); skins live in `chrome/sharrim.css`; each page
  embeds only Goudy plus its own display face. When a sibling tractate
  gains real folios, its shaar ToC rows gain anchors exactly as Aliyah's
  did.
- **luach** — chart folio: the center block is a reference table (difficulty
  charts, weapons, backlash ladder, Merits/Flaws), commentary frame thinner.
  Precedent: the Vilna's own diagram pages in Eruvin. **Implemented** (proof:
  f435a/b). Conventions, per the proof: the content dict is a daf whose
  `center` is a one-paragraph caption Mishnah + `<table class="luach">`
  (+ optionally a short Gemara below the table); `type: 'luach'` renders via
  `render_daf` with a `luach-page` class; wide tables set `center_w: '44%'`
  in the dict (a `--center-w` override on the leaf). Table CSS lives in
  daf.css (Vilna look: horizontal rules only, Abbess letterspaced header
  row, alternating row tint, `.num` right-aligned). Charts **restate the
  structure and cite the grain**: fine-grained source ladders may be
  abridged to bands with an Ein Mishpat note (ruling recorded in f435b's
  outer commentary). Budgets: the daf word budgets apply with the caption +
  table text counted as the center; verify must pass unchanged.
- **seder** — ordered-procedure page for character creation: numbered steps as
  the center, commentary wrapped around each step. The Haggadah's genre.
  **Not yet implemented.**
- **shtar** — the character sheet as a formal deed (ketubah tradition of
  fixed-formula documents). **Not yet implemented.**

## 4. Geometry contract (daf pages)

The interlock is computed at runtime by `chrome/engine.js`:
- The title box and center Text are absolutely positioned; floated `.sp`
  spacers inside each flow carve their silhouette, sized from measured pixels.
  Flows therefore run above the Text (to the title box's shoulders), beside
  it, and beneath it.
- **Requirements** (enforced by `verify.py` at 1280px):
  - No commentary line may overlap the Text (hard fail).
  - Both flows should wrap beneath the Text — `under > 0` on both sides
    (warning). Target a stagger: the two flows ending 0–90px apart, or one
    outrunning the other by a few lines. A blank corner > ~150px means a flow
    is too short.
- **Length budgets** (empirical, at the default type sizes): center 350–520
  words; each commentary 1.3–1.6× the center's word count. If verify warns
  `does not wrap beneath`, add a lemma paragraph to the short flow; content
  should be added, never padding.
- Mobile (≤860px) stacks: title, center, inner, outer, glosses, bottom. The
  engine zeroes the spacers; nothing else to do.

## 5. Chapter plan (the whole corebook)

Folio numbers = M20 pages. ✅ = built. Budgets are folio counts, not promises.

| # | Chapter (perek) | Folios | Contents | Budget |
|---|---|---|---|---|
| I | The Nine Seats | 2a ✅ 2b ✅ 3a ✅ 3b, 143 | Founding, betrayal, judgments; the Disparates' answer (3b); Certámen as trial by ordeal (143) | 5 |
| II | The Awakening | 38, 43, 46 | What a mage is; the Avatar and its Essences; Arete and the War | 3 |
| III | The World | 62, 78, 82 | Consensus; Quintessence/Tass/Nodes; the Gauntlet | 3 |
| IV | The Worlds Beyond | 89, 91, 109 | Penumbra; three Umbrae compressed hard; Horizon (cite 2a) | 3 |
| V | Avot: The Traditions | 148–164, odd | One folio each, Pirkei Avot form: Mishnah = paradigm/practice/instruments/Sphere as law; Gemara = lineage aggada ("X received from Y…"); outer = the Tradition's internal factions arguing | 9 |
| VI | The Union | 168, 186–194 | Precepts of Damian; five Conventions. Register swap option: inner commentary in procedures-manual deadpan, outer carries Tradition polemic | 6 |
| VII | The Unseated and the Fallen | 197, 224, 234 | Disparates as a body (this is 3b's promise kept), Nephandi, Marauders | 3–4 |
| VIII | The Order of Making | 250, 273, 275, 303, 328 | Chargen as **seder**; Attributes/Abilities/Backgrounds as **luach**; Arete/Willpower/Quintessence | 5 |
| IX | Middot: Measures | 384, 385, 393, 406 | Golden Rule; dice, difficulties, actions; botches and the Rule of One (its theology goes in the hagahah); health | 4 |
| X | Strife | 409, 423, 430, 435 | Combat phases as a Mishnah ladder; magick-and-violence; Do; duels; hazards **luach** | 5 |
| XI | The Book of Magick | 500, 512–524, 533 ✅✅, 554, 567–586, 607 | Casting step-by-step; **nine Sphere folios** (dot-ladder as Mishnah, rank-boundary disputes as outer commentary); Paradox ✅ Witnesses ✅; Quiet; Focus (belief/practice/instrument — 3 folios, the paradigm heart); rotes & procedures | 18 |
| — | Minor tractates | K.*, B.* | **Kelim** (Wonders); Bestiary/antagonists | 4–5 |

**Cut entirely:** vehicle systems, drug/poison tables, deep Digital Web
mechanics, the ten individual Disparate writeups, standalone fiction chapters
(fiction dissolves into gemara). Compress, don't apologize.

Total ≈ 70 folios + shaar.

## 6. Production workflow

1. Copy the nearest existing content module in `content/` as a template;
   name it `f{NNN}{a|b}_{slug}.py`.
2. Write the dict. HTML entity conventions: `&mdash; &rsquo; &ldquo; &rdquo;
   &middot;` (files are ASCII with entities, matching the ported folios).
3. Add the module to `MANIFEST` in build.py (keep `'...'` lacunae markers
   between non-adjacent folios), and un-wanting its line in
   `content/shaar.py`'s ToC (set the anchor). ToC rows are one per **folio
   number**, not per side: the anchor is the `a` side, the label is the bare
   number, and the recto and verso titles are joined with a middot
   ("Forces · Conjunctions"). When a folio's `b` side is bound later, extend
   the existing row's title rather than adding a row.
4. `python3 build.py` → `python3 verify.py`.
5. If verify warns a flow doesn't wrap: add a lemma to that flow (see §4).
6. Eyeball the page in a browser at desktop and ≤860px widths.

## 7. Phase plan

- **Phase 1 (next): template proofs.** One folio of each unbuilt page type,
  proving the molds: **f515 Forces** (Sphere daf — "control vs. create" is the
  juiciest dot-boundary dispute), **f148 Akashayana** (Avot daf), **f435
  Hazards or f273 Attributes** (luach — requires implementing `render_luach`),
  **f250 The Seder of Creation** (seder — requires `render_seder`).
- **Phase 2: chapters in dependency order.** IX Middot and X Strife early
  (everything cites the dice); then XI (Spheres batch-produced against the
  f515 mold); then V/VI (Traditions/Conventions against f148); II–IV; VII;
  VIII; minor tractates last.
- **Phase 3: bindery.** Chapter-grouped binder (a tabs row per perek or a
  dropdown), shaar ToC auto-generated from MANIFEST instead of hand-kept,
  print stylesheet, optional search.

## 8. Voice miscellany (earned rules — keep them)

- The tractate's thesis, stated at 3a and citable: *all of Ascension's law is
  the law of who is watching.* New folios should notice when they are secretly
  about witnesses, and say so in the Masoret.
- Later Authorities always end concretely: what to declare in session zero,
  what to put on the table, what the ruling does to genre.
- Hagahot are earned, one per page, and funnier for being dry.
- "The Mishnah rules what ought; the aggada records what was" — the licensed
  move for law/history contradictions.
- Ein lemedin min ha-aggada — except when one does. The exception is the whole
  of play.
