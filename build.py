#!/usr/bin/env python3
"""Build Tractate Aliyah: compiles content/*.py modules into standalone folio
pages and the bound codex (dist/tractate-aliyah.html).

Usage:  python3 build.py            # build everything
        python3 build.py f533a      # build only folios matching a prefix
"""
import base64
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
CHROME = ROOT / 'chrome'
CONTENT = ROOT / 'content'
DIST = ROOT / 'dist'

# The binder's leaf order. Lacunae ('...') mark wanting folios between entries.
MANIFEST = [
    'shaar',
    'f002a_convocation',
    'f002b_betrayal',
    'f003a_judgments',
    'f003b_unseated',
    '...',
    'f148a_akashayana',
    'f148b_the_wheel',
    'f150a_chorus',
    'f150b_reformation',
    'f152a_ecstasy',
    'f152b_burden',
    'f154a_dreamspeakers',
    'f154b_the_people',
    'f156a_chakravanti',
    'f156b_jhor',
    'f158a_hermes',
    'f158b_houses',
    'f160a_ether',
    'f160b_paradigma',
    'f162a_verbena',
    'f162b_garden',
    'f164a_adepts',
    'f164b_the_web',
    '...',
    'f384a_golden_rule',
    'f384b_contract',
    'f385a_dice',
    'f385b_count',
    '...',
    'f393a_rule_of_one',
    'f393b_comment',
    '...',
    'f406a_health',
    'f406b_wound',
    '...',
    'f512a_correspondence',
    'f512b_the_reach',
    'f514a_entropy',
    'f514b_fortune',
    'f515a_forces',
    'f515b_conjunctions',
    'f516a_life',
    'f516b_healing',
    'f517a_matter',
    'f517b_workshop',
    'f519a_mind',
    'f519b_seeming',
    'f520a_prime',
    'f520b_the_well',
    'f521a_spirit',
    'f521b_crossing',
    'f522a_time',
    'f522b_rewind',
    'f533a_paradox',
    'f533b_witnesses',
]


