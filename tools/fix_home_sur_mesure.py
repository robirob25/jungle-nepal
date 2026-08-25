with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# In desktop nav:
old_nav = """      <a href="#concept" class="text-white hover:text-amber-300 transition-colors whitespace-nowrap">L'esprit safari</a>"""
if old_nav not in c:
    old_nav = """      <a href="#concept" class="hover:text-amber-300 transition-colors">L'esprit safari</a>"""

new_nav = """      <button type="button" onclick="openCustomTourModal()" class="hover:text-amber-300 text-amber-300 font-extrabold transition-colors whitespace-nowrap flex items-center gap-1.5 cursor-pointer bg-white/10 px-3.5 py-1.5 rounded-full border border-amber-300/30 shadow-sm hover:bg-white/20">
        <span>✨</span>
        <span>Sur-mesure</span>
      </button>
      <a href="#concept" class="hover:text-amber-300 transition-colors">L'esprit safari</a>"""

c = c.replace(old_nav, new_nav)

# In mobile nav:
old_mob = """      <a href="#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        <span>🌿</span><span>L'esprit safari</span>
      </a>"""
if old_mob not in c:
    old_mob = """      <a href="#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        L'esprit safari
      </a>"""

new_mob = """      <button type="button" onclick="toggleMobileMenu(); openCustomTourModal();" class="w-full text-left px-4 py-3 rounded-2xl bg-gradient-to-r from-emerald-600/30 to-emerald-500/20 hover:bg-emerald-500/30 border border-emerald-500/40 flex items-center gap-3 text-white font-extrabold transition-all cursor-pointer shadow-lg">
        <span class="text-lg">✨</span>
        <span class="text-sm">Créer un voyage sur-mesure</span>
        <span class="ml-auto text-[10px] bg-emerald-500 px-2 py-0.5 rounded-full font-black text-slate-950 uppercase">Devis 24h</span>
      </button>
      <a href="#concept" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        L'esprit safari
      </a>"""

c = c.replace(old_mob, new_mob)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Successfully added prominent Sur-mesure button to index.astro!")
