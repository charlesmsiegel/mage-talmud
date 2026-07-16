/* DafEngine - carves the silhouette of the title box and central Text out of
   each commentary flow, so commentaries run above, beside, and beneath the
   Text: the interlock of a printed daf. Class-scoped: works on any element
   containing one .well (with .titlebox, .center-text, .inner-flow,
   .outer-flow, and two .sp spacers per flow). */
window.DafEngine = (function () {
  var mq = window.matchMedia('(max-width: 860px)');

  function px(n) { return Math.ceil(n) + 'px'; }

  function layoutLeaf(leaf) {
    var well   = leaf.querySelector('.well');
    var title  = leaf.querySelector('.titlebox');
    var center = leaf.querySelector('.center-text');
    if (!well || !title || !center) return;   /* non-daf page types (shaar, luach) */

    var flows = [leaf.querySelector('.inner-flow'), leaf.querySelector('.outer-flow')];
    var sps = flows.map(function (f) {
      var s = f.querySelectorAll('.sp');
      return [s[0], s[1]];
    });

    if (mq.matches) {
      sps.forEach(function (pair) {
        pair.forEach(function (s) { s.style.width = s.style.height = '0'; });
      });
      center.style.top = '';
      well.style.minHeight = '';
      return;
    }

    var gap = parseFloat(getComputedStyle(document.documentElement)
                .getPropertyValue('font-size')) * 0.9;   /* --gap */
    var halfGap = gap / 2;

    var titleH = title.offsetHeight;
    var centerTop = titleH + gap;
    center.style.top = px(centerTop);
    var centerH = center.offsetHeight;

    var titleIntrude  = title.offsetWidth / 2 + halfGap;
    var centerIntrude = center.offsetWidth / 2 + halfGap;

    sps.forEach(function (pair) {
      pair[0].style.width  = px(titleIntrude);
      pair[0].style.height = px(titleH + gap * 0.75);
      pair[1].style.width  = px(centerIntrude);
      pair[1].style.height = px(centerTop + centerH + gap - (titleH + gap * 0.75));
    });

    var glossMax = 0;
    leaf.querySelectorAll('.gloss').forEach(function (g) {
      glossMax = Math.max(glossMax, g.offsetHeight);
    });
    well.style.minHeight = px(Math.max(centerTop + centerH + gap, glossMax));
  }

  return { layoutLeaf: layoutLeaf, mq: mq };
})();
