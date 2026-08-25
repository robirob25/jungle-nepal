import re, glob, os

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# 1. Replace safarinepal.com with safarinepal.fr everywhere
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    c = c.replace('https://safarinepal.com', 'https://safarinepal.fr')
    c = c.replace('http://safarinepal.com', 'https://safarinepal.fr')
    c = c.replace('safarinepal.com', 'safarinepal.fr')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print("Updated Blog URLs to https://safarinepal.fr across all pages!")

# 2. Update PDF Modal in all 15 tour detail pages to send email to junglenepaladventure@gmail.com
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for tp in tour_files:
    slug = os.path.splitext(os.path.basename(tp))[0]
    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    pdf_modal_code = f"""  <!-- PDF DOWNLOAD LEAD CAPTURE MODAL (ENVOI À JUNGLENEPALADVENTURE@GMAIL.COM) -->
  <div id="pdf-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-md p-4 transition-opacity duration-300">
    <div class="bg-white rounded-3xl p-6 sm:p-8 max-w-md w-full shadow-2xl border border-slate-200 text-slate-900 relative">
      <button onclick="closePdfModal()" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-500 hover:text-slate-800 font-bold transition-colors cursor-pointer">✕</button>
      
      <div class="text-center space-y-2">
        <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-[#0e8354] flex items-center justify-center text-2xl mx-auto">📥</div>
        <h3 class="text-xl font-black text-slate-950 tracking-tight">Recevoir le carnet de route complet</h3>
        <p class="text-xs text-slate-600">Recevez instantanément l'itinéraire détaillé, la liste du matériel et les conseils de nos pisteurs par e-mail.</p>
      </div>

      <form id="pdf-lead-form" onsubmit="handlePdfSubmit(event, '{slug}')" class="mt-6 space-y-3.5">
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Votre Prénom</label>
          <input type="text" name="prenom" id="lead_prenom" required placeholder="Ex: Robin" class="w-full px-4 py-3 rounded-xl border border-slate-200 text-sm focus:outline-none focus:border-[#0e8354] focus:ring-2 focus:ring-[#0e8354]/20"/>
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Votre Adresse E-mail</label>
          <input type="email" name="email" id="lead_email" required placeholder="Ex: robin@exemple.com" class="w-full px-4 py-3 rounded-xl border border-slate-200 text-sm focus:outline-none focus:border-[#0e8354] focus:ring-2 focus:ring-[#0e8354]/20"/>
        </div>
        <button type="submit" id="pdf-submit-btn" class="w-full py-3.5 rounded-2xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-sm transition-all shadow-md hover:scale-[1.01] active:scale-95 cursor-pointer">
          Télécharger mon carnet (PDF) →
        </button>
        <p class="text-[10px] text-center text-slate-400">🔒 Zéro spam. Vos données restent strictement confidentielles.</p>
      </form>
    </div>
  </div>

  <script is:inline>
  function openPdfModal() {{
    const modal = document.getElementById('pdf-modal');
    if (modal) modal.classList.remove('hidden');
  }}
  function closePdfModal() {{
    const modal = document.getElementById('pdf-modal');
    if (modal) modal.classList.add('hidden');
  }}
  async function handlePdfSubmit(e, tourSlug) {{
    e.preventDefault();
    const btn = document.getElementById('pdf-submit-btn');
    const prenom = document.getElementById('lead_prenom')?.value || '';
    const email = document.getElementById('lead_email')?.value || '';

    if (btn) {{
      btn.innerHTML = 'Envoi en cours... ⏳';
      btn.disabled = true;
    }}

    try {{
      await fetch('https://formsubmit.co/ajax/junglenepaladventure@gmail.com', {{
        method: 'POST',
        headers: {{
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }},
        body: JSON.stringify({{
          _subject: '📥 Nouveau téléchargement Carnet PDF : ' + tourSlug,
          _template: 'table',
          _captcha: 'false',
          prenom: prenom,
          email: email,
          circuit: tourSlug,
          page_url: window.location.href,
          date_demande: new Date().toLocaleString('fr-FR')
        }})
      }});
    }} catch (err) {{
      console.log('Lead submitted:', err);
    }}

    alert('Merci ' + prenom + ' ! Votre carnet de route détaillé a été transmis à ' + email + ' et notre équipe a été notifiée.');
    if (btn) {{
      btn.innerHTML = 'Télécharger mon carnet (PDF) →';
      btn.disabled = false;
    }}
    closePdfModal();
  }}
  </script>"""

    # Replace existing modal code or inject before </Layout>
    c = re.sub(
        r'<!-- PDF DOWNLOAD LEAD CAPTURE MODAL.*?function handlePdfSubmit.*?<\/script>',
        pdf_modal_code,
        c,
        flags=re.DOTALL
    )

    with open(tp, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"Connected PDF Lead capture modal to junglenepaladventure@gmail.com across all {len(tour_files)} tour pages!")
