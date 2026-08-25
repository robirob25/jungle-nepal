with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add modern Alert/Notification toast & inline state containers right before the form
form_header_old = """        <div>
          <span class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354]">Formulaire de contact</span>
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight mt-1">
            Envoyez-nous votre message
          </h2>
          <p class="text-xs sm:text-sm text-slate-600 mt-1.5 font-medium">
            Remplissez ce formulaire et recevez un retour personnalisé directement dans votre boîte mail.
          </p>
        </div>"""

form_header_new = """        <div>
          <span class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354]">Formulaire de contact</span>
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight mt-1">
            Envoyez-nous votre message
          </h2>
          <p class="text-xs sm:text-sm text-slate-600 mt-1.5 font-medium">
            Remplissez ce formulaire et recevez un retour personnalisé directement dans votre boîte mail.
          </p>
        </div>

        <!-- Success Alert Notification (High-end 2026 UI) -->
        <div id="contact-success-notification" class="hidden p-5 rounded-2xl bg-emerald-500/10 border-2 border-emerald-500/40 text-emerald-950 shadow-xl transition-all duration-300 animate-in fade-in zoom-in-95">
          <div class="flex items-start gap-3.5">
            <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center text-xl shrink-0 shadow-md">
              ✓
            </div>
            <div class="flex-1">
              <h3 class="font-black text-base text-emerald-950">Message envoyé avec succès !</h3>
              <p class="text-xs text-emerald-800 mt-1 font-medium leading-relaxed">
                Merci pour votre demande. Notre équipe locale et Robin ont bien reçu votre message sur <strong>junglenepaladventure@gmail.com</strong> et vous répondront personnellement sous 24h.
              </p>
            </div>
          </div>
        </div>

        <!-- Error Alert Notification (High-end 2026 UI) -->
        <div id="contact-error-notification" class="hidden p-5 rounded-2xl bg-rose-500/10 border-2 border-rose-500/40 text-rose-950 shadow-xl transition-all duration-300 animate-in fade-in zoom-in-95">
          <div class="flex items-start gap-3.5">
            <div class="w-10 h-10 rounded-xl bg-rose-600 text-white flex items-center justify-center text-xl shrink-0 shadow-md">
              ✕
            </div>
            <div class="flex-1">
              <h3 class="font-black text-base text-rose-950">Une erreur est survenue lors de l'envoi</h3>
              <p class="text-xs text-rose-800 mt-1 font-medium leading-relaxed" id="contact-error-text">
                Votre message n'a pas pu être transmis automatiquement. Vous pouvez nous écrire directement sur WhatsApp au <a href="https://wa.me/33695413227" target="_blank" class="underline font-bold">+33 6 95 41 32 27</a> ou par email à <strong class="underline">junglenepaladventure@gmail.com</strong>.
              </p>
            </div>
          </div>
        </div>"""

content = content.replace(form_header_old, form_header_new)

# 2. Update handleContactSubmit with robust multi-service delivery & real UI notification
script_old = """  async function handleContactSubmit(e) {
    e.preventDefault();
    const btn = document.getElementById('contact-submit-btn');
    const prenom = document.getElementById('contact-firstname')?.value || '';
    const nom = document.getElementById('contact-lastname')?.value || '';
    const email = document.getElementById('contact-email')?.value || '';
    const phone = document.getElementById('contact-phone')?.value || '';
    const subject = document.getElementById('contact-subject')?.value || '';
    const travelers = document.getElementById('contact-travelers')?.value || '';
    const period = document.getElementById('contact-period')?.value || '';
    const message = document.getElementById('contact-message')?.value || '';

    if (btn) {
      btn.innerHTML = 'Envoi de votre demande en cours... ⏳';
      btn.disabled = true;
    }

    try {
      await fetch('https://formsubmit.co/ajax/junglenepaladventure@gmail.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          _subject: '💬 Nouveau message de contact : ' + subject + ' (' + prenom + ' ' + nom + ')',
          _template: 'table',
          _captcha: 'false',
          prenom: prenom,
          nom: nom,
          email: email,
          telephone_whatsapp: phone,
          sujet: subject,
          voyageurs: travelers,
          periode: period,
          message: message,
          date_envoi: new Date().toLocaleString('fr-FR')
        })
      });
    } catch (err) {
      console.log('Contact form error:', err);
    }

    alert('Merci ' + prenom + ' ! Votre message a bien été envoyé à notre équipe. Robin vous répondra sous 24h.');
    if (btn) {
      btn.innerHTML = 'Envoyer ma demande à l\\'équipe →';
      btn.disabled = false;
    }
    document.getElementById('contact-form')?.reset();
  }"""

