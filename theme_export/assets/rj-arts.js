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

/* ==========================================================================
   COLLECTION PAGE  (sections/rj-collection.liquid)
   Filter drawer open/close, filter-group accordion, sort-by navigation.
   Filtering itself is plain <a href> links (Shopify's own filter URLs), so it
   keeps working with JavaScript disabled and with Search & Discovery filters.
   ========================================================================== */
(function () {
  function initCollection(root) {
    var scope = root || document;
    var drawer = scope.querySelector('[data-rj-filter-drawer]');
    var overlay = scope.querySelector('[data-rj-filter-overlay]');
    if (!drawer) return;

    var lastFocus = null;

    function open() {
      lastFocus = document.activeElement;
      drawer.hidden = false;
      if (overlay) overlay.hidden = false;
      // next frame so the transition runs from translateX(-100%)
      requestAnimationFrame(function () {
        drawer.classList.add('is-open');
        if (overlay) overlay.classList.add('is-open');
      });
      document.body.classList.add('rj-drawer-open');
      var close = drawer.querySelector('[data-rj-close-filter]');
      if (close) close.focus();
    }

    function close() {
      drawer.classList.remove('is-open');
      if (overlay) overlay.classList.remove('is-open');
      document.body.classList.remove('rj-drawer-open');
      window.setTimeout(function () {
        drawer.hidden = true;
        if (overlay) overlay.hidden = true;
      }, 520);
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }

    scope.querySelectorAll('[data-rj-open-filter]').forEach(function (button) {
      button.addEventListener('click', open);
    });
    drawer.querySelectorAll('[data-rj-close-filter]').forEach(function (button) {
      button.addEventListener('click', close);
    });
    if (overlay) overlay.addEventListener('click', close);

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && drawer.classList.contains('is-open')) close();
    });

    /* accordion */
    drawer.querySelectorAll('[data-rj-fgroup]').forEach(function (group) {
      var head = group.querySelector('.rj-fgroup__h');
      if (!head) return;
      head.addEventListener('click', function () {
        var isOpen = group.classList.toggle('is-open');
        head.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
    });
  }

  function initSort(root) {
    var select = (root || document).querySelector('[data-rj-sort]');
    if (!select) return;
    select.addEventListener('change', function () {
      var url = new URL(window.location.href);
      url.searchParams.set('sort_by', select.value);
      url.searchParams.delete('page');
      window.location.href = url.toString();
    });
  }

  function boot(root) {
    initCollection(root);
    initSort(root);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      boot(document);
    });
  } else {
    boot(document);
  }

  document.addEventListener('shopify:section:load', function (event) {
    boot(event.target);
  });
})();

/* ==========================================================================
   PRODUCT PAGE  (sections/rj-product.liquid)
   Gallery thumbs, variant buttons -> price/SKU/stock/image/URL updates,
   quantity stepper, accordion, sticky add bar. Add-to-cart itself is Dawn's
   product-form element (AJAX + cart drawer), we only drive the hidden variant
   id and the quantity input it reads.
   ========================================================================== */
