with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old handleContactSubmit in the script tag
old_handle_start = "  // Contact form submission to junglenepaladventure@gmail.com"
old_handle_end = "  // Header and UI scripts"

new_handle = """  // Contact form submission to junglenepaladventure@gmail.com
  async function handleContactSubmit(e) {
    if (e && e.preventDefault) e.preventDefault();
    
    const btn = document.getElementById('contact-submit-btn');
    const successBox = document.getElementById('contact-success-notification');
    const errorBox = document.getElementById('contact-error-notification');
    const form = document.getElementById('contact-form');

    // Hide alerts
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
        document.getElementById('contact-error-text').textContent = 'Veuillez remplir tous les champs obligatoires (*).';
        errorBox.classList.remove('hidden');
        errorBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      return false;
    }

    if (btn) {
      btn.innerHTML = '<span class="inline-flex items-center justify-center gap-2"><span>Envoi en cours...</span> <svg class="animate-spin w-4 h-4 text-white" viewBox="0 0 24 24" fill="none"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path></svg></span>';
      btn.disabled = true;
    }

    const payload = {
      _subject: '🌿 Nouveau message de contact : ' + (subject || 'Demande de séjour') + ' (' + prenom + ' ' + nom + ')',
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
      date_envoi: new Date().toLocaleString('fr-FR')
    };

    let sent = false;

    // 1. Try AJAX to FormSubmit
    try {
      const res = await fetch('https://formsubmit.co/ajax/junglenepaladventure@gmail.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(payload)
      });
      const data = await res.json().catch(() => ({}));
      if (res.ok || data.success === "true" || data.success === true) {
        sent = true;
      }
    } catch (err) {
      console.warn('FormSubmit AJAX attempt error:', err);
    }

    // 2. Fallback using FormSubmit standard post or mailto/webhook if needed
    if (!sent) {
      try {
        const res2 = await fetch('https://formsubmit.co/junglenepaladventure@gmail.com', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(payload)
        });
        if (res2.ok) {
          sent = true;
        }
      } catch (err2) {
        console.warn('Fallback error:', err2);
      }
    }

    // Always notify the user clearly
    if (sent) {
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
        }, 5000);
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
    return false;
  }

  """

idx_start = content.find(old_handle_start)
idx_end = content.find(old_handle_end)

if idx_start != -1 and idx_end != -1:
    content = content[:idx_start] + new_handle + content[idx_end:]
    with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully injected updated handleContactSubmit!")
else:
    print("Could not find start/end marks in contact.astro")
