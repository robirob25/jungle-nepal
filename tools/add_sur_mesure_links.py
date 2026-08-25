import re, glob, os

# 1. Update Header.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'r', encoding='utf-8') as f:
    hdr = f.read()

# In desktop nav: add "Sur-mesure" right after "Tous les 15 séjours" (or Destinations)
old_nav_item = """        <a href="/index.html#concept" class={isTransparent ? "hover:text-amber-300 transition-colors whitespace-nowrap" : "hover:text-[#0e8354] transition-colors whitespace-nowrap"}>
          L'esprit safari
        </a>"""

new_nav_item = """        <button type="button" onclick="openCustomTourModal()" class={isTransparent ? "hover:text-amber-300 transition-colors whitespace-nowrap flex items-center gap-1.5 cursor-pointer font-bold" : "hover:text-[#0e8354] transition-colors whitespace-nowrap flex items-center gap-1.5 cursor-pointer font-bold"}>
          <span>✨</span>
          <span>Sur-mesure</span>
        </button>
        <a href="/index.html#concept" class={isTransparent ? "hover:text-amber-300 transition-colors whitespace-nowrap" : "hover:text-[#0e8354] transition-colors whitespace-nowrap"}>
          L'esprit safari
        </a>"""

hdr = hdr.replace(old_nav_item, new_nav_item)

# In mobile menu drawer: add "Sur-mesure" button
old_mob_item = """      <a href="/index.html#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        L'esprit safari
      </a>"""

new_mob_item = """      <button type="button" onclick="toggleMobileMenu(); openCustomTourModal();" class="w-full text-left px-3.5 py-2.5 rounded-2xl bg-emerald-500/15 hover:bg-emerald-500/25 border border-emerald-500/30 flex items-center gap-2.5 text-[#10b981] font-bold transition-colors cursor-pointer">
        <span>✨</span>
        <span>Créer un séjour sur-mesure</span>
        <span class="ml-auto text-[10px] bg-emerald-500/30 px-2 py-0.5 rounded-full font-black text-white uppercase">Devis 24h</span>
      </button>
      <a href="/index.html#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        L'esprit safari
      </a>"""

hdr = hdr.replace(old_mob_item, new_mob_item)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'w', encoding='utf-8') as f:
    f.write(hdr)
print("✓ Updated Header.astro with Sur-mesure links")

# 2. Also update index.astro custom header if present
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

idx_old_item = """        <a href="#concept" class="text-white hover:text-amber-300 transition-colors whitespace-nowrap">L'esprit safari</a>"""
idx_new_item = """        <button type="button" onclick="openCustomTourModal()" class="text-white hover:text-amber-300 transition-colors whitespace-nowrap flex items-center gap-1.5 cursor-pointer font-bold">
          <span>✨</span>
          <span>Sur-mesure</span>
        </button>
        <a href="#concept" class="text-white hover:text-amber-300 transition-colors whitespace-nowrap">L'esprit safari</a>"""

idx = idx.replace(idx_old_item, idx_new_item)

idx_mob_old = """      <a href="#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        L'esprit safari
      </a>"""

idx_mob_new = """      <button type="button" onclick="toggleMobileMenu(); openCustomTourModal();" class="w-full text-left px-3.5 py-2.5 rounded-2xl bg-emerald-500/15 hover:bg-emerald-500/25 border border-emerald-500/30 flex items-center gap-2.5 text-[#10b981] font-bold transition-colors cursor-pointer">
        <span>✨</span>
        <span>Créer un séjour sur-mesure</span>
        <span class="ml-auto text-[10px] bg-emerald-500/30 px-2 py-0.5 rounded-full font-black text-white uppercase">Devis 24h</span>
      </button>
      <a href="#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        L'esprit safari
      </a>"""

idx = idx.replace(idx_mob_old, idx_mob_new)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

print("✓ Updated index.astro with Sur-mesure links")

# 3. Update all 15 tour pages with Sur-mesure link in their desktop and mobile headers
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')
for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        tc = f.read()
    orig = tc
    tc = tc.replace(
        """        <a href="/index.html#concept" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">
          L'esprit safari
        </a>""",
        """        <button type="button" onclick="openCustomTourModal()" class="hover:text-[#0e8354] transition-colors whitespace-nowrap flex items-center gap-1.5 cursor-pointer font-bold">
          <span>✨</span>
          <span>Sur-mesure</span>
        </button>
        <a href="/index.html#concept" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">
          L'esprit safari
        </a>"""
    )
    tc = tc.replace(
        """      <a href="/index.html#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        L'esprit safari
      </a>""",
        """      <button type="button" onclick="toggleMobileMenu(); openCustomTourModal();" class="w-full text-left px-3.5 py-2.5 rounded-2xl bg-emerald-500/15 hover:bg-emerald-500/25 border border-emerald-500/30 flex items-center gap-2.5 text-[#10b981] font-bold transition-colors cursor-pointer">
        <span>✨</span>
        <span>Créer un séjour sur-mesure</span>
        <span class="ml-auto text-[10px] bg-emerald-500/30 px-2 py-0.5 rounded-full font-black text-white uppercase">Devis 24h</span>
      </button>
      <a href="/index.html#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        L'esprit safari
      </a>"""
    )
    if tc != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(tc)

print("All navigation menus updated with custom tour trigger!")