(function () {
  function initProduct(root) {
    var scope = root || document;
    var wrap = scope.querySelector('[data-rj-product]');
    if (!wrap) return;

    var dataEl = document.querySelector('[data-rj-variants]');
    var variants = [];
    if (dataEl) {
      try {
        variants = JSON.parse(dataEl.textContent);
      } catch (error) {
        variants = [];
      }
    }

    var form = wrap.querySelector('[data-type="add-to-cart-form"]');
    var idInput = wrap.querySelector('.product-variant-id');
    var priceEl = wrap.querySelector('[data-rj-price]');
    var wasEl = wrap.querySelector('[data-rj-was]');
    var skuEl = wrap.querySelector('[data-rj-sku]');
    var stockEl = wrap.querySelector('[data-rj-stock]');
    var stockText = wrap.querySelector('[data-rj-stock-text]');
    var badgeEl = wrap.querySelector('[data-rj-badge]');
    var addBtn = wrap.querySelector('[data-rj-add]');
    var addText = wrap.querySelector('[data-rj-add-text]');
    var stageImg = wrap.querySelector('[data-rj-stage]');
    var stickyPrice = wrap.querySelector('[data-rj-sticky-price]');
    var stickyWas = wrap.querySelector('[data-rj-sticky-was]');
    var stickyAdd = wrap.querySelector('[data-rj-sticky-add]');
    var labels = {
      inStock: wrap.dataset.labelInStock || (stockText ? stockText.textContent.trim() : 'In stock'),
      add: wrap.dataset.labelAdd || (addText ? addText.textContent.trim() : 'Add to cart'),
      soldOut: wrap.dataset.labelSoldOut || 'Sold out'
    };

    var selected = [];
    wrap.querySelectorAll('[data-option-position]').forEach(function (button) {
      var position = parseInt(button.dataset.optionPosition, 10) - 1;
      if (button.classList.contains('is-active')) selected[position] = button.dataset.rjOptValue;
      button.addEventListener('click', function () {
        selected[position] = button.dataset.rjOptValue;
        wrap.querySelectorAll('[data-option-position="' + (position + 1) + '"]').forEach(function (sibling) {
          var active = sibling === button;
          sibling.classList.toggle('is-active', active);
          sibling.setAttribute('aria-pressed', active ? 'true' : 'false');
        });
        var nameEl = wrap.querySelector('[data-rj-opt-name="' + (position + 1) + '"]');
        if (nameEl) nameEl.textContent = button.dataset.rjOptValue;
        syncVariant();
      });
    });

    function findVariant() {
      for (var i = 0; i < variants.length; i += 1) {
        var options = variants[i].options;
        var match = true;
        for (var j = 0; j < options.length; j += 1) {
          if (selected[j] !== undefined && selected[j] !== options[j]) {
            match = false;
            break;
          }
        }
        if (match) return variants[i];
      }
      return null;
    }

    function syncVariant() {
      var variant = findVariant();
      if (!variant) return;

      if (idInput) {
        idInput.value = variant.id;
        idInput.disabled = !variant.available;
      }
      if (priceEl) priceEl.textContent = variant.price;
      if (wasEl) {
        if (variant.compare) {
          wasEl.textContent = variant.compare;
          wasEl.hidden = false;
        } else {
          wasEl.textContent = '';
          wasEl.hidden = true;
        }
      }
      if (badgeEl) {
        if (variant.discount) {
          badgeEl.textContent = badgeEl.dataset.prefix + variant.discount + '%';
          badgeEl.hidden = false;
        } else {
          badgeEl.hidden = true;
        }
      }
      if (skuEl) skuEl.textContent = variant.sku || '—';
      if (stockEl) stockEl.classList.toggle('is-out', !variant.available);
      if (stockText) stockText.textContent = variant.available ? labels.inStock : labels.soldOut;
      if (addBtn) {
        addBtn.disabled = !variant.available;
        if (addText) addText.textContent = variant.available ? labels.add : labels.soldOut;
      }
      if (stickyAdd) stickyAdd.disabled = !variant.available;
      if (stickyPrice) stickyPrice.textContent = variant.price;
      if (stickyWas) {
        if (variant.compare) {
          stickyWas.textContent = variant.compare;
          stickyWas.hidden = false;
        } else {
          stickyWas.hidden = true;
        }
      }
      if (variant.image && stageImg) {
        stageImg.src = variant.image;
        if (stageImg.srcset) stageImg.srcset = '';
        wrap.querySelectorAll('[data-rj-thumb]').forEach(function (thumb) {
          thumb.classList.toggle('is-active', thumb.dataset.mediaId === String(variant.media_id));
        });
      }

      var url = new URL(window.location.href);
      url.searchParams.set('variant', variant.id);
      window.history.replaceState({}, '', url.toString());
    }

    /* badge prefix, so JS keeps the merchant's wording */
    if (badgeEl) {
      var prefix = (badgeEl.textContent || '').replace(/[0-9]+%?$/, '');
      badgeEl.dataset.prefix = prefix;
    }

    /* gallery */
    wrap.querySelectorAll('[data-rj-thumb]').forEach(function (thumb) {
      thumb.addEventListener('click', function () {
        if (!stageImg || !thumb.dataset.full) return;
        stageImg.src = thumb.dataset.full;
        if (stageImg.srcset) stageImg.srcset = '';
        wrap.querySelectorAll('[data-rj-thumb]').forEach(function (other) {
          other.classList.toggle('is-active', other === thumb);
        });
      });
    });

    /* quantity */
    var qtyInput = wrap.querySelector('[data-rj-qty-input]');
    wrap.querySelectorAll('[data-rj-qty]').forEach(function (button) {
      button.addEventListener('click', function () {
        if (!qtyInput) return;
        var step = parseInt(button.dataset.rjQty, 10) || 1;
        var value = parseInt(qtyInput.value, 10) || 1;
        value = Math.max(1, value + step);
        qtyInput.value = value;
      });
    });

    /* accordion */
    wrap.querySelectorAll('[data-rj-acc] .rj-acc__head').forEach(function (head) {
      head.addEventListener('click', function () {
        var item = head.closest('[data-rj-acc]');
        var isOpen = item.classList.toggle('is-open');
        head.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
    });

    /* sticky add bar */
    var sticky = wrap.querySelector('[data-rj-sticky]');
    if (sticky && addBtn) {
      var toggleSticky = function () {
        var past = addBtn.getBoundingClientRect().bottom < 0;
        sticky.hidden = !past;
        sticky.classList.toggle('is-shown', past);
      };
      window.addEventListener('scroll', toggleSticky, { passive: true });
      toggleSticky();
    }

    if (stickyAdd && form) {
      stickyAdd.addEventListener('click', function () {
        var submit = form.querySelector('[name="add"]');
        if (submit) submit.click();
      });
    }
  }

  function bootProduct(root) {
    initProduct(root);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      bootProduct(document);
    });
  } else {
    bootProduct(document);
  }

  document.addEventListener('shopify:section:load', function (event) {
    bootProduct(event.target);
  });
})();

