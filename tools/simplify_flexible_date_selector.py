import re

short_tours = [
    'bardia-explorateur',
    'chitwan-culture',
    'bardia-nuit-sauvage',
    'bardia-babai-camping',
    'babai-special',
    'chitwan-bardia-complete'
]

ultra_clean_departures_html = """          <!-- Departures Selector (CLEAN & MINIMAL) -->
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs font-bold">
              <label class="text-slate-700 uppercase tracking-wider text-[11px]">Votre date d'arrivée :</label>
              <span class="text-[#0e8354] flex items-center gap-1.5 text-xs font-bold">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                <span>Toute l'année</span>
              </span>
            </div>
            <input 
              type="date" 
              id="custom_departure_date" 
              class="w-full px-4 py-3 rounded-2xl border border-slate-200 text-sm font-semibold text-slate-800 bg-slate-50 focus:bg-white focus:outline-none focus:border-[#0e8354] transition-all cursor-pointer shadow-sm"
            />
          </div>"""

for slug in short_tours:
    fpath = f'/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/{slug}.astro'
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace the verbose box
    c = re.sub(
        r'<!-- Departures Selector.*?<!-- Primary CTA Button',
        ultra_clean_departures_html + '\n\n          <!-- Primary CTA Button',
        c,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"Simplified date selector across all {len(short_tours)} short tours!")
