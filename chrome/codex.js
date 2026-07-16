/* CodexNav - binds the leaves into a turnable volume. Requires DafEngine.
   No tab bar: pages are turned with the side arrows, arrow keys, swipe, or
   a #folio hash (the shaar ToC links navigate this way). */
(function () {
  var leaves = Array.prototype.slice.call(document.querySelectorAll('.leaf'));
  var prevBtn = document.querySelector('.turn.prev');
  var nextBtn = document.querySelector('.turn.next');
  var names = leaves.map(function (l) { return l.getAttribute('data-folio'); });
  var titles = leaves.map(function (l) { return l.getAttribute('data-name'); });
  var current = -1;

  function settleActive() {
    if (current < 0) return;
    window.DafEngine.layoutLeaf(leaves[current]);
    requestAnimationFrame(function () { window.DafEngine.layoutLeaf(leaves[current]); });
  }

  function show(i, dir) {
    if (i < 0 || i >= leaves.length || i === current) return;
    if (current >= 0) leaves[current].className = 'leaf';
    current = i;
    leaves[i].className = 'leaf active' + (dir ? ' ' + dir : '');
    prevBtn.disabled = (i === 0);
    nextBtn.disabled = (i === leaves.length - 1);
    document.title = 'Tractate Aliyah \u00b7 ' +
      (names[i] === 'shaar' ? 'Shaar' : 'Folio ' + names[i]) + ' \u2014 ' + titles[i];
    if (history.replaceState) {
      try { history.replaceState(null, '', '#' + names[i]); } catch (e) {}
    }
    window.scrollTo(0, 0);
    settleActive();
  }

  window.addEventListener('hashchange', function () {
    var i = names.indexOf(location.hash.slice(1));
    if (i >= 0 && i !== current) show(i, i > current ? 'fwd' : 'bwd');
  });

  prevBtn.addEventListener('click', function () { show(current - 1, 'bwd'); });
  nextBtn.addEventListener('click', function () { show(current + 1, 'fwd'); });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight') show(current + 1, 'fwd');
    if (e.key === 'ArrowLeft')  show(current - 1, 'bwd');
  });

  var touchX = null;
  document.addEventListener('touchstart', function (e) {
    touchX = e.touches[0].clientX;
  }, { passive: true });
  document.addEventListener('touchend', function (e) {
    if (touchX === null) return;
    var dx = e.changedTouches[0].clientX - touchX;
    touchX = null;
    if (Math.abs(dx) > 70) {
      if (dx < 0) show(current + 1, 'fwd'); else show(current - 1, 'bwd');
    }
  }, { passive: true });

  window.addEventListener('resize', settleActive);
  window.DafEngine.mq.addEventListener
    ? window.DafEngine.mq.addEventListener('change', settleActive)
    : window.DafEngine.mq.addListener(settleActive);
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(settleActive);
  }
  window.addEventListener('load', settleActive);

  var start = Math.max(0, names.indexOf(location.hash.slice(1)));
  show(start, null);
})();
