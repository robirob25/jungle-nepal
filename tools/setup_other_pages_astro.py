# 1. Destinations Hub: src/pages/destinations/index.astro
dest_hub = """---
import Layout from '../../layouts/Layout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import destinationsData from '../../data/destinations.json';
---

<Layout 
  title="Toutes les Destinations Sauvages du Népal"
  description="Découvrez les 5 territoires d'exception au Népal : Bardia, Chitwan, Suklaphanta, Annapurna et Vallée de Katmandou."
  lang="fr"
  isDarkHeader={true}
>
  <Header lang="fr" currentPath="/destinations" />

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 font-sans space-y-12">
    
    <div class="text-center max-w-3xl mx-auto space-y-4">
      <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">TERRITOIRES D'EXCEPTION</span>
      <h1 class="text-3xl sm:text-5xl font-black text-slate-950 tracking-tight">
        Les 5 Sanctuaires Sauvages du Népal
      </h1>
      <p class="text-slate-600 text-base sm:text-lg leading-relaxed">
        Des jungles tropicales du Teraï peuplées de tigres et rhinocéros aux crêtes majestueuses de l'Himalaya.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {destinationsData.map((dest) => (
        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col group">
          <div class="relative h-56 overflow-hidden">
            <img src={dest.heroImage} alt={dest.name} class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
            <div class="absolute top-4 left-4">
              <span class="text-2xl p-2 rounded-2xl bg-white/90 backdrop-blur-md shadow-md block">
                {dest.icon}
              </span>
            </div>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <h3 class="font-black text-xl text-slate-950 group-hover:text-[#0e8354] transition-colors">
                {dest.name}
              </h3>
              <p class="text-xs font-bold text-[#0e8354] mt-1">{dest.tagline}</p>
              <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                {dest.desc}
              </p>
            </div>
            <a href={`/destinations/${dest.slug}`} class="w-full py-3 rounded-2xl bg-slate-950 hover:bg-[#0e8354] text-white font-bold text-xs text-center transition-colors shadow">
              Explorer cette destination →
            </a>
          </div>
        </div>
      ))}
    </div>

  </main>

  <Footer lang="fr" />
</Layout>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro', 'w', encoding='utf-8') as f:
    f.write(dest_hub)

en_dest_hub = dest_hub.replace('lang="fr"', 'lang="en"').replace('currentPath="/destinations"', 'currentPath="/en/destinations"')
en_dest_hub = en_dest_hub.replace('TERRITOIRES D\'EXCEPTION', 'EXCEPTIONAL SANCTUARIES')
en_dest_hub = en_dest_hub.replace('Les 5 Sanctuaires Sauvages du Népal', 'The 5 Wild Sanctuaries of Nepal')
en_dest_hub = en_dest_hub.replace('Explorer cette destination →', 'Explore this destination →')
en_dest_hub = en_dest_hub.replace('href={`/destinations/${dest.slug}`}', 'href={`/en/destinations/${dest.slug}`}')
en_dest_hub = en_dest_hub.replace('<Footer lang="fr" />', '<Footer lang="en" />')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/destinations/index.astro', 'w', encoding='utf-8') as f:
    f.write(en_dest_hub)

# 2. À propos: src/pages/a-propos.astro
about_astro = """---
import Layout from '../layouts/Layout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
---

<Layout 
  title="Notre Histoire & Équipe – Jungle Nepal Adventure"
  description="Découvrez les fondateurs de Jungle Nepal Adventure : Robin, Pawan et Kiran. Une agence née de l'amour du Népal sauvage et du respect de la faune."
  lang="fr"
  isDarkHeader={true}
>
  <Header lang="fr" currentPath="/a-propos" />

  <main class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-16 font-sans space-y-16">
    
    <div class="text-center max-w-3xl mx-auto space-y-4">
      <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">NOTRE HISTOIRE</span>
      <h1 class="text-3xl sm:text-5xl font-black text-slate-950 tracking-tight">
        L'Amour du Népal Sauvage & des Maîtres Pisteurs
      </h1>
      <p class="text-slate-600 text-base sm:text-lg leading-relaxed">
        Jungle Nepal Adventure est née d'une rencontre entre Robin, passionné de faune sauvage, et Pawan & Kiran, maîtres pisteurs natifs du parc national de Bardia.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center bg-white p-8 rounded-3xl border border-slate-200/90 shadow-sm">
      <img src="https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png" alt="Safari Bardia" class="rounded-2xl w-full h-[320px] object-cover shadow" />
      <div class="space-y-4">
        <h2 class="text-2xl font-black text-slate-950">Notre Philosophie Éthique</h2>
        <p class="text-sm text-slate-700 leading-relaxed">
          Nous refusons le tourisme de masse et les abus envers les animaux. Chez nous, aucun safari à dos d'éléphant : nous marchons à pied dans la jungle avec nos pisteurs pour écouter les bruits de la forêt et approcher les animaux dans le respect le plus absolu de leur territoire.
        </p>
        <div class="pt-2">
          <a href="/#prochains-departs" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-bold text-xs transition-all">
            <span>Découvrir nos séjours</span>
            <span>→</span>
          </a>
        </div>
      </div>
    </div>

    <!-- Contact direct -->
    <div class="bg-slate-950 text-white p-8 sm:p-12 rounded-3xl text-center space-y-6">
      <h3 class="text-2xl sm:text-3xl font-black">Envie d'échanger sur votre projet de voyage ?</h3>
      <p class="text-slate-300 max-w-xl mx-auto text-sm">
        Robin répond directement à toutes vos questions sur WhatsApp pour vous conseiller le séjour idéal selon la saison.
      </p>
      <a href="https://wa.me/33695413227" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-white text-slate-950 font-black text-sm hover:bg-emerald-50 hover:scale-105 transition-all shadow-xl">
        <span>Échanger sur WhatsApp (+33 6 95 41 32 27)</span>
        <span>→</span>
      </a>
    </div>

  </main>

  <Footer lang="fr" />
