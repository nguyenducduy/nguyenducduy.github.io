// Motion: reveal on scroll, cover parallax, reading progress. No dependencies.
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Reveal figures and post entries as they scroll into view
  var items = document.querySelectorAll('.prose figure, .entry');
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  var bar = document.querySelector('.read-progress span');
  var article = document.querySelector('[itemprop="articleBody"]');
  var cover = reduce ? null : document.querySelector('[data-parallax]');
  if (!bar && !cover) return;

  var ticking = false;

  function update() {
    ticking = false;
    var vh = window.innerHeight;

    if (bar && article) {
      var a = article.getBoundingClientRect();
      // 0 when the article enters the viewport, 1 when its end reaches the bottom
      var p = (vh - a.top) / (a.height);
      bar.style.transform = 'scaleX(' + Math.min(1, Math.max(0, p)).toFixed(4) + ')';
    }

    if (cover) {
      var f = cover.parentElement.getBoundingClientRect();
      if (f.bottom > 0 && f.top < vh) {
        // -1 (frame below centre) .. 1 (frame above centre)
        var t = ((vh / 2) - (f.top + f.height / 2)) / (vh / 2 + f.height / 2);
        var shift = f.height * 0.055; // stays inside the 1.12 scale overscan
        cover.style.setProperty('--parallax', (t * shift).toFixed(1) + 'px');
      }
    }
  }

  function onScroll() {
    if (!ticking) {
      ticking = true;
      window.requestAnimationFrame(update);
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  update();
})();
