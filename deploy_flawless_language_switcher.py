import os
import re

base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'

def get_lang_dropdown_html(rel_path, is_english=False, is_dark_header=False):
    # Determine the corresponding FR and EN URLs
    if is_english:
        # e.g. en/index.html -> fr: ../index.html, en: index.html
        # e.g. en/tours/bardia-explorateur.html -> fr: ../../tours/bardia-explorateur.html, en: bardia-explorateur.html
        if rel_path == 'en/index.html':
            fr_url = '../index.html'
            en_url = 'index.html'
        elif rel_path.startswith('en/destinations/'):
            fname = os.path.basename(rel_path)
            fr_url = f'../../destinations/{fname}'
            en_url = fname
        elif rel_path.startswith('en/tours/'):
            fname = os.path.basename(rel_path)
            fr_url = f'../../tours/{fname}'
            en_url = fname
        else: # e.g. en/a-propos.html
            fname = os.path.basename(rel_path)
            fr_url = f'../{fname}'
            en_url = fname
    else:
        # e.g. index.html -> en: en/index.html, fr: index.html
        # e.g. tours/bardia-explorateur.html -> en: ../en/tours/bardia-explorateur.html, fr: bardia-explorateur.html
        if rel_path == 'index.html':
            fr_url = 'index.html'
            en_url = 'en/index.html'
        elif rel_path.startswith('destinations/'):
            fname = os.path.basename(rel_path)
            fr_url = fname
            en_url = f'../en/destinations/{fname}'
        elif rel_path.startswith('tours/'):
            fname = os.path.basename(rel_path)
            fr_url = fname
            en_url = f'../en/tours/{fname}'
        else:
            fname = os.path.basename(rel_path)
            fr_url = fname
            en_url = f'en/{fname}'

    btn_bg = "bg-white/10 hover:bg-white/20 border-white/20 text-white" if not is_dark_header else "bg-slate-100 hover:bg-slate-200 border-slate-200 text-slate-700"
    icon_color = "text-white" if not is_dark_header else "text-slate-700"

    fr_active = "bg-white/15 text-[#10b981]" if not is_english else "text-slate-300 hover:bg-white/10 hover:text-white"
    en_active = "bg-white/15 text-[#10b981]" if is_english else "text-slate-300 hover:bg-white/10 hover:text-white"
    
    fr_check = '<svg class="w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>' if not is_english else ''
    en_check = '<svg class="w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>' if is_english else ''

    return f"""<!-- LANGUAGE SWITCHER (GLOBE) -->
      <div class="relative group/lang py-1">
        <button onclick="toggleLangMenu(this)" class="w-9 h-9 sm:w-10 sm:h-10 rounded-full {btn_bg} border backdrop-blur-md flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Changer de langue / Change language">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 {icon_color}" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </button>
        <div class="lang-dropdown-box absolute right-0 top-full mt-1.5 w-44 opacity-0 translate-y-2 pointer-events-none group-hover/lang:opacity-100 group-hover/lang:translate-y-0 group-hover/lang:pointer-events-auto transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-1.5 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-0.5 text-xs font-bold text-white">
            <a href="{fr_url}" onclick="setLanguagePref('fr')" class="lang-btn-fr w-full flex items-center justify-between px-3 py-2 rounded-xl {fr_active} transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>
              {fr_check}
            </a>
            <a href="{en_url}" onclick="setLanguagePref('en')" class="lang-btn-en w-full flex items-center justify-between px-3 py-2 rounded-xl {en_active} transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>
              {en_check}
            </a>
          </div>
        </div>
      </div>"""

# Update all pages
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if not f.endswith('.html'):
            continue
        fpath = os.path.join(root, f)
        rel_path = os.path.relpath(fpath, base_dir)
        is_en = rel_path.startswith('en/')
        is_dark = rel_path.startswith('tours/') or rel_path.startswith('en/tours/') or rel_path.startswith('destinations/') or rel_path.startswith('en/destinations/')
        
        with open(fpath, 'r', encoding='utf-8') as file:
            content = file.read()

        lang_block = get_lang_dropdown_html(rel_path, is_english=is_en, is_dark_header=is_dark)

        # Replace existing globe or language switcher
        if '<!-- LANGUAGE SWITCHER (GLOBE) -->' in content:
            content = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', lang_block, content, flags=re.DOTALL)
        elif '<button class="hidden sm:flex items-center text-white/90 hover:text-white p-1" aria-label="Langue">' in content:
            content = content.replace('<button class="hidden sm:flex items-center text-white/90 hover:text-white p-1" aria-label="Langue">\n        <i data-lucide="globe" class="w-5 h-5"></i>\n      </button>', lang_block)
        elif '<button class="hidden sm:flex items-center text-white/90 hover:text-white p-1" aria-label="Language">' in content:
            content = content.replace('<button class="hidden sm:flex items-center text-white/90 hover:text-white p-1" aria-label="Language">\n        <i data-lucide="globe" class="w-5 h-5"></i>\n      </button>', lang_block)
        elif '<i data-lucide="globe"' in content and '<header' in content:
            content = re.sub(r'<button[^>]*aria-label="(?:Langue|Language|Changer de langue)"[^>]*>.*?</button>', lang_block, content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as file:
            file.write(content)

print("Applied language switcher dropdown to all HTML pages!")
