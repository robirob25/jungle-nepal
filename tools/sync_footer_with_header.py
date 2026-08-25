import glob, re

# Header navigation items are:
# 1. Tous les 15 séjours (/index.html#prochains-departs)
# 2. Destinations (Bardia, Chitwan, Suklaphanta, Annapurna, Katmandou)
# 3. L'esprit safari (/index.html#concept)
# 4. Maîtres pisteurs (/index.html#pisteurs)
# 5. À propos (/a-propos.html)
# 6. Blog (https://safarinepal.fr)
# 7. Contact (/contact.html)

# We want the footer columns and links to strictly align with Header.astro:
# - Col 2: TOUS LES 15 SÉJOURS (list of trips + Voir les 15 séjours →)
# - Col 3: DESTINATIONS (Bardia, Chitwan, Suklaphanta, Annapurnas, Katmandou + Toutes les destinations →)
# - Col 4: NAVIGATION DU SITE (L'esprit safari, Maîtres pisteurs, À propos, Blog ↗, Contact)
# - Col 5: CONTACT & INFOS (Demande de devis, WhatsApp, Micro-groupes, Pisteurs)

new_footer_cols = """      <!-- COL 2: Tous les 15 Séjours -->
      <div class="space-y-3">
        <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">
          Tous les 15 Séjours
        </h4>
        <ul class="space-y-2 text-slate-400">
          <li><a href="/tours/bardia-explorateur.html" class="hover:text-slate-200 transition-colors">Bardia Explorateur (5j)</a></li>
          <li><a href="/tours/chitwan-culture.html" class="hover:text-slate-200 transition-colors">Chitwan & Jungle (4j)</a></li>
          <li><a href="/tours/nepal-sauvage.html" class="hover:text-slate-200 transition-colors">Népal Sauvage 360° (15j)</a></li>
          <li><a href="/tours/babai-special.html" class="hover:text-slate-200 transition-colors">Babai Spécial Tigres (5j)</a></li>
          <li><a href="/tours/bardia-babai-camping.html" class="hover:text-slate-200 transition-colors">Bardia Babai Bivouac (8j)</a></li>
          <li><a href="/tours/rafting-safari.html" class="hover:text-slate-200 transition-colors">Rafting Karnali & Safari (18j)</a></li>
          <li><a href="/tours/tiji-mustang.html" class="hover:text-slate-200 transition-colors">Tiji Festival Mustang (13j)</a></li>
          <li><a href="/tours/nepal-immersion-totale.html" class="hover:text-slate-200 transition-colors">Népal Immersion Totale (14j)</a></li>
          <li class="pt-1"><a href="/index.html#prochains-departs" class="text-amber-100 font-bold hover:underline">Voir les 15 séjours →</a></li>
        </ul>
      </div>

      <!-- COL 3: Destinations -->
      <div class="space-y-3">
        <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">Destinations</h4>
        <ul class="space-y-2 text-slate-400">
          <li><a href="/destinations/bardia.html" class="hover:text-slate-200 transition-colors">Parc national de Bardia</a></li>
          <li><a href="/destinations/chitwan.html" class="hover:text-slate-200 transition-colors">Parc national de Chitwan</a></li>
          <li><a href="/destinations/suklaphanta.html" class="hover:text-slate-200 transition-colors">Parc national de Suklaphanta</a></li>
          <li><a href="/destinations/annapurna.html" class="hover:text-slate-200 transition-colors">Les Annapurna & Pokhara</a></li>
          <li><a href="/destinations/katmandou.html" class="hover:text-slate-200 transition-colors">Katmandou</a></li>
          <li class="pt-1"><a href="/destinations.html" class="text-amber-100 font-bold hover:underline">Toutes les destinations →</a></li>
        </ul>
      </div>

      <!-- COL 4: Navigation (Exact Header Match) -->
      <div class="space-y-3">
        <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">
          Navigation
        </h4>
        <ul class="space-y-2 text-slate-400">
          <li><a href="/index.html#concept" class="hover:text-slate-200 transition-colors">L'esprit safari</a></li>
          <li><a href="/index.html#pisteurs" class="hover:text-slate-200 transition-colors">Maîtres pisteurs</a></li>
          <li><a href="/a-propos.html" class="hover:text-slate-200 transition-colors">À propos</a></li>
          <li><a href="https://safarinepal.fr" target="_blank" rel="noopener noreferrer" class="hover:text-slate-200 transition-colors flex items-center justify-between"><span>Blog</span><span class="text-[10px] bg-white/10 text-slate-300 px-1 py-0.2 rounded font-mono">↗</span></a></li>
          <li><a href="/contact.html" class="hover:text-slate-200 transition-colors">Contact</a></li>
        </ul>
      </div>

      <!-- COL 5: Contact & Réservation -->
      <div class="space-y-3">
        <h4 class="font-black text-white text-xs uppercase tracking-widest border-b border-white/10 pb-2">
          Contact & Réservation
        </h4>
        <ul class="space-y-2 text-slate-400">
          <li><a href="/contact.html" class="hover:text-slate-200 transition-colors">Demande de devis sur-mesure</a></li>
          <li><a href="https://wa.me/33695413227" target="_blank" rel="noopener noreferrer" class="hover:text-slate-200 transition-colors">Contacter Robin sur WhatsApp</a></li>
          <li class="pt-2 text-slate-500 font-medium">
            <span class="block text-slate-200 font-bold">Micro-groupes 4 à 10</span>
            <span>100% Pisteurs natifs</span>
          </li>
        </ul>
      </div>"""

