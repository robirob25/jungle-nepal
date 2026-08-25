import re, glob, os

files_to_update = ['/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro'] + glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in files_to_update:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # Pattern to match trip card footer
    pattern = r'<div class="mt-6 pt-5 border-t border-slate-200/70 flex items-end justify-between">\s*<div>\s*<p class="text-\[11px\] uppercase tracking-wider font-bold text-slate-400">À partir de</p>\s*<div class="flex items-baseline gap-2 mt-0\.5">\s*<span class="font-black text-2xl sm:text-3xl text-jungle-950 tracking-tight">([0-9\s,\.]+)€?</span>\s*</div>\s*<p class="text-\[11px\] text-\[#0e8354\] font-bold mt-0\.5 flex items-center gap-1">\s*<svg [^>]*>.*?</svg>\s*<span>Départs confirmés 2026/2027</span>\s*</p>\s*</div>\s*<a href="([^"]+)" class="[^"]*">\s*<span>Voir le séjour</span>\s*<i [^>]*></i>\s*</a>\s*</div>'

    def repl(m):
        price = m.group(1).strip()
        url = m.group(2).strip()
        return f"""<div class="mt-5 pt-4 border-t border-slate-200/80">
              <div class="flex items-center justify-between gap-2">
                <div>
                  <p class="text-[10px] uppercase tracking-wider font-extrabold text-slate-400">À partir de</p>
                  <span class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight leading-none">{price}€</span>
                </div>
                <span class="inline-flex items-center gap-1.5 text-[11px] font-bold text-[#0e8354] bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200/80">
                  <span class="w-1.5 h-1.5 rounded-full bg-[#0e8354]"></span>
                  <span>Départs 2026/2027</span>
                </span>
              </div>
              <a href="{url}" class="w-full mt-3.5 py-3 px-4 rounded-2xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-extrabold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-md shadow-emerald-950/20 active:scale-98 transition-all text-center">
                <span>Découvrir le circuit</span>
                <span>→</span>
              </a>
            </div>"""

    content = re.sub(pattern, repl, content, flags=re.DOTALL)

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed trip card footers in: {os.path.basename(fpath)}")

print("\nAll trip card footers successfully updated with perfectly centered buttons and breathable layout!")
