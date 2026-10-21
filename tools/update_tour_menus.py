import os
import glob

FR_DESKTOP_TARGET = '<a href="/#prochains-departs" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Circuits & voyages</a>'
FR_DESKTOP_REPL = '<a href="/safari-nepal/" class="text-[#0e8354] hover:text-[#0b6842] font-bold transition-colors whitespace-nowrap">Safari au Népal</a>\n          <a href="/#prochains-departs" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Circuits & voyages</a>'

FR_DROPDOWN_TARGET = '<a href="/destinations/bardia" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">'
FR_DROPDOWN_REPL = '''<a href="/safari-nepal/" class="flex items-center gap-3 p-2.5 rounded-xl bg-emerald-900/40 hover:bg-emerald-900/70 border border-emerald-500/30 transition-colors group/item">
                  <div class="flex-1">
                    <p class="font-extrabold text-xs text-amber-300 group-hover/item:text-amber-200 transition-colors">🐾 Safari au Népal (Grand Guide)</p>
                    <p class="text-[10px] text-emerald-200/80">Bardia, Chitwan, tigres & circuits</p>
                  </div>
                </a>
                <a href="/destinations/bardia" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">'''

FR_MOBILE_TARGET = '<a href="/#prochains-departs" onclick="toggleMobileMenu()"'
FR_MOBILE_REPL = '''<a href="/safari-nepal/" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl bg-emerald-900/30 border border-emerald-500/30 flex items-center justify-between text-emerald-300 hover:text-white hover:bg-emerald-800/40 font-bold transition-colors">
        <span class="flex items-center gap-2.5"><span>🐾 Safari au Népal (Grand Guide)</span></span>
        <span class="text-[10px] uppercase tracking-wider bg-emerald-700/60 text-emerald-100 px-2 py-0.5 rounded-full font-semibold">Top</span>
      </a>
      <a href="/#prochains-departs" onclick="toggleMobileMenu()"'''

FR_MOBILE_SUB_TARGET = '<div id="mobile-dest-sub" class="hidden px-2 pb-2.5 space-y-1 border-t border-white/5 pt-2">\n          <a href="/destinations/bardia"'
FR_MOBILE_SUB_REPL = '''<div id="mobile-dest-sub" class="hidden px-2 pb-2.5 space-y-1 border-t border-white/5 pt-2">
          <a href="/safari-nepal/" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl bg-emerald-950/50 text-xs text-amber-300 hover:text-amber-200 transition-colors">
            <div><p class="font-bold text-amber-300">🐾 Safari au Népal (Grand Guide)</p><p class="text-[10px] text-emerald-300">Bardia, Chitwan, tigres & safaris</p></div>
          </a>
          <a href="/destinations/bardia"'''


EN_DESKTOP_TARGET = '<a href="/en/#prochains-departs" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Tours & expeditions</a>'
EN_DESKTOP_REPL = '<a href="/en/safari-nepal/" class="text-[#0e8354] hover:text-[#0b6842] font-bold transition-colors whitespace-nowrap">Nepal Safari</a>\n          <a href="/en/#prochains-departs" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Tours & expeditions</a>'

EN_DROPDOWN_TARGET = '<a href="/en/destinations/bardia" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">'
EN_DROPDOWN_REPL = '''<a href="/en/safari-nepal/" class="flex items-center gap-3 p-2.5 rounded-xl bg-emerald-900/40 hover:bg-emerald-900/70 border border-emerald-500/30 transition-colors group/item">
                  <div class="flex-1">
                    <p class="font-extrabold text-xs text-amber-300 group-hover/item:text-amber-200 transition-colors">🐾 Nepal Safari (Master Guide)</p>
                    <p class="text-[10px] text-emerald-200/80">Bardia, Chitwan, Tigers & Safaris</p>
                  </div>
                </a>
                <a href="/en/destinations/bardia" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item">'''

EN_MOBILE_TARGET = '<a href="/en/#prochains-departs" onclick="toggleMobileMenu()"'
EN_MOBILE_REPL = '''<a href="/en/safari-nepal/" onclick="toggleMobileMenu()" class="px-3.5 py-2.5 rounded-2xl bg-emerald-900/30 border border-emerald-500/30 flex items-center justify-between text-emerald-300 hover:text-white hover:bg-emerald-800/40 font-bold transition-colors">
        <span class="flex items-center gap-2.5"><span>🐾 Nepal Safari (Master Guide)</span></span>
        <span class="text-[10px] uppercase tracking-wider bg-emerald-700/60 text-emerald-100 px-2 py-0.5 rounded-full font-semibold">Top</span>
      </a>
      <a href="/en/#prochains-departs" onclick="toggleMobileMenu()"'''

EN_MOBILE_SUB_TARGET = '<div id="mobile-dest-sub" class="hidden px-2 pb-2.5 space-y-1 border-t border-white/5 pt-2">\n          <a href="/en/destinations/bardia"'
EN_MOBILE_SUB_REPL = '''<div id="mobile-dest-sub" class="hidden px-2 pb-2.5 space-y-1 border-t border-white/5 pt-2">
          <a href="/en/safari-nepal/" onclick="toggleMobileMenu()" class="flex items-center gap-2.5 p-2 rounded-xl bg-emerald-950/50 text-xs text-amber-300 hover:text-amber-200 transition-colors">
            <div><p class="font-bold text-amber-300">🐾 Nepal Safari (Master Guide)</p><p class="text-[10px] text-emerald-300">Bardia, Chitwan, Tigers & Safaris</p></div>
          </a>
          <a href="/en/destinations/bardia"'''

def process_file(filepath, is_en=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Don't re-add if already present in header nav
    if (is_en and '/en/safari-nepal/' in content[:20000]) or (not is_en and '/safari-nepal/' in content[:20000]):
        # check if it is already in the nav
        if ('<a href="/safari-nepal/"' in content) or ('<a href="/en/safari-nepal/"' in content):
            return False

    orig = content
    if not is_en:
        if FR_DESKTOP_TARGET in content:
            content = content.replace(FR_DESKTOP_TARGET, FR_DESKTOP_REPL, 1)
        if FR_DROPDOWN_TARGET in content:
            content = content.replace(FR_DROPDOWN_TARGET, FR_DROPDOWN_REPL, 1)
        if FR_MOBILE_TARGET in content:
            content = content.replace(FR_MOBILE_TARGET, FR_MOBILE_REPL, 1)
        if FR_MOBILE_SUB_TARGET in content:
            content = content.replace(FR_MOBILE_SUB_TARGET, FR_MOBILE_SUB_REPL, 1)
    else:
        if EN_DESKTOP_TARGET in content:
            content = content.replace(EN_DESKTOP_TARGET, EN_DESKTOP_REPL, 1)
        if EN_DROPDOWN_TARGET in content:
            content = content.replace(EN_DROPDOWN_TARGET, EN_DROPDOWN_REPL, 1)
        if EN_MOBILE_TARGET in content:
            content = content.replace(EN_MOBILE_TARGET, EN_MOBILE_REPL, 1)
        if EN_MOBILE_SUB_TARGET in content:
            content = content.replace(EN_MOBILE_SUB_TARGET, EN_MOBILE_SUB_REPL, 1)

    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

fr_files = glob.glob('src/pages/tours/*.astro')
en_files = glob.glob('src/pages/en/tours/*.astro')

updated_fr = sum(1 for f in fr_files if process_file(f, is_en=False))
updated_en = sum(1 for f in en_files if process_file(f, is_en=True))

print(f"Updated {updated_fr}/{len(fr_files)} FR tour files, {updated_en}/{len(en_files)} EN tour files.")
