import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove the Sur-mesure button from the main header nav
old_header_btn = """      <button type="button" onclick="openCustomTourModal()" class="hover:text-amber-300 text-amber-300 font-extrabold transition-colors whitespace-nowrap flex items-center gap-1.5 cursor-pointer bg-white/10 px-3.5 py-1.5 rounded-full border border-amber-300/30 shadow-sm hover:bg-white/20">
        <span>✨</span>
        <span>Sur-mesure</span>
      </button>"""

c = c.replace(old_header_btn + "\n", "")
c = c.replace(old_header_btn, "")

# 2. In #prochains-departs header: Replace the simple count badge with the "Affichage de 15 séjours" + "✨ Créer un séjour sur-mesure" CTA button
old_right_col = """        <div>
          <span id="trip-count-badge" class="text-xs sm:text-sm font-extrabold text-slate-700 bg-white px-4 py-2.5 rounded-full border border-slate-200 shadow-sm">
            Affichage de <strong>15 séjours</strong>
          </span>
        </div>"""

new_right_col = """        <div class="flex flex-wrap items-center gap-3 shrink-0">
          <span id="trip-count-badge" class="hidden sm:inline-flex text-xs sm:text-sm font-extrabold text-slate-700 bg-white px-4 py-2.5 rounded-full border border-slate-200 shadow-sm">
            Affichage de <strong>15 séjours</strong>
          </span>
          <button type="button" onclick="openCustomTourModal()" class="inline-flex items-center gap-2 px-5 py-2.5 sm:px-6 sm:py-3 rounded-full bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-black text-xs sm:text-sm shadow-lg shadow-[#0e8354]/25 hover:scale-105 active:scale-95 transition-all duration-300 cursor-pointer">
            <span>✨</span>
            <span>Créer un séjour sur-mesure</span>
          </button>
        </div>"""

c = c.replace(old_right_col, new_right_col)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Relocated Sur-mesure to the 15 Séjours section header!")
