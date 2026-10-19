import re, glob

# Elite 2026 Mobile Bar Component Upgrade
# Replaces the generic/raw bar with an ultra-polished, luxury glassmorphic bar
# Features:
# - Deep zinc-950/90 glassmorphism with subtle 1px white/10 top border and ambient light
# - Status pulse dot (Emerald green for "Disponibilité immédiate" / "Instant availability")
# - High-contrast price with clear label
# - Direct WhatsApp button with native branded green icon SVG (no emoji!)
# - Bold primary CTA button with tactile active:scale-95 and spring-like feel

FR_REPLACEMENT = '''  <!-- LUXE STICKY MOBILE CONVERSION BAR (ELITE 2026 UI/UX) -->
  <aside 
    class="fixed bottom-0 inset-x-0 bg-zinc-950/90 backdrop-blur-xl border-t border-white/10 px-4 pt-3 pb-[max(0.75rem,env(safe-area-inset-bottom))] z-40 lg:hidden shadow-[0_-8px_30px_rgba(0,0,0,0.5)] transition-transform duration-300" 
    aria-label="Barre d'action rapide"
  >
    <div class="max-w-lg mx-auto flex items-center justify-between gap-3">
      <!-- Price & Availability Status -->
      <div class="min-w-0 flex flex-col justify-center">
        <div class="flex items-center gap-1.5 mb-0.5">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400 truncate">
            Dispo immédiate
          </span>
        </div>
        <div class="flex items-baseline gap-1">
          <span id="mobile-bottom-price" class="text-xl font-black text-white tracking-tight leading-none">
            50€
          </span>
          <span class="text-[11px] font-semibold text-zinc-400">/ pers.</span>
        </div>
      </div>

      <!-- Actions (WhatsApp + Direct Booking) -->
      <div class="flex items-center gap-2 shrink-0">
        <!-- WhatsApp Direct Founder Button -->
        <a 
          id="mobile-bottom-whatsapp"
          href="https://wa.me/33695413227" 
          target="_blank" 
          rel="noopener noreferrer" 
          class="h-11 w-11 rounded-xl bg-emerald-500/15 hover:bg-emerald-500/25 active:scale-95 text-[#25D366] border border-emerald-500/30 flex items-center justify-center shadow-sm transition-all"
          aria-label="Contacter Robin sur WhatsApp"
        >
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
            <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.664-.698c.969.585 1.961.947 2.796.947 3.179 0 5.765-2.587 5.767-5.766.001-3.18-2.585-5.734-5.767-5.734zm3.375 8.163c-.144.405-.837.774-1.17.824-.311.045-.712.072-2.072-.494-1.637-.682-2.738-2.316-2.822-2.428-.084-.112-.667-.887-.667-1.689 0-.802.42-1.197.57-1.36.15-.163.33-.203.441-.203.11 0 .221.002.318.007.102.006.239-.039.373.285.14.337.478 1.168.52 1.254.042.086.07.187.012.302-.058.115-.088.187-.175.289-.087.102-.183.228-.261.306-.089.088-.182.185-.078.363.104.178.463.765.994 1.238.683.609 1.259.798 1.437.886.178.088.283.078.388-.044.106-.122.455-.53.576-.712.122-.182.244-.153.41-.092.167.061 1.058.499 1.239.59.181.091.303.136.347.213.044.077.044.448-.1 1.053z"/>
          </svg>
        </a>

        <!-- Primary Booking Button -->
        <button 
          onclick="openTourBookingModal()" 
          class="h-11 px-5 rounded-xl bg-gradient-to-r from-emerald-600 to-emerald-500 hover:from-emerald-500 hover:to-emerald-400 active:scale-95 text-white font-black text-xs uppercase tracking-wider shadow-lg shadow-emerald-950/40 border border-emerald-400/30 transition-all flex items-center gap-2 cursor-pointer"
        >
          <span>Réserver</span>
          <svg class="w-4 h-4 text-emerald-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M5 12h14m-7-7 7 7-7 7"/>
          </svg>
        </button>
      </div>
    </div>
  </aside>'''

