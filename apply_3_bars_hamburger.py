import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

bars_dark_header = """<button onclick="toggleMobileMenu()" class="lg:hidden w-10 h-10 rounded-2xl bg-white/15 hover:bg-white/25 text-white border border-white/30 backdrop-blur-md flex flex-col items-center justify-center gap-1.5 transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer shadow-lg p-2" aria-label="Menu principal">
        <span class="w-5 h-[2.5px] bg-white rounded-full block"></span>
        <span class="w-5 h-[2.5px] bg-white rounded-full block"></span>
        <span class="w-5 h-[2.5px] bg-white rounded-full block"></span>
      </button>"""

bars_light_header = """<button onclick="toggleMobileMenu()" class="lg:hidden w-10 h-10 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-900 border border-slate-300 backdrop-blur-md flex flex-col items-center justify-center gap-1.5 transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer shadow-sm p-2" aria-label="Menu principal">
        <span class="w-5 h-[2.5px] bg-slate-900 rounded-full block"></span>
        <span class="w-5 h-[2.5px] bg-slate-900 rounded-full block"></span>
        <span class="w-5 h-[2.5px] bg-slate-900 rounded-full block"></span>
      </button>"""

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    is_tour = '/tours/' in fpath
    target_btn = bars_light_header if is_tour else bars_dark_header

    # Replace any previous hamburger button
    c = re.sub(
        r'<button\s+onclick=["\'](?:toggleMobileMenu\(\)|document\.getElementById\([\'"]mobile-menu[\'"]\)\.classList\.toggle\([\'"]hidden[\'"]\))["\'][^>]*>.*?</button>',
        target_btn,
        c,
        flags=re.DOTALL
    )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Applied crisp 3 horizontal bars hamburger button across {updated} files!")