def load(name):
    spec = importlib.util.spec_from_file_location(name, CONTENT / (name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.FOLIO


def font_css():
    ab = base64.b64encode((CHROME / 'fonts/ABBESSOpti.otf').read_bytes()).decode()
    go = base64.b64encode((CHROME / 'fonts/GOUDOS.TTF').read_bytes()).decode()
    return (
        "@font-face { font-family: 'Abbess'; src: url(data:font/otf;base64,%s) "
        "format('opentype'); font-display: swap; }\n"
        "@font-face { font-family: 'Goudy Old Style'; src: url(data:font/ttf;base64,%s) "
        "format('truetype'); font-display: swap; }\n" % (ab, go))


def render_daf(m):
    """The standard daf body: glosses, title box, center Text, two flows,
    bottom band. Geometry is applied at runtime by chrome/engine.js."""
    return f"""<main class="page">
  <div class="frame">
    <header class="running-head">
      <div class="folio">SEDER CHASHAK &middot; \u05d7\u05e9\u05da</div>
      <div class="masechet">Tractate Aliyah</div>
      <div class="folio right">FOLIO {m['folio']}</div>
    </header>
    <p class="subtitle">{m['subtitle']}</p>
    <div class="well">
      <aside class="gloss gloss-left">
        <div class="g-head">EIN MISHPAT</div>
        {m['glossL']}
      </aside>
      <aside class="gloss gloss-right">
        <div class="g-head">MASORET</div>
        {m['glossR']}
      </aside>
      <div class="titlebox">
        <div class="chapter">{m['chapter']}</div>
        <h1>{m['h1']}</h1>
        <div class="rubric">{m['rubric']}</div>
      </div>
      <article class="center-text">
        {m['center']}
      </article>
      <div class="flow inner-flow">
        <div class="sp"></div><div class="sp"></div>
        <h2 class="comm-head">{m['inner_head']}</h2>
        {m['inner']}
      </div>
      <div class="flow outer-flow">
        <div class="sp"></div><div class="sp"></div>
        <h2 class="comm-head">{m['outer_head']}</h2>
        {m['outer']}
      </div>
    </div><!-- /well -->
    <div class="bottom-band">
      <h2 class="comm-head">{m['bottom_head']}</h2>
      <div class="bottom-cols">
        {m['bottom']}
      </div>
      <div class="hagahah"><span class="g-title">Gloss</span>{m['hagahah']}</div>
    </div>
    <footer class="colophon">{m['colophon']}</footer>
  </div>
</main>"""


DARKPACK_TEXT = (
    'Unofficial fan content made under Paradox Interactive&rsquo;s '
    '<a href="https://www.paradoxinteractive.com/games/world-of-darkness/community/dark-pack-agreement">'
    'Dark Pack agreement</a>; not official World of Darkness material. '
    'Portions of the materials are the copyrights and trademarks of Paradox '
    'Interactive AB, and are used with permission. All rights reserved. For more '
    'information please visit <a href="https://www.worldofdarkness.com">worldofdarkness.com</a>.')


def darkpack_logo_uri():
    b = base64.b64encode((CHROME / 'darkpack-logo.png').read_bytes()).decode()
    return 'data:image/png;base64,' + b


def render_shaar(m):
    chapters = []
    for head, entries in m['toc']:
        rows = []
        for anchor, label, title in entries:
            if anchor:
                rows.append(f'<div><a href="#{anchor}"><span class="fol">{label}</span>{title}</a></div>')
            else:
                rows.append(f'<div class="toc-wanting"><span class="fol">{label}</span>{title} &mdash; wanting</div>')
        chapters.append('<div class="toc-chapter"><div class="toc-head">%s</div>%s</div>'
                        % (head, '\n'.join(rows)))
    return f"""<main class="page shaar-page">
  <div class="frame">
    <div class="shaar-arch">
      <div class="shaar-seder">{m['seder']}</div>
      <div class="shaar-hebrew">{m['hebrew']}</div>
      <h1 class="shaar-title">{m['tractate']}</h1>
      <p class="shaar-imprint">{m['imprint']}</p>
      <hr class="shaar-rule">
      <div class="shaar-toc">
        {''.join(chapters)}
      </div>
      <hr class="shaar-rule">
      <div class="darkpack">
        <img src="{darkpack_logo_uri()}" alt="World of Darkness Dark Pack logo">
        <p>{DARKPACK_TEXT}</p>
      </div>
      <p class="shaar-colophon">{m['colophon']}</p>
    </div>
  </div>
</main>"""


# The eight tractates of Seder Chashak, shelved in publication order of the
# game lines they answer to. Hebrew names per SPEC section 1; a spine lights
# up and becomes clickable when its tractate is bound.
SHELF = [
    ('Masekha',  '\u05de\u05e1\u05db\u05d4',             'Vampire: the Masquerade',   None),
    ('Acharit',  '\u05d0\u05d7\u05e8\u05d9\u05ea',       'Werewolf: the Apocalypse',  None),
    ('Aliyah',   '\u05e2\u05dc\u05d9\u05d9\u05d4',       'Mage: the Ascension',       'tractate-aliyah.html'),
    ('Neshiyah', '\u05e0\u05e9\u05d9\u05d9\u05d4',       'Wraith: the Oblivion',      None),
    ('Chalom',   '\u05d7\u05dc\u05d5\u05dd',             'Changeling: the Dreaming',  None),
    ('Din',      '\u05d3\u05d9\u05df',                   'Hunter: the Reckoning',     None),
    ('Techiyah', '\u05ea\u05d7\u05d9\u05d9\u05d4',       'Mummy: the Resurrection',   None),
    ('Nefilim',  '\u05e0\u05e4\u05d9\u05dc\u05d9\u05dd', 'Demon: the Fallen',         None),
]


def render_shelf():
    spines = []
    for i, (name, hebrew, line, href) in enumerate(SHELF, 1):
        if href:
            spines.append(
                f'<a class="book-spine aliyah" href="{href}" '
                f'title="Tractate {name} \u00b7 {line}">\n'
                f'  <span class="spine-word">{hebrew}</span>\n'
                f'  <span class="spine-title">Tractate {name}</span>\n'
                f'  <span class="spine-band"></span>\n'
                f'</a>')
        else:
            spines.append(
                f'<div class="book-spine wanting b{i}" '
                f'title="Tractate {name} \u00b7 {line}">\n'
                f'  <span class="spine-word">{hebrew}</span>\n'
                f'  <span class="spine-title">Tractate {name}</span>\n'
                f'  <span class="spine-band"></span>\n'
                f'</div>')
    return f"""<main class="shelf-room">
  <header class="shelf-head">
    <div class="shelf-hebrew">\u05d7\u05e9\u05da</div>
    <div class="shelf-seder">Seder Chashak</div>
  </header>
  <div class="shelf">
    <div class="books">
      {chr(10).join(spines)}
    </div>
    <div class="plank"></div>
    <div class="plank-shadow"></div>
  </div>
</main>"""


RENDERERS = {'daf': render_daf, 'shaar': render_shaar}


def page_shell(title, body, extra_css='', extra_js=''):
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'<title>{title}</title>\n'
        '<style>\n' + font_css() + (CHROME / 'daf.css').read_text()
        + extra_css + '\n</style>\n</head>\n<body>\n'
        + body
        + f'\n<footer class="darkpack-legal">{DARKPACK_TEXT}</footer>\n'
        + '\n<script>\n' + (CHROME / 'engine.js').read_text() + '\n</script>\n'
        + extra_js + '</body>\n</html>\n')


STANDALONE_INIT = """<script>
(function () {
  var leaf = document.body;
  function settle() {
    window.DafEngine.layoutLeaf(leaf);
    requestAnimationFrame(function () { window.DafEngine.layoutLeaf(leaf); });
  }
  window.addEventListener('resize', settle);
  window.DafEngine.mq.addEventListener
    ? window.DafEngine.mq.addEventListener('change', settle)
    : window.DafEngine.mq.addListener(settle);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(settle);
  window.addEventListener('load', settle);
  settle();
})();
</script>
"""


def build():
    DIST.mkdir(exist_ok=True)
    only = sys.argv[1] if len(sys.argv) > 1 else None
    leaves = []
    for entry in MANIFEST:
        if entry == '...':
            leaves.append(None)
            continue
        m = load(entry)
        body = RENDERERS[m['type']](m)
        leaves.append((m, body))
        if only and not entry.startswith(only):
            continue
        out = DIST / (entry + '.html')
        css = '\n' + (CHROME / 'shaar.css').read_text() if m['type'] == 'shaar' else ''
        out.write_text(page_shell(m['title'], body, extra_css=css, extra_js=STANDALONE_INIT))
        print(f'built {out.name}  ({out.stat().st_size:,} bytes)')

    # ---- the bound codex ----
    leaf_divs = []
    for item in leaves:
        if item is None:
            continue
        m, body = item
        anchor = m['folio'].lower()
        leaf_divs.append(f'<div class="leaf" data-folio="{anchor}" data-name="{m["name"]}">\n'
                         f'{body}\n</div>')

    nav = ('<nav class="codex-links">\n'
           '  <a class="shelf-link" href="./" title="return the volume to the shelf">'
           '&lsaquo; the shelf</a>\n'
           '  <a class="toc-link" href="#shaar" title="return to the shaar (table of contents)">'
           'contents</a>\n'
           '</nav>\n'
           '<button class="turn prev" aria-label="previous folio">&lsaquo;</button>\n'
           '<button class="turn next" aria-label="next folio">&rsaquo;</button>\n')

    codex = page_shell(
        'Tractate Aliyah \u00b7 Seder Chashak \u2014 the bound folios',
        nav + '<div class="book">\n' + '\n'.join(leaf_divs) + '\n</div>',
        extra_css='\n' + (CHROME / 'shaar.css').read_text()
                  + '\n' + (CHROME / 'codex.css').read_text(),
        extra_js='<script>\n' + (CHROME / 'codex.js').read_text() + '\n</script>\n')
    out = DIST / 'tractate-aliyah.html'
    out.write_text(codex)
    print(f'built {out.name}  ({out.stat().st_size:,} bytes)')

    # ---- the shelf (site home page) ----
    out = DIST / 'index.html'
    out.write_text(page_shell(
        'Seder Chashak \u2014 the shelf',
        render_shelf(),
        extra_css='\n' + (CHROME / 'shelf.css').read_text()))
    print(f'built {out.name}  ({out.stat().st_size:,} bytes)')


if __name__ == '__main__':
    build()
