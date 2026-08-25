import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

legal_brand_info = """          <div class="pt-2.5 text-[11px] text-slate-400 space-y-1 font-medium border-t border-white/10 mt-3">
            <p class="font-bold text-slate-200">Jungle Nepal Adventure Pvt. Ltd.</p>
            <p>🏛️ Immatriculation d'État : <strong class="text-slate-200 font-mono">N° 384414/82/83</strong></p>
            <p>📜 Numéro fiscal (PAN) : <strong class="text-slate-200 font-mono">623537310</strong></p>
            <p>📍 Thakurdwara-09, Parc National de Bardia, Népal</p>
          </div>"""

legal_bottom_bar = """      <!-- Bottom Bar with Official Legal Certifications -->
      <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-slate-400">
        <div class="space-y-1 text-center md:text-left">
          <p>© 2026 Jungle Nepal Adventure Pvt. Ltd. Tous droits réservés.</p>
          <p class="text-[11px] text-slate-400">Agence locale officielle agréée par le Ministère de l'Industrie et du Tourisme du Népal • Reg. 384414/82/83 • PAN 623537310</p>
        </div>
        <div class="flex items-center gap-4 text-xs">
          <button onclick="openLegalModal()" class="text-emerald-400 hover:text-emerald-300 font-bold transition-colors cursor-pointer flex items-center gap-1.5 bg-emerald-500/10 px-3 py-1.5 rounded-xl border border-emerald-500/20">
            <span>🇳🇵</span>
            <span>Agréments & Licences officielles</span>
          </button>
          <span>•</span>
          <a href="/a-propos.html" class="hover:text-white transition-colors">À propos</a>
          <span>•</span>
          <a href="/contact.html" class="hover:text-white transition-colors">Contact</a>
        </div>
      </div>"""

legal_modal_html = """  <!-- MODAL AGRÉMENTS LÉGAUX ET LICENCES OFFICIELLES DU NÉPAL -->
  <div id="legal-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-slate-950/85 backdrop-blur-md p-4 transition-opacity duration-300">
    <div class="bg-white rounded-3xl p-6 sm:p-8 max-w-lg w-full shadow-2xl border border-slate-200 text-slate-900 relative max-h-[90vh] overflow-y-auto">
      <button onclick="closeLegalModal()" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-500 hover:text-slate-800 font-bold transition-colors cursor-pointer">✕</button>
      
      <div class="text-center space-y-2 pb-4 border-b border-slate-100">
        <div class="w-14 h-14 rounded-2xl bg-emerald-500/15 text-[#0e8354] flex items-center justify-center text-3xl mx-auto">🏛️</div>
        <span class="text-[10px] font-extrabold uppercase tracking-widest text-[#0e8354] bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">Gouvernement du Népal</span>
        <h3 class="text-xl sm:text-2xl font-black text-slate-950 tracking-tight">Jungle Nepal Adventure Pvt. Ltd.</h3>
        <p class="text-xs text-slate-500 font-medium">Société d'écotourisme et d'expéditions officiellement enregistrée et agréée au Népal</p>
      </div>

      <div class="py-5 space-y-3.5 text-xs text-slate-700">
        <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-slate-500 uppercase text-[10px]">Certificat d'incorporation</span>
            <span class="font-black text-[#0e8354] bg-emerald-100/60 px-2 py-0.5 rounded text-[10px]">Officiel</span>
          </div>
          <p class="text-slate-900 font-black text-sm">Registre des Compagnies (Office of the Company Registrar)</p>
          <p class="font-mono text-xs font-bold text-slate-700">N° d'enregistrement : 384414/82/83</p>
          <p class="text-[11px] text-slate-500">Conformément à la sous-section (1) de la section 5 du Companies Act, 2006 du Népal.</p>
        </div>

        <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-slate-500 uppercase text-[10px]">Enregistrement Fiscal & Taxes</span>
            <span class="font-black text-[#0e8354] bg-emerald-100/60 px-2 py-0.5 rounded text-[10px]">Vérifié</span>
          </div>
          <p class="text-slate-900 font-black text-sm">Département des Revenus Intérieurs (Inland Revenue Department)</p>
          <p class="font-mono text-xs font-bold text-slate-700">Numéro PAN : 623537310</p>
          <p class="text-[11px] text-slate-500">Bureau fiscal de référence : Inland Revenue Office Nepalgunj.</p>
        </div>

        <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 space-y-2">
          <span class="font-bold text-slate-500 uppercase text-[10px] block">Siège Social & Exploitation</span>
          <p class="font-bold text-slate-900 text-xs">Thakurdwara Ward No. 9, Thakurbaba Municipality, Bardia District, Lumbini Province, Népal</p>
          <p class="text-[11px] text-slate-500">Fondateur & Gérant : Pawan Kumar Thapa (Chef Pisteur natif de Bardia)</p>
        </div>

        <div class="p-4 rounded-2xl bg-emerald-50/80 border border-emerald-200 text-slate-800 space-y-1.5 font-medium">
          <p class="font-bold text-[#0e8354] text-xs">🛡️ Activités autorisées sous licence d'État :</p>
          <p class="text-[11px] leading-relaxed text-slate-700">Organisation officielle de safaris faune sauvage (Wildlife Safaris), traque pédestre du tigre du Bengale, expéditions en rivières sauvages (Rafting Karnali), logistique de bivouacs et éco-tourisme certifié.</p>
        </div>
      </div>

      <div class="pt-2">
        <button onclick="closeLegalModal()" class="w-full py-3.5 rounded-2xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs transition-colors cursor-pointer">
          Fermer les informations légales
        </button>
      </div>
    </div>
  </div>

  <script is:inline>
  function openLegalModal() {
    const m = document.getElementById('legal-modal');
    if (m) m.classList.remove('hidden');
  }
  function closeLegalModal() {
    const m = document.getElementById('legal-modal');
    if (m) m.classList.add('hidden');
  }
  </script>"""

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Inject legal credentials in Col 1 of footer if missing
    if 'N° 384414/82/83' not in c:
        c = re.sub(
            r'(<p class="text-slate-400">Email\s*:\s*<strong class="text-white">[^<]+</strong></p>\s*</div>)',
            rf'\1\n{legal_brand_info}',
            c,
            flags=re.DOTALL
        )

    # 2. Update Bottom Bar in footer
    if 'Agréments & Licences officielles' not in c:
        c = re.sub(
            r'<!-- Bottom Bar -->.*?</div>\s*</div>\s*</footer>',
            f'{legal_bottom_bar}\n\n    </div>\n  </footer>',
            c,
            flags=re.DOTALL
        )

    # 3. Add legal modal if missing before </Layout>
    if 'id="legal-modal"' not in c:
        c = c.replace('</Layout>', f'{legal_modal_html}\n</Layout>')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Added legal documents & official government licenses to footers across {updated} files!")
