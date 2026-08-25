import json
import re
import os

# 1. Update Homepage Buttons
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Enhance Navbar buttons
old_nav_cta = r'<a href="#prochains-departs" class="inline-flex items-center gap-2 bg-gradient-to-r from-fire-600 to-fire-500[^"]*"[^>]*>'
new_nav_cta = '<a href="#prochains-departs" class="group inline-flex items-center gap-2 bg-gradient-to-r from-fire-600 via-fire-500 to-fire-600 bg-[length:200%_auto] hover:bg-right text-white text-xs sm:text-sm font-extrabold px-5 py-2.5 rounded-full shadow-[0_4px_16px_rgba(234,88,12,0.4)] hover:shadow-[0_6px_24px_rgba(234,88,12,0.6)] hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-300 border-t border-white/25">'
html = re.sub(old_nav_cta, new_nav_cta, html)

old_nav_sur_mesure = r'<button onclick="openCustomTripModal\(\)" class="hidden sm:flex items-center gap-1.5 px-4 py-2[^"]*"[^>]*>'
new_nav_sur_mesure = '<button onclick="openCustomTripModal()" class="hidden sm:flex items-center gap-2 px-4 py-2 rounded-full text-xs font-extrabold bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20 hover:border-amber-300/60 text-slate-100 hover:text-amber-200 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200">'
html = re.sub(old_nav_sur_mesure, new_nav_sur_mesure, html)

# Enhance Hero Search Bar Button
old_search_btn = r'<button type="submit" class="w-full lg:w-auto px-8 h-13 py-3.5[^"]*"[^>]*>'
new_search_btn = '<button type="submit" class="w-full lg:w-auto px-8 py-3.5 bg-gradient-to-r from-fire-600 via-fire-500 to-fire-600 bg-[length:200%_auto] hover:bg-right text-white font-black text-sm sm:text-base rounded-full flex items-center justify-center gap-2.5 shadow-[0_6px_20px_rgba(234,88,12,0.45)] hover:shadow-[0_10px_30px_rgba(234,88,12,0.65)] hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-300 border-t border-white/30 whitespace-nowrap">'
html = re.sub(old_search_btn, new_search_btn, html)

# Enhance Category Pills
old_cat_btn = r'class="category-pill([^"]*)"'
def replace_cat_pill(match):
    cls = match.group(1)
    if 'active' in cls:
        return 'class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-jungle-950 text-amber-300 font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-amber-400/40 hover:scale-105 active:scale-95 transition-all duration-200"'
    else:
        return 'class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-800 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200"'

html = re.sub(old_cat_btn, replace_cat_pill, html)

# Enhance Card "Voir le voyage" buttons
old_card_btn = r'<a href="([^"]+)" class="inline-flex items-center gap-2 px-5 py-3 rounded-full bg-gradient-to-r from-fire-600 to-fire-500[^"]*"[^>]*>'
new_card_btn = r'<a href="\1" class="group/btn inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-gradient-to-r from-fire-600 via-fire-500 to-fire-600 bg-[length:200%_auto] hover:bg-right text-white font-extrabold text-xs sm:text-sm shadow-[0_4px_14px_rgba(234,88,12,0.35)] hover:shadow-[0_8px_24px_rgba(234,88,12,0.55)] hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-300 border-t border-white/25 whitespace-nowrap"><span>Voir le voyage</span><i data-lucide="arrow-right" class="w-4 h-4 group-hover/btn:translate-x-1 transition-transform"></i></a>'
html = re.sub(old_card_btn, new_card_btn, html)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Homepage buttons upgraded!")

# 2. Update all 14 Tour Pages Buttons
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Sticky Booking Button
    content = re.sub(
        r'<button onclick="openBookingForm\(\)" class="w-full py-4 rounded-2xl bg-gradient-to-r from-fire-600[^"]*"[^>]*>',
        '<button onclick="openBookingForm()" class="w-full py-4 rounded-2xl bg-gradient-to-r from-fire-600 via-fire-500 to-fire-600 bg-[length:200%_auto] hover:bg-right text-white font-black text-base shadow-[0_8px_25px_rgba(234,88,12,0.45)] hover:shadow-[0_12px_35px_rgba(234,88,12,0.65)] hover:-translate-y-0.5 active:translate-y-0 active:scale-[0.98] transition-all duration-300 border-t border-white/30 text-center tracking-tight">',
        content
    )

    # Nav "Départs & Prix" Button
    content = re.sub(
        r'<button onclick="scrollToBooking\(\)" class="inline-flex items-center gap-2 bg-gradient-to-r from-fire-600[^"]*"[^>]*>',
        '<button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-gradient-to-r from-fire-600 via-fire-500 to-fire-600 bg-[length:200%_auto] hover:bg-right text-white text-xs sm:text-sm font-black px-4 sm:px-5 py-2.5 rounded-full shadow-[0_4px_16px_rgba(234,88,12,0.4)] hover:shadow-[0_6px_24px_rgba(234,88,12,0.6)] hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-300 border-t border-white/25">',
        content
    )

    # Modal Submit Button
    content = re.sub(
        r'<button type="submit" class="w-full py-4 rounded-2xl bg-fire-600[^"]*"[^>]*>',
        '<button type="submit" class="w-full py-4 rounded-2xl bg-gradient-to-r from-fire-600 via-fire-500 to-fire-600 bg-[length:200%_auto] hover:bg-right text-white font-black text-base shadow-[0_8px_25px_rgba(234,88,12,0.45)] hover:shadow-[0_12px_35px_rgba(234,88,12,0.65)] hover:-translate-y-0.5 active:translate-y-0 active:scale-[0.98] transition-all duration-300 border-t border-white/30">',
        content
    )

    # WhatsApp Button
    content = re.sub(
        r'class="flex items-center justify-center gap-2 py-2\.5 rounded-xl bg-emerald-50 text-emerald-900 font-bold hover:bg-emerald-100 transition-colors"',
        'class="flex items-center justify-center gap-2 py-3 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-md shadow-emerald-600/30 hover:shadow-lg hover:shadow-emerald-600/45 hover:-translate-y-0.5 active:translate-y-0 transition-all"',
        content
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("All 14 tour pages buttons upgraded successfully!")
