import glob, os, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Extract tour title and price for this page
    title_m = re.search(r'<h1[^>]*>([^<]+)</h1>', c)
    raw_title = title_m.group(1).strip() if title_m else "Séjour Népal Sauvage"
    # Clean title to keep it punchy (e.g. before "–" or "Expédition")
    short_title = raw_title.split('–')[0].split('-')[0].strip()

    price_m = re.search(r'À PARTIR DE[^\d]*([\d\s,]+€)', c, re.IGNORECASE) or \
              re.search(r'([\d\s,]+€)\s*<span[^>]*>/ person', c) or \
              re.search(r'([\d\s,]+€)\s*</span>\s*<span[^>]*>/', c)
    price = price_m.group(1).strip() if price_m else ""

    # 2. Change main header from sticky top-0 to relative
    c = c.replace(
        '<header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 py-2.5 shadow-sm">',
        '<header class="relative z-40 bg-white border-b border-slate-200 py-2.5 shadow-sm">'
    )

    # 3. Update right sidebar booking widget from top-[136px] to top-[76px]
    c = c.replace('sticky top-[136px]', 'sticky top-[76px]')

    # 4. Replace the old sticky subnav with the new Hybrid Conversion Bar (Option 1)
    new_subnav = f"""    <!-- STICKY SUB-NAV CONVERSION BAR (AIRBNB / WEROAD HYBRID) -->
    <nav class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/90 shadow-sm py-2.5 sm:py-3 transition-all -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8 mb-8 sm:mb-10" aria-label="Navigation du séjour">
      <div class="flex items-center justify-between gap-4">
        
        <!-- Left: Quick Tour Summary -->
        <div class="hidden sm:flex items-center gap-2.5 shrink-0 min-w-0">
          <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-emerald-50 text-[#0e8354] font-black text-xs shrink-0">🐾</span>
          <div class="min-w-0">
            <p class="font-extrabold text-xs text-slate-900 truncate max-w-[180px] md:max-w-[240px] lg:max-w-[300px]">{short_title}</p>
            {f'<p class="text-[11px] font-bold text-[#0e8354]">{price} <span class="text-slate-400 font-normal">/ pers.</span></p>' if price else ''}
          </div>
        </div>

        <!-- Center: Section Navigation Tabs -->
        <div class="flex items-center gap-4 sm:gap-6 lg:gap-8 overflow-x-auto no-scrollbar text-xs sm:text-sm font-bold text-slate-600 py-1">
          <a href="#apercu" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Aperçu</a>
          <a href="#pour-moi" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Profil</a>
          <a href="#programme" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Itinéraire</a>
          <a href="#inclusions" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Inclus</a>
          <a href="#avis-voyageurs" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Avis</a>
          <a href="#faq" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">FAQ</a>
        </div>

        <!-- Right: Instant Booking CTA Button -->
        <div class="flex items-center gap-2 shrink-0">
          <a href="#booking-widget" class="inline-flex items-center gap-1.5 px-4 sm:px-5 py-2 sm:py-2.5 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs shadow-md shadow-[#0e8354]/25 hover:scale-105 active:scale-95 transition-all whitespace-nowrap">
            <span>Réserver</span>
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-7-7 7 7-7 7"/></svg>
          </a>
        </div>

      </div>
    </nav>"""

    # Replace the existing sticky subnav block
    old_subnav_pattern = re.compile(
        r'[ \t]*(?:<!-- STICKY SUB-NAV.*?-->\s*)?<div class="sticky top-\[\d+px\].*?</div>\s*</div>',
        re.DOTALL
    )

    c_new = old_subnav_pattern.sub(new_subnav, c, count=1)

    if c_new != c:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c_new)
        print(f"✅ Option 1 applied to: {os.path.basename(fpath)}")
    else:
        print(f"⚠️ Pattern match failed for: {os.path.basename(fpath)}")

print("All tour pages upgraded to Option 1!")
