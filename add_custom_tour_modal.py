with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

# 1. Add Custom Tour Modal to Layout.astro (Available globally across every page)
custom_tour_modal = """
  <!-- MODAL VOYAGE SUR-MESURE (HAUT DE GAMME & RESPONSIVE) -->
  <div id="custom-tour-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-md transition-all duration-300 overflow-y-auto">
    <div class="relative w-full max-w-2xl bg-white rounded-3xl sm:rounded-[32px] shadow-2xl border border-slate-200/90 overflow-hidden my-auto max-h-[92vh] flex flex-col animate-in fade-in zoom-in-95 duration-200">
      
      <!-- Top Modal Header -->
      <div class="relative bg-gradient-to-r from-[#032317] via-[#053222] to-[#032317] text-white p-6 sm:p-8 shrink-0">
        <!-- Close Button -->
        <button type="button" onclick="closeCustomTourModal()" class="absolute top-4 right-4 sm:top-6 sm:right-6 w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10 hover:bg-white/25 border border-white/20 flex items-center justify-center text-white font-bold transition-all hover:scale-105 active:scale-95 cursor-pointer z-10" aria-label="Fermer la fenêtre">
          ✕
        </button>

        <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 text-[#10b981] font-extrabold text-[11px] uppercase tracking-widest border border-emerald-500/30 mb-2">
          <span>🌿</span> <span>Projet sur-mesure & Privatisé</span>
        </span>
        <h3 class="text-xl sm:text-3xl font-black text-white tracking-tight leading-tight">
          Concevez votre voyage idéal au Népal
        </h3>
        <p class="text-xs sm:text-sm text-slate-300 mt-1.5 font-medium leading-relaxed max-w-lg">
          Itinéraire personnalisé, dates flexibles, safaris exclusifs ou combiné sur-mesure. Pawan et Robin créent votre séjour de A à Z.
        </p>
      </div>

      <!-- Scrollable Form Body -->
      <div class="p-6 sm:p-8 overflow-y-auto space-y-5 text-slate-900 flex-1">
        
        <!-- Success Alert Notification -->
        <div id="custom-tour-success" class="hidden p-5 rounded-2xl bg-emerald-500/10 border-2 border-emerald-500/40 text-emerald-950 shadow-xl transition-all">
          <div class="flex items-start gap-3">
            <div class="w-9 h-9 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-black text-base shrink-0 shadow-md">✓</div>
            <div>
              <h4 class="font-black text-base text-emerald-950">Demande sur-mesure transmise !</h4>
              <p class="text-xs text-emerald-800 mt-1 font-medium leading-relaxed">
                Merci ! Nous avons bien reçu vos souhaits. Robin et notre équipe locale vous recontacteront sous 24h avec une première proposition d'itinéraire chiffrée.
              </p>
            </div>
          </div>
        </div>

        <!-- Error Alert Notification -->
        <div id="custom-tour-error" class="hidden p-4 rounded-2xl bg-rose-500/10 border-2 border-rose-500/40 text-rose-950 shadow-md">
          <p class="text-xs font-semibold" id="custom-tour-error-text">Une erreur est survenue. Veuillez vérifier vos informations ou nous contacter par WhatsApp.</p>
        </div>

        <form id="custom-tour-form" onsubmit="handleCustomTourSubmit(event)" class="space-y-4 text-sm">
          
          <!-- L'expérience recherchée -->
          <div>
            <label class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1.5">
              Vos priorités de voyage <span class="text-[#0e8354]">*</span>
            </label>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs font-semibold">
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Pistage Tigres à pied (Bardia)" class="rounded text-[#0e8354] focus:ring-[#0e8354]" checked />
                <span>🐅 Tigres à pied</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Rhinocéros & Pirogue (Chitwan)" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🦏 Rhinos Chitwan</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Panthère des neiges (Himalaya)" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🐆 Panthère des neiges</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Bivouac & Nuit sauvage" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>⛺ Bivouac jungle</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Expédition Photo & Vidéo" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>📸 Photo animalière</span>
              </label>
              <label class="flex items-center gap-2 p-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer transition-colors">
                <input type="checkbox" name="custom_priority" value="Culture & Temples Katmandou" class="rounded text-[#0e8354] focus:ring-[#0e8354]" />
                <span>🕉️ Temples & Culture</span>
              </label>
            </div>
          </div>

          <!-- Prénom & Nom -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
            <div>
              <label class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1">
                Prénom <span class="text-[#0e8354]">*</span>
              </label>
              <input type="text" id="custom-firstname" placeholder="Votre prénom" required class="w-full p-3 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all" />
            </div>
            <div>
              <label class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1">
                Nom <span class="text-[#0e8354]">*</span>
              </label>
              <input type="text" id="custom-lastname" placeholder="Votre nom" required class="w-full p-3 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all" />
            </div>
          </div>

          <!-- Email & WhatsApp -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
            <div>
              <label class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1">
                Email de contact <span class="text-[#0e8354]">*</span>
              </label>
              <input type="email" id="custom-email" placeholder="nom@email.com" required class="w-full p-3 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all" />
            </div>
            <div>
              <label class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1">
                Téléphone / WhatsApp <span class="text-[#0e8354]">*</span>
              </label>
              <input type="tel" id="custom-phone" placeholder="+33 6 12 34 56 78" required class="w-full p-3 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all" />
            </div>
          </div>

          <!-- Nombre de voyageurs & Durée estimée -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
            <div>
              <label class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1">
                Nombre de voyageurs
              </label>
              <select id="custom-travelers" class="w-full p-3 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all cursor-pointer">
                <option value="1 voyageur (Solo)">1 voyageur (Solo)</option>
                <option value="2 voyageurs (Couple / Duo)" selected>2 voyageurs (Couple / Duo)</option>
                <option value="3 à 5 personnes (Famille / Amis)">3 à 5 personnes (Famille / Amis)</option>
                <option value="6 à 10 personnes (Groupe constitué)">6 à 10 personnes (Groupe constitué)</option>
              </select>
            </div>
            <div>
              <label class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1">
                Durée estimée sur place
              </label>
              <select id="custom-duration" class="w-full p-3 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all cursor-pointer">
                <option value="5 à 7 jours (Court séjour intensif)">5 à 7 jours (Court séjour intensif)</option>
                <option value="8 à 12 jours (Safari complet)" selected>8 à 12 jours (Safari complet)</option>
                <option value="14 à 18 jours (Grand tour immersion)">14 à 18 jours (Grand tour immersion)</option>
                <option value="3 semaines ou plus">3 semaines ou plus</option>
              </select>
            </div>
          </div>

          <!-- Description des souhaits -->
          <div>
            <label class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1">
              Vos envies & détails du projet <span class="text-[#0e8354]">*</span>
            </label>
            <textarea id="custom-notes" rows="3" placeholder="Période envisagée (ex: Octobre 2026), type d'hébergement souhaité, rythme de marche, centres d'intérêt particuliers..." required class="w-full p-3 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all"></textarea>
          </div>

          <!-- Bouton Submit -->
          <div class="pt-2">
            <button type="submit" id="custom-tour-submit-btn" class="w-full py-4 rounded-2xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white font-extrabold text-sm shadow-xl shadow-[#0e8354]/30 hover:scale-100 active:scale-95 transition-all text-center cursor-pointer">
              Envoyer ma demande de voyage sur-mesure →
            </button>
            <p class="text-[11px] text-center text-slate-400 mt-2 font-medium">
              🔒 Réponse et devis personnalisés sans engagement sous 24h par Robin.
            </p>
          </div>

        </form>

      </div>

    </div>
  </div>

  <script is:inline>
    // Universal Custom Tour Modal Controls
    window.openCustomTourModal = function() {
      var m = document.getElementById('custom-tour-modal');
      if (m) {
        m.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
      }
    };

    window.closeCustomTourModal = function() {
      var m = document.getElementById('custom-tour-modal');
      if (m) {
        m.classList.add('hidden');
        document.body.style.overflow = '';
      }
    };

    // Close on background click
    document.addEventListener('click', function(e) {
      var m = document.getElementById('custom-tour-modal');
      if (m && e.target === m) {
        closeCustomTourModal();
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeCustomTourModal();
      }
    });

    // Handle Custom Tour Submission to FormSubmit
    window.handleCustomTourSubmit = async function(e) {
      if (e && e.preventDefault) e.preventDefault();

      var btn = document.getElementById('custom-tour-submit-btn');
      var successBox = document.getElementById('custom-tour-success');
      var errorBox = document.getElementById('custom-tour-error');
      var form = document.getElementById('custom-tour-form');

      if (successBox) successBox.classList.add('hidden');
      if (errorBox) errorBox.classList.add('hidden');

      var prenom = (document.getElementById('custom-firstname')?.value || '').trim();
      var nom = (document.getElementById('custom-lastname')?.value || '').trim();
      var email = (document.getElementById('custom-email')?.value || '').trim();
      var phone = (document.getElementById('custom-phone')?.value || '').trim();
      var travelers = (document.getElementById('custom-travelers')?.value || '').trim();
      var duration = (document.getElementById('custom-duration')?.value || '').trim();
      var notes = (document.getElementById('custom-notes')?.value || '').trim();

      // Collect selected priorities checkboxes
      var priorities = [];
      var checkedBoxes = document.querySelectorAll('input[name="custom_priority"]:checked');
      checkedBoxes.forEach(function(box) { priorities.push(box.value); });

      if (!prenom || !nom || !email || !phone || !notes) {
        if (errorBox) {
          document.getElementById('custom-tour-error-text').textContent = 'Veuillez remplir tous les champs obligatoires (*).';
          errorBox.classList.remove('hidden');
        }
        return false;
      }

      if (btn) {
        btn.innerHTML = '<span class="inline-flex items-center gap-2"><span>Transmission en cours...</span> <svg class="animate-spin w-4 h-4 text-white" viewBox="0 0 24 24" fill="none"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path></svg></span>';
        btn.disabled = true;
      }

      var payload = {
        _subject: '🌟 NOUVEAU PROJET SUR-MESURE : ' + prenom + ' ' + nom + ' (' + travelers + ' - ' + duration + ')',
        _template: 'table',
        _captcha: 'false',
        _replyto: email,
        type_demande: 'Voyage Sur-Mesure & Privatisé',
        client_nom_complet: prenom + ' ' + nom,
        email: email,
        telephone_whatsapp: phone,
        nombre_voyageurs: travelers,
        duree_estimee: duration,
        priorites_choisies: priorities.join(', '),
        details_du_projet: notes,
        date_envoi: new Date().toLocaleString('fr-FR')
      };

      var isSuccess = false;
      try {
        var res = await fetch('https://formsubmit.co/ajax/junglenepaladventure@gmail.com', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (res.ok) isSuccess = true;
      } catch (err) {
        console.warn('Custom tour form fetch error:', err);
      }

      if (!isSuccess) {
        try {
          var res2 = await fetch('https://formsubmit.co/junglenepaladventure@gmail.com', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
            body: JSON.stringify(payload)
          });
          if (res2.ok) isSuccess = true;
        } catch (err2) {}
      }

      if (isSuccess) {
        if (form) form.reset();
        if (successBox) successBox.classList.remove('hidden');
        if (btn) {
          btn.innerHTML = '✓ Projet transmis avec succès !';
          btn.classList.add('bg-emerald-700');
          setTimeout(function() {
            closeCustomTourModal();
            btn.innerHTML = 'Envoyer ma demande de voyage sur-mesure →';
            btn.classList.remove('bg-emerald-700');
            btn.disabled = false;
          }, 3500);
        }
      } else {
        if (errorBox) {
          errorBox.classList.remove('hidden');
        }
        if (btn) {
          btn.innerHTML = 'Réessayer l\\'envoi →';
          btn.disabled = false;
        }
      }
      return false;
    };
  </script>
"""

# Insert modal right before </body> in Layout.astro
layout = layout.replace('</body>', custom_tour_modal + '\n</body>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)

print("✓ Added global custom tour modal to Layout.astro!")
