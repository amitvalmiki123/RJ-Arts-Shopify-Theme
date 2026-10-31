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

/* ==========================================================================
   RJ ARTS - <rj-showroom>: pill tabs + snap-rail arrows
   (design "TABBED PRODUCT SLIDER"). Self-contained custom element, so a
   section reload in the theme editor just re-runs connectedCallback.
   ========================================================================== */
(function () {
  if (window.rjShowroomDefined || customElements.get('rj-showroom')) return;
  window.rjShowroomDefined = true;

  customElements.define('rj-showroom', class RjShowroom extends HTMLElement {
    connectedCallback() {
      if (this.dataset.rjReady) return;
      this.dataset.rjReady = '1';

      this.tabs = Array.prototype.slice.call(this.querySelectorAll('[data-rj-tab]'));
      this.panels = Array.prototype.slice.call(this.querySelectorAll('[data-rj-panel]'));
      this.rail = this.panels.length ? this.panels[0].querySelector('[data-rj-rail]') : null;

      this.tabs.forEach((tab) => {
        tab.addEventListener('click', () => this.select(tab));
        tab.addEventListener('keydown', (event) => this.onKey(event, tab));
      });

      this.querySelectorAll('[data-rj-rail-dir]').forEach((button) => {
        button.addEventListener('click', () => this.scrollRail(parseInt(button.dataset.rjRailDir, 10)));
      });

      this.setIntervalOnce = null;
    }

    get activeIndex() {
      return this.tabs.findIndex((tab) => tab.classList.contains('is-active'));
    }

    select(tab) {
      const index = parseInt(tab.dataset.rjTab, 10);
      this.tabs.forEach((item, i) => {
        const on = i === index;
        item.classList.toggle('is-active', on);
        item.setAttribute('aria-selected', on ? 'true' : 'false');
        item.setAttribute('tabindex', on ? '0' : '-1');
      });
      this.panels.forEach((panel, i) => {
        const on = i === index;
        panel.classList.toggle('is-active', on);
        if (on) panel.removeAttribute('hidden');
        else panel.setAttribute('hidden', '');
      });
      this.rail = this.panels[index] ? this.panels[index].querySelector('[data-rj-rail]') : null;
      if (this.rail) this.rail.scrollLeft = 0;
    }

    onKey(event, tab) {
      const keys = { ArrowLeft: -1, ArrowRight: 1 };
      if (!(event.key in keys) || !this.tabs.length) return;
      event.preventDefault();
      const next = (this.activeIndex + keys[event.key] + this.tabs.length) % this.tabs.length;
      this.select(this.tabs[next]);
      this.tabs[next].focus();
    }

    scrollRail(dir) {
      if (!this.rail) return;
      const card = this.rail.querySelector('.rj-pcard');
      const step = card ? card.getBoundingClientRect().width + 22 : this.rail.clientWidth * 0.8;
      this.rail.scrollBy({ left: step * dir, behavior: 'smooth' });
    }
  });
})();

/* ==========================================================================
   RJ ARTS - <rj-carousel>: round arrow pair scrolling a snap rail
   (collection carousel). Independent of <rj-showroom>.
   ========================================================================== */
(function () {
  if (customElements.get('rj-carousel')) return;

  customElements.define('rj-carousel', class RjCarousel extends HTMLElement {
    connectedCallback() {
      if (this.dataset.rjReady) return;
      this.dataset.rjReady = '1';

      this.rail = this.querySelector('[data-rj-rail]');
      if (!this.rail) return;

      this.querySelectorAll('[data-rj-rail-dir]').forEach((button) => {
        button.addEventListener('click', () => this.scrollRail(parseInt(button.dataset.rjRailDir, 10)));
      });
    }

    scrollRail(dir) {
      const card = this.rail.querySelector('.rj-pcard, .rj-rcard');
      const gap = parseFloat(getComputedStyle(this.rail).columnGap) || 22;
      const step = card ? card.getBoundingClientRect().width + gap : this.rail.clientWidth * 0.8;
      this.rail.scrollBy({ left: step * dir, behavior: 'smooth' });
    }
  });
})();
