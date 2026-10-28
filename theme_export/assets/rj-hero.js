/* RJ ARTS — hero slider (design .hero behaviour) */
(function () {
  if (customElements.get('rj-hero')) return;

  class RjHero extends HTMLElement {
    connectedCallback() {
      this.slides = Array.from(this.querySelectorAll('.rj-hero__slide'));
      this.dots = Array.from(this.querySelectorAll('[data-rj-hero-dots] button'));
      this.counter = this.querySelector('[data-rj-hero-count]');
      this.autoplay = this.dataset.autoplay === 'true';
      this.speed = (parseFloat(this.dataset.speed) || 6) * 1000;
      this.index = 0;
      this.timer = null;
      this.reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      if (this.slides.length < 2) return;

      this.bind();
      if (this.autoplay && !this.reduced) this.start();
    }

    disconnectedCallback() {
      this.stop();
    }

    bind() {
      const arrows = this.querySelector('.rj-hero__arrows');
      if (arrows) {
        arrows.addEventListener('click', (event) => {
          const button = event.target.closest('button[data-dir]');
          if (!button) return;
          this.go(this.index + parseInt(button.dataset.dir, 10));
          this.restart();
        });
      }

      this.dots.forEach((dot) => {
        dot.addEventListener('click', () => {
          this.go(parseInt(dot.dataset.index, 10));
          this.restart();
        });
      });

      // swipe (mobile)
      let startX = 0;
      let startY = 0;
      let tracking = false;
      this.addEventListener(
        'touchstart',
        (event) => {
          const touch = event.touches[0];
          startX = touch.clientX;
          startY = touch.clientY;
          tracking = true;
        },
        { passive: true }
      );
      this.addEventListener(
        'touchend',
        (event) => {
          if (!tracking) return;
          tracking = false;
          const touch = event.changedTouches[0];
          const dx = touch.clientX - startX;
          const dy = touch.clientY - startY;
          if (Math.abs(dx) < 45 || Math.abs(dx) < Math.abs(dy)) return;
          this.go(this.index + (dx < 0 ? 1 : -1));
          this.restart();
        },
        { passive: true }
      );

      document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
          this.stop();
        } else if (this.autoplay && !this.reduced) {
          this.start();
        }
      });
    }

    go(next) {
      const total = this.slides.length;
      this.index = ((next % total) + total) % total;

      this.slides.forEach((slide, i) => {
        const active = i === this.index;
        slide.classList.toggle('is-active', active);
        if (active) {
          slide.removeAttribute('aria-hidden');
        } else {
          slide.setAttribute('aria-hidden', 'true');
        }
      });

      this.dots.forEach((dot, i) => {
        const shouldBeActive = i === this.index;
        if (shouldBeActive && !dot.classList.contains('is-active')) {
          // restart the progress-bar animation from zero
          dot.classList.remove('is-active');
          void dot.offsetWidth;
        }
        dot.classList.toggle('is-active', shouldBeActive);
      });

      if (this.counter) {
        this.counter.textContent = String(this.index + 1).padStart(2, '0');
      }
    }

    start() {
      this.stop();
      this.timer = setInterval(() => this.go(this.index + 1), this.speed);
    }

    stop() {
      if (this.timer) {
        clearInterval(this.timer);
        this.timer = null;
      }
    }

    restart() {
      if (this.autoplay && !this.reduced) this.start();
    }
  }

  customElements.define('rj-hero', RjHero);
})();
