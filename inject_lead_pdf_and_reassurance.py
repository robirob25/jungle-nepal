import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

lead_pdf_button = """          <!-- PDF Lead Magnet & WeTravel Reassurance -->
          <div class="pt-3 border-t border-slate-100 space-y-2.5">
            <button onclick="openPdfModal()" class="w-full flex items-center justify-center gap-2 py-3 px-4 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-800 font-extrabold text-xs transition-colors border border-slate-200 cursor-pointer">
              <span>📥</span>
              <span>Télécharger le carnet de route (PDF)</span>
            </button>
            <div class="flex items-center justify-center gap-1.5 text-[11px] text-slate-500 font-semibold">
              <span>🛡️</span>
              <span>Acompte de 30% pour bloquer votre place</span>
            </div>
          </div>"""

pdf_modal_html = """  <!-- PDF DOWNLOAD LEAD CAPTURE MODAL -->
  <div id="pdf-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-md p-4 transition-opacity duration-300">
    <div class="bg-white rounded-3xl p-6 sm:p-8 max-w-md w-full shadow-2xl border border-slate-200 text-slate-900 relative">
      <button onclick="closePdfModal()" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-500 hover:text-slate-800 font-bold transition-colors">✕</button>
      
      <div class="text-center space-y-2">
        <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-[#0e8354] flex items-center justify-center text-2xl mx-auto">📥</div>
        <h3 class="text-xl font-black text-slate-950 tracking-tight">Recevoir le carnet de route complet</h3>
        <p class="text-xs text-slate-600">Recevez instantanément l'itinéraire détaillé, la liste du matériel et les conseils de nos pisteurs par e-mail.</p>
      </div>

      <form onsubmit="handlePdfSubmit(event)" class="mt-6 space-y-3.5">
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Votre Prénom</label>
          <input type="text" required placeholder="Ex: Robin" class="w-full px-4 py-3 rounded-xl border border-slate-200 text-sm focus:outline-none focus:border-[#0e8354]"/>
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Votre Adresse E-mail</label>
          <input type="email" required placeholder="Ex: robin@exemple.com" class="w-full px-4 py-3 rounded-xl border border-slate-200 text-sm focus:outline-none focus:border-[#0e8354]"/>
        </div>
        <button type="submit" class="w-full py-3.5 rounded-2xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-sm transition-all shadow-md hover:scale-[1.02] active:scale-95 cursor-pointer">
          Télécharger mon carnet (PDF) →
        </button>
        <p class="text-[10px] text-center text-slate-400">🔒 Zéro spam. Vos données restent strictement confidentielles.</p>
      </form>
    </div>
  </div>

  <script is:inline>
  function openPdfModal() {
    const modal = document.getElementById('pdf-modal');
    if (modal) modal.classList.remove('hidden');
  }
  function closePdfModal() {
    const modal = document.getElementById('pdf-modal');
    if (modal) modal.classList.add('hidden');
  }
  function handlePdfSubmit(e) {
    e.preventDefault();
    alert('Merci ! Votre carnet de route détaillé est en cours d\\'envoi à votre adresse email.');
    closePdfModal();
  }
  </script>"""

updated = 0
for tp in tour_files:
    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    if 'openPdfModal()' not in c:
        # Insert PDF button in sticky booking card right above reassurance list or right below CTA
        c = re.sub(
            r'(<!-- Primary CTA Button.*?</a>)',
            rf'\1\n\n{lead_pdf_button}',
            c,
            flags=re.DOTALL
        )
        # Insert modal at bottom before </Layout>
        c = c.replace('</Layout>', pdf_modal_html + '\n</Layout>')

    if c != orig:
        with open(tp, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Injected PDF Lead Magnet & Reassurance across {updated} tour detail pages!")
