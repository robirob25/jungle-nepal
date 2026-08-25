import os
import re

dark_green_share_fr = """        <!-- Dropdown Menu Partage Sombre Opaque (Même vert #041d13 que Destinations) -->
        <div id="share-menu" class="absolute right-0 top-full mt-2 w-64 opacity-0 translate-y-2 pointer-events-none transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-2 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-1 text-white">
            <button onclick="copyTourLink()" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0">
                <i data-lucide="link" class="w-3.5 h-3.5"></i>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Copier le lien direct</span>
            </button>
            <a id="share-whatsapp" href="#" target="_blank" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-[#25D366] flex items-center justify-center shrink-0">
                <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Envoyer sur WhatsApp</span>
            </a>
            <a id="share-email" href="#" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-slate-300 flex items-center justify-center shrink-0">
                <i data-lucide="mail" class="w-3.5 h-3.5"></i>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Partager par Email</span>
            </a>
          </div>
        </div>"""

dark_green_share_en = """        <!-- Dropdown Menu Share Dark Opaque (#041d13) -->
        <div id="share-menu" class="absolute right-0 top-full mt-2 w-64 opacity-0 translate-y-2 pointer-events-none transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-2 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-1 text-white">
            <button onclick="copyTourLink()" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0">
                <i data-lucide="link" class="w-3.5 h-3.5"></i>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Copy direct link</span>
            </button>
            <a id="share-whatsapp" href="#" target="_blank" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-[#25D366] flex items-center justify-center shrink-0">
                <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Send via WhatsApp</span>
            </a>
            <a id="share-email" href="#" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-slate-300 flex items-center justify-center shrink-0">
                <i data-lucide="mail" class="w-3.5 h-3.5"></i>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Share via Email</span>
            </a>
          </div>
        </div>"""

pattern = r'<!-- Dropdown Menu Partage.*?</div>\s*</div>'

# 1. Update tours/*.html
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = re.sub(pattern, dark_green_share_fr, c, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("1. Applied dark green #041d13 share dropdown to all 14 French tour pages!")

# 2. Update en/tours/*.html
en_tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/tours'
for fname in os.listdir(en_tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(en_tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = re.sub(pattern, dark_green_share_en, c, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("2. Applied dark green #041d13 share dropdown to all 14 English tour pages!")
