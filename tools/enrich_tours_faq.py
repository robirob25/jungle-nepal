import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

# The 5 official FAQ questions to integrate across all tours:
faq_addition = """
            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Comment réserver un tour ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <div class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal space-y-1.5">
                <p>Une fois que vous avez choisi votre tour, nous vous enverrons un contrat par email.</p>
                <p>Pour confirmer votre réservation, vous devrez verser un acompte.</p>
                <p>Le solde restant sera dû le premier jour de votre voyage à Katmandou.</p>
              </div>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Puis-je personnaliser mon voyage ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <div class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal space-y-1.5">
                <p>Absolument ! Notre équipe peut vous aider à créer une expérience sur mesure selon votre budget et vos préférences. Dites-nous simplement ce que vous recherchez.</p>
              </div>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Y a-t-il des réductions disponibles ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <div class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal space-y-1.5">
                <p>Oui, nous proposons des réductions pour les réservations de groupe. Contactez-nous pour plus de détails sur nos tarifs groupés.</p>
              </div>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Ai-je besoin d’une assurance voyage ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <div class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal space-y-1.5">
                <p>Oui, vous devez souscrire une assurance voyage dans votre pays d’origine couvrant les activités prévues et les rapatriements.</p>
              </div>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Qu’est-ce qui est inclus dans le prix du tour ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <div class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal space-y-1.5">
                <p>Nos tours incluent généralement l’hébergement, les repas, le transport, les excursions guidées et les permis nécessaires. Les détails peuvent varier selon le tour, donc veuillez consulter la description ou nous contacter pour des informations précises.</p>
              </div>
            </details>"""

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Remove the generic "Comment se passe la réservation et le règlement ?" if present so it doesn't duplicate with "Comment réserver un tour ?"
    c = re.sub(r'<details class="group bg-white p-4 rounded-2xl border border-slate-200">\s*<summary[^>]*>.*?Comment se passe la réservation et le règlement\s*\?.*?</details>', '', c, flags=re.DOTALL)

    # Insert the full FAQ into the <section id="faq">
    # Replace closing </div>\s*</section> in faq
    faq_match = re.search(r'(<section id="faq"[^>]*>.*?<div class="space-y-3 text-sm">)(.*?)(</div>\s*</section>)', c, flags=re.DOTALL)
    if faq_match:
        existing_items = faq_match.group(2).strip()
        new_faq_content = faq_match.group(1) + '\n' + faq_addition + '\n' + existing_items + '\n          ' + faq_match.group(3)
        c = c[:faq_match.start()] + new_faq_content + c[faq_match.end():]
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Enriched FAQ in {fpath.split('/')[-1]}")

print("Done updating FAQ on all 15 tour pages!")
