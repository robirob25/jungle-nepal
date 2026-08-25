import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

print(f"Standardizing buttons across {len(astro_files)} files...")

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Standardize cursor-pointer on ALL <button> tags
    c = re.sub(r'<button\s+(?!.*cursor-pointer)([^>]*?)class=[\'"]([^\'"]*?)[\'"]', r'<button \1class="\2 cursor-pointer"', c)

    # 2. Standardize Header 'Départs & Prix' / 'WhatsApp Direct' buttons with 2026 physics spring interaction
    c = re.sub(
        r'class=[\'"][^\'"]*bg-gradient-to-r\s+from-\[#0e8354\][^\'"]*Départs & Prix[^\'"]*[\'"]',
        'class="inline-flex items-center gap-2 bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white text-xs sm:text-[13px] font-black px-4 py-2 sm:px-5 sm:py-2.5 rounded-full shadow-md shadow-[#0e8354]/25 hover:shadow-lg hover:shadow-[#0e8354]/40 hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-200 whitespace-nowrap cursor-pointer select-none"',
        c
    )

    # 3. Standardize Primary Booking CTA 'Réserver ma place →' in sticky widget
    c = re.sub(
        r'<button\s+onclick=[\'"]openBookingForm\(\)[\'"]\s+class=[\'"][^\'"]*[\'"]>',
        '<button onclick="openBookingForm()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white font-black text-sm shadow-lg shadow-[#0e8354]/30 hover:shadow-xl hover:shadow-[#0e8354]/45 hover:-translate-y-0.5 active:translate-y-0 active:scale-[0.98] transition-all duration-200 border-t border-white/20 text-center tracking-tight cursor-pointer select-none focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0e8354] focus-visible:ring-offset-2">',
        c
    )

    # 4. Standardize Secondary 'WhatsApp' & 'Carnet PDF' buttons in sticky widget
    c = re.sub(
        r'<a\s+href=[\'"]https://wa\.me/33695413227[^\'"]*[\'"]\s+target=[\'"]_blank[\'"]\s+rel=[\'"]noopener noreferrer[\'"]\s+class=[\'"][^\'"]*bg-emerald-50[^\'"]*[\'"]',
        '<a href="https://wa.me/33695413227" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-2xl bg-emerald-50/90 hover:bg-emerald-100 text-[#0e8354] font-bold text-xs border border-emerald-200/80 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-200 cursor-pointer select-none whitespace-nowrap"',
        c
    )
    c = re.sub(
        r'<button\s+onclick=[\'"]openPdfModal\(\)[\'"]\s+class=[\'"][^\'"]*bg-slate-100[^\'"]*[\'"]',
        '<button onclick="openPdfModal()" class="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-2xl bg-slate-100 hover:bg-slate-200/90 text-slate-700 font-bold text-xs border border-slate-200/80 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-200 cursor-pointer select-none whitespace-nowrap"',
        c
    )

    # 5. Standardize 'Voir toutes les photos' floating pill
    c = re.sub(
        r'class=[\'"][^\'"]*Voir toutes les photos[^\'"]*[\'"]',
        'class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-extrabold text-xs sm:text-sm px-4 py-2.5 rounded-2xl shadow-lg border border-slate-200/90 flex items-center gap-2 hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-200 cursor-pointer select-none"',
        c
    )

    # 6. Standardize Trip card 'Voir le séjour →' buttons
    c = re.sub(
        r'class=[\'"][^\'"]*inline-flex items-center justify-center gap-1\.5 px-5 py-2\.5 rounded-full bg-\[#0e8354\][^\'"]*[\'"]',
        'class="inline-flex items-center justify-center gap-1.5 px-5 py-2.5 rounded-2xl bg-gradient-to-r from-[#0e8354] to-[#109363] text-white font-extrabold text-xs shadow-md shadow-[#0e8354]/25 hover:shadow-lg hover:shadow-[#0e8354]/40 hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-200 whitespace-nowrap cursor-pointer select-none"',
        c
    )

    # 7. Standardize WhatsApp floating button in bottom right
    c = re.sub(
        r'class=[\'"][^\'"]*fixed bottom-6 right-6[^\'"]*[\'"]',
        'class="fixed bottom-6 right-6 z-40 bg-gradient-to-tr from-[#0e8354] to-[#10b981] hover:from-[#0c6d46] hover:to-[#059669] text-white p-3.5 sm:p-4 rounded-2xl shadow-[0_10px_30px_rgba(16,185,129,0.4)] hover:shadow-[0_14px_40px_rgba(16,185,129,0.6)] hover:-translate-y-1 active:translate-y-0 active:scale-90 transition-all duration-300 flex items-center justify-center cursor-pointer select-none group"',
        c
    )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Successfully standardized buttons across {updated} files with unified 2026 design norms!")
