import os
import re

def generate_full_footer(prefix="", is_english=False):
    logo_src = f"{prefix}assets/logo.png"
    home_link = f"{prefix}index.html" if not is_english else f"{prefix}en/index.html"
    tours_prefix = f"{prefix}tours/" if not is_english else f"{prefix}en/tours/"
    dest_prefix = f"{prefix}destinations/" if not is_english else f"{prefix}en/destinations/"
    about_link = f"{prefix}a-propos.html" if not is_english else f"{prefix}en/a-propos.html"
    contact_link = f"{prefix}contact.html" if not is_english else f"{prefix}en/contact.html"

    if is_english:
        return f"""  <!-- =========================================================================
       FOOTER COMPLET AVEC TOUT LE MENU DU SITE
       ========================================================================= -->
  <footer class="bg-slate-950 text-slate-300 pt-16 sm:pt-20 pb-12 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-8 sm:gap-10 pb-14 border-b border-white/10 text-xs">
        
        <!-- COL 1: Brand & Contact -->
        <div class="space-y-4 lg:col-span-1">
          <a href="{home_link}" class="inline-block">
            <img src="{logo_src}" alt="Jungle Nepal Adventure" class="h-16 w-auto object-contain filter drop-shadow"/>
          </a>
          <p class="text-slate-400 text-xs leading-relaxed">
            Local travel agency specializing in immersive wildlife safaris and ethical nature expeditions in Nepal.
          </p>
          <div class="pt-2 space-y-2">
            <a href="https://wa.me/33695413227" target="_blank" class="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-emerald-500/20 text-[#10b981] font-bold text-xs hover:bg-emerald-500/30 transition-colors border border-emerald-500/30">
              <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
              <span>WhatsApp : +33 6 95 41 32 27</span>
            </a>
            <p class="text-slate-400">Email : <strong class="text-white">contact@junglenepal.com</strong></p>
          </div>
        </div>

        <!-- COL 2: Nos 14 Séjours -->
        <div class="space-y-3">
          <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">Expeditions</h4>
          <ul class="space-y-2 text-slate-400">
            <li><a href="{tours_prefix}bardia-explorateur.html" class="hover:text-[#10b981] transition-colors">Bardia Explorer (5d)</a></li>
            <li><a href="{tours_prefix}chitwan-culture.html" class="hover:text-[#10b981] transition-colors">Chitwan & Wildlife (4d)</a></li>
            <li><a href="{tours_prefix}nepal-sauvage.html" class="hover:text-[#10b981] transition-colors">Wild Nepal (15d)</a></li>
            <li><a href="{tours_prefix}babai-special.html" class="hover:text-[#10b981] transition-colors">Babai Valley Tiger Special (5d)</a></li>
            <li><a href="{tours_prefix}bardia-babai-camping.html" class="hover:text-[#10b981] transition-colors">Babai Wild Bivouac (8d)</a></li>
            <li><a href="{tours_prefix}rafting-safari.html" class="hover:text-[#10b981] transition-colors">Karnali Rafting & Safari (18d)</a></li>
            <li><a href="{tours_prefix}tiji-mustang.html" class="hover:text-[#10b981] transition-colors">Tiji Festival Mustang (13d)</a></li>
            <li><a href="{tours_prefix}nepal-immersion-totale.html" class="hover:text-[#10b981] transition-colors">Nepal Total Immersion (14d)</a></li>
            <li class="pt-1"><a href="{home_link}#prochains-departs" class="text-amber-300 font-bold hover:underline">View all 14 trips →</a></li>
          </ul>
        </div>

        <!-- COL 3: Destinations -->
        <div class="space-y-3">
          <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">Destinations</h4>
          <ul class="space-y-2 text-slate-400">
            <li><a href="{dest_prefix}bardia.html" class="hover:text-[#10b981] transition-colors">🐅 Bardia National Park</a></li>
            <li><a href="{dest_prefix}chitwan.html" class="hover:text-[#10b981] transition-colors">🦏 Chitwan National Park</a></li>
            <li><a href="{dest_prefix}suklaphanta.html" class="hover:text-[#10b981] transition-colors">🦌 Suklaphanta Wildlife</a></li>
            <li><a href="{dest_prefix}annapurna.html" class="hover:text-[#10b981] transition-colors">🏔️ Annapurna & Pokhara</a></li>
            <li><a href="{dest_prefix}katmandou.html" class="hover:text-[#10b981] transition-colors">🕉️ Kathmandu Valley</a></li>
            <li class="pt-1"><a href="{dest_prefix}index.html" class="text-amber-300 font-bold hover:underline">All Destinations →</a></li>
          </ul>
        </div>

        <!-- COL 4: L'Agence & Esprit Safari -->
        <div class="space-y-3">
          <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">The Experience</h4>
          <ul class="space-y-2 text-slate-400">
            <li><a href="{home_link}#concept" class="hover:text-[#10b981] transition-colors">Safari Philosophy</a></li>
            <li><a href="{home_link}#pisteurs" class="hover:text-[#10b981] transition-colors">Master Trackers (Pawan & Kiran)</a></li>
            <li><a href="{about_link}" class="hover:text-[#10b981] transition-colors">Our Story & Mission</a></li>
            <li><a href="{home_link}#avis" class="hover:text-[#10b981] transition-colors">Traveler Reviews (5.0/5 ⭐)</a></li>
            <li><a href="{home_link}#faq" class="hover:text-[#10b981] transition-colors">FAQ & Travel Guide</a></li>
          </ul>
        </div>

        <!-- COL 5: Booking & Contact -->
        <div class="space-y-3">
          <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">Plan Your Trip</h4>
          <ul class="space-y-2 text-slate-400">
            <li><a href="{contact_link}" class="hover:text-[#10b981] transition-colors">Custom Quote Request</a></li>
            <li><a href="https://wa.me/33695413227" target="_blank" class="hover:text-[#10b981] transition-colors">Chat with Robin on WhatsApp</a></li>
            <li class="pt-2 text-slate-500 font-medium">
              <span class="block text-emerald-400 font-bold">✨ Micro-groups 4 to 8</span>
              <span>100% Native trackers</span>
            </li>
          </ul>
        </div>

      </div>

      <!-- Bottom Bar -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-400">
        <p>© 2026 Jungle Nepal Adventure. All rights reserved.</p>
        <div class="flex items-center gap-4">
          <a href="{about_link}" class="hover:text-white transition-colors">About Us</a>
          <span>•</span>
          <a href="{contact_link}" class="hover:text-white transition-colors">Contact</a>
          <span>•</span>
          <span class="text-amber-300 font-bold">Crafted for Wild Nepal 🇳🇵</span>
        </div>
      </div>

    </div>
  </footer>"""
    else:
        return f"""  <!-- =========================================================================
       FOOTER COMPLET AVEC TOUT LE MENU DU SITE
       ========================================================================= -->
  <footer class="bg-slate-950 text-slate-300 pt-16 sm:pt-20 pb-12 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-8 sm:gap-10 pb-14 border-b border-white/10 text-xs">
        
        <!-- COL 1: Brand & Contact -->
        <div class="space-y-4 lg:col-span-1">
          <a href="{home_link}" class="inline-block">
            <img src="{logo_src}" alt="Jungle Nepal Adventure" class="h-16 w-auto object-contain filter drop-shadow"/>
          </a>
          <p class="text-slate-400 text-xs leading-relaxed">
            Agence locale d'écotourisme d'exception et de safaris immersifs au Népal. Katmandou & Parc National de Bardia.
          </p>
          <div class="pt-2 space-y-2">
            <a href="https://wa.me/33695413227" target="_blank" class="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-emerald-500/20 text-[#10b981] font-bold text-xs hover:bg-emerald-500/30 transition-colors border border-emerald-500/30">
              <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
              <span>WhatsApp : +33 6 95 41 32 27</span>
            </a>
            <p class="text-slate-400">Email : <strong class="text-white">contact@junglenepal.com</strong></p>
          </div>
        </div>

        <!-- COL 2: Nos 14 Séjours -->
        <div class="space-y-3">
          <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">Nos 14 Séjours</h4>
          <ul class="space-y-2 text-slate-400">
            <li><a href="{tours_prefix}bardia-explorateur.html" class="hover:text-[#10b981] transition-colors">Bardia Explorateur (5j)</a></li>
            <li><a href="{tours_prefix}chitwan-culture.html" class="hover:text-[#10b981] transition-colors">Chitwan & Jungle (4j)</a></li>
            <li><a href="{tours_prefix}nepal-sauvage.html" class="hover:text-[#10b981] transition-colors">Népal Sauvage 360° (15j)</a></li>
            <li><a href="{tours_prefix}babai-special.html" class="hover:text-[#10b981] transition-colors">Babai Spécial Tigres (5j)</a></li>
            <li><a href="{tours_prefix}bardia-babai-camping.html" class="hover:text-[#10b981] transition-colors">Bardia Babai Bivouac (8j)</a></li>
            <li><a href="{tours_prefix}rafting-safari.html" class="hover:text-[#10b981] transition-colors">Rafting Karnali & Safari (18j)</a></li>
            <li><a href="{tours_prefix}tiji-mustang.html" class="hover:text-[#10b981] transition-colors">Tiji Festival Mustang (13j)</a></li>
            <li><a href="{tours_prefix}nepal-immersion-totale.html" class="hover:text-[#10b981] transition-colors">Népal Immersion Totale (14j)</a></li>
            <li class="pt-1"><a href="{home_link}#prochains-departs" class="text-amber-300 font-bold hover:underline">Voir les 14 séjours →</a></li>
          </ul>
        </div>

        <!-- COL 3: Destinations -->
        <div class="space-y-3">
          <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">Destinations</h4>
          <ul class="space-y-2 text-slate-400">
            <li><a href="{dest_prefix}bardia.html" class="hover:text-[#10b981] transition-colors">🐅 Parc national de Bardia</a></li>
            <li><a href="{dest_prefix}chitwan.html" class="hover:text-[#10b981] transition-colors">🦏 Parc national de Chitwan</a></li>
            <li><a href="{dest_prefix}suklaphanta.html" class="hover:text-[#10b981] transition-colors">🦌 Parc de Suklaphanta</a></li>
            <li><a href="{dest_prefix}annapurna.html" class="hover:text-[#10b981] transition-colors">🏔️ Les Annapurna & Pokhara</a></li>
            <li><a href="{dest_prefix}katmandou.html" class="hover:text-[#10b981] transition-colors">🕉️ Vallée de Katmandou</a></li>
            <li class="pt-1"><a href="{dest_prefix}index.html" class="text-amber-300 font-bold hover:underline">Toutes les destinations →</a></li>
          </ul>
        </div>

        <!-- COL 4: L'Agence & Esprit Safari -->
        <div class="space-y-3">
          <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">L'Expérience</h4>
          <ul class="space-y-2 text-slate-400">
            <li><a href="{home_link}#concept" class="hover:text-[#10b981] transition-colors">L'esprit safari (Concept)</a></li>
            <li><a href="{home_link}#pisteurs" class="hover:text-[#10b981] transition-colors">Maîtres pisteurs (Pawan & Kiran)</a></li>
            <li><a href="{about_link}" class="hover:text-[#10b981] transition-colors">Notre histoire & Équipe</a></li>
            <li><a href="{home_link}#avis" class="hover:text-[#10b981] transition-colors">Avis voyageurs (5.0/5 ⭐)</a></li>
            <li><a href="{home_link}#faq" class="hover:text-[#10b981] transition-colors">Foire aux questions (FAQ)</a></li>
          </ul>
        </div>

        <!-- COL 5: Réservation & Contact -->
        <div class="space-y-3">
          <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">Contact & Devis</h4>
          <ul class="space-y-2 text-slate-400">
            <li><a href="{contact_link}" class="hover:text-[#10b981] transition-colors">Demande de devis sur-mesure</a></li>
            <li><a href="https://wa.me/33695413227" target="_blank" class="hover:text-[#10b981] transition-colors">Échanger sur WhatsApp avec Robin</a></li>
            <li class="pt-2 text-slate-500 font-medium">
              <span class="block text-emerald-400 font-bold">✨ Micro-groupes 4 à 8</span>
              <span>100% Pisteurs natifs</span>
            </li>
          </ul>
        </div>

      </div>

      <!-- Bottom Bar -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-400">
        <p>© 2026 Jungle Nepal Adventure. Tous droits réservés.</p>
        <div class="flex items-center gap-4">
          <a href="{about_link}" class="hover:text-white transition-colors">À propos</a>
          <span>•</span>
          <a href="{contact_link}" class="hover:text-white transition-colors">Contact</a>
          <span>•</span>
          <span class="text-amber-300 font-bold">Créé avec passion pour le Népal 🇳🇵</span>
        </div>
      </div>

    </div>
  </footer>"""

