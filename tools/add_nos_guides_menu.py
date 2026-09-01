import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# 1. Update src/components/Footer.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Footer.astro', 'r', encoding='utf-8') as f:
    fc = f.read()

# Add "Nos guides" link into Navigation column in Footer
fc = fc.replace(
    '<li><a href="/index.html#galerie-faune" class="hover:text-slate-200 transition-colors">Galerie</a></li>',
    '<li><a href="/index.html#concept" class="hover:text-slate-200 transition-colors">Nos guides</a></li>\n          <li><a href="/index.html#galerie-faune" class="hover:text-slate-200 transition-colors">Galerie</a></li>'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Footer.astro', 'w', encoding='utf-8') as f:
    f.write(fc)

# 2. Update Header & Mobile Drawers & Footers across all .astro pages
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Desktop Header Navigation: Insert "Nos guides" before "Galerie" (or right after Destinations)
    # Index.astro header:
    if 'index.astro' in fpath:
        c = c.replace(
            '<a href="#galerie-faune" class="hover:text-amber-100 transition-colors">Galerie</a>',
            '<a href="#concept" class="hover:text-amber-100 transition-colors">Nos guides</a>\n      <a href="#galerie-faune" class="hover:text-amber-100 transition-colors">Galerie</a>'
        )
    else:
        c = c.replace(
            '<a href="/index.html#galerie-faune"',
            '<a href="/index.html#concept" class="hover:text-amber-100 transition-colors whitespace-nowrap">Nos guides</a>\n      <a href="/index.html#galerie-faune"'
        )
        c = c.replace(
            '<a href="/index.html#concept" class="hover:text-amber-100 transition-colors whitespace-nowrap">Nos guides</a>\n      <a href="/index.html#galerie-faune" class="hover:text-[#0e8354]',
            '<a href="/index.html#concept" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Nos guides</a>\n          <a href="/index.html#galerie-faune" class="hover:text-[#0e8354]'
        )

    # Mobile Drawer:
    mobile_guide = """      <!-- Nos guides -->
      <a href="/index.html#concept" onclick="toggleMobileMenu()" class="flex items-center gap-3 p-3 rounded-2xl hover:bg-white/10 text-white font-extrabold text-sm transition-colors group/item">
        <div class="w-8 h-8 rounded-xl bg-white/10 text-slate-200 flex items-center justify-center group-hover/item:bg-[#0e8354] group-hover/item:text-white transition-colors">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M22 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
        </div>
        <span>Nos guides</span>
      </a>"""

    if '<!-- Galerie -->' in c and '<!-- Nos guides -->' not in c:
        c = c.replace('<!-- Galerie -->', mobile_guide + '\n      <!-- Galerie -->')

    # Footer navigation column:
    c = c.replace(
        '<li><a href="/index.html#galerie-faune" class="hover:text-slate-200 transition-colors">Galerie</a></li>',
        '<li><a href="/index.html#concept" class="hover:text-slate-200 transition-colors">Nos guides</a></li>\n          <li><a href="/index.html#galerie-faune" class="hover:text-slate-200 transition-colors">Galerie</a></li>'
    )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Added 'Nos guides' in {fpath.split('/')[-1]}")

print("Done adding 'Nos guides' to Header and Footer across all pages!")
