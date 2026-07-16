# Tractate Aliyah

Mage: the Ascension rendered as a Talmudic tractate — the rules as Mishnah,
the setting's history retold as aggada, and interlocking commentaries arguing
about both. Five folios exist; the plan for ~70 is in `SPEC.md` §5.

This is a fan work. No sourcebook text is reproduced anywhere in the project
(see SPEC §0, rule 1 — the inviolable one); mechanics are restated in original
wording and the fiction is retold, with Ein Mishpat glosses citing the real
page numbers instead.

## Dark Pack

<img src="assets/darkpack_logo.png" alt="World of Darkness Dark Pack logo" width="180">

This project is unofficial fan content made under Paradox Interactive's
[Dark Pack agreement](https://www.paradoxinteractive.com/games/world-of-darkness/community/dark-pack-agreement).
It is not official World of Darkness material, it is non-commercial, and it
is free to access.

> Portions of the materials are the copyrights and trademarks of Paradox
> Interactive AB, and are used with permission. All rights reserved. For more
> information please visit [worldofdarkness.com](https://www.worldofdarkness.com).

The build embeds this notice and the Dark Pack logo into the site itself
(logo on the shaar; a legal line in every page's footer).

## Website

Every push to `main` builds `dist/` and publishes it to GitHub Pages
(`.github/workflows/site.yml`): the bound codex is the front page, and each
standalone folio is reachable at its own path (e.g. `/f533a_paradox.html`).
Pull requests run the same build plus `verify.py` as checks.

## Quickstart

```bash
pip install playwright && playwright install chromium   # for verify.py only
python3 build.py        # builds dist/: five standalone folios + the codex
python3 verify.py       # geometry checks on every leaf of the codex
open dist/tractate-aliyah.html
```

## Layout

```
CLAUDE.md           project orientation for Claude Code (read first)
build.py            compiles content/ -> dist/ (standalone folios + bound codex)
verify.py           playwright harness: interlock geometry per leaf
SPEC.md             THE FORMAT BIBLE. Read before writing any folio.
PLAN.md             roadmap, status tables, phase checklists
plans/
  folio-briefs.md   a content brief for every planned folio (~65)
  pagetypes.md      design specs: luach, seder, shtar; shaar upgrades
assets/
  darkpack_logo.png Dark Pack logo (README display copy)
chrome/
  daf.css           shared page styles (fontless; fonts injected at build)
  codex.css         binder bar, page-turn animation
  shaar.css         title-page styles (standalone shaar + codex)
  engine.js         DafEngine: runtime interlock layout (class-scoped)
  codex.js          CodexNav: tabs, arrows, keyboard, swipe, hash routing
  fonts/            Abbess + Goudy Old Style, base64-embedded at build time
  darkpack-logo.png small Dark Pack logo, base64-embedded into the shaar
content/
  shaar.py          title page + table of contents (anchors = binder hashes)
  f002a_*.py ...    one module per folio; dict format documented by example
dist/               build products (self-contained HTML, safe to share singly)
```

## Working on it (Claude Code notes)

- To add a folio: SPEC §6 is the checklist. Copy the nearest content module,
  write the dict, register it in `build.py` MANIFEST and `content/shaar.py`,
  build, verify.
- `verify.py` warnings about a flow not wrapping beneath the Text mean that
  commentary is too short — add a lemma paragraph, never padding (SPEC §4
  has the length budgets).
- Phase 1 tasks (the template proofs) are enumerated in SPEC §7: Forces (515),
  the Akashayana (148), a luach, and the character-creation seder — the last
  two need small new renderers in `build.py` plus CSS.
- The existing five folios are the style reference. When in doubt, read 533b
  and 3a: one mechanics daf, one derivation daf, between them the whole voice.
