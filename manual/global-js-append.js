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
