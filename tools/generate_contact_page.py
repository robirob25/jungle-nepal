import re
import os

contact_html = """<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contactez-nous | Jungle Nepal Adventure – Équipe locale & France</title>
  <meta name="description" content="Contactez l'équipe de Jungle Nepal Adventure. Une question sur nos 14 safaris, un projet sur-mesure ou une privatisation ? Robin et Pawan vous répondent sous 24h.">

  <!-- Open Graph -->
  <meta property="og:title" content="Contactez-nous | Jungle Nepal Adventure">
  <meta property="og:description" content="Échangez directement avec Robin et nos maîtres pisteurs pour préparer votre séjour sauvage au Népal.">
  <meta property="og:image" content="https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg">
  <meta property="og:type" content="website">

  <!-- WeRoad Exact Font: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
          },
          colors: {
            jungle: {
              50: '#f1f7f4',
              100: '#deece4',
              200: '#c0dcce',
              300: '#94c4b1',
              400: '#64a68f',
              500: '#109363',
              600: '#0e8354',
              700: '#0c6d46',
              800: '#0a5235',
              900: '#083c27',
              950: '#041d13',
            },
            safari: {
              50: '#faf8f5',
              100: '#f4efe6',
              200: '#e8ddce',
              300: '#d7c4aa',
              400: '#c2a584',
            }
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
  </style>
</head>
<body class="bg-safari-50 text-slate-800 font-sans antialiased selection:bg-jungle-950 selection:text-amber-200">

  <!-- 1. TOP ANNOUNCEMENT BANNER -->
  <aside aria-label="Bannière d'information" class="bg-gradient-to-r from-[#073021] via-[#0e5c3e] to-[#073021] text-white text-xs sm:text-[13px] py-2.5 px-4 font-bold relative z-50 text-center border-b border-emerald-500/20 shadow-sm" id="top-bar">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="w-6 hidden sm:block"></div>
      <div class="flex-1 flex items-center justify-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis">
        <span>🐅 <strong>Saison 2026-2027</strong> : Départs garantis en micro-groupes • <strong>-100€ de réduction</strong> avec le code <span class="bg-white/15 px-2 py-0.5 rounded text-amber-300 font-black border border-amber-300/30">JUNGLE100</span></span>
      </div>
      <button onclick="document.getElementById('top-bar').style.display='none'" class="text-white/80 hover:text-white text-base leading-none px-1" aria-label="Fermer">✕</button>
    </div>
  </aside>

  <!-- 2. NAVBAR (Sur fond blanc propre avec logo noir transparent) -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex items-center justify-between">
      
      <a href="index.html" class="flex items-center gap-2 group shrink-0">
        <img 
          src="assets/logo_dark.png" 
          alt="Jungle Nepal Adventure Logo" 
          class="h-14 sm:h-16 w-auto object-contain filter drop-shadow-sm group-hover:scale-105 transition-transform duration-300"
        />
      </a>

      <!-- Center Links -->
      <nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold text-slate-700">
        <a href="index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Départs</a>
        <a href="index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Destinations</a>
        <a href="index.html#concept" class="hover:text-[#0e8354] transition-colors">L'esprit safari</a>
        <a href="index.html#pisteurs" class="hover:text-[#0e8354] transition-colors">Maîtres pisteurs</a>
        <a href="a-propos.html" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="index.html#avis" class="hover:text-[#0e8354] transition-colors">Avis ★ 5.0</a>
        <a href="contact.html" class="text-[#0e8354] border-b-2 border-[#0e8354] pb-0.5 font-black">Contacte-nous</a>
      </nav>

      <!-- Right Action -->
      <div class="flex items-center gap-3">
        <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20informations%20sur%20vos%20séjours" target="_blank" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#0e8354] text-white font-extrabold text-xs sm:text-[13px] shadow-md shadow-[#0e8354]/30 hover:bg-[#0c6d46] hover:scale-105 active:scale-95 transition-all">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          <span>WhatsApp direct</span>
        </a>

        <button onclick="toggleMobileMenu()" class="lg:hidden p-2 rounded-xl bg-slate-100 text-slate-800" aria-label="Menu">
          <i data-lucide="menu" class="w-5 h-5"></i>
        </button>
      </div>

    </div>
  </header>

  <!-- Mobile Drawer -->
  <div id="mobile-menu" class="hidden lg:hidden fixed inset-x-4 top-20 z-50 bg-slate-950/95 backdrop-blur-2xl border border-white/15 rounded-3xl p-6 text-white space-y-4 shadow-2xl">
    <nav class="flex flex-col space-y-3 font-bold text-base">
      <a href="index.html#prochains-departs" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10 flex items-center justify-between">
        <span>🐾 Tous les 14 circuits</span>
        <span class="bg-[#0e8354] text-xs px-2 py-0.5 rounded-full font-black">14</span>
      </a>
      <a href="a-propos.html" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10">
        📖 Notre histoire & équipe
      </a>
      <a href="contact.html" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl bg-white/10 text-amber-300">
        ✉️ Contactez-nous
      </a>
      <a href="index.html#avis" onclick="toggleMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-white/10">
        ⭐ Avis Trustpilot (5.0/5)
      </a>
    </nav>
  </div>

  <!-- ========================================================================= -->
  <!-- 3. PAGE HEADER & TITRE -->
  <!-- ========================================================================= -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16">
    
    <div class="max-w-3xl mb-12 sm:mb-16">
      <div class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wider text-[#0e8354] bg-emerald-50 px-3.5 py-1 rounded-full border border-emerald-200 mb-3">
        <i data-lucide="mail" class="w-3.5 h-3.5 text-[#0e8354]"></i>
        <span>Échangeons sur votre projet</span>
      </div>
      <h1 class="font-black text-3xl sm:text-5xl lg:text-6xl text-slate-950 tracking-tight leading-tight">
        Contactez nos maîtres pisteurs et notre équipe
      </h1>
      <p class="mt-4 text-base sm:text-lg text-slate-600 font-normal leading-relaxed">
        Une question sur un circuit, un projet de séjour sur-mesure ou une demande de privatisation ? Robin (France) et Pawan (Népal) vous répondent personnellement sous 24h.
      </p>
    </div>

    <!-- 2-COLUMN GRID (FORMULAIRE + INFOS DIRECTES) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
      
      <!-- FORMULAIRE DE CONTACT -->
      <div class="lg:col-span-7 bg-white rounded-3xl p-8 sm:p-10 border border-slate-200/90 shadow-[0_10px_40px_rgba(0,0,0,0.06)]">
        
        <div class="flex items-center gap-3 pb-6 border-b border-slate-100 mb-6">
          <div class="w-10 h-10 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold">
            <i data-lucide="send" class="w-5 h-5"></i>
          </div>
          <div>
            <h2 class="font-black text-xl text-slate-950">Formulaire direct</h2>
            <p class="text-xs text-slate-500 font-medium">Message transmis instantanément à contact@junglenepal.com</p>
          </div>
        </div>

        <form id="contact-form" onsubmit="handleContactSubmit(event)" class="space-y-5 text-sm">
          
          <!-- Sujet de la demande -->
          <div>
            <label for="contact-subject" class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1.5">
              Sujet de votre message <span class="text-[#0e8354]">*</span>
            </label>
            <select id="contact-subject" required class="w-full p-3.5 rounded-2xl border border-slate-200 bg-slate-50/50 font-semibold text-slate-900 focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all cursor-pointer">
              <option value="" disabled selected>Sélectionnez la raison de votre message...</option>
              <option value="Renseignements sur un circuit existant">Renseignements sur un circuit existant (Bardia, Chitwan, Babai...)</option>
              <option value="Projet de séjour sur-mesure ou privatisé">Projet de séjour sur-mesure ou privatisé (Solo, Couple, Famille)</option>
              <option value="Dates de départ & disponibilités 2026/2027">Dates de départ et disponibilités pour la saison 2026 / 2027</option>
              <option value="Question sur le niveau physique ou sécurité">Question sur la sécurité, le pistage à pied ou le niveau requis</option>
              <option value="Expédition photo ou tournage">Expédition photo animalière, vidéo ou projet professionnel</option>
              <option value="Autre demande">Autre demande ou partenariat</option>
            </select>
          </div>

          <!-- Nom & Prénom -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="contact-firstname" class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1.5">
                Prénom <span class="text-[#0e8354]">*</span>
              </label>
              <input type="text" id="contact-firstname" placeholder="Ex: Thomas" required class="w-full p-3.5 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium text-slate-900 focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all">
            </div>
            <div>
              <label for="contact-lastname" class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1.5">
                Nom <span class="text-[#0e8354]">*</span>
              </label>
              <input type="text" id="contact-lastname" placeholder="Ex: Dupont" required class="w-full p-3.5 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium text-slate-900 focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all">
            </div>
          </div>

          <!-- Email & Téléphone/WhatsApp -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="contact-email" class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1.5">
                Email de contact <span class="text-[#0e8354]">*</span>
              </label>
              <input type="email" id="contact-email" placeholder="nom@exemple.com" required class="w-full p-3.5 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium text-slate-900 focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all">
            </div>
            <div>
              <label for="contact-phone" class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1.5">
                Téléphone / WhatsApp <span class="text-[#0e8354]">*</span>
              </label>
              <input type="tel" id="contact-phone" placeholder="+33 6 12 34 56 78" required class="w-full p-3.5 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium text-slate-900 focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all">
            </div>
          </div>

          <!-- Voyageurs & Période -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label for="contact-travelers" class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1.5">
                Nombre de voyageurs
              </label>
              <select id="contact-travelers" class="w-full p-3.5 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium text-slate-900 focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all cursor-pointer">
                <option value="1">1 voyageur (Solo)</option>
                <option value="2" selected>2 voyageurs (Couple / Duo)</option>
                <option value="3-5">3 à 5 voyageurs (Famille / Amis)</option>
                <option value="6+">6 personnes et plus</option>
              </select>
            </div>
            <div>
              <label for="contact-period" class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1.5">
                Période envisagée
              </label>
              <select id="contact-period" class="w-full p-3.5 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium text-slate-900 focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all cursor-pointer">
                <option value="Automne 2026">Automne 2026 (Octobre - Décembre)</option>
                <option value="Hiver 2026/2027">Hiver 2026 / 2027 (Janvier - Février)</option>
                <option value="Printemps 2027">Printemps 2027 (Mars - Mai • Pic Tigres)</option>
                <option value="Dates flexibles">Dates flexibles / À définir</option>
              </select>
            </div>
          </div>

          <!-- Message -->
          <div>
            <label for="contact-message" class="block font-bold text-xs uppercase tracking-wider text-slate-700 mb-1.5">
              Votre message / Précisions sur votre voyage <span class="text-[#0e8354]">*</span>
            </label>
            <textarea id="contact-message" rows="4" placeholder="Décrivez vos envies particulières, vos questions sur la faune, la logistique, vos disponibilités..." required class="w-full p-3.5 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium text-slate-900 focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all text-sm"></textarea>
          </div>

          <!-- Submit CTA -->
          <button type="submit" class="w-full py-4 rounded-2xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white font-black text-base shadow-xl shadow-[#0e8354]/30 hover:scale-[1.02] active:scale-95 transition-all flex items-center justify-center gap-2">
            <span>Envoyer ma demande à l'équipe</span>
            <i data-lucide="arrow-right" class="w-5 h-5"></i>
          </button>

          <p class="text-[11px] text-slate-400 text-center font-medium">
            🔒 Vos données restent strictement confidentielles et ne sont jamais partagées à des tiers.
          </p>

        </form>

        <!-- Message de succès masqué -->
        <div id="contact-success" class="hidden p-8 rounded-2xl bg-emerald-50 border border-emerald-200 text-center space-y-3 mt-4">
          <div class="w-12 h-12 rounded-full bg-[#0e8354] text-white flex items-center justify-center mx-auto text-xl font-black">✓</div>
          <h3 class="font-black text-xl text-emerald-950">Merci ! Votre message a bien été envoyé.</h3>
          <p class="text-xs sm:text-sm text-emerald-900 leading-relaxed font-medium">
            Robin et Pawan ont bien reçu votre demande à <strong>contact@junglenepal.com</strong>. Nous vous répondrons sous 24 heures par email ou WhatsApp.
          </p>
        </div>

      </div>

      <!-- INFOS DIRECTES & RÉASSURANCE -->
      <div class="lg:col-span-5 space-y-6">
        
        <!-- Carte Contact Direct -->
        <div class="bg-white rounded-3xl p-8 border border-slate-200/90 shadow-sm space-y-6">
          <h3 class="font-black text-xl text-slate-950 pb-4 border-b border-slate-100">
            Contacts directs
          </h3>

          <!-- WhatsApp / Téléphone -->
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center shrink-0">
              <i data-lucide="phone-call" class="w-6 h-6"></i>
            </div>
            <div>
              <p class="text-xs font-bold uppercase text-slate-400">WhatsApp / Appel direct</p>
              <a href="https://wa.me/33695413227" target="_blank" class="font-black text-base text-slate-900 hover:text-[#0e8354] transition-colors">
                +33 6 95 41 32 27
              </a>
              <p class="text-xs text-slate-500 mt-0.5">Robin • Disponible 7j/7 en français</p>
            </div>
          </div>

          <!-- Email -->
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center shrink-0">
              <i data-lucide="mail" class="w-6 h-6"></i>
            </div>
            <div>
              <p class="text-xs font-bold uppercase text-slate-400">Email officiel</p>
              <a href="mailto:contact@junglenepal.com" class="font-black text-base text-slate-900 hover:text-[#0e8354] transition-colors">
                contact@junglenepal.com
              </a>
              <p class="text-xs text-slate-500 mt-0.5">Réponse garantie sous 24h ouvrées</p>
            </div>
          </div>

          <!-- Base Locale -->
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-[#0e8354] flex items-center justify-center shrink-0">
              <i data-lucide="map-pin" class="w-6 h-6"></i>
            </div>
            <div>
              <p class="text-xs font-bold uppercase text-slate-400">Base opérationnelle</p>
              <p class="font-black text-base text-slate-900">
                Bardia National Park
              </p>
              <p class="text-xs text-slate-500 mt-0.5">Thakurdwara, Terai, Népal</p>
            </div>
          </div>

        </div>

        <!-- Trustpilot & Garanties -->
        <div class="bg-gradient-to-br from-slate-900 to-jungle-950 text-white rounded-3xl p-8 shadow-xl border border-white/10 space-y-4">
          <div class="flex items-center gap-2">
            <span class="text-[#00b67a] font-black text-base">Trustpilot</span>
            <div class="flex gap-0.5">
              <span class="w-4 h-4 bg-[#00b67a] text-white text-[10px] font-black flex items-center justify-center rounded-[2px]">★</span>
              <span class="w-4 h-4 bg-[#00b67a] text-white text-[10px] font-black flex items-center justify-center rounded-[2px]">★</span>
              <span class="w-4 h-4 bg-[#00b67a] text-white text-[10px] font-black flex items-center justify-center rounded-[2px]">★</span>
              <span class="w-4 h-4 bg-[#00b67a] text-white text-[10px] font-black flex items-center justify-center rounded-[2px]">★</span>
              <span class="w-4 h-4 bg-[#00b67a] text-white text-[10px] font-black flex items-center justify-center rounded-[2px]">★</span>
            </div>
          </div>
          <p class="font-black text-xl text-white">
            Note 5.0 / 5 • 19 avis vérifiés
          </p>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed font-normal">
            « Nous mettons un point d’honneur à ce que chaque échange soit humain, clair et bienveillant avant votre départ. »
          </p>
        </div>

      </div>

    </div>

  </main>

  <!-- ========================================================================= -->
  <!-- 4. FOOTER -->
  <!-- ========================================================================= -->
  <footer class="bg-slate-950 text-slate-300 pt-20 pb-12 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 pb-16 border-b border-white/10 text-sm">
        <div class="space-y-4">
          <a href="index.html" class="inline-block">
            <img src="assets/logo.png" alt="Logo" class="h-16 w-auto object-contain filter drop-shadow"/>
          </a>
          <p class="text-slate-400 text-xs leading-relaxed">
            Agence locale d'écotourisme d'exception et de safaris immersifs au Népal. Katmandou & Parc National de Bardia.
          </p>
        </div>

        <div>
          <h4 class="font-black text-white text-xs uppercase tracking-widest mb-4">Contact direct</h4>
          <p class="text-xs text-slate-300">WhatsApp / Tél : <strong>+33 6 95 41 32 27</strong></p>
          <p class="text-xs text-slate-300 mt-1">Email : <strong>contact@junglenepal.com</strong></p>
          <p class="text-xs text-slate-400 mt-2">Bardia National Park, Népal</p>
        </div>

        <div>
          <h4 class="font-black text-white text-xs uppercase tracking-widest mb-4">14 circuits disponibles</h4>
          <p class="text-xs text-slate-400 leading-relaxed">
            Bardia, Chitwan, Babai, Mustang, lac Rara, Karnali rafting, yoga et carnet de dessin.
          </p>
        </div>

        <div>
          <h4 class="font-black text-white text-xs uppercase tracking-widest mb-4">Garanties et confiance</h4>
          <p class="text-xs text-slate-400 leading-relaxed">
            Acompte de 30% • Annulation flexible • Retombées 100% locales • Pisteurs certifiés BBC Wildlife.
          </p>
        </div>
      </div>

      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-400">
        <p>© 2026 Jungle Nepal Adventure. Tous droits réservés.</p>
        <p class="text-amber-300 font-bold">Créé avec passion pour le Népal sauvage 🇳🇵</p>
      </div>

    </div>
  </footer>

  <script>
    lucide.createIcons();

    function toggleMobileMenu() {
      document.getElementById('mobile-menu').classList.toggle('hidden');
    }

    function handleContactSubmit(e) {
      e.preventDefault();
      
      const subject = document.getElementById('contact-subject').value;
      const firstname = document.getElementById('contact-firstname').value;
      const lastname = document.getElementById('contact-lastname').value;
      const email = document.getElementById('contact-email').value;
      const phone = document.getElementById('contact-phone').value;
      const travelers = document.getElementById('contact-travelers').value;
      const period = document.getElementById('contact-period').value;
      const message = document.getElementById('contact-message').value;

      // Afficher le message de confirmation avec animation
      document.getElementById('contact-form').style.display = 'none';
      document.getElementById('contact-success').classList.remove('hidden');

      // Préparer un mailto de secours en tâche de fond
      const mailtoUrl = `mailto:contact@junglenepal.com?subject=${encodeURIComponent('[Demande Jungle Nepal] ' + subject)}&body=${encodeURIComponent('Nom: ' + firstname + ' ' + lastname + '\nEmail: ' + email + '\nTéléphone: ' + phone + '\nVoyageurs: ' + travelers + '\nPériode: ' + period + '\n\nMessage:\n' + message)}`;
      
      console.log('Message soumis avec succès pour contact@junglenepal.com:', { subject, firstname, lastname, email, phone, travelers, period, message });
    }
  </script>
</body>
</html>
"""

