import re, glob, os, json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours_data = json.load(f)

tours_by_slug = {t.get('slug'): t for t in tours_data}

def upgrade_tour_page(file_path, is_en=False):
    slug = os.path.basename(file_path).replace('.astro', '')
    tour_meta = tours_by_slug.get(slug, {})
    price = tour_meta.get('price', '450€')
    title = tour_meta.get('title_en' if is_en else 'title', 'Séjour au Népal')

    with open(file_path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Update Photo Mosaic Container for mobile heights
    c = re.sub(
        r'<div class="grid grid-cols-1 md:grid-cols-4 gap-3 rounded-3xl overflow-hidden h-\[\d+px\] sm:h-\[\d+px\]',
        '<div class="grid grid-cols-1 md:grid-cols-4 gap-2.5 sm:gap-3 rounded-2xl sm:rounded-3xl overflow-hidden h-[280px] sm:h-[380px] md:h-[460px]',
        c
    )

    # 2. Update Sticky Subnav for touch scrolling
    c = re.sub(
        r'<div class="sticky top-\[69px\] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8">',
        '<div class="sticky top-[56px] sm:top-[69px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-2.5 sm:py-3 mb-6 sm:mb-8 shadow-sm">\n      <div class="flex items-center gap-4 sm:gap-6 overflow-x-auto no-scrollbar text-xs sm:text-sm font-bold text-slate-600 px-1 py-0.5">',
        c
    )

    # 3. Add Sticky Mobile Bottom Booking Bar before </Layout>
    wa_text = f"Hello Robin, I am interested in {title} ({price})" if is_en else f"Bonjour Robin, je suis intéressé par le séjour {title} ({price})"
    wa_encoded = wa_text.replace(' ', '%20')

    if is_en:
        bottom_bar = f"""
  <!-- STICKY MOBILE BOTTOM BOOKING BAR (MOBILE / TABLET) -->
  <div class="fixed bottom-0 inset-x-0 bg-slate-950/95 backdrop-blur-xl border-t border-white/15 p-3 sm:px-6 z-40 lg:hidden flex items-center justify-between gap-3 shadow-[0_-10px_30px_rgba(0,0,0,0.5)]">
    <div>
      <span class="text-[10px] text-slate-400 font-bold block uppercase tracking-wider">All-inclusive from</span>
      <span class="text-xl sm:text-2xl font-black text-amber-300">{price} <span class="text-[10px] text-slate-400 font-normal">/ pers</span></span>
    </div>
    <div class="flex items-center gap-2">
      <a href="https://wa.me/33695413227?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 px-4 sm:px-6 py-2.5 sm:py-3 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs shadow-lg active:scale-95 transition-all whitespace-nowrap">
        <svg class="w-4 h-4 text-white shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        <span>Book on WhatsApp</span>
      </a>
    </div>
  </div>
"""
    else:
        bottom_bar = f"""
  <!-- STICKY MOBILE BOTTOM BOOKING BAR (MOBILE / TABLET) -->
  <div class="fixed bottom-0 inset-x-0 bg-slate-950/95 backdrop-blur-xl border-t border-white/15 p-3 sm:px-6 z-40 lg:hidden flex items-center justify-between gap-3 shadow-[0_-10px_30px_rgba(0,0,0,0.5)]">
    <div>
      <span class="text-[10px] text-slate-400 font-bold block uppercase tracking-wider">Tout compris à partir de</span>
      <span class="text-xl sm:text-2xl font-black text-amber-300">{price} <span class="text-[10px] text-slate-400 font-normal">/ pers</span></span>
    </div>
    <div class="flex items-center gap-2">
      <a href="https://wa.me/33695413227?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 px-4 sm:px-6 py-2.5 sm:py-3 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs shadow-lg active:scale-95 transition-all whitespace-nowrap">
        <svg class="w-4 h-4 text-white shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        <span>Réserver sur WhatsApp</span>
      </a>
    </div>
  </div>
"""

    # Remove existing bottom bar if any
    c = re.sub(r'<!-- STICKY MOBILE BOTTOM BOOKING BAR.*?</div>\s*</div>', '', c, flags=re.DOTALL)

    # Insert bottom bar before </Layout>
    c = c.replace('</Layout>', bottom_bar + '\n</Layout>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"✓ Upgraded responsive UX on {os.path.basename(file_path)} ({'EN' if is_en else 'FR'})")

for f in glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro'):
    upgrade_tour_page(f, is_en=False)

for f in glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/*.astro'):
    upgrade_tour_page(f, is_en=True)

print("Upgraded all 30 tour pages with mobile/tablet sticky booking bar and smooth responsive layout!")
