import json, re, glob, os

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

tour_map = {t['slug']: t for t in tours}
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for tp in tour_files:
    slug = os.path.splitext(os.path.basename(tp))[0]
    tdata = tour_map.get(slug)
    if not tdata:
        continue

    is_short = int(tdata.get('daysCount', 10)) < 12
    price_val = str(tdata.get('price', '490€'))
    if not price_val.endswith('€'):
        price_val += '€'
    
    title_val = tdata['title']
    duration_val = f"{tdata.get('daysCount', 5)} jours • Micro-groupe (4 à 8 pers)"
    badge_val = tdata.get('style', 'Safari & Lodge Confort')

    if is_short:
        date_section = """          <!-- Date Selector (Toute l'année) -->
          <div class="space-y-1">
            <div class="flex items-center justify-between text-[11px] font-bold">
              <label class="text-slate-700">Votre date d'arrivée :</label>
              <span class="text-[#0e8354] flex items-center gap-1 text-[10px]">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                <span>Toute l'année</span>
              </span>
            </div>
            <input 
              type="date" 
              id="custom_departure_date" 
              class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-800 bg-slate-50 focus:bg-white focus:outline-none focus:border-[#0e8354] cursor-pointer shadow-sm"
            />
          </div>"""
    else:
        date_section = """          <!-- Departures Selector (Expéditions) -->
          <div class="space-y-1">
            <div class="flex items-center justify-between text-[11px] font-bold">
              <label class="text-slate-700">Prochaine session :</label>
              <span class="text-amber-600 text-[10px] font-bold">🔥 3 places restantes</span>
            </div>
            <select class="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-800 bg-slate-50 focus:bg-white focus:outline-none focus:border-[#0e8354] cursor-pointer shadow-sm">
              <option>10 Oct – 27 Oct 2026 (Départ confirmé)</option>
              <option>15 Nov – 02 Déc 2026 (Départ confirmé)</option>
              <option>05 Mars – 22 Mars 2027 (Départ garanti)</option>
            </select>
          </div>"""

    compact_widget = f"""      <!-- RIGHT COLUMN: STICKY BOOKING CARD COMPACT (FITS DESKTOP VIEWPORT) -->
      <div class="lg:col-span-4">
        <div id="booking-widget" class="sticky top-[86px] bg-white rounded-2xl sm:rounded-3xl p-4 sm:p-5 border border-slate-200 shadow-xl space-y-3.5">
          
          <!-- Title & Price Row -->
          <div class="flex items-start justify-between gap-2 pb-2.5 border-b border-slate-100">
            <div>
              <span class="text-[10px] font-extrabold uppercase tracking-wider text-[#0e8354] block">{badge_val}</span>
              <h3 class="font-black text-sm sm:text-base text-slate-950 leading-tight mt-0.5">
                {title_val}
              </h3>
              <p class="text-[11px] text-slate-500 font-medium mt-0.5">{duration_val}</p>
            </div>
            <div class="text-right shrink-0">
              <p class="text-[9px] font-extrabold uppercase text-slate-400">À partir de</p>
              <span class="font-black text-xl sm:text-2xl text-slate-950 tracking-tight">{price_val}</span>
            </div>
          </div>

{date_section}

          <!-- Primary CTA Button -->
          <button onclick="openBookingForm()" class="w-full py-2.5 sm:py-3 rounded-xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:opacity-95 text-white font-black text-xs sm:text-sm shadow-md shadow-[#0e8354]/30 hover:scale-[1.01] active:scale-95 transition-all text-center cursor-pointer">
            Réserver ma place →
          </button>

          <!-- Dual Secondary Actions (WhatsApp + PDF) -->
          <div class="grid grid-cols-2 gap-2 pt-0.5">
            <a href="https://wa.me/33695413227?text=Bonjour%20Robin,%20je%20souhaite%20des%20informations%20sur%20le%20circuit%20{slug}" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-1.5 py-2 px-2 rounded-xl bg-emerald-50 hover:bg-emerald-100 text-[#0e8354] font-bold text-[11px] border border-emerald-200 transition-colors">
              <span>💬</span>
              <span>WhatsApp</span>
            </a>
            <button onclick="openPdfModal()" class="flex items-center justify-center gap-1.5 py-2 px-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-[11px] border border-slate-200 transition-colors cursor-pointer">
              <span>📥</span>
              <span>Carnet PDF</span>
            </button>
          </div>

          <!-- Compact Reassurance Footer -->
          <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500 font-medium">
            <span>🛡️ Acompte 30%</span>
            <span>•</span>
            <span>🔄 Annulation 30j</span>
            <span>•</span>
            <span>🔒 Paiement sécurisé</span>
          </div>

        </div>
      </div>"""

    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace the right column
    c = re.sub(
        r'<!-- RIGHT COLUMN:.*?</div>\s*</div>\s*(?=<!-- SECTION : AUTRES SÉJOURS SIMILAIRES|</div>\s*<!-- SECTION : AUTRES)',
        compact_widget + '\n\n    ',
        c,
        flags=re.DOTALL
    )

    with open(tp, 'w', encoding='utf-8') as f:
        f.write(c)

print("Applied ultra-compact, desktop-optimized booking card across all 15 tour detail pages!")
