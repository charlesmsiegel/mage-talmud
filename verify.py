#!/usr/bin/env python3
"""Verify the built codex: for every daf leaf, assert the interlock geometry.

Checks per leaf:
  - exactly one leaf visible at a time
  - no commentary line overlaps the central Text
  - both commentary flows wrap beneath the Text (warn if either doesn't;
    fail only on overlap)
Run:  python3 verify.py  [dist/tractate-aliyah.html]
"""
import sys
import pathlib
from playwright.sync_api import sync_playwright

TARGET = sys.argv[1] if len(sys.argv) > 1 else 'dist/tractate-aliyah.html'

GEO = """
() => {
  const leaf = document.querySelector('.leaf.active');
  const center = leaf.querySelector('.center-text');
  if (!center) return {folio: leaf.getAttribute('data-folio'), daf: false};
  const c = center.getBoundingClientRect();
  function lines(sel){
    const el = leaf.querySelector(sel);
    const r = document.createRange(); r.selectNodeContents(el);
    return Array.from(r.getClientRects()).filter(x=>x.width>30&&x.height>5&&x.height<30);
  }
  function stats(ls, side){
    const under = ls.filter(l=>l.top>=c.bottom && (side==='L' ? l.right>c.left+20 : l.left<c.right-20)).length;
    const overlap = ls.some(l=> l.top<c.bottom&&l.bottom>c.top && (side==='L' ? l.right>c.left+1 : l.left<c.right-1));
    return {under, overlap};
  }
  return {folio: leaf.getAttribute('data-folio'), daf: true,
          visible: document.querySelectorAll('.leaf.active').length,
          inner: stats(lines('.inner-flow'),'L'),
          outer: stats(lines('.outer-flow'),'R')};
}
"""


def main():
    path = pathlib.Path(TARGET).resolve()
    failures, warnings = [], []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        errs = []
        page.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
        page.goto('file://' + str(path))
        page.wait_for_timeout(1200)
        n = page.evaluate("() => document.querySelectorAll('.tabs button').length")
        for i in range(n):
            page.evaluate(f"() => document.querySelectorAll('.tabs button')[{i}].click()")
            page.wait_for_timeout(750)
            r = page.evaluate(GEO)
            if r.get('visible', 1) != 1:
                failures.append(f"{r['folio']}: {r['visible']} leaves visible")
            if not r['daf']:
                print(f"  {r['folio']:8s} non-daf leaf, geometry skipped")
                continue
            line = (f"  {r['folio']:8s} inner under {r['inner']['under']:3d} "
                    f"overlap {r['inner']['overlap']} | outer under {r['outer']['under']:3d} "
                    f"overlap {r['outer']['overlap']}")
            print(line)
            for side in ('inner', 'outer'):
                if r[side]['overlap']:
                    failures.append(f"{r['folio']}: {side} flow overlaps the Text")
                if r[side]['under'] == 0:
                    warnings.append(f"{r['folio']}: {side} flow does not wrap beneath the Text "
                                    f"(lengthen it; see SPEC.md length budgets)")
        browser.close()
    if errs:
        failures.append(f"console errors: {errs}")
    for w in warnings:
        print('WARN', w)
    for f in failures:
        print('FAIL', f)
    print('verify:', 'FAILED' if failures else ('PASSED with warnings' if warnings else 'PASSED'))
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