# 1. Update index.html, a-propos.html, contact.html
root_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'
for fname in ['index.html', 'a-propos.html', 'contact.html']:
    fpath = os.path.join(root_dir, fname)
    if not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_footer = generate_full_footer(prefix="", is_english=False)
    c = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("1. Applied complete footer menu to root pages!")

# 2. Update destinations/*.html
dest_dir = os.path.join(root_dir, 'destinations')
for fname in os.listdir(dest_dir):
    if not fname.endswith('.html'): continue
    fpath = os.path.join(dest_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_footer = generate_full_footer(prefix="../", is_english=False)
    c = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("2. Applied complete footer menu to destination pages!")

# 3. Update tours/*.html
tours_dir = os.path.join(root_dir, 'tours')
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'): continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_footer = generate_full_footer(prefix="../", is_english=False)
    if '<footer' in c:
        c = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, c, flags=re.DOTALL)
    else:
        # Insert before modal/scripts
        c = c.replace('<!-- LIGHTBOX MODAL', f'{new_footer}\n\n  <!-- LIGHTBOX MODAL')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("3. Applied complete footer menu to all tour pages!")

# 4. Update English mirrors (en/...)
en_root = os.path.join(root_dir, 'en')
for fname in ['index.html', 'a-propos.html', 'contact.html']:
    fpath = os.path.join(en_root, fname)
    if not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_footer = generate_full_footer(prefix="../", is_english=True)
    c = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

en_dest = os.path.join(en_root, 'destinations')
for fname in os.listdir(en_dest):
    if not fname.endswith('.html'): continue
    fpath = os.path.join(en_dest, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_footer = generate_full_footer(prefix="../../", is_english=True)
    c = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, c, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

en_tours = os.path.join(en_root, 'tours')
for fname in os.listdir(en_tours):
    if not fname.endswith('.html'): continue
    fpath = os.path.join(en_tours, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_footer = generate_full_footer(prefix="../../", is_english=True)
    if '<footer' in c:
        c = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, c, flags=re.DOTALL)
    else:
        c = c.replace('<!-- LIGHTBOX MODAL', f'{new_footer}\n\n  <!-- LIGHTBOX MODAL')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("4. Applied complete footer menu to all English pages!")
