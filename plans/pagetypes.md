# Page-type design specs

The daf and shaar are implemented (build.py: `render_daf`, `render_shaar`).
This file specifies the three unbuilt types and the shaar's phase-3 upgrades.
When implementing, add the renderer to build.py's RENDERERS, the CSS to
chrome/daf.css (page-scoped classes), and a `'type'` value to the content
dict format — then record the finalized conventions in SPEC §3.

General rule for all types: same running head, subtitle, frame, colophon,
and Ein Mishpat/Masoret discipline as the daf. The page types vary the
*center* of the page, not its apparatus.

---

## luach (chart folio) — needed by f273, f275, f303, f435, K.*, B.*

Precedent: the Vilna edition's own diagram pages (Eruvin). The reference
table IS the center text; commentary frames it.

Layout:
- Center block: an HTML `<table class="luach">` replacing the Mishnah/Gemara
  article. A one-paragraph Mishnah caption above the table (the rule the
  table expands), set like a regular Mishnah opener.
- The interlock engine works unchanged if the table lives inside
  `.center-text` — the engine measures the element's height, not its
  contents. Prefer that route over a new well geometry.
- Commentary flows are *thinner in content*, not in width: one lemma per
  table region (a column, a band of rows), disputes about edge cases.
  Glosses cite the source pages for each table section.
- Wide tables (weapons, hazards): allow `--center-w: 44%` via a per-page
  CSS variable override on the leaf (`style="--center-w:44%"` on `.page`);
  verify still must pass.

Table CSS (add to daf.css): Goudy 0.78rem; header row in Abbess small size,
maroon, letterspaced; row rules `1px solid rgba(95,29,37,0.25)`; alternating
row tint `rgba(95,29,37,0.04)`; numeric columns right-aligned; no vertical
rules (the Vilna look is horizontal).

Content dict: as daf, but `center` contains caption + table markup, and the
`type` is `'luach'`. Renderer can be `render_daf` with a different class on
`<main>` if no structural change proves necessary — decide during f435.

## seder (ordered-procedure folio) — needed by f250

The Haggadah's genre: a numbered ritual whose steps are the center, with
commentary wrapped around the sequence.

Layout:
- Center: the steps as a numbered list styled as Mishnah clauses — each step
  a `<p>` opening with `<span class="term">Step N.</span>` and a terse
  imperative ("Choose who she is before what she can do."). After the last
  step, a short Gemara noting where the order came from and why it is an
  order (concept precedes numbers; numbers precede magick).
- Inner commentary: one lemma per step — the plain sense, the numbers
  involved (point totals live here, not in the center; the center is ritual,
  the commentary is arithmetic).
- Outer commentary: the disputes — freeform vs. priority allocation across
  editions (variant manuscripts), "concept first" vs. "mechanics first" table
  cultures, the prelude question (play it out vs. write it down).
- Later Authorities: session-zero procedure; troupe-style creation; what to
  do with the player who arrives with a finished sheet.
- No new geometry needed: it is a daf whose center is a liturgy. `type:
  'seder'` may alias render_daf with a `seder-page` class for numbered-step
  styling.

## shtar (the character sheet as deed) — minor tractate appendix

The ketubah tradition: a fixed-formula legal instrument with blanks.

Layout:
- A single ornamental instrument (no commentary flows): bordered like the
  shaar arch, text in formulaic clauses with rule-lined blanks — name, Nature
  and Demeanor, Essence, Tradition and the seat it holds, Attributes/Abilities
  as witnessed declarations, Arete sworn before witnesses (two signature
  lines: mentor and Storyteller — the witnesses law of 533b, made into a
  form).
- Fillable: plain HTML inputs styled as blanks; a print stylesheet that
  hides input chrome. No storage; it prints or it screenshots.
- One hagahah at the foot; Ein Mishpat cites the character-creation pages.
- This is the one page type that is allowed to be beautiful first and
  disputatious second.

## shaar — built; phase-3 upgrades

- Auto-generate the ToC from build.py MANIFEST + per-brief titles, replacing
  the hand-kept list in content/shaar.py (single source of truth; "wanting"
  entries come from briefs not yet in MANIFEST).
- Chapter anchors: when the binder becomes chapter-grouped, shaar chapter
  heads link to the first folio of the chapter.
- Keep the imprint paragraph's fan-work/no-reproduction statement verbatim —
  it is the project's license plate.
