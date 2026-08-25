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

for fpath in astro_files:
    fname = os.path.basename(fpath)
    if fname not in bardia_tours:
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract base price from file
    price_match = re.search(r'"price":\s*"([0-9\s,\.]+)"', content)
    if not price_match:
        price_match = re.search(r'<span class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight">([0-9\s,\.]+)€?</span>', content)
    
    if not price_match:
        print(f"Could not find price in {fname}")
        continue

    base_price_raw = price_match.group(1).replace(' ', '').replace(',', '')
    try:
        base_price_int = int(float(base_price_raw))
    except:
        base_price_int = 490

    # 1. Update the price display in sidebar to have id="tour-price-display" and add the camping notification badge below it
    sidebar_price_pattern = r'<div class="flex items-baseline gap-2">\s*<span [^>]*>[0-9\s,\.]+€?</span>\s*<span [^>]*>/ personne</span>\s*</div>(?:\s*<!-- Notification Badge: Option Camping incluse -->.*?</div>)?'
    
    new_sidebar_price = f"""<div class="flex items-baseline gap-2">
                <span id="tour-price-display" data-base-price="{base_price_int}" class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight">{base_price_int}€</span>
                <span class="text-xs text-slate-500 font-medium">/ personne</span>
              </div>
              <!-- Notification Badge: Option Camping incluse -->
              <div id="camping-included-badge" class="hidden mt-2.5 p-2.5 rounded-2xl bg-emerald-50 border border-emerald-300 text-[11px] font-extrabold text-emerald-800 flex items-center gap-2 shadow-sm transition-all duration-300">
                <span class="text-sm">🏕️</span>
                <span>Inclut la nuit en camping sauvage (+350 €)</span>
              </div>"""

    content = re.sub(sidebar_price_pattern, new_sidebar_price, content, count=1, flags=re.DOTALL)

    # 2. Update Sticky Bar price span
    sticky_pattern = r'<a href="#dates-prix" class="text-right hover:opacity-80 transition-opacity">\s*<p class="text-\[11px\] font-bold text-\[#0e8354\]">[0-9\s,\.]+€?\s*<span class="text-slate-400 font-normal">/ pers\.</span></p>\s*</a>'
    new_sticky = f"""<a href="#dates-prix" class="text-right hover:opacity-80 transition-opacity">
            <p id="sticky-price-display" class="text-[11px] font-bold text-[#0e8354]">{base_price_int}€ <span class="text-slate-400 font-normal">/ pers.</span></p>
          </a>"""
    content = re.sub(sticky_pattern, new_sticky, content, count=1)

    # 3. Update Option Card
    new_camping_card = f"""            <!-- Option Camping Sauvage au Cœur du Parc de Bardia (+350€) -->
            <div id="camping-option-card" class="mt-6 p-5 sm:p-6 rounded-3xl bg-gradient-to-r from-emerald-950 via-slate-900 to-emerald-950 text-white border border-emerald-500/30 shadow-xl flex flex-col sm:flex-row items-start sm:items-center justify-between gap-5 col-span-1 sm:col-span-2 transition-all duration-300">
              <div class="space-y-1.5 flex-1">
                <div class="flex items-center gap-2.5">
                  <span id="camping-badge-tag" class="px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-black uppercase tracking-wider">
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
                <button 
                  id="toggle-camping-btn"
                  onclick="toggleCampingOption(350)" 
                  class="w-full sm:w-auto px-6 py-3.5 rounded-full bg-emerald-600 hover:bg-emerald-500 text-white font-black text-xs sm:text-sm text-center shadow-lg shadow-emerald-950/50 transition-all hover:scale-105 active:scale-95 whitespace-nowrap cursor-pointer flex items-center justify-center gap-2"
                >
                  <span id="camping-btn-icon">⊕</span>
                  <span id="camping-btn-text">Ajouter l'option (+350 €)</span>
                </button>
              </div>
            </div>"""

    content = re.sub(
        r'<!-- Option Camping Sauvage au Cœur du Parc de Bardia.*?</div>\s*</div>\s*(?=</div>\s*</section>)',
        new_camping_card + '\n          ',
        content,
        flags=re.DOTALL
    )

    # 4. Inject or update JavaScript
    js_script = f"""
  <script is:inline>
    var baseTourPrice = {base_price_int};
    var isCampingSelected = false;

    function toggleCampingOption(extraCost) {{
      extraCost = extraCost || 350;
      isCampingSelected = !isCampingSelected;
      var total = isCampingSelected ? (baseTourPrice + extraCost) : baseTourPrice;

      // 1. Update Main Sidebar Price Display
      var priceEl = document.getElementById('tour-price-display');
      if (priceEl) {{
        priceEl.textContent = total + '€';
      }}

      // 2. Update Sticky Bar Price Display
      var stickyEl = document.getElementById('sticky-price-display');
      if (stickyEl) {{
        stickyEl.innerHTML = total + '€ <span class="text-slate-400 font-normal">/ pers.</span>';
      }}

      // 3. Toggle Notification Badge under the Price
      var badgeEl = document.getElementById('camping-included-badge');
      if (badgeEl) {{
        if (isCampingSelected) {{
          badgeEl.classList.remove('hidden');
        }} else {{
          badgeEl.classList.add('hidden');
        }}
      }}

      // 4. Update Button State and Card Styling
      var btn = document.getElementById('toggle-camping-btn');
      var btnText = document.getElementById('camping-btn-text');
      var btnIcon = document.getElementById('camping-btn-icon');
      var card = document.getElementById('camping-option-card');
      var badgeTag = document.getElementById('camping-badge-tag');

      if (btn && btnText && btnIcon) {{
        if (isCampingSelected) {{
          btn.classList.remove('bg-emerald-600', 'hover:bg-emerald-500', 'text-white');
          btn.classList.add('bg-amber-400', 'hover:bg-amber-300', 'text-slate-950', 'shadow-amber-500/30');
          btnIcon.textContent = '✓';
          btnText.textContent = "Option Camping incluse (Retirer)";
          if (card) card.classList.add('ring-2', 'ring-amber-400/80', 'border-amber-400/50');
          if (badgeTag) {{
            badgeTag.classList.remove('bg-amber-500/20', 'text-amber-300', 'border-amber-500/30');
            badgeTag.classList.add('bg-emerald-500/20', 'text-emerald-300', 'border-emerald-500/40');
            badgeTag.textContent = '✓ Option Activée (+350€)';
          }}
        }} else {{
          btn.classList.remove('bg-amber-400', 'hover:bg-amber-300', 'text-slate-950', 'shadow-amber-500/30');
          btn.classList.add('bg-emerald-600', 'hover:bg-emerald-500', 'text-white');
          btnIcon.textContent = '⊕';
          btnText.textContent = "Ajouter l'option (+350 €)";
          if (card) card.classList.remove('ring-2', 'ring-amber-400/80', 'border-amber-400/50');
          if (badgeTag) {{
            badgeTag.classList.remove('bg-emerald-500/20', 'text-emerald-300', 'border-emerald-500/40');
            badgeTag.classList.add('bg-amber-500/20', 'text-amber-300', 'border-amber-500/30');
            badgeTag.textContent = "🏕️ Option d'exception";
          }}
        }}
      }}
    }}
  </script>
"""

    if "function toggleCampingOption" not in content:
        content = content.replace("</Layout>", js_script + "\n</Layout>")
    else:
        # replace old script block
        content = re.sub(r'<script is:inline>\s*var baseTourPrice =.*?</script>', js_script.strip(), content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Configured reactive camping option in {fname} (Base: {base_price_int}€)")

print("\nAll Bardia tour pages updated with dynamic reactive pricing and camping notification!")
