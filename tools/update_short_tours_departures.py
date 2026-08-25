import os, glob, re, json

# 1. Fix panthere-des-neiges daysCount in tours.json to 17
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    if t['slug'] == 'panthere-des-neiges':
        t['daysCount'] = 17
    days = int(t.get('daysCount', 10))
    if days < 12:
        t['departures_type'] = 'flexible'
    else:
        t['departures_type'] = 'scheduled'

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

# 2. Flexible Date Selector for Short Tours (< 12 days)
short_tours = [
    'bardia-explorateur',
    'chitwan-culture',
    'bardia-nuit-sauvage',
    'bardia-babai-camping',
    'babai-special',
    'chitwan-bardia-complete'
]

flexible_departures_html = """          <!-- Departures Selector (AVAILABLE ALL YEAR ROUND - ALWAYS AVAILABLE) -->
          <div class="space-y-3">
            <div class="bg-emerald-50/90 border border-emerald-200/90 rounded-2xl p-3.5 space-y-1.5 shadow-sm">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
                <span class="font-extrabold text-xs text-[#0e8354] uppercase tracking-wide">Disponible toute l'année</span>
                <span class="text-[10px] bg-emerald-200/60 text-[#0c6d46] px-2 py-0.5 rounded-full font-bold ml-auto">Places garanties</span>
              </div>
              <p class="text-xs text-slate-700 font-medium leading-relaxed">
                Ce séjour part <strong>à la date exacte de votre choix</strong>. Guides et lodges sont disponibles en continu 365j / an.
              </p>
            </div>

            <div>
              <label class="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-1.5">
                Indiquez votre date d'arrivée souhaitée :
              </label>
              <input 
                type="date" 
                id="custom_departure_date" 
                class="w-full px-4 py-3 rounded-2xl border border-slate-200 text-sm font-semibold text-slate-800 bg-slate-50 focus:bg-white focus:outline-none focus:border-[#0e8354] focus:ring-2 focus:ring-[#0e8354]/20 transition-all cursor-pointer"
              />
            </div>
          </div>"""

for slug in short_tours:
    fpath = f'/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/{slug}.astro'
    if not os.path.exists(fpath):
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace the fixed departures selector in the sticky card
    c = re.sub(
        r'<!-- Departures Selector -->.*?<!-- Primary CTA Button',
        flexible_departures_html + '\n\n          <!-- Primary CTA Button',
        c,
        flags=re.DOTALL
    )

    # Update WhatsApp CTA link to mention flexible dates on short tours
    c = re.sub(
        r'href=[\'"]https://wa\.me/33695413227\?text=[^\'"]*[\'"]',
        f'href="https://wa.me/33695413227?text=Bonjour%20Robin,%20je%20souhaite%20r%C3%A9server%20le%20s%C3%A9jour%20{slug}%20%C3%A0%20mes%20dates%20toute%20l%27ann%C3%A9e."',
        c
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"Updated all {len(short_tours)} short tours (< 12 days) to 'Disponible toute l'année / Départs sur-mesure'!")
