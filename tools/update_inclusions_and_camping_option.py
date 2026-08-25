import os, glob, re

tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours'
astro_files = glob.glob(os.path.join(tours_dir, '*.astro'))

bardia_tours = [
    'bardia-explorateur.astro',
    'jungle-extreme.astro',
    'nepal-sauvage.astro',
    'chitwan-bardia-complete.astro',
    'nepal-immersion-totale.astro',
    'babai-special.astro',
    'rara-lake-bardia.astro',
    'rafting-safari.astro',
    'bardia-nuit-sauvage.astro',
    'bardia-babai-camping.astro'
]

camping_option_html = """
            <!-- Option Camping Sauvage au Cœur du Parc de Bardia (+350€) -->
            <div class="mt-6 p-5 sm:p-6 rounded-3xl bg-gradient-to-r from-emerald-950 via-slate-900 to-emerald-950 text-white border border-emerald-500/30 shadow-xl flex flex-col sm:flex-row items-start sm:items-center justify-between gap-5 col-span-1 sm:col-span-2">
              <div class="space-y-1.5 flex-1">
                <div class="flex items-center gap-2.5">
                  <span class="px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-black uppercase tracking-wider">
                    🏕️ Option d'exception
                  </span>
                  <span class="text-xs font-mono font-bold text-emerald-400">
                    +350 € / personne
                  </span>
                </div>
                <h3 class="text-base sm:text-lg font-black text-white tracking-tight">
                  Option Nuit en Camping sauvage au cœur du Parc de Bardia
                </h3>
                <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                  Vivez l'expérience immersive d'une nuit en campement éphémère au cœur du territoire des tigres avec nos maîtres pisteurs Pawan & Kiran. Matériel complet, dîner chaud au feu de bois et veillée aux bruits purs de la jungle.
                </p>
              </div>
              <div class="shrink-0 flex items-center gap-3 w-full sm:w-auto">
                <a 
                  href="https://wa.me/33695413227?text=Bonjour%20Robin,%20je%20souhaite%20ajouter%20l'option%20Camping%20au%20cœur%20du%20Parc%20de%20Bardia%20(350€)" 
                  target="_blank" 
                  class="w-full sm:w-auto px-5 py-3 rounded-full bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs text-center shadow-lg transition-all hover:scale-105 active:scale-95 whitespace-nowrap"
                >
                  Ajouter l'option (+350 €) →
                </a>
              </div>
            </div>"""

for fpath in astro_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Clean up "tentes de bivouac" in "Inclus dans le tarif"
    if fname in ['bardia-babai-camping.astro', 'bardia-nuit-sauvage.astro']:
        content = content.replace(
            'Tous les hébergements (éco-lodges traditionnels ou tentes de bivouac)',
            'Tous les hébergements (éco-lodges traditionnels et campement de brousse complet)'
        )
    else:
        content = content.replace(
            'Tous les hébergements (éco-lodges traditionnels ou tentes de bivouac)',
            'Tous les hébergements (éco-lodges de charme et hôtels traditionnels sélectionnés)'
        )

    # 2. Add the +350€ Camping Option to all Bardia tours (if not already present)
    if fname in bardia_tours:
        if "Option Nuit en Camping sauvage au cœur du Parc de Bardia" not in content:
            # Insert inside the grid of inclusions right after the second col
            pattern = r'(</div>\s*</div>\s*</section>\s*<!-- SECTION 5: AVIS)'
            # Let's find the closing of the 2-col inclusions grid:
            # Look for <div class="grid grid-cols-1 sm:grid-cols-2 gap-6"> ... </div>
            match = re.search(r'(<div class="grid grid-cols-1 sm:grid-cols-2 gap-6">.*?</div>\s*</div>)', content, re.DOTALL)
            if match:
                grid_block = match.group(1)
                # Insert the option before the last </div>
                # The grid block has the 2 cards, then closes with </div>
                updated_grid = grid_block[:-6] + camping_option_html + "\n          </div>"
                content = content.replace(grid_block, updated_grid, 1)
                print(f"  ✓ Added +350€ Camping option in: {fname}")

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated inclusions in: {fname}")

print("\nAll tour inclusions and Bardia +350€ camping options successfully updated!")
