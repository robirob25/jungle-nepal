import re, glob, os

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours/*.html') + \
             glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/tours/*.html')

LINK_CLASS = 'hover:text-[#0e8354] transition-colors pb-1.5 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap'

FR_LINKS = [
    ('#apercu',        'Aperçu'),
    ('#pour-moi',      'Profil Voyage'),
    ('#programme',     'Itinéraire détaillé'),
    ('#inclusions',    'Inclus &amp; Extras'),
    ('#avis-voyageurs','Avis'),
    ('#faq',           'FAQ'),
]

EN_LINKS = [
    ('#apercu',        'Overview'),
    ('#pour-moi',      'Trip Profile'),
    ('#programme',     'Detailed Itinerary'),
    ('#inclusions',    'Included &amp; Extras'),
    ('#avis-voyageurs','Reviews'),
    ('#faq',           'FAQ'),
]

def build_subnav(is_en):
    links = EN_LINKS if is_en else FR_LINKS
    link_html = '\n'.join(
        f'        <a href="{href}" class="{LINK_CLASS}">{label}</a>'
        for href, label in links
    )
    return (
        '\n  <!-- STICKY SUB-NAV WEROAD -->\n'
        '  <nav class="w-full sticky top-[68px] sm:top-[76px] z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm" aria-label="Navigation sections">\n'
        '    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 sm:py-5">\n'
        '      <div class="flex items-center gap-6 sm:gap-8 lg:gap-12 overflow-x-auto no-scrollbar text-sm font-bold text-slate-600">\n'
        + link_html + '\n'
        '      </div>\n'
        '    </div>\n'
        '  </nav>\n'
    )

for fpath in tour_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    is_en = '/en/' in fpath

    # Step 1: Remove old subnav block from inside <main>
    c_new = re.sub(
        r'[ \t]*<!-- STICKY SUB-NAV WEROAD -->.*?</div>[ \t]*\n[ \t]*\n[ \t]*<!-- 2-COLUMN MAIN CONTENT GRID -->',
        '\n    <!-- 2-COLUMN MAIN CONTENT GRID -->',
        c,
        flags=re.DOTALL
    )

    if c_new == c:
        print(f"  WARN no subnav-in-main found: {os.path.basename(fpath)}")
        continue

    # Step 2: Insert new standalone subnav between </header> and <main>
    new_subnav = build_subnav(is_en)

    # Try inserting after </header> before <!-- MAIN TOUR CONTENT -->
    c_new2 = re.sub(
        r'(</header>)([ \t]*\n[ \t]*\n[ \t]*<!-- MAIN TOUR CONTENT[^\n]*\n[ \t]*<main)',
        r'\1' + new_subnav + r'  <!-- MAIN TOUR CONTENT AREA -->\n  <main',
        c_new,
        count=1
    )

    if c_new2 == c_new:
        # Fallback: insert after </header> before <main>
        c_new2 = re.sub(
            r'(</header>)([ \t]*\n[ \t]*\n[ \t]*<main)',
            r'\1' + new_subnav + r'  <main',
            c_new,
            count=1
        )

    if c_new2 == c_new:
        print(f"  WARN could not insert subnav: {os.path.basename(fpath)}")
        continue

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c_new2)
    print(f"  OK: {os.path.basename(fpath)}")

print("Done.")
