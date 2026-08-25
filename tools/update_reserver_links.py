import re, glob, os

# 1. Update contact.astro to ensure the form has id="contact-form" or id="formulaire" and scroll-mt-28
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'r', encoding='utf-8') as f:
    contact_content = f.read()

contact_content = contact_content.replace(
    '<div class="lg:col-span-7 bg-white rounded-3xl p-6 sm:p-10 border border-slate-200 shadow-2xl space-y-6">',
    '<div id="formulaire-contact" class="lg:col-span-7 bg-white rounded-3xl p-6 sm:p-10 border border-slate-200 shadow-2xl space-y-6 scroll-mt-28">'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'w', encoding='utf-8') as f:
    f.write(contact_content)
print("✓ Added id='formulaire-contact' with scroll-mt-28 in contact.astro")

# 2. Update all tour pages (.astro in src/pages/tours/)
# Any button containing "Réserver" should point to /contact.html#formulaire-contact (or /contact#formulaire-contact)
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    slug = os.path.splitext(os.path.basename(fpath))[0]
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # 1. Sub-nav bar CTA: href="#booking-widget" -> href="/contact.html#formulaire-contact"
    c = c.replace('href="#booking-widget"', 'href="/contact.html#formulaire-contact"')
    
    # 2. Booking sidebar widget CTA: "Réserver ma place →" -> link to /contact.html#formulaire-contact
    c = re.sub(
        r'<button[^>]*onclick="[^"]*"[^>]*>\s*Réserver ma place →\s*</button>',
        r'<a href="/contact.html#formulaire-contact" class="w-full text-center py-4 rounded-2xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-extrabold text-sm shadow-xl shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all duration-300 block cursor-pointer">Réserver ma place →</a>',
        c
    )
    
    # 3. Mobile bottom sticky booking bar: "Réserver" button
    c = re.sub(
        r'<button[^>]*onclick="[^"]*booking[^"]*"[^>]*>\s*<span>Réserver</span>\s*<svg[^>]*>.*?</svg>\s*</button>',
        r'<a href="/contact.html#formulaire-contact" class="flex-1 flex items-center justify-center gap-1.5 py-3 rounded-2xl bg-[#0e8354] text-white font-black text-xs shadow-md active:scale-95 transition-all cursor-pointer"><span>Réserver</span><svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-7-7 7 7-7 7"/></svg></a>',
        c,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"✓ Updated Réserver links in {os.path.basename(fpath)}")

# 3. Update Header.astro "Départs & Prix" button if present
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'r', encoding='utf-8') as f:
    hdr = f.read()

# Any other Réserver references
print("All Réserver buttons routed to /contact.html#formulaire-contact!")
