import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the category pills section with pure black Lucide icons
pills_replacement = """        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200" data-filter="all">
          <i data-lucide="compass" class="w-4 h-4"></i>
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>
        </button>

        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="safari">
          <i data-lucide="binoculars" class="w-4 h-4 text-slate-900"></i>
          <span>Safaris et pistage Bardia</span>
        </button>

        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="bivouac">
          <i data-lucide="tent" class="w-4 h-4 text-slate-900"></i>
          <span>Bivouacs et nuits sauvages</span>
        </button>

        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="chitwan">
          <i data-lucide="trees" class="w-4 h-4 text-slate-900"></i>
          <span>Chitwan et rhinocéros</span>
        </button>

        <button onclick="filterTrips('trek')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="trek">
          <i data-lucide="mountain" class="w-4 h-4 text-slate-900"></i>
          <span>Treks et lac Rara</span>
        </button>

        <button onclick="filterTrips('culture')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="culture">
          <i data-lucide="palette" class="w-4 h-4 text-slate-900"></i>
          <span>Culture, yoga et carnet</span>
        </button>

        <button onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200" data-filter="rafting">
          <i data-lucide="waves" class="w-4 h-4 text-slate-900"></i>
          <span>Rafting Karnali</span>
        </button>"""

# Replace the pills block in html
pattern_pills = r'<div class=\"flex items-center gap-2\.5 overflow-x-auto no-scrollbar py-1\">.*?</div>\s*</div>\s*</section>'
html = re.sub(pattern_pills, f'<div class="flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1">\n{pills_replacement}\n      </div>\n    </div>\n  </section>', html, flags=re.DOTALL)

# 2. Update filterTrips JS function so the active pill stays sleek black & white
html = html.replace(
    "pill.classList.add('bg-slate-950', 'text-amber-300', 'border-amber-400/40', 'scale-105');",
    "pill.classList.add('bg-slate-950', 'text-white', 'border-slate-900', 'scale-105'); const icon = pill.querySelector('i'); if (icon) icon.classList.remove('text-slate-900'); if (icon) icon.classList.add('text-white');"
)
html = html.replace(
    "pill.classList.remove('bg-slate-950', 'text-amber-300', 'border-amber-400/40', 'scale-105');",
    "pill.classList.remove('bg-slate-950', 'text-white', 'border-slate-900', 'scale-105'); const icon = pill.querySelector('i'); if (icon) icon.classList.remove('text-white'); if (icon) icon.classList.add('text-slate-900');"
)

# 3. Clean any remaining colored emojis in cards and concept badges
html = html.replace('<span>🐅</span>\n              <span>Pistage du tigre à pied</span>', '<i data-lucide="binoculars" class="w-4 h-4 text-white"></i>\n              <span>Pistage du tigre à pied</span>')
html = html.replace('<span>🦏</span>\n              <span>Sanctuaires inviolés</span>', '<i data-lucide="shield" class="w-4 h-4 text-white"></i>\n              <span>Sanctuaires inviolés</span>')
html = html.replace('<span>⛺</span>\n              <span>Micro-groupes de 4 à 8</span>', '<i data-lucide="tent" class="w-4 h-4 text-white"></i>\n              <span>Micro-groupes de 4 à 8</span>')
html = html.replace('<span>🐾 Tous les 14 circuits</span>', '<i data-lucide="compass" class="w-4 h-4"></i><span>Tous les 14 circuits</span>')
html = html.replace('🧭 L\'esprit safari', '<i data-lucide="trees" class="w-4 h-4"></i> L\'esprit safari')
html = html.replace('🐅 Nos maîtres pisteurs', '<i data-lucide="users" class="w-4 h-4"></i> Nos maîtres pisteurs')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced all colored emojis with clean monochrome black vector icons!")