# 1. Update src/components/Footer.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Footer.astro', 'w', encoding='utf-8') as f:
    f.write(f"""---
interface Props {{
  lang?: 'fr' | 'en';
}}

const {{ lang = 'fr' }} = Astro.props;
---

<footer class="bg-slate-950 text-slate-300 pt-16 sm:pt-20 pb-12 border-t border-white/10">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-8 sm:gap-10 pb-14 border-b border-white/10 text-xs">
      
      <!-- COL 1: Brand & Contact -->
      <div class="space-y-4 lg:col-span-1">
        <a href="/index.html" class="inline-block">
          <img src="/assets/logo_nav_white.webp" alt="Jungle Nepal Adventure" class="h-11 sm:h-12 w-auto object-contain group-hover:scale-105 transition-transform"/>
        </a>
        <p class="text-slate-400 text-xs leading-relaxed">
          Agence locale d'écotourisme d'exception et de safaris immersifs au Népal. Katmandou & Parc National de Bardia.
        </p>
        <div class="pt-2 space-y-2">
          <a href="https://wa.me/33695413227" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-white/10 text-slate-200 font-bold text-xs hover:bg-emerald-900/30 transition-colors border border-white/10 whitespace-nowrap"><svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg><span class="whitespace-nowrap">WhatsApp : +33 6 95 41 32 27</span></a>
          <p class="text-slate-400">Email : <strong class="text-white">contact@junglenepal.com</strong></p>
        </div>
        <div class="pt-2.5 text-[11px] text-slate-400 space-y-1 font-medium border-t border-white/10 mt-3">
          <p class="font-bold text-slate-200">Jungle Nepal Adventure Pvt. Ltd.</p>
          <p>Immatriculation d'État : <strong class="text-slate-200 font-mono">N° 384414/82/83</strong></p>
          <p>Numéro fiscal (PAN) : <strong class="text-slate-200 font-mono">623537310</strong></p>
          <p>Thakurdwara-09, Parc National de Bardia, Népal</p>
        </div>
      </div>

{new_footer_cols}

    </div>

    <!-- Bottom Bar with Official Legal Certifications -->
    <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-slate-400">
      <div class="space-y-1 text-center md:text-left">
        <p>© 2026 Jungle Nepal Adventure Pvt. Ltd. Tous droits réservés.</p>
        <p class="text-[11px] text-slate-400">Agence locale officielle agréée par le Ministère de l'Industrie et du Tourisme du Népal • Reg. 384414/82/83 • PAN 623537310</p>
      </div>
      <div class="flex items-center gap-4 text-xs">
        <button onclick="openLegalModal()" class="text-slate-200 hover:text-slate-200 font-bold transition-colors cursor-pointer flex items-center gap-1.5 bg-emerald-900/10 px-3 py-1.5 rounded-xl border border-emerald-800/20">
          <span>Agréments & Licences officielles</span>
        </button>
        <span>•</span>
        <a href="/a-propos.html" class="hover:text-white transition-colors">À propos</a>
        <span>•</span>
        <a href="/contact.html" class="hover:text-white transition-colors">Contact</a>
      </div>
    </div>

  </div>
</footer>
""")

# 2. Update inline footers across all Astro pages (index, a-propos, contact, destinations, tours)
all_astro = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

footer_regex = r'<!-- COL 2: Nos 15 Séjours -->.*?</div>\s*<!-- COL 3: Destinations -->.*?</div>\s*<!-- COL 4:.*?-->.*?</div>\s*<!-- COL 5:.*?-->.*?</div>'

for fpath in all_astro:
    if fpath.endswith('Footer.astro'):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    new_c = re.sub(footer_regex, new_footer_cols, c, flags=re.DOTALL)
    
    # Also handle alternate header titles like "<!-- COL 2:..."
    if new_c == c:
        alt_regex = r'<div class="space-y-3">\s*<h4[^>]*>.*?Nos 15 Séjours.*?</h4>.*?<div class="space-y-3">\s*<h4[^>]*>.*?Destinations.*?</h4>.*?<div class="space-y-3">\s*<h4[^>]*>.*?L\'Expérience.*?</h4>.*?<div class="space-y-3">\s*<h4[^>]*>.*?Contact & Devis.*?</h4>.*?</div>\s*</div>'
        new_c = re.sub(alt_regex, new_footer_cols + '\n      </div>', c, flags=re.DOTALL)

    if new_c != c:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"✓ Synchronized footer in {fpath.split('/')[-1]}")

print("Done synchronizing footer with header navigation across the entire website!")
