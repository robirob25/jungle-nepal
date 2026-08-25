import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/*.astro') + \
              glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/**/*.astro')

custom_dropdown_html = """        <!-- LANGUAGE SWITCHER (GLOBE) -->
      <div class="relative group/lang py-1">
        <button onclick="toggleLangMenu(this)" class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10 hover:bg-white/20 border-white/20 text-white border backdrop-blur-md flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Changer de langue / Change language">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </button>
        <div class="lang-dropdown-box absolute right-0 top-full mt-1.5 w-48 opacity-0 translate-y-2 pointer-events-none group-hover/lang:opacity-100 group-hover/lang:translate-y-0 group-hover/lang:pointer-events-auto transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-1.5 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-0.5 text-xs font-bold text-white">
            <button onclick="changeLanguage('fr')" data-lang-btn="fr" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>
            </button>
            <button onclick="changeLanguage('en')" data-lang-btn="en" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>
            </button>
            <button onclick="changeLanguage('de')" data-lang-btn="de" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇩🇪</span><span>Deutsch</span></span>
            </button>
            <button onclick="changeLanguage('es')" data-lang-btn="es" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇪🇸</span><span>Español</span></span>
            </button>
          </div>
        </div>
      </div>"""

# For light headers (e.g. tour detail pages with white bg header)
custom_dropdown_light_header = """        <!-- LANGUAGE SWITCHER (GLOBE) -->
      <div class="relative group/lang py-1">
        <button onclick="toggleLangMenu(this)" class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-slate-100 hover:bg-slate-200 border-slate-200 text-slate-700 border backdrop-blur-md flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Changer de langue / Change language">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-slate-700" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </button>
        <div class="lang-dropdown-box absolute right-0 top-full mt-1.5 w-48 opacity-0 translate-y-2 pointer-events-none group-hover/lang:opacity-100 group-hover/lang:translate-y-0 group-hover/lang:pointer-events-auto transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-1.5 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-0.5 text-xs font-bold text-white">
            <button onclick="changeLanguage('fr')" data-lang-btn="fr" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>
            </button>
            <button onclick="changeLanguage('en')" data-lang-btn="en" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>
            </button>
            <button onclick="changeLanguage('de')" data-lang-btn="de" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇩🇪</span><span>Deutsch</span></span>
            </button>
            <button onclick="changeLanguage('es')" data-lang-btn="es" class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇪🇸</span><span>Español</span></span>
            </button>
          </div>
        </div>
      </div>"""

updated_count = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    is_tour = '/tours/' in fpath
    target_dd = custom_dropdown_light_header if is_tour else custom_dropdown_html

    # Replace old language switcher block
    c = re.sub(
        r'<!-- LANGUAGE SWITCHER \(GLOBE\).*?</div>\s*</div>\s*</div>',
        target_dd,
        c,
        flags=re.DOTALL
    )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_count += 1

print(f"Updated in-place language switcher dropdown across {updated_count} pages!")
