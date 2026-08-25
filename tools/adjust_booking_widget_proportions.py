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
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs font-bold">
              <label class="text-slate-700 uppercase tracking-wider text-[11px]">Date de départ souhaitée :</label>
              <span class="text-[#0e8354] flex items-center gap-1.5 text-xs font-extrabold bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200/60">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                <span>Toute l'année</span>
              </span>
            </div>
            <input 
              type="date" 
              id="custom_departure_date" 
              class="w-full px-3.5 py-2.5 rounded-2xl border border-slate-200 text-sm font-semibold text-slate-800 bg-slate-50 focus:bg-white focus:outline-none focus:border-[#0e8354] transition-all cursor-pointer shadow-sm"
            />
          </div>"""
    else:
        date_section = """          <!-- Departures Selector (Expéditions) -->
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs font-bold">
              <label class="text-slate-700 uppercase tracking-wider text-[11px]">Prochaine session :</label>
              <span class="text-amber-600 text-xs font-extrabold bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">🔥 3 places</span>
            </div>
            <select class="w-full px-3.5 py-2.5 rounded-2xl border border-slate-200 text-xs font-bold text-slate-800 bg-slate-50 focus:bg-white focus:outline-none focus:border-[#0e8354] transition-all cursor-pointer shadow-sm">
              <option>10 Oct – 27 Oct 2026 (Confirmé)</option>
              <option>15 Nov – 02 Déc 2026 (Confirmé)</option>
              <option>05 Mars – 22 Mars 2027 (Garanti)</option>
            </select>
          </div>"""

    balanced_widget = f"""      <!-- RIGHT COLUMN: STICKY BOOKING CARD (PERFECTLY BALANCED PROPORTIONS) -->
      <div class="lg:col-span-4">
        <div id="booking-widget" class="sticky top-[92px] bg-white rounded-3xl p-5 sm:p-6 border border-slate-200/90 shadow-xl space-y-4">
          
          <!-- Header: Badge & Title -->
          <div>
            <span class="text-[11px] font-extrabold uppercase tracking-wider text-[#0e8354]">{badge_val}</span>
            <h3 class="font-black text-lg sm:text-xl text-slate-950 leading-snug mt-1 tracking-tight">
              {title_val}
            </h3>
            <p class="text-xs text-slate-500 font-semibold mt-1">{duration_val}</p>
          </div>

          <!-- Price Row -->
          <div class="pt-3 border-t border-slate-100 flex items-baseline justify-between">
            <div>
              <p class="text-[10px] font-extrabold uppercase text-slate-400 tracking-wider">À partir de</p>
              <div class="flex items-baseline gap-2">
                <span class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight">{price_val}</span>
                <span class="text-xs text-slate-500 font-medium">/ personne</span>
              </div>
            </div>
          </div>

{date_section}

          <!-- Primary CTA Button -->
          <button onclick="openBookingForm()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:opacity-95 text-white font-black text-sm shadow-lg shadow-[#0e8354]/30 hover:scale-[1.01] active:scale-95 transition-all text-center cursor-pointer">
            Réserver ma place →
          </button>

          <!-- Dual Secondary Actions (WhatsApp & PDF) -->
          <div class="grid grid-cols-2 gap-2.5 pt-1">
            <a href="https://wa.me/33695413227?text=Bonjour%20Robin,%20je%20souhaite%20des%20informations%20sur%20le%20circuit%20{slug}" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-2xl bg-emerald-50 hover:bg-emerald-100 text-[#0e8354] font-bold text-xs border border-emerald-200/80 transition-colors">
              <span>💬</span>
              <span>WhatsApp</span>
            </a>
            <button onclick="openPdfModal()" class="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs border border-slate-200 transition-colors cursor-pointer">
              <span>📥</span>
              <span>Carnet PDF</span>
            </button>
          </div>

          <!-- Reassurance List -->
          <div class="space-y-1.5 text-xs text-slate-500 pt-3 border-t border-slate-100 font-medium">
            <div class="flex items-center gap-2">
              <svg class="w-3.5 h-3.5 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Acompte de 30% seulement à l'inscription</span>
            </div>
            <div class="flex items-center gap-2">
              <svg class="w-3.5 h-3.5 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Annulation flexible jusqu'à 30 jours</span>
            </div>
            <div class="flex items-center gap-2">
              <svg class="w-3.5 h-3.5 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Paiement sécurisé & guides 100% natifs</span>
            </div>
          </div>

        </div>
      </div>"""

    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace the right column
    c = re.sub(
        r'<!-- RIGHT COLUMN:.*?</div>\s*</div>\s*(?=<!-- SECTION : AUTRES SÉJOURS SIMILAIRES|</div>\s*<!-- SECTION : AUTRES)',
        balanced_widget + '\n\n    ',
        c,
        flags=re.DOTALL
    )

    with open(tp, 'w', encoding='utf-8') as f:
        f.write(c)

print("Applied beautifully balanced booking card across all 15 tour pages!")
