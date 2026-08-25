with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the flex container to only keep the "Créer un séjour sur-mesure" button
old_block = """        <div class="flex flex-wrap items-center gap-3 shrink-0">
          <span id="trip-count-badge" class="hidden sm:inline-flex text-xs sm:text-sm font-extrabold text-slate-700 bg-white px-4 py-2.5 rounded-full border border-slate-200 shadow-sm">
            Affichage de <strong>15 séjours</strong>
          </span>
          <button type="button" onclick="openCustomTourModal()" class="inline-flex items-center gap-2 px-5 py-2.5 sm:px-6 sm:py-3 rounded-full bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-black text-xs sm:text-sm shadow-lg shadow-[#0e8354]/25 hover:scale-105 active:scale-95 transition-all duration-300 cursor-pointer">
            <span>✨</span>
            <span>Créer un séjour sur-mesure</span>
          </button>
        </div>"""

new_block = """        <div class="shrink-0">
          <button type="button" onclick="openCustomTourModal()" class="inline-flex items-center gap-2 px-5 py-2.5 sm:px-6 sm:py-3 rounded-full bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-black text-xs sm:text-sm shadow-lg shadow-[#0e8354]/25 hover:scale-105 active:scale-95 transition-all duration-300 cursor-pointer">
            <span>✨</span>
            <span>Créer un séjour sur-mesure</span>
          </button>
        </div>"""

c = c.replace(old_block, new_block)

# In JS filterTrips, make sure trip-count-badge update doesn't throw if element doesn't exist
c = c.replace(
    "if (badge) {",
    "var badge = document.getElementById('trip-count-badge');\n    if (badge) {"
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Removed trip count badge successfully!")
