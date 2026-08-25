import os, glob, re

tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours'
astro_files = glob.glob(os.path.join(tours_dir, '*.astro'))

for fpath in astro_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract price
    price_match = re.search(r'"price":\s*"([0-9\s,\.]+)"', content)
    if not price_match:
        price_match = re.search(r'<span class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight">([0-9\s,\.]+)€?</span>', content)
    base_price = price_match.group(1).replace(' ', '') if price_match else "490"

    # Extract tour title
    title_match = re.search(r'<h1 class="font-black text-2xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-\[1\.1\]">\s*(.*?)\s*</h1>', content, re.DOTALL)
    tour_title = title_match.group(1).strip() if title_match else "Séjour Safari"

    # 1. Clean and enhance Mobile Bottom Booking Bar with safe-area-inset, dual touch actions (WhatsApp + Réserver), and reactive price ID
    new_mobile_bar = f"""  <!-- STICKY MOBILE BOTTOM BOOKING BAR (100% RESPONSIVE & ERGONOMIC) -->
  <div class="fixed bottom-0 inset-x-0 bg-slate-950/95 backdrop-blur-2xl border-t border-white/15 px-4 pt-3 pb-[max(0.75rem,env(safe-area-inset-bottom))] z-40 lg:hidden flex items-center justify-between gap-3 shadow-[0_-10px_35px_rgba(0,0,0,0.6)]">
    <div class="min-w-0">
      <span class="text-[9px] text-slate-400 font-bold block uppercase tracking-wider truncate">Dès / pers.</span>
      <span id="mobile-bottom-price" class="text-xl font-black text-amber-300 font-mono tracking-tight">{base_price}€</span>
    </div>
    <div class="flex items-center gap-2 shrink-0">
      <a 
        href="https://wa.me/33695413227?text=Bonjour%20Robin,%20je%20souhaite%20des%20renseignements%20sur%20le%20circuit%20{re.sub(r'<.*?>', '', tour_title)}" 
        target="_blank" 
        rel="noopener noreferrer" 
        class="w-10 h-10 rounded-2xl bg-white/10 hover:bg-white/20 text-emerald-400 border border-white/15 flex items-center justify-center text-sm shadow-md active:scale-95 transition-all"
        aria-label="Contacter sur WhatsApp"
      >
        💬
      </a>
      <button 
        onclick="openBookingForm()" 
        class="px-5 py-2.5 rounded-2xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white font-black text-xs shadow-lg shadow-emerald-950/50 active:scale-95 transition-all flex items-center gap-1.5"
      >
        <span>Réserver</span>
        <span>→</span>
      </button>
    </div>
  </div>"""

    # Replace old mobile bottom bar
    content = re.sub(
        r'<!-- STICKY MOBILE BOTTOM BOOKING BAR.*?</div>\s*</div>\s*(?=<!-- PDF DOWNLOAD|\n\s*<div id="pdf-modal")',
        new_mobile_bar + '\n\n  ',
        content,
        flags=re.DOTALL
    )

    # 2. Update reactive toggleCampingOption JS to also update mobile-bottom-price
    if "isCampingSelected" in content:
        # Check if mobile-bottom-price is updated
        if "mobile-bottom-price" not in content:
            content = content.replace(
                "if (priceEl) {",
                """var mobileBottomEl = document.getElementById('mobile-bottom-price');
      if (mobileBottomEl) {
        mobileBottomEl.textContent = total + '€';
      }
      if (priceEl) {"""
            )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Enhanced mobile bottom bar in {fname}")

print("\nAll tour pages successfully upgraded with ergonomic mobile bottom bar!")
