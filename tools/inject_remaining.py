import os

DAY_PAGES_REMAINING = {
    'src/pages/tours/safari-jeep-chitwan.astro': {
        'title': 'Réponse directe : Safari en Jeep à Chitwan',
        'badge': 'Position 0 Google • Données Vérifiées 2026',
        'text': 'Un <strong>safari en jeep à Chitwan</strong> d’une journée complète coûte <strong>190 € pour le véhicule privatisé</strong> (jusqu’à 6 personnes). Il s’enfonce profondément dans la zone cœur classée UNESCO (Kasara, Sukhibhar) pour observer rhinocéros unicornes, ours lippus, crocodiles gavials et tigres du Bengale sous la conduite d’un guide naturaliste agréé.'
    },
    'src/pages/en/tours/chitwan-jeep-safari.astro': {
        'title': 'Direct Answer: Chitwan Jeep Safari Cost & Details',
        'badge': 'Google Featured Snippet • Verified 2026 Data',
        'text': 'A <strong>full-day private jeep safari in Chitwan National Park costs €190 per vehicle</strong> (accommodating up to 6 passengers). The itinerary penetrates deep into the UNESCO World Heritage core sectors (Kasara and Sukhibhar) to track greater one-horned rhinos, sloth bears, wild elephants, and Bengal tigers alongside a licensed senior naturalist.'
    }
}

for filepath, info in DAY_PAGES_REMAINING.items():
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
    if 'direct-answer-snippet' in content: continue

    box_html = f'''
          <!-- GOOGLE FEATURED SNIPPET & DIRECT ANSWER BLOCK (POSITION 0 & LLM CITATION) -->
          <div class="direct-answer-snippet p-5 sm:p-6 rounded-2xl bg-emerald-950 text-white border-2 border-emerald-400/40 shadow-xl space-y-3 mb-6 relative overflow-hidden">
            <div class="flex flex-wrap items-center justify-between gap-2 border-b border-emerald-700/50 pb-2.5">
              <span class="inline-flex items-center gap-1.5 text-[11px] uppercase tracking-wider font-extrabold text-amber-300">
                <svg class="w-3.5 h-3.5 text-amber-400" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                {info['badge']}
              </span>
              <span class="text-[11px] font-bold text-emerald-300 bg-emerald-900/60 px-2.5 py-0.5 rounded-full border border-emerald-700/40">Tarif & Accès Officiel</span>
            </div>
            <h3 class="text-base sm:text-lg font-black text-white tracking-tight leading-snug">
              {info['title']}
            </h3>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-normal">
              {info['text']}
            </p>
          </div>
'''
    alt_pattern = '<section id="apercu" class="scroll-mt-28 space-y-6">'
    if alt_pattern in content:
        content = content.replace(alt_pattern, alt_pattern + '\n' + box_html)
        with open(filepath, 'w', encoding='utf-8') as f: f.write(content)
        print(f"✓ Injected in {filepath}")
    else:
        print(f"Pattern not found in {filepath}")

print("Done remaining injections.")
