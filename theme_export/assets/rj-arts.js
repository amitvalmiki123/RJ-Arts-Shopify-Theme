/* ==========================================================================
   RJ ARTS — appended helpers (scroll reveal + header scrolled state)
   Written for design/THE-RJ-ARTS.html. Re-append this block if Dawn replaces
   global.js. Loaded by Dawn's own <script src="global.js" defer>.
   ========================================================================== */
/* RJ ARTS — shared behaviours: scroll reveal, header scrolled state */
(function () {
  if (window.rjArtsInit) return;
  window.rjArtsInit = true;

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function initReveal(root) {
    const targets = (root || document).querySelectorAll('.rj-reveal:not(.is-in)');
    if (!targets.length) return;

    if (prefersReduced || !('IntersectionObserver' in window)) {
      targets.forEach((el) => el.classList.add('is-in'));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-in');
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.12 }
    );

    targets.forEach((el) => observer.observe(el));
  }

  // Dawn's default header keeps its own sticky behaviour; we only add the
  // design's scrolled state (hairline + more opaque cream) at > 30px.
  function initHeader(root) {
    const headers = (root || document).querySelectorAll('.section-header .header-wrapper');
    if (!headers.length) return;
    const onScroll = () => {
      headers.forEach((header) => header.classList.toggle('rj-scrolled', window.scrollY > 30));
    };
    onScroll();
    if (!window.rjHeaderScrollBound) {
      window.rjHeaderScrollBound = true;
      window.addEventListener('scroll', onScroll, { passive: true });
    }
  }

  function boot(root) {
    initReveal(root);
    initHeader(root);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => boot(document));
  } else {
    boot(document);
  }

  // theme editor: re-run when a section is reloaded
  document.addEventListener('shopify:section:load', (event) => boot(event.target));
})();

/* ==========================================================================
   RJ ARTS - mega menu opens on hover (design behaviour)
   Desktop pointers only. The parent title is a real link now, so a click
   navigates to the menu item's URL while the panel opens on hover.
   ========================================================================== */
(function () {
  if (window.rjMegaHover) return;
  window.rjMegaHover = true;

  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

  var CLOSE_DELAY = 120;

  function closeOthers(current) {
    var open = document.querySelectorAll('details.mega-menu[open]');
    Array.prototype.forEach.call(open, function (other) {
      if (other !== current) other.removeAttribute('open');
    });
  }

  function init() {
    var menus = document.querySelectorAll('details.mega-menu');
    Array.prototype.forEach.call(menus, function (details) {
      var timer = null;

      details.addEventListener('mouseenter', function () {
        window.clearTimeout(timer);
        closeOthers(details);
        details.setAttribute('open', '');
      });

      details.addEventListener('mouseleave', function () {
        window.clearTimeout(timer);
        timer = window.setTimeout(function () {
          if (details.contains(document.activeElement)) return;
          details.removeAttribute('open');
        }, CLOSE_DELAY);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
