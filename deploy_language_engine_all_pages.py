import os
import re

globe_hero_dark = """      <!-- INTERACTIVE LANGUAGE SWITCHER (GLOBE) -->
      <div class="relative group/lang py-1">
        <button onclick="this.parentElement.querySelector('#lang-menu-dark').classList.toggle('opacity-100'); this.parentElement.querySelector('#lang-menu-dark').classList.toggle('pointer-events-auto');" class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 backdrop-blur-md flex items-center justify-center text-white transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Changer de langue / Change language">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </button>
        <div id="lang-menu-dark" class="absolute right-0 top-full mt-1.5 w-44 opacity-0 translate-y-2 pointer-events-none group-hover/lang:opacity-100 group-hover/lang:translate-y-0 group-hover/lang:pointer-events-auto transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-1.5 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-0.5 text-xs font-bold text-white">
            <button onclick="setSiteLanguage('fr')" class="lang-btn-fr w-full flex items-center justify-between px-3 py-2 rounded-xl bg-white/15 text-[#10b981] hover:bg-white/10 transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>
              <svg class="lang-check-fr w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </button>
            <button onclick="setSiteLanguage('en')" class="lang-btn-en w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>
              <svg class="lang-check-en hidden w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </button>
          </div>
        </div>
      </div>"""

globe_light_header = """      <!-- INTERACTIVE LANGUAGE SWITCHER (GLOBE) -->
      <div class="relative group/lang py-1">
        <button onclick="this.parentElement.querySelector('#lang-menu-light').classList.toggle('opacity-100'); this.parentElement.querySelector('#lang-menu-light').classList.toggle('pointer-events-auto');" class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 flex items-center justify-center text-slate-700 transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Changer de langue / Change language">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-slate-700" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </button>
        <div id="lang-menu-light" class="absolute right-0 top-full mt-1.5 w-44 opacity-0 translate-y-2 pointer-events-none group-hover/lang:opacity-100 group-hover/lang:translate-y-0 group-hover/lang:pointer-events-auto transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-1.5 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-0.5 text-xs font-bold text-white">
            <button onclick="setSiteLanguage('fr')" class="lang-btn-fr w-full flex items-center justify-between px-3 py-2 rounded-xl bg-white/15 text-[#10b981] hover:bg-white/10 transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>
              <svg class="lang-check-fr w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </button>
            <button onclick="setSiteLanguage('en')" class="lang-btn-en w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
              <span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>
              <svg class="lang-check-en hidden w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </button>
          </div>
        </div>
      </div>"""

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any old static globe button with globe_hero_dark
old_globe_pattern = r'<button class=\"w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10.*?<\/button>'
if re.search(old_globe_pattern, html, flags=re.DOTALL):
    html = re.sub(old_globe_pattern, globe_hero_dark, html, flags=re.DOTALL)
elif '<!-- INTERACTIVE LANGUAGE SWITCHER' not in html:
    html = html.replace('<span>WhatsApp Direct</span>\n        </a>', f'{globe_hero_dark}\n        <span>WhatsApp Direct</span>\n        </a>')

# Add translator script before </body>
if 'translator.js' not in html:
    html = html.replace('</body>', '  <script src="assets/js/translator.js"></script>\n</body>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("1. Injected translation engine into index.html!")

# 2. Update a-propos.html & contact.html
for fname in ['a-propos.html', 'contact.html']:
    fpath = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal', fname)
    if not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if '<!-- INTERACTIVE LANGUAGE SWITCHER' not in c:
        c = c.replace('<a href="https://wa.me/33695413227"', f'{globe_hero_dark}\n        <a href="https://wa.me/33695413227"')
    if 'translator.js' not in c:
        c = c.replace('</body>', '  <script src="assets/js/translator.js"></script>\n</body>')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
print("2. Injected translation engine into a-propos.html & contact.html!")

# 3. Update all destination pages (destinations/*.html)
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations'
for fname in os.listdir(dest_dir):
    if not fname.endswith('.html'): continue
    fpath = os.path.join(dest_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if '<!-- INTERACTIVE LANGUAGE SWITCHER' not in c:
        c = c.replace('<a href="https://wa.me/33695413227"', f'{globe_hero_dark}\n        <a href="https://wa.me/33695413227"')
    if 'translator.js' not in c:
        c = c.replace('</body>', '  <script src="../assets/js/translator.js"></script>\n</body>')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
print("3. Injected translation engine into all destination pages!")

# 4. Update all 14 tour pages (tours/*.html)
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'): continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if '<!-- INTERACTIVE LANGUAGE SWITCHER' not in c:
        c = c.replace('<button onclick="scrollToBooking()"', f'{globe_light_header}\n        <button onclick="scrollToBooking()"')
    if 'translator.js' not in c:
        c = c.replace('</body>', '  <script src="../assets/js/translator.js"></script>\n</body>')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
print("4. Injected translation engine into all 14 tour pages!")

