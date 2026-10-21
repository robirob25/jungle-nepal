import re
import glob

def standardize_fr_tour(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Desktop Nav: place Safari au Népal between Activités and Destinations
    # First remove any Safari au Népal before circuits
    c = re.sub(
        r'<a href="/safari-nepal/" class="[^"]*">Safari au Népal</a>\s*',
        '',
        c
    )

    # Insert Safari au Népal between Activités and Destinations if not already there
    # Check if Activités is followed by Destinations
    fr_desktop_search = r'(<a href="/#activites" class="hover:text-\[#0e8354\] transition-colors whitespace-nowrap">Activités</a>)'
    fr_desktop_replace = r'\1\n          <a href="/safari-nepal/" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Safari au Népal</a>'
    if '/safari-nepal/' not in c[c.find('<nav class="hidden lg:flex'):c.find('<!-- Destinations Dropdown -->')]:
        c = re.sub(fr_desktop_search, fr_desktop_replace, c, count=1)

    # 2. Dropdown link: remove emojis and green border, clean format
    old_dropdown_fr = re.compile(
        r'<a href="/safari-nepal/" class="flex items-center gap-3 p-2\.5 rounded-xl bg-emerald-900/40 hover:bg-emerald-900/70 border border-emerald-500/30 transition-colors group/item">\s*<div class="flex-1">\s*<p class="font-extrabold text-xs text-amber-300 group-hover/item:text-amber-200 transition-colors">🐾 Safari au Népal \(Grand Guide\)</p>\s*<p class="text-\[10px\] text-emerald-200/80">Bardia, Chitwan, tigres & circuits</p>\s*</div>\s*</a>',
        re.DOTALL
    )
    new_dropdown_fr = '''<a href="/safari-nepal/" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                  <div class="flex-1">
                    <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Safari au Népal</p>
                    <p class="text-[10px] text-slate-400">Bardia, Chitwan, tigres & circuits</p>
                  </div>
                </a>'''
    c = old_dropdown_fr.sub(new_dropdown_fr, c)

    # 3. Mobile top button: remove old Top button before circuits
    old_mobile_top_fr = re.compile(
        r'<a href="/safari-nepal/" onclick="toggleMobileMenu\(\)" class="px-3\.5 py-2\.5 rounded-2xl bg-emerald-900/30 border border-emerald-500/30 flex items-center justify-between text-emerald-300 hover:text-white hover:bg-emerald-800/40 font-bold transition-colors">\s*<span class="flex items-center gap-2\.5"><span>🐾 Safari au Népal \(Grand Guide\)</span></span>\s*<span class="text-\[10px\] uppercase tracking-wider bg-emerald-700/60 text-emerald-100 px-2 py-0\.5 rounded-full font-semibold">Top</span>\s*</a>\s*',
        re.DOTALL
    )
    c = old_mobile_top_fr.sub('', c)

    # Insert Safari au Népal between Activités and Destinations accordion
    old_mobile_act_fr = re.compile(
        r'(<!-- Activités -->\s*<a href="/#activites" onclick="toggleMobileMenu\(\)"[^>]*>.*?</a>\s*)'
        r'(\s*<!-- 2\. Destinations Dropdown Accordion -->|\s*<div class="rounded-2xl bg-white/5 overflow-hidden">)',
        re.DOTALL
    )
    if '<span>Safari au Népal</span>' not in c:
        def insert_mobile_safari_fr(m):
            act_part = m.group(1)
            dest_part = m.group(2)
            safari_link = '''\n      <a href="/safari-nepal/" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl bg-white/5 hover:bg-white/10 flex items-center justify-between text-white transition-colors">
        <span>Safari au Népal</span>
      </a>\n'''
            return act_part + safari_link + dest_part
        c = old_mobile_act_fr.sub(insert_mobile_safari_fr, c, count=1)

    # 4. Mobile sub-destinations: clean up link
    old_mobile_sub_fr = re.compile(
        r'<a href="/safari-nepal/" onclick="toggleMobileMenu\(\)" class="flex items-center gap-2\.5 p-2 rounded-xl bg-emerald-950/50 text-xs text-amber-300 hover:text-amber-200 transition-colors">\s*<div><p class="font-bold text-amber-300">🐾 Safari au Népal \(Grand Guide\)</p><p class="text-\[10px\] text-emerald-300">Bardia, Chitwan, tigres & safaris</p></div>\s*</a>',
        re.DOTALL
    )
    new_mobile_sub_fr = '''<a href="/safari-nepal/" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <div><p class="font-bold text-white">Safari au Népal</p><p class="text-[10px] text-slate-400">Bardia, Chitwan, tigres & safaris</p></div>
          </a>'''
    c = old_mobile_sub_fr.sub(new_mobile_sub_fr, c)

    if c != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        return True
    return False


def standardize_en_tour(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Desktop Nav: place Nepal Safari between Activities and Destinations
    # First remove any Nepal Safari before tours
    c = re.sub(
        r'<a href="/en/safari-nepal/" class="[^"]*">Nepal Safari</a>\s*',
        '',
        c
    )

    # Insert Nepal Safari between Activities and Destinations if not already there
    en_desktop_search = r'(<a href="/en/#activites" class="hover:text-\[#0e8354\] transition-colors whitespace-nowrap">Activities</a>)'
    en_desktop_replace = r'\1\n          <a href="/en/safari-nepal/" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Nepal Safari</a>'
    if '/en/safari-nepal/' not in c[c.find('<nav class="hidden lg:flex'):c.find('<!-- Destinations Dropdown -->')]:
        c = re.sub(en_desktop_search, en_desktop_replace, c, count=1)

    # 2. Dropdown link: remove emojis and green border, clean format
    old_dropdown_en = re.compile(
        r'<a href="/en/safari-nepal/" class="flex items-center gap-3 p-2\.5 rounded-xl bg-emerald-900/40 hover:bg-emerald-900/70 border border-emerald-500/30 transition-colors group/item">\s*<div class="flex-1">\s*<p class="font-extrabold text-xs text-amber-300 group-hover/item:text-amber-200 transition-colors">🐾 Nepal Safari \(Master Guide\)</p>\s*<p class="text-\[10px\] text-emerald-200/80">Bardia, Chitwan, Tigers & Safaris</p>\s*</div>\s*</a>',
        re.DOTALL
    )
    new_dropdown_en = '''<a href="/en/safari-nepal/" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">
                  <div class="flex-1">
                    <p class="font-extrabold text-xs text-white group-hover/item:text-amber-100 transition-colors">Safari in Nepal</p>
                    <p class="text-[10px] text-slate-400">Bardia, Chitwan, Tigers & Safaris</p>
                  </div>
                </a>'''
    c = old_dropdown_en.sub(new_dropdown_en, c)

    # 3. Mobile top button: remove old Top button before tours
    old_mobile_top_en = re.compile(
        r'<a href="/en/safari-nepal/" onclick="toggleMobileMenu\(\)" class="px-3\.5 py-2\.5 rounded-2xl bg-emerald-900/30 border border-emerald-500/30 flex items-center justify-between text-emerald-300 hover:text-white hover:bg-emerald-800/40 font-bold transition-colors">\s*<span class="flex items-center gap-2\.5"><span>🐾 Nepal Safari \(Master Guide\)</span></span>\s*<span class="text-\[10px\] uppercase tracking-wider bg-emerald-700/60 text-emerald-100 px-2 py-0\.5 rounded-full font-semibold">Top</span>\s*</a>\s*',
        re.DOTALL
    )
    c = old_mobile_top_en.sub('', c)

    # Insert Nepal Safari between Activities and Destinations accordion
    old_mobile_act_en = re.compile(
        r'(<!-- Activit[eé]s -->\s*<a href="/en/#activites" onclick="toggleMobileMenu\(\)"[^>]*>.*?</a>\s*)'
        r'(\s*<!-- 2\. Destinations Dropdown Accordion -->|\s*<div class="rounded-2xl bg-white/5 overflow-hidden">)',
        re.DOTALL
    )
    if '<span>Nepal Safari</span>' not in c:
        def insert_mobile_safari_en(m):
            act_part = m.group(1)
            dest_part = m.group(2)
            safari_link = '''\n      <a href="/en/safari-nepal/" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl bg-white/5 hover:bg-white/10 flex items-center justify-between text-white transition-colors">
        <span>Nepal Safari</span>
      </a>\n'''
            return act_part + safari_link + dest_part
        c = old_mobile_act_en.sub(insert_mobile_safari_en, c, count=1)

    # 4. Mobile sub-destinations: clean up link
    old_mobile_sub_en = re.compile(
        r'<a href="/en/safari-nepal/" onclick="toggleMobileMenu\(\)" class="flex items-center gap-2\.5 p-2 rounded-xl bg-emerald-950/50 text-xs text-amber-300 hover:text-amber-200 transition-colors">\s*<div><p class="font-bold text-amber-300">🐾 Nepal Safari \(Master Guide\)</p><p class="text-\[10px\] text-emerald-300">Bardia, Chitwan, Tigers & Safaris</p></div>\s*</a>',
        re.DOTALL
    )
    new_mobile_sub_en = '''<a href="/en/safari-nepal/" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl hover:bg-white/10 text-xs text-slate-300 hover:text-white transition-colors">
            <div><p class="font-bold text-white">Safari in Nepal</p><p class="text-[10px] text-slate-400">Bardia, Chitwan, Tigers & Safaris</p></div>
          </a>'''
    c = old_mobile_sub_en.sub(new_mobile_sub_en, c)

    if c != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        return True
    return False

if __name__ == '__main__':
    fr_files = sorted(glob.glob('src/pages/tours/*.astro'))
    en_files = sorted(glob.glob('src/pages/en/tours/*.astro'))

    up_fr = sum(1 for f in fr_files if standardize_fr_tour(f))
    up_en = sum(1 for f in en_files if standardize_en_tour(f))

    print(f"Updated {up_fr}/{len(fr_files)} FR tours, {up_en}/{len(en_files)} EN tours.")