EN_REPLACEMENT = '''  <!-- LUXE STICKY MOBILE CONVERSION BAR (ELITE 2026 UI/UX) -->
  <aside 
    class="fixed bottom-0 inset-x-0 bg-zinc-950/90 backdrop-blur-xl border-t border-white/10 px-4 pt-3 pb-[max(0.75rem,env(safe-area-inset-bottom))] z-40 lg:hidden shadow-[0_-8px_30px_rgba(0,0,0,0.5)] transition-transform duration-300" 
    aria-label="Quick booking bar"
  >
    <div class="max-w-lg mx-auto flex items-center justify-between gap-3">
      <!-- Price & Availability Status -->
      <div class="min-w-0 flex flex-col justify-center">
        <div class="flex items-center gap-1.5 mb-0.5">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400 truncate">
            Instant Availability
          </span>
        </div>
        <div class="flex items-baseline gap-1">
          <span id="mobile-bottom-price" class="text-xl font-black text-white tracking-tight leading-none">
            50€
          </span>
          <span class="text-[11px] font-semibold text-zinc-400">/ person</span>
        </div>
      </div>

      <!-- Actions (WhatsApp + Direct Booking) -->
      <div class="flex items-center gap-2 shrink-0">
        <!-- WhatsApp Direct Founder Button -->
        <a 
          id="mobile-bottom-whatsapp"
          href="https://wa.me/33695413227" 
          target="_blank" 
          rel="noopener noreferrer" 
          class="h-11 w-11 rounded-xl bg-emerald-500/15 hover:bg-emerald-500/25 active:scale-95 text-[#25D366] border border-emerald-500/30 flex items-center justify-center shadow-sm transition-all"
          aria-label="Chat with Robin on WhatsApp"
        >
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
            <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.664-.698c.969.585 1.961.947 2.796.947 3.179 0 5.765-2.587 5.767-5.766.001-3.18-2.585-5.734-5.767-5.734zm3.375 8.163c-.144.405-.837.774-1.17.824-.311.045-.712.072-2.072-.494-1.637-.682-2.738-2.316-2.822-2.428-.084-.112-.667-.887-.667-1.689 0-.802.42-1.197.57-1.36.15-.163.33-.203.441-.203.11 0 .221.002.318.007.102.006.239-.039.373.285.14.337.478 1.168.52 1.254.042.086.07.187.012.302-.058.115-.088.187-.175.289-.087.102-.183.228-.261.306-.089.088-.182.185-.078.363.104.178.463.765.994 1.238.683.609 1.259.798 1.437.886.178.088.283.078.388-.044.106-.122.455-.53.576-.712.122-.182.244-.153.41-.092.167.061 1.058.499 1.239.59.181.091.303.136.347.213.044.077.044.448-.1 1.053z"/>
          </svg>
        </a>

        <!-- Primary Booking Button -->
        <button 
          onclick="openTourBookingModal()" 
          class="h-11 px-5 rounded-xl bg-gradient-to-r from-emerald-600 to-emerald-500 hover:from-emerald-500 hover:to-emerald-400 active:scale-95 text-white font-black text-xs uppercase tracking-wider shadow-lg shadow-emerald-950/40 border border-emerald-400/30 transition-all flex items-center gap-2 cursor-pointer"
        >
          <span>Book Now</span>
          <svg class="w-4 h-4 text-emerald-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M5 12h14m-7-7 7 7-7 7"/>
          </svg>
        </button>
      </div>
    </div>
  </aside>'''

# Pattern matching the old mobile bottom bar
old_bar_regex = re.compile(r'<div class="fixed bottom-0 inset-x-0 bg-slate-950/95.*?</div>\s*</div>', re.DOTALL)

for fpath in glob.glob('src/pages/**/*.astro', recursive=True):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not old_bar_regex.search(content):
        continue

    # Extract price from original file to maintain exact tour price
    price_match = re.search(r'id="mobile-bottom-price"[^>]*>([^<]+)</span>', content)
    curr_price = price_match.group(1).strip() if price_match else "50€"

    # Extract whatsapp link to keep customized message
    wa_match = re.search(r'id="mobile-bottom-whatsapp"\s+href="([^"]+)"', content)
    curr_wa = wa_match.group(1) if wa_match else "https://wa.me/33695413227"

    is_en = '/en/' in fpath
    repl = EN_REPLACEMENT if is_en else FR_REPLACEMENT

    # Replace price and whatsapp dynamically
    repl_custom = repl.replace('50€', curr_price).replace('https://wa.me/33695413227', curr_wa)

    new_content = old_bar_regex.sub(repl_custom, content)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Upgraded elite mobile bar in {fpath} (Price: {curr_price})")

print("All mobile conversion bars successfully upgraded.")