/* ==========================================================================
   QUICK VIEW POPUP  (snippets/rj-quickview.liquid)
   The markup for every card lives in an inert <template>, so opening the popup
   is a DOM clone: no fetch, no app. Add-to-cart is Dawn's own product-form,
   which upgrades as soon as the cloned nodes are inserted.
   ========================================================================== */
(function () {
  var lastTrigger = null;
  var bound = false;

  function findModal(trigger) {
    var section = trigger.closest('.shopify-section');
    if (section) {
      var local = section.querySelector('[data-rj-qv]');
      if (local) return local;
    }
    return document.querySelector('[data-rj-qv]');
  }

  function setBusy(modal, busy) {
    var dialog = modal.querySelector('.rj-qv__dialog');
    if (dialog) dialog.setAttribute('aria-busy', busy ? 'true' : 'false');
  }

  function wireContent(modal) {
    var content = modal.querySelector('[data-rj-qv-content]');
    if (!content) return;

    var stage = content.querySelector('[data-rj-qv-stage]');
    var priceEl = content.querySelector('[data-rj-qv-price]');
    var wasEl = content.querySelector('[data-rj-qv-was]');
    var select = content.querySelector('[data-rj-qv-variant]');
    var idInput = content.querySelector('.product-variant-id');
    var submit = content.querySelector('[name="add"]');
    var submitText = content.querySelector('[data-rj-qv-add-text]');
    var addLabel = submitText ? submitText.textContent.trim() : 'Add to cart';

    /* thumbnails */
    content.querySelectorAll('[data-rj-qv-thumb]').forEach(function (thumb) {
      thumb.addEventListener('click', function () {
        if (!stage || !thumb.dataset.full) return;
        stage.src = thumb.dataset.full;
        if (stage.srcset) stage.srcset = '';
        content.querySelectorAll('[data-rj-qv-thumb]').forEach(function (other) {
          other.classList.toggle('is-active', other === thumb);
        });
      });
    });

    /* variant dropdown */
    if (select) {
      select.addEventListener('change', function () {
        var option = select.options[select.selectedIndex];
        if (!option) return;
        if (idInput) {
          idInput.value = option.value;
          idInput.disabled = option.dataset.available === 'false';
        }
        if (priceEl && option.dataset.price) priceEl.textContent = option.dataset.price;
        if (wasEl) {
          var compare = option.dataset.compare || '';
          wasEl.textContent = compare;
          wasEl.hidden = !compare;
        }
        if (stage && option.dataset.image) {
          stage.src = option.dataset.image;
          if (stage.srcset) stage.srcset = '';
        }
        if (submit) {
          var available = option.dataset.available !== 'false';
          submit.disabled = !available;
          if (submitText) submitText.textContent = available ? addLabel : 'Sold out';
        }
      });
    }

    /* quantity */
    var qtyInput = content.querySelector('[data-rj-qty-input]');
    content.querySelectorAll('[data-rj-qty]').forEach(function (button) {
      button.addEventListener('click', function () {
        if (!qtyInput) return;
        var step = parseInt(button.dataset.rjQty, 10) || 1;
        var value = parseInt(qtyInput.value, 10) || 1;
        qtyInput.value = Math.max(1, value + step);
      });
    });

    /* close the popup once the add-to-cart request settled */
    var formEl = content.querySelector('form');
    if (formEl) {
      formEl.addEventListener('submit', function () {
        window.setTimeout(function () {
          var error = modal.querySelector('.product-form__error-message-wrapper');
          if (error && !error.hasAttribute('hidden')) return;
          close(modal);
        }, 900);
      });
    }
  }

  function focusables(modal) {
    return Array.prototype.slice
      .call(
        modal.querySelectorAll(
          'a[href], button:not([disabled]), select, input, [tabindex]:not([tabindex="-1"])'
        )
      )
      .filter(function (el) {
        return el.offsetParent !== null;
      });
  }

  function open(modal, trigger) {
    var content = modal.querySelector('[data-rj-qv-content]');
    var template = document.querySelector('template[data-rj-qv-template="' + trigger.dataset.rjQvOpen + '"]');
    if (!content || !template) return;

    lastTrigger = trigger;
    content.innerHTML = '';
    content.appendChild(template.content.cloneNode(true));
    wireContent(modal);

    modal.hidden = false;
    document.body.classList.add('rj-qv-lock');
    window.requestAnimationFrame(function () {
      modal.classList.add('is-open');
      var closeButton = modal.querySelector('.rj-qv__x');
      if (closeButton) closeButton.focus();
    });
  }

  function close(modal) {
    if (!modal) return;
    modal.classList.remove('is-open');
    document.body.classList.remove('rj-qv-lock');
    window.setTimeout(function () {
      modal.hidden = true;
      var content = modal.querySelector('[data-rj-qv-content]');
      if (content) content.innerHTML = '';
    }, 350);
    if (lastTrigger && lastTrigger.focus) lastTrigger.focus();
  }

  function boot() {
    if (bound) return;
    bound = true;

    document.addEventListener('click', function (event) {
      var trigger = event.target.closest('[data-rj-qv-open]');
      if (trigger) {
        event.preventDefault();
        var modal = findModal(trigger);
        if (modal) open(modal, trigger);
        return;
      }

      var closer = event.target.closest('[data-rj-qv-close]');
      if (closer) {
        event.preventDefault();
        close(closer.closest('[data-rj-qv]'));
      }
    });

    document.addEventListener('keydown', function (event) {
      var modal = document.querySelector('[data-rj-qv].is-open');
      if (!modal) return;

      if (event.key === 'Escape') {
        close(modal);
        return;
      }

      /* keep Tab inside the dialog */
      if (event.key !== 'Tab') return;
      var items = focusables(modal);
      if (items.length === 0) return;
      var first = items[0];
      var last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();

/* ==========================================================================
   RJ ARTS — gallery lightbox (sections/rj-page-about.liquid)
   Contract:
     trigger  a[data-rj-lightbox][href="<full image url>"]
     shell    [data-rj-lightbox-modal] + [data-rj-lightbox-img] + [data-rj-lightbox-close]
   Closes on Esc, overlay click, close button. Locks body scroll while open.
   ========================================================================== */
(function () {
  if (window.rjLightboxInit) return;
  window.rjLightboxInit = true;

  var modal = null;
  var img = null;
  var lastFocus = null;

  function shell() {
    if (modal) return modal;
    modal = document.querySelector('[data-rj-lightbox-modal]');
    if (modal) img = modal.querySelector('[data-rj-lightbox-img]');
    return modal;
  }

  function open(trigger) {
    if (!shell()) return;
    var full = trigger.getAttribute('href') || '';
    if (!full) return;

    lastFocus = trigger;
    img.setAttribute('src', full);
    img.setAttribute('alt', trigger.getAttribute('data-rj-lightbox-alt') || trigger.getAttribute('aria-label') || '');

    modal.hidden = false;
    /* next frame so the opacity transition runs */
    requestAnimationFrame(function () {
      modal.classList.add('is-open');
    });
    document.body.classList.add('rj-lb-lock');

    var closeBtn = modal.querySelector('[data-rj-lightbox-close]');
    if (closeBtn) closeBtn.focus();
  }

  function close() {
    if (!shell()) return;
    modal.classList.remove('is-open');
    document.body.classList.remove('rj-lb-lock');
    window.setTimeout(function () {
      modal.hidden = true;
      img.setAttribute('src', '');
    }, 300);
    if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus();
    lastFocus = null;
  }

  function onDocClick(event) {
    var trigger = event.target.closest('[data-rj-lightbox]');
    if (trigger) {
      event.preventDefault();
      open(trigger);
      return;
    }

    if (event.target.closest('[data-rj-lightbox-close]')) {
      event.preventDefault();
      close();
      return;
    }

    /* clicking the dark overlay (not the image itself) closes */
    var overlay = event.target.closest('[data-rj-lightbox-modal]');
    if (overlay && event.target === overlay) close();
  }

  function onKeydown(event) {
    if (event.key !== 'Escape') return;
    if (!modal || modal.hidden) return;
    close();
  }

  document.addEventListener('click', onDocClick);
  document.addEventListener('keydown', onKeydown);
})();
