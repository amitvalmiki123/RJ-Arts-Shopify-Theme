RJ ARTS - changed files only (22 files)
=======================================

>>> IS ROUND ME SIRF YE 4 FILES (Collection page):
      assets/rj-arts.css                  (4140 lines - Collection page CSS)
      assets/rj-arts.js                   (303 lines - drawer + sort JS)
      sections/rj-collection.liquid       (466 lines - NAYI FILE)
      templates/collection.json           (28 lines - collection template)

      config/settings_data.json           (382 lines - Colours panel, AB TAK PENDING)

    Collection page par Dawn ke main-collection-banner +
    main-collection-product-grid hat jayenge (jaan-boojh kar - design ek hi
    section maangta hai). Filters Search & Discovery app se aate hain;
    filters add na karein to Filter button chhup jata hai, page normal chalta hai.

    announcement-bar.liquid paste karne ki zaroorat NAHI - aapki already set
    hai. Design me ticker sticky nahi hai, header sticky hai, isliye scroll
    down par bar upar chala jata hai (yehi intended behaviour hai).

    App install (Judge.me / Wishlist Hero) abhi pending hai - code fallback
    par chalta hai: reviews = 4 blocks, wishlist heart = /pages/wishlist.

⚠️  YE ZIP THEME UPLOAD KARNE KE LIYE NAHI HAI.
    Sirf copy-paste ke liye hai. Upload ke liye "rj-arts-theme.zip" use karein.

Paste karne ka tarika (har file):
  Ctrl+Home -> Ctrl+A -> Ctrl+V -> Ctrl+S
  (beech me Delete/Backspace kabhi na dabayein, warna
   "config/settings_data.json could not be deleted" popup aata hai)

---- REPLACE (11 files) ----
  config/settings_schema.json          1551 lines
  config/settings_data.json             382 lines  <- colours/fonts/cart yahin se
  layout/theme.liquid                   641 lines
  sections/announcement-bar.liquid       180 lines
  sections/header.liquid                 820 lines
  snippets/header-mega-menu.liquid       134 lines
  sections/header-group.json             150 lines
  sections/footer-group.json              63 lines
  sections/footer.liquid                447 lines   <- REPLACE (Dawn ki file)
  templates/index.json                   416 lines
  templates/collection.json               28 lines  <- NAYA (is round)

---- NAYI FILE - sections me New file banakar paste karein ----
  sections/rj-hero.liquid                411 lines
  sections/rj-usp.liquid                 145 lines
  sections/rj-showroom.liquid            357 lines   <- NAYA (Showroom edit)
  sections/rj-categories.liquid          201 lines   <- NAYA (Category tiles)
  sections/rj-band.liquid                188 lines   <- NAYA (Feature band)
  sections/rj-about.liquid               220 lines   <- NAYA (About story)
  sections/rj-best.liquid                239 lines   <- NAYA (Best sellers)
  sections/rj-collections.liquid         212 lines   <- NAYA (Collection carousel)
  sections/rj-reviews.liquid             272 lines   <- Reviews (Judge.me source)
  sections/rj-collection.liquid          466 lines   <- NAYA (Collection page)
  assets/rj-arts.css                    4140 lines   <- poora replace
  assets/rj-arts.js                      303 lines

---- manual/ - OPTIONAL (sirf patch karna ho to) ----
  manual/snippet-1-color-scheme-fallback.liquid   102 lines
  manual/snippet-2-rj-tokens.liquid                14 lines
  manual/snippet-3-settings-schema-rj-group.json   81 lines

Dawn ke baaki 335 files bilkul stock rahenge - base.css / global.js ko haath
nahi lagana.

Collection page ke liye admin me (code nahi, data):
  1) Collections banayein (Bedroom / Living Room / Dining / New Arrivals / Best Sellers)
  2) Har collection me wide image (2000px+) - hero me 16% opacity par dikhti hai
  3) Collection description - hero ka paragraph
  4) Apps -> Search & Discovery -> Filters: Availability, Price, Product type,
     Vendor, Size, Finish (Finish ko Swatch presentation dein)
  5) Sort options default list hi use hoti hai, kuch nahi karna

⚠️  AGAR THEME ME config/settings_data.json HI NAHI DIKH RAHA
    (editor banner "The configuration file config/settings_data.json needs to
    be added..." + Colours panel me "No color schemes defined"):
    MANUAL-STEPS.md -> section 5.1 dekhein. Short version:
      1) Edit code -> config -> file ho to Step 2 ka content paste karein
      2) file na ho to config me New file -> naam `settings_data.json` -> paste
      3) New file option na mile to Customize me koi chhota change -> Save
         (Shopify file khud bana dega), phir content paste karein
      4) Phir bhi na ho to theme delete -> `rj-arts-theme.zip` dobara upload

Pura step-by-step guide + merchant data-entry checklist: MANUAL-STEPS.md