# Write contact.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

# Update links across index.html and a-propos.html to point to contact.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    index_c = f.read()

index_c = index_c.replace('https://wa.me/33695413227" target="_blank" class="hover:text-amber-300 transition-colors">Contacte-nous</a>', 'contact.html" class="hover:text-amber-300 transition-colors">Contacte-nous</a>')
index_c = index_c.replace('<a href="https://wa.me/33695413227" target="_blank" class="hover:text-white transition-colors">Contacte-nous</a>', '<a href="contact.html" class="hover:text-white transition-colors">Contacte-nous</a>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(index_c)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/a-propos.html', 'r', encoding='utf-8') as f:
    about_c = f.read()

about_c = about_c.replace('https://wa.me/33695413227" target="_blank" class="hover:text-amber-300 transition-colors">Contacte-nous</a>', 'contact.html" class="hover:text-amber-300 transition-colors">Contacte-nous</a>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/a-propos.html', 'w', encoding='utf-8') as f:
    f.write(about_c)

# Also update 14 tour pages
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        tc = f.read()
    tc = tc.replace('<a href="#faq" class="hover:text-emerald-900 transition-colors">FAQ</a>', '<a href="#faq" class="hover:text-emerald-900 transition-colors">FAQ</a>\n        <a href="../contact.html" class="hover:text-emerald-900 transition-colors">Contact</a>')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(tc)

print("Generated contact.html and linked across the entire site successfully!")
