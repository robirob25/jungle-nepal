import os

# Create src/pages/tours/[slug].astro
tour_astro_content = """---
import Layout from '../../layouts/Layout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import toursData from '../../data/tours.json';

export async function getStaticPaths() {
  return toursData.map((tour) => ({
    params: { slug: tour.slug },
    props: { tour },
  }));
}

const { tour } = Astro.props;
const { slug } = Astro.params;

const titleClean = tour.title;
const titleEncoded = encodeURIComponent(titleClean);
const overviewClean = tour.overview.slice(0, 180);

function getDots(score: number) {
  let dots = [];
  for (let i = 0; i < 5; i++) {
    dots.push(i < score);
  }
  return dots;
}
---

<Layout 
  title={tour.title}
  description={overviewClean}
  image={tour.images[0]}
  lang="fr"
  isDarkHeader={true}
>
  <Header lang="fr" currentPath={`/tours/${slug}`} />

  <!-- MAIN TOUR CONTENT -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-24 font-sans">
    
    <!-- Breadcrumbs -->
    <nav class="flex items-center gap-2 text-xs text-slate-500 font-semibold mb-3 overflow-x-auto whitespace-nowrap">
      <a href="/" class="hover:text-slate-900 flex items-center gap-1">
        <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
        <span>Accueil</span>
      </a>
      <span>›</span>
      <a href="/#prochains-departs" class="hover:text-slate-900">Nos 14 Séjours</a>
      <span>›</span>
      <span class="text-slate-900 font-bold truncate">{tour.title}</span>
    </nav>

    <!-- Header Title & Badges Row -->
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6">
      <div>
        <h1 class="font-black text-2xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight">
          {tour.title}
        </h1>
        <div class="mt-3 flex flex-wrap items-center gap-3 text-xs sm:text-sm">
          <span class="inline-flex items-center gap-1.5 font-bold text-slate-700 bg-amber-50 border border-amber-200 px-3 py-1 rounded-full">
            <svg class="w-4 h-4 text-amber-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2"></path><path d="M12 20v2"></path><path d="m4.93 4.93 1.41 1.41"></path><path d="m17.66 17.66 1.41 1.41"></path><path d="M2 12h2"></path><path d="M20 12h2"></path><path d="m6.34 17.66-1.41 1.41"></path><path d="m19.07 4.93-1.41 1.41"></path></svg>
            <span>{tour.duration}</span>
          </span>
          <div class="inline-flex items-center gap-1.5 bg-emerald-50 text-emerald-900 font-bold px-3 py-1 rounded-full border border-emerald-200">
            <span class="text-amber-500">★</span>
            <span>{tour.rating} ({tour.reviews} avis vérifiés)</span>
          </div>
          <span class="text-xs font-bold bg-slate-900 text-amber-300 px-3 py-1 rounded-full border border-amber-300/30">
            {tour.badge}
          </span>
        </div>
      </div>

      <!-- BOUTON PARTAGER -->
      <div class="relative shrink-0">
        <button id="share-btn" onclick="handleShareTour()" class="flex items-center gap-2 px-4 py-2 rounded-xl border border-slate-200 bg-white text-xs font-extrabold text-slate-800 hover:text-[#0e8354] hover:border-[#0e8354] shadow-sm hover:shadow transition-all group cursor-pointer">
          <svg class="w-4 h-4 text-slate-500 group-hover:text-[#0e8354] transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"></line><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"></line></svg>
          <span>Partager ce séjour</span>
        </button>

        <!-- Dropdown Menu Partage Sombre Opaque (#041d13) -->
        <div id="share-menu" class="absolute right-0 top-full mt-2 w-64 opacity-0 translate-y-2 pointer-events-none transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-2 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-1 text-white">
            <button onclick="copyTourLink()" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Copier le lien direct</span>
            </button>
            <a id="share-whatsapp" href="#" target="_blank" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-[#25D366] flex items-center justify-center shrink-0">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Envoyer sur WhatsApp</span>
            </a>
            <a id="share-email" href="#" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-slate-300 flex items-center justify-center shrink-0">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Partager par Email</span>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- PHOTO MOSAIC GALLERY -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-3 rounded-3xl overflow-hidden h-[340px] sm:h-[460px] mb-8 relative shadow-lg">
      <div class="md:col-span-2 h-full overflow-hidden">
        <img src={tour.images[0]} alt={tour.title} class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(0)"/>
      </div>
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src={tour.images[1]} alt={tour.title} class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(1)"/>
      </div>
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img src={tour.images[2]} alt={tour.title} class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(2)"/>
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img src={tour.images[3]} alt={tour.title} class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(3)"/>
        </div>
      </div>

      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105 cursor-pointer">
        <svg class="w-4 h-4 text-[#0e8354]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path></svg>
        <span>Voir toutes les photos</span>
      </button>
    </div>

    <!-- STICKY SUB-NAV -->
    <div class="sticky top-[69px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8">
      <div class="flex items-center gap-6 overflow-x-auto text-xs sm:text-sm font-bold text-slate-600">
        <a href="#apercu" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Aperçu</a>
        <a href="#pour-moi" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Profil Voyage</a>
        <a href="#programme" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Itinéraire ({tour.daysCount}j)</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Inclus & Extras</a>
        <a href="#avis-voyageurs" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Avis</a>
        <a href="#faq" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">FAQ</a>
      </div>
    </div>

    <!-- 2-COLUMN MAIN CONTENT GRID -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <!-- LEFT COLUMN -->
      <div class="lg:col-span-8 space-y-12">
        
        <!-- SECTION 1: APERÇU -->
        <section id="apercu" class="space-y-6">
          <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
            {tour.overview}
          </p>

          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm">
            <h3 class="font-bold text-lg text-slate-950 mb-4 flex items-center gap-2">
              <span class="text-amber-500">✨</span>
              <span>Les temps forts du voyage</span>
            </h3>
            <ul class="space-y-3 text-sm sm:text-base text-slate-700">
              {tour.highlights.map((h: string) => (
                <li class="flex items-start gap-3">
                  <span class="w-2 h-2 rounded-full bg-[#0e8354] mt-2 shrink-0"></span>
                  <span>{h}</span>
                </li>
              ))}
            </ul>
          </div>
        </section>

        <!-- SECTION 2: CE VOYAGE EST POUR MOI ? -->
        <section id="pour-moi" class="pt-6 border-t border-slate-200">
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 mb-6">
            Ce voyage est-il fait pour moi ?
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/90 shadow-sm">
            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🐅</span> Faune & Pistage</span>
                <div class="flex gap-1.5">
                  {getDots(tour.radar.wildlife).map((active) => (
                    <span class={`w-2.5 h-2.5 rounded-full ${active ? 'bg-[#0e8354]' : 'bg-slate-200'}`}></span>
                  ))}
                </div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🌿</span> Nature & Aventure</span>
                <div class="flex gap-1.5">
                  {getDots(tour.radar.nature).map((active) => (
                    <span class={`w-2.5 h-2.5 rounded-full ${active ? 'bg-[#0e8354]' : 'bg-slate-200'}`}></span>
                  ))}
                </div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🛕</span> Culture & Vie locale</span>
                <div class="flex gap-1.5">
                  {getDots(tour.radar.culture).map((active) => (
                    <span class={`w-2.5 h-2.5 rounded-full ${active ? 'bg-[#0e8354]' : 'bg-slate-200'}`}></span>
                  ))}
                </div>
              </div>
            </div>

            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🧘</span> Relax & Contemplation</span>
                <div class="flex gap-1.5">
                  {getDots(tour.radar.relax).map((active) => (
                    <span class={`w-2.5 h-2.5 rounded-full ${active ? 'bg-[#0e8354]' : 'bg-slate-200'}`}></span>
                  ))}
                </div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🎉</span> Soirées & Fête</span>
                <div class="flex gap-1.5">
                  {getDots(tour.radar.nightlife).map((active) => (
                    <span class={`w-2.5 h-2.5 rounded-full ${active ? 'bg-[#0e8354]' : 'bg-slate-200'}`}></span>
                  ))}
                </div>
              </div>
              <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-sm font-bold">
                <span class="text-slate-500">Rythme & Effort :</span>
                <span class="text-[#0e8354] bg-emerald-50 px-3 py-0.5 rounded-full border border-emerald-200">{tour.difficulty}</span>
              </div>
            </div>
          </div>
        </section>

        <!-- SECTION 3: ITINÉRAIRE DÉTAILLÉ -->
        <section id="programme" class="pt-6 border-t border-slate-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-black text-2xl sm:text-3xl text-slate-950">
                Itinéraire détaillé ({tour.days.length} jours)
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1">
                Programme jour par jour encadré par nos pisteurs natifs de Bardia et guides d'expédition.
              </p>
            </div>
            <button onclick="toggleAllDays()" class="text-xs font-bold text-[#0e8354] hover:text-[#0c6d46] transition-colors cursor-pointer">
              Tout déplier / replier
            </button>
          </div>

          <div class="space-y-3">
            {tour.days.map((d: any, idx: number) => (
              <details open={idx === 0} class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
                <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                  <div class="flex items-center gap-3.5">
                    <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                      J{d.day}
                    </span>
                    <h4 class="font-bold text-sm sm:text-base text-slate-900">
                      {d.title}
                    </h4>
                  </div>
                  <svg class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"></path></svg>
                </summary>
                <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                  <p class="pt-3">{d.desc}</p>
                </div>
              </details>
            ))}
          </div>
        </section>

        <!-- SECTION 4: INCLUS & EXTRAS -->
        <section id="inclusions" class="pt-8 border-t border-slate-200">
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 mb-6">
            Ce qui est inclus dans votre séjour
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div class="bg-emerald-50/70 p-6 sm:p-8 rounded-3xl border border-emerald-200">
              <h3 class="font-bold text-lg text-emerald-950 mb-4 flex items-center gap-2">
                <span class="text-emerald-600">✓</span>
                <span>Inclus dans le tarif</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-emerald-950 font-medium">
                <li class="flex items-start gap-2"><span>✓</span><span>Tous les hébergements (éco-lodges traditionnels ou tentes de bivouac)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Pension complète en jungle (3 repas sains et locaux par jour)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Vols intérieurs & transferts privés mentionnés au programme</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Permis officiels des Parcs Nationaux et taxes de conservation</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Encadrement par des maîtres pisteurs certifiés (Pawan / Kiran)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Assistance francophone 24h/24 par Robin</span></li>
              </ul>
            </div>

            <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200">
              <h3 class="font-bold text-lg text-slate-900 mb-4 flex items-center gap-2">
                <span class="text-slate-400">✕</span>
                <span>Non inclus</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-slate-600 font-medium">
                <li class="flex items-start gap-2"><span>✕</span><span>Vols internationaux aller-retour (Paris/Europe - Katmandou)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Frais de visa népalais (environ 30$ à 50$ à l'arrivée)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Boissons alcoolisées et dépenses personnelles</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Assurance voyage personnelle obligatoire</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Pourboires pour les équipes locales</span></li>
              </ul>
            </div>
          </div>
        </section>

        <!-- SECTION 5: AVIS VOYAGEURS VERBATIM -->
        <section id="avis-voyageurs" class="pt-8 border-t border-slate-200">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
            <div>
              <h2 class="font-black text-2xl sm:text-3xl text-slate-950">
                Avis de voyageurs ayant vécu l'aventure
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1 font-medium">
                Retours d'expérience 100% authentiques vérifiés sur Google Reviews.
              </p>
            </div>
            <a href="https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 bg-emerald-50 px-4 py-2 rounded-2xl border border-emerald-200 self-start sm:self-auto hover:bg-emerald-100 transition-colors">
              <span class="text-[#00b67a] font-black text-lg">★ 5.0</span>
              <span class="text-xs font-bold text-slate-700">Google Reviews</span>
            </a>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-white p-6 rounded-3xl border border-slate-200/90 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-800 font-black text-sm flex items-center justify-center">
                    AN
                  </div>
                  <div>
                    <h4 class="font-bold text-sm text-slate-900">Adrien Noat</h4>
                    <p class="text-[11px] text-slate-400">Voyageur vérifié • Safari Bardia & Babai</p>
                  </div>
                </div>
                <div class="flex text-amber-400 text-xs">★★★★★</div>
              </div>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed italic font-normal">
                « Une expérience inoubliable avec Pawan et Robin. Observer un tigre du Bengale à pied en toute sécurité reste le plus grand moment de voyage de ma vie. Tout était parfaitement orchestré. »
              </p>
            </div>

            <div class="bg-white p-6 rounded-3xl border border-slate-200/90 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-800 font-black text-sm flex items-center justify-center">
                    JT
                  </div>
                  <div>
                    <h4 class="font-bold text-sm text-slate-900">Jean Tramoy</h4>
                    <p class="text-[11px] text-slate-400">Voyageur vérifié • Expédition Bivouac</p>
                  </div>
                </div>
                <div class="flex text-amber-400 text-xs">★★★★★</div>
              </div>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed italic font-normal">
                « Les nuits en bivouac au cœur de la vallée de Babai sont magiques. L'expertise naturaliste des pisteurs est impressionnante. Un voyage authentique et respectueux de la nature. »
              </p>
            </div>
          </div>
        </section>

        <!-- SECTION 6: FAQ -->
        <section id="faq" class="pt-8 border-t border-slate-200">
          <h2 class="font-black text-2xl text-slate-950 mb-6 tracking-tight">
            Questions fréquentes sur ce voyage
          </h2>

          <div class="space-y-3 text-sm">
            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Comment se passe la réservation et le règlement ?</span>
                <svg class="w-4 h-4 transition-transform group-open:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"></path></svg>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal">
                Pour sécuriser votre place, un acompte de 30% est demandé par virement bancaire ou carte sécurisée. Le solde est réglé avant le départ ou directement à Katmandou.
              </p>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Combien de personnes partent par groupe ?</span>
                <svg class="w-4 h-4 transition-transform group-open:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"></path></svg>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal">
                Nos séjours sont exclusivement limités à 4 à 8 explorateurs pour garantir le silence requis lors du pistage des animaux et préserver la sécurité de tous.
              </p>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Quel est le niveau de difficulté ?</span>
                <svg class="w-4 h-4 transition-transform group-open:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"></path></svg>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal">
                Ce séjour est classé <strong>{tour.difficulty}</strong>. Nos pisteurs adaptent le rythme de marche pour que chacun profite sereinement de l'aventure.
              </p>
            </details>
          </div>
        </section>

      </div>

      <!-- RIGHT COLUMN: STICKY BOOKING CARD -->
      <div class="lg:col-span-4">
        <div id="booking-widget" class="sticky top-28 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-[0_12px_40px_rgba(0,0,0,0.08)] space-y-6">
          
          <div>
            <span class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354]">{tour.style}</span>
            <h3 class="font-black text-xl sm:text-2xl text-slate-950 mt-1 tracking-tight">
              {tour.title}
            </h3>
            <p class="text-xs text-slate-500 mt-1 font-semibold">{tour.duration} • Micro-groupe (4 à 8 pers)</p>
          </div>

          <!-- Price -->
          <div class="pt-4 border-t border-slate-100 flex items-baseline justify-between">
            <div>
              <p class="text-[11px] font-extrabold uppercase text-slate-400">À partir de</p>
              <div class="flex items-baseline gap-2">
                <span class="font-black text-3xl text-slate-950 tracking-tight">{tour.price}</span>
                {tour.originalPrice && (
                  <span class="text-xs sm:text-sm text-slate-400 line-through font-bold">{tour.originalPrice}</span>
                )}
              </div>
            </div>
            {tour.originalPrice && (
              <span class="px-2.5 py-1 rounded-full bg-rose-50 border border-rose-200 text-rose-700 text-xs font-black">Promo</span>
            )}
          </div>

          <!-- Departures Selector -->
          <div class="space-y-2.5">
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-600">
              Sélectionnez votre départ :
            </label>
            <div class="space-y-2 text-xs">
              <label class="flex items-center justify-between p-3 rounded-2xl border border-[#0e8354] bg-emerald-50/50 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Automne 2026" checked class="text-[#0e8354] focus:ring-[#0e8354]" />
                  <div>
                    <p class="font-bold text-slate-900">10 Oct - 24 Oct 2026</p>
                    <p class="text-[10px] text-slate-500">4 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-[#0e8354]">Confirmé</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-slate-200 hover:border-slate-300 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Novembre 2026" class="text-[#0e8354] focus:ring-[#0e8354]" />
                  <div>
                    <p class="font-bold text-slate-900">07 Nov - 21 Nov 2026</p>
                    <p class="text-[10px] text-slate-500">2 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-[#0c6d46]">Dernières places</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-slate-200 hover:border-slate-300 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Printemps 2027" class="text-[#0e8354] focus:ring-[#0e8354]" />
                  <div>
                    <p class="font-bold text-slate-900">15 Mars - 29 Mars 2027</p>
                    <p class="text-[10px] text-slate-500">6 places disponibles</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-[#0e8354]">Saison tigres</span>
              </label>
            </div>
          </div>

          <!-- Primary CTA Button -->
          <button onclick="openBookingForm()" class="w-full py-4 rounded-2xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] bg-[length:200%_auto] hover:bg-right text-white font-black text-base shadow-[0_8px_25px_rgba(14,131,84,0.45)] hover:shadow-[0_12px_35px_rgba(14,131,84,0.65)] hover:-translate-y-0.5 active:translate-y-0 active:scale-[0.98] transition-all duration-300 border-t border-white/30 text-center tracking-tight cursor-pointer">
            Réserver ma place →
          </button>

          <!-- Reassurance list -->
          <div class="space-y-2 text-xs text-slate-500 pt-2 border-t border-slate-100 font-medium">
            <div class="flex items-center gap-2">
              <svg class="w-4 h-4 text-emerald-600 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Acompte de 30% seulement à l'inscription</span>
            </div>
            <div class="flex items-center gap-2">
              <svg class="w-4 h-4 text-emerald-600 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Annulation flexible jusqu'à 30 jours</span>
            </div>
            <div class="flex items-center gap-2">
              <svg class="w-4 h-4 text-emerald-600 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Règlement sécurisé (CB / Virement)</span>
            </div>
          </div>

          <div class="pt-4 border-t border-slate-100 flex flex-col gap-2.5 text-xs">
            <a href={`https://wa.me/33695413227?text=Bonjour%20Robin%2C%20j'ai%20une%20question%20sur%20le%20circuit%20${titleEncoded}`} target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 py-3 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-md shadow-emerald-600/30 hover:shadow-lg hover:shadow-emerald-600/45 hover:-translate-y-0.5 active:translate-y-0 transition-all">
              <svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
              <span>Poser une question sur WhatsApp</span>
            </a>
          </div>

        </div>
      </div>

    </div>

  </main>

  <Footer lang="fr" />

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox-modal" class="fixed inset-0 bg-black/95 backdrop-blur-xl z-50 hidden opacity-0 transition-opacity duration-300 flex items-center justify-center p-4">
    <div class="absolute top-6 left-6 right-6 flex items-center justify-between text-white z-10">
      <div id="lightbox-counter" class="bg-white/10 backdrop-blur-md px-4 py-1.5 rounded-full text-xs font-extrabold border border-white/20">
        1 / 4
      </div>
      <button onclick="closeLightbox()" class="w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 flex items-center justify-center text-white transition-all hover:scale-105 active:scale-95 cursor-pointer" aria-label="Fermer">
        ✕
      </button>
    </div>

    <button onclick="prevLightboxImage(event)" class="absolute left-4 sm:left-8 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-black/60 hover:bg-black/90 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-20 shadow-2xl cursor-pointer" aria-label="Photo précédente">
      ‹
    </button>
    <button onclick="nextLightboxImage(event)" class="absolute right-4 sm:right-8 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-black/60 hover:bg-black/90 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-20 shadow-2xl cursor-pointer" aria-label="Photo suivante">
      ›
    </button>

    <div class="relative max-w-5xl max-h-[85vh] flex items-center justify-center">
      <img id="lightbox-image" src="" alt="Photo agrandie" class="max-w-full max-h-[85vh] object-contain rounded-2xl shadow-2xl transition-all duration-300" />
    </div>
  </div>

  <script is:inline define:vars={{ tourImages: tour.images, tourTitle: tour.title }}>
    let currentImageIndex = 0;

    window.openLightbox = function(index) {
      currentImageIndex = index;
      updateLightboxContent();
      const modal = document.getElementById('lightbox-modal');
      modal.classList.remove('hidden');
      setTimeout(() => {
        modal.classList.remove('opacity-0');
        modal.classList.add('opacity-100');
      }, 10);
      document.body.style.overflow = 'hidden';
    };

    window.closeLightbox = function() {
      const modal = document.getElementById('lightbox-modal');
      modal.classList.remove('opacity-100');
      modal.classList.add('opacity-0');
      setTimeout(() => {
        modal.classList.add('hidden');
        document.body.style.overflow = '';
      }, 300);
    };

    function updateLightboxContent() {
      const img = document.getElementById('lightbox-image');
      const counter = document.getElementById('lightbox-counter');
      if (img && tourImages[currentImageIndex]) {
        img.src = tourImages[currentImageIndex];
      }
      if (counter) {
        counter.textContent = (currentImageIndex + 1) + ' / ' + tourImages.length;
      }
    }

    window.prevLightboxImage = function(e) {
      if (e) e.stopPropagation();
      currentImageIndex = (currentImageIndex - 1 + tourImages.length) % tourImages.length;
      updateLightboxContent();
    };

    window.nextLightboxImage = function(e) {
      if (e) e.stopPropagation();
      currentImageIndex = (currentImageIndex + 1) % tourImages.length;
      updateLightboxContent();
    };

    document.addEventListener('keydown', (e) => {
      const modal = document.getElementById('lightbox-modal');
      if (modal && !modal.classList.contains('hidden')) {
        if (e.key === 'ArrowLeft') window.prevLightboxImage();
        if (e.key === 'ArrowRight') window.nextLightboxImage();
        if (e.key === 'Escape') window.closeLightbox();
      }
    });

    window.toggleAllDays = function() {
      const details = document.querySelectorAll('#programme details');
      const anyClosed = Array.from(details).some(d => !d.open);
      details.forEach(d => d.open = anyClosed);
    };

    window.openBookingForm = function() {
      const date = document.querySelector('input[name="departure_date"]:checked')?.value || 'Non spécifiée';
      const msg = encodeURIComponent(`Bonjour Robin ! Je souhaite réserver ma place sur le séjour "${tourTitle}" pour le départ : ${date}. Merci de me communiquer les modalités !`);
      window.open(`https://wa.me/33695413227?text=${msg}`, '_blank');
    };

    window.handleShareTour = function() {
      const pageUrl = window.location.href;
      const waLink = document.getElementById('share-whatsapp');
      if (waLink) {
        waLink.href = `https://api.whatsapp.com/send?text=${encodeURIComponent('Découvre ce séjour au Népal : ' + tourTitle + ' ' + pageUrl)}`;
      }
      const emailLink = document.getElementById('share-email');
      if (emailLink) {
        emailLink.href = `mailto:?subject=${encodeURIComponent(tourTitle)}&body=${encodeURIComponent('Je voulais te partager ce séjour au Népal avec Jungle Nepal Adventure : ' + pageUrl)}`;
      }

      if (navigator.share && /mobile|android|iphone|ipad/i.test(navigator.userAgent)) {
        navigator.share({
          title: tourTitle,
          text: "Découvre ce séjour d'immersion au Népal avec Jungle Nepal Adventure",
          url: pageUrl
        }).catch(() => {});
        return;
      }

      const menu = document.getElementById('share-menu');
      if (menu) {
        const isOpen = menu.classList.contains('opacity-100');
        if (isOpen) {
          menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        } else {
          menu.classList.remove('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }
      }
    };

    window.copyTourLink = function() {
      const pageUrl = window.location.href;
      navigator.clipboard.writeText(pageUrl).then(() => {
        showToast('✅ Lien du séjour copié dans le presse-papier !');
        const menu = document.getElementById('share-menu');
        if (menu) {
          menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }
      }).catch(() => {
        showToast('Lien : ' + pageUrl);
      });
    };

    function showToast(msg) {
      let toast = document.getElementById('toast-notification');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast-notification';
        toast.className = 'fixed bottom-8 left-1/2 -translate-x-1/2 bg-slate-950/95 backdrop-blur-xl text-white text-xs sm:text-sm font-black px-5 py-3 rounded-full border border-white/20 shadow-[0_20px_50px_rgba(0,0,0,0.4)] transition-all duration-300 z-50 opacity-0 translate-y-4 pointer-events-none flex items-center gap-2';
        document.body.appendChild(toast);
      }
      toast.innerHTML = `<span class="text-amber-300 font-bold">✨</span> <span>${msg}</span>`;
      toast.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
      toast.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
      setTimeout(() => {
        toast.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
        toast.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }, 2800);
    }
  </script>
</Layout>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/[slug].astro', 'w', encoding='utf-8') as f:
    f.write(tour_astro_content)

# English tour page
en_tour_astro_content = tour_astro_content.replace('lang="fr"', 'lang="en"').replace('currentPath={`/tours/${slug}`}', 'currentPath={`/en/tours/${slug}`}')
en_tour_astro_content = en_tour_astro_content.replace('<span>Accueil</span>', '<span>Home</span>')
en_tour_astro_content = en_tour_astro_content.replace('<span>Nos 14 Séjours</span>', '<span>All 14 Trips</span>')
en_tour_astro_content = en_tour_astro_content.replace('<span>Partager ce séjour</span>', '<span>Share this trip</span>')
en_tour_astro_content = en_tour_astro_content.replace('Copier le lien direct', 'Copy direct link')
en_tour_astro_content = en_tour_astro_content.replace('Envoyer sur WhatsApp', 'Send via WhatsApp')
en_tour_astro_content = en_tour_astro_content.replace('Partager par Email', 'Share via Email')
en_tour_astro_content = en_tour_astro_content.replace('Voir toutes les photos', 'View all photos')
en_tour_astro_content = en_tour_astro_content.replace('Aperçu', 'Overview')
en_tour_astro_content = en_tour_astro_content.replace('Profil Voyage', 'Trip Profile')
en_tour_astro_content = en_tour_astro_content.replace('Itinéraire', 'Itinerary')
en_tour_astro_content = en_tour_astro_content.replace('Inclus & Extras', 'Inclusions & Extras')
en_tour_astro_content = en_tour_astro_content.replace('Avis', 'Reviews')
en_tour_astro_content = en_tour_astro_content.replace('Les temps forts du voyage', 'Trip Highlights')
en_tour_astro_content = en_tour_astro_content.replace('Ce voyage est-il fait pour moi ?', 'Is this trip made for you?')
en_tour_astro_content = en_tour_astro_content.replace('Faune & Pistage', 'Wildlife & Tracking')
en_tour_astro_content = en_tour_astro_content.replace('Nature & Aventure', 'Nature & Adventure')
en_tour_astro_content = en_tour_astro_content.replace('Culture & Vie locale', 'Culture & Local Life')
en_tour_astro_content = en_tour_astro_content.replace('Relax & Contemplation', 'Relax & Peace')
en_tour_astro_content = en_tour_astro_content.replace('Soirées & Fête', 'Evenings & Vibes')
en_tour_astro_content = en_tour_astro_content.replace('Rythme & Effort :', 'Pace & Effort:')
en_tour_astro_content = en_tour_astro_content.replace('Itinéraire détaillé', 'Detailed Itinerary')
en_tour_astro_content = en_tour_astro_content.replace('Tout déplier / replier', 'Expand / Collapse all')
en_tour_astro_content = en_tour_astro_content.replace('Ce qui est inclus dans votre séjour', "What's included in your trip")
en_tour_astro_content = en_tour_astro_content.replace('Inclus dans le tarif', 'Included in the price')
en_tour_astro_content = en_tour_astro_content.replace('Non inclus', 'Not included')
en_tour_astro_content = en_tour_astro_content.replace('Questions fréquentes sur ce voyage', 'Frequently Asked Questions')
en_tour_astro_content = en_tour_astro_content.replace('Sélectionnez votre départ :', 'Select your departure:')
en_tour_astro_content = en_tour_astro_content.replace('Réserver ma place →', 'Book My Spot →')
en_tour_astro_content = en_tour_astro_content.replace('Acompte de 30% seulement à l\'inscription', 'Only 30% deposit upon registration')
en_tour_astro_content = en_tour_astro_content.replace('Annulation flexible jusqu\'à 30 jours', 'Flexible cancellation up to 30 days')
en_tour_astro_content = en_tour_astro_content.replace('Règlement sécurisé (CB / Virement)', 'Secure payment (Card / Wire)')
en_tour_astro_content = en_tour_astro_content.replace('Poser une question sur WhatsApp', 'Ask a question on WhatsApp')
en_tour_astro_content = en_tour_astro_content.replace('<Footer lang="fr" />', '<Footer lang="en" />')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/[slug].astro', 'w', encoding='utf-8') as f:
    f.write(en_tour_astro_content)

print("Created src/pages/tours/[slug].astro and src/pages/en/tours/[slug].astro successfully!")