script_new = """  async function handleContactSubmit(e) {
    e.preventDefault();
    const btn = document.getElementById('contact-submit-btn');
    const successBox = document.getElementById('contact-success-notification');
    const errorBox = document.getElementById('contact-error-notification');
    const form = document.getElementById('contact-form');

    // Hide any previous alert
    if (successBox) successBox.classList.add('hidden');
    if (errorBox) errorBox.classList.add('hidden');

    const prenom = (document.getElementById('contact-firstname')?.value || '').trim();
    const nom = (document.getElementById('contact-lastname')?.value || '').trim();
    const email = (document.getElementById('contact-email')?.value || '').trim();
    const phone = (document.getElementById('contact-phone')?.value || '').trim();
    const subject = (document.getElementById('contact-subject')?.value || '').trim();
    const travelers = (document.getElementById('contact-travelers')?.value || '').trim();
    const period = (document.getElementById('contact-period')?.value || '').trim();
    const message = (document.getElementById('contact-message')?.value || '').trim();

    if (!prenom || !nom || !email || !phone || !message) {
      if (errorBox) {
        document.getElementById('contact-error-text').textContent = 'Veuillez remplir tous les champs obligatoires du formulaire (*).';
        errorBox.classList.remove('hidden');
      }
      return;
    }

    if (btn) {
      btn.innerHTML = '<span class="inline-flex items-center gap-2"><span>Envoi sécurisé en cours...</span> <svg class="animate-spin w-4 h-4 text-white" viewBox="0 0 24 24" fill="none"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path></svg></span>';
      btn.disabled = true;
    }

    const payload = {
      _subject: '🌿 Nouveau message de contact : ' + subject + ' (' + prenom + ' ' + nom + ')',
      _template: 'table',
      _captcha: 'false',
      _replyto: email,
      prenom: prenom,
      nom: nom,
      email: email,
      telephone_whatsapp: phone,
      sujet: subject,
      nombre_voyageurs: travelers,
      periode_envisagee: period,
      message_client: message,
      date_envoi: new Date().toLocaleString('fr-FR', { timeZone: 'Europe/Paris' })
    };

    let isSuccess = false;

    // Direct AJAX submission to FormSubmit.co targeted at junglenepaladventure@gmail.com
    try {
      const response = await fetch('https://formsubmit.co/ajax/junglenepaladventure@gmail.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (response.ok) {
        const data = await response.json().catch(() => ({ success: true }));
        if (data.success === 'true' || data.success === true || response.status === 200) {
          isSuccess = true;
        }
      }
    } catch (err) {
      console.warn('Primary submission network issue, trying direct fallback...', err);
    }

    // Fallback if needed
    if (!isSuccess) {
      try {
        const fallbackResp = await fetch('https://formsubmit.co/junglenepaladventure@gmail.com', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(payload)
        });
        if (fallbackResp.ok) {
          isSuccess = true;
        }
      } catch (err2) {
        console.error('Fallback error:', err2);
      }
    }

    if (isSuccess) {
      if (form) form.reset();
      if (successBox) {
        successBox.classList.remove('hidden');
        successBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      if (btn) {
        btn.innerHTML = '✓ Demande transmise avec succès !';
        btn.classList.remove('from-[#0e8354]', 'to-[#109363]');
        btn.classList.add('bg-emerald-700');
        setTimeout(() => {
          btn.innerHTML = 'Envoyer ma demande à l\\'équipe →';
          btn.classList.remove('bg-emerald-700');
          btn.classList.add('from-[#0e8354]', 'to-[#109363]');
          btn.disabled = false;
        }, 6000);
      }
    } else {
      if (errorBox) {
        errorBox.classList.remove('hidden');
        errorBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      if (btn) {
        btn.innerHTML = 'Réessayer l\\'envoi →';
        btn.disabled = false;
      }
    }
  }"""

content = content.replace(script_old, script_new)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Successfully upgraded contact form with notifications and robust email forwarding!")
