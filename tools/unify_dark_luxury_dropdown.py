import os
import re

def get_dark_dropdown(prefix=""):
    return f"""<div class="relative group py-2">
        <a href="{prefix}destinations/index.html" class="hover:text-[#0e8354] transition-colors flex items-center gap-1.5 cursor-pointer font-bold">
          <span>Destinations</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" /></svg>
        </a>

        <!-- Menu Déroulant Sombre Opaque Élite (Identique à l'accueil) -->
        <div class="absolute top-full left-0 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
          <div class="bg-slate-950/98 backdrop-blur-2xl border border-white/20 rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.6)] space-y-1 text-white">
            
            <a href="{prefix}destinations/bardia.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🐅
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Bardia</p>
                <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
              </div>
            </a>

            <a href="{prefix}destinations/chitwan.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🦏
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Chitwan</p>
                <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
              </div>
            </a>

            <a href="{prefix}destinations/suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🦌
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Suklaphanta</p>
                <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
              </div>
            </a>

            <a href="{prefix}destinations/annapurna.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🏔️
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Les Annapurna & Pokhara</p>
                <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
              </div>
            </a>

            <a href="{prefix}destinations/katmandou.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🕉️
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Katmandou</p>
                <p class="text-[10px] text-slate-400">Vallée des rois & temples sacrés</p>
              </div>
            </a>

            <div class="pt-2 border-t border-white/10 mt-1">
              <a href="{prefix}destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                Voir toutes les destinations →
              </a>
            </div>

          </div>
        </div>
      </div>"""

# 1. Update all 14 tour pages (tours/*.html)
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
dropdown_tour = get_dark_dropdown("../")

for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace any existing dropdown container
    pattern = r'<div class=\"relative group py-2\">\s*<a href=\"(?:\.\./)?destinations/index\.html\".*?<!-- Menu Déroulant.*?</div>\s*</div>\s*</div>'
    c = re.sub(pattern, dropdown_tour, c, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("1. Applied dark luxury dropdown across all 14 tour pages!")

# 2. Update all destination pages (destinations/*.html)
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations'
dropdown_dest = get_dark_dropdown("")
dropdown_dest_hub = f"""<div class="relative group py-2">
        <a href="index.html" class="text-[#0e8354] font-black border-b-2 border-[#0e8354] pb-0.5 flex items-center gap-1.5 cursor-pointer">
          <span>Destinations</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" /></svg>
        </a>

        <!-- Menu Déroulant Sombre Opaque Élite -->
        <div class="absolute top-full left-0 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
          <div class="bg-slate-950/98 backdrop-blur-2xl border border-white/20 rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.6)] space-y-1 text-white">
            
            <a href="bardia.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🐅
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Bardia</p>
                <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
              </div>
            </a>

            <a href="chitwan.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🦏
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Chitwan</p>
                <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
              </div>
            </a>

            <a href="suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🦌
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Suklaphanta</p>
                <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
              </div>
            </a>

            <a href="annapurna.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🏔️
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Les Annapurna & Pokhara</p>
                <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
              </div>
            </a>

            <a href="katmandou.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
              <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                🕉️
              </div>
              <div class="flex-1">
                <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Katmandou</p>
                <p class="text-[10px] text-slate-400">Vallée des rois & temples sacrés</p>
              </div>
            </a>

            <div class="pt-2 border-t border-white/10 mt-1">
              <a href="index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                Voir toutes les destinations →
              </a>
            </div>

          </div>
        </div>
      </div>"""

for fname in os.listdir(dest_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(dest_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    pattern = r'<div class=\"relative group py-2\">\s*<a href=\"(?:index\.html|destinations/index\.html)\".*?<!-- Menu Déroulant.*?</div>\s*</div>\s*</div>'
    target = dropdown_dest_hub if fname == 'index.html' else dropdown_dest
    c = re.sub(pattern, target, c, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("2. Applied dark luxury dropdown across all destination pages!")

# 3. Update contact.html
contact_path = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/contact.html'
with open(contact_path, 'r', encoding='utf-8') as f:
    c = f.read()
pattern = r'<div class=\"relative group py-2\">\s*<a href=\"destinations/index\.html\".*?<!-- Menu Déroulant.*?</div>\s*</div>\s*</div>'
c = re.sub(pattern, get_dark_dropdown(""), c, flags=re.DOTALL)
with open(contact_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("3. Applied dark luxury dropdown across contact.html!")