</Layout>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(about_astro)

en_about = about_astro.replace('lang="fr"', 'lang="en"').replace('currentPath="/a-propos"', 'currentPath="/en/a-propos"')
en_about = en_about.replace('NOTRE HISTOIRE', 'OUR STORY')
en_about = en_about.replace('L\'Amour du Népal Sauvage & des Maîtres Pisteurs', 'Love for Wild Nepal & Master Trackers')
en_about = en_about.replace('Notre Philosophie Éthique', 'Our Ethical Philosophy')
en_about = en_about.replace('Découvrir nos séjours', 'Explore our expeditions')
en_about = en_about.replace('/#prochains-departs', '/en#prochains-departs')
en_about = en_about.replace('Envie d\'échanger sur votre projet de voyage ?', 'Want to discuss your trip to Nepal?')
en_about = en_about.replace('Échanger sur WhatsApp', 'Chat on WhatsApp')
en_about = en_about.replace('<Footer lang="fr" />', '<Footer lang="en" />')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(en_about)

# 3. Contact: src/pages/contact.astro
contact_astro = """---
import Layout from '../layouts/Layout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
---

<Layout 
  title="Contactez-nous & Devis – Jungle Nepal Adventure"
  description="Contactez Robin pour réserver votre séjour ou créer votre expédition sur-mesure au Népal."
  lang="fr"
  isDarkHeader={true}
>
  <Header lang="fr" currentPath="/contact" />

  <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16 font-sans space-y-12">
    
    <div class="text-center space-y-4">
      <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">DISCUTONS DE VOTRE SÉJOUR</span>
      <h1 class="text-3xl sm:text-5xl font-black text-slate-950 tracking-tight">
        Contactez l'Équipe
      </h1>
      <p class="text-slate-600 text-base sm:text-lg max-w-xl mx-auto">
        Une question sur les dates, l'acompte de 30% ou la condition physique ? Nous sommes à votre écoute 7j/7.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      
      <div class="bg-white p-8 rounded-3xl border border-slate-200/90 shadow-sm space-y-6">
        <h3 class="font-black text-xl text-slate-950">WhatsApp Direct</h3>
        <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
          Le moyen le plus rapide pour obtenir une réponse immédiate de Robin sur la disponibilité des séjours.
        </p>
        <a href="https://wa.me/33695413227" target="_blank" rel="noopener noreferrer" class="w-full py-3.5 rounded-2xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs flex items-center justify-center gap-2 transition-all shadow-md">
          <span>Ouvrir WhatsApp (+33 6 95 41 32 27)</span>
          <span>→</span>
        </a>
      </div>

      <div class="bg-white p-8 rounded-3xl border border-slate-200/90 shadow-sm space-y-6">
        <h3 class="font-black text-xl text-slate-950">Email & Devis</h3>
        <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
          Envoyez-nous vos dates souhaitées et le nombre d'explorateurs pour recevoir un devis détaillé sous 24h.
        </p>
        <a href="mailto:contact@junglenepal.com" class="w-full py-3.5 rounded-2xl bg-slate-950 hover:bg-slate-800 text-white font-black text-xs flex items-center justify-center gap-2 transition-all shadow-md">
          <span>Envoyer un email (contact@junglenepal.com)</span>
          <span>→</span>
        </a>
      </div>

    </div>

  </main>

  <Footer lang="fr" />
</Layout>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'w', encoding='utf-8') as f:
    f.write(contact_astro)

en_contact = contact_astro.replace('lang="fr"', 'lang="en"').replace('currentPath="/contact"', 'currentPath="/en/contact"')
en_contact = en_contact.replace('DISCUTONS DE VOTRE SÉJOUR', 'PLAN YOUR EXPEDITION')
en_contact = en_contact.replace('Contactez l\'Équipe', 'Contact Our Team')
en_contact = en_contact.replace('Une question sur les dates, l\'acompte de 30% ou la condition physique ? Nous sommes à votre écoute 7j/7.', 'Any questions about dates, 30% deposit, or physical fitness? We are here 7 days a week.')
en_contact = en_contact.replace('Ouvrir WhatsApp', 'Open WhatsApp')
en_contact = en_contact.replace('Envoyer un email', 'Send an Email')
en_contact = en_contact.replace('<Footer lang="fr" />', '<Footer lang="en" />')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/contact.astro', 'w', encoding='utf-8') as f:
    f.write(en_contact)

print("Created all other pages (Destinations hub, A-propos, Contact) in French and English!")
