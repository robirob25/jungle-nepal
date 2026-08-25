import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

highlighted_slugs = ['bardia-explorateur', 'nepal-sauvage', 'chitwan-culture']
highlighted_tours = [t for t in tours if t['slug'] in highlighted_slugs]

# Read French a-propos.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    fr_content = f.read()

# Make sure Header and Footer and toursData are imported
if 'import Header' not in fr_content:
    fr_content = fr_content.replace("import Layout from '../layouts/Layout.astro';", "import Layout from '../layouts/Layout.astro';\nimport Header from '../components/Header.astro';\nimport Footer from '../components/Footer.astro';\nimport toursData from '../data/tours.json';\n\nconst highlightedTours = toursData.filter(t => ['bardia-explorateur', 'nepal-sauvage', 'chitwan-culture'].includes(t.slug));")

# Replace header block if static
fr_content = fr_content.replace("<Layout title=\"À propos | Jungle Nepal Adventure – Notre histoire & nos pisteurs\" lang=\"fr\">", "<Layout title=\"À propos | Jungle Nepal Adventure – Notre histoire & nos pisteurs\" lang=\"fr\">\n  <Header lang=\"fr\" currentPath=\"/a-propos.html\" />")

# Build the 3 Highlighted Tours Section HTML for FR
highlighted_section_fr = """
  <!-- ========================================================================= -->
  <!-- 7. 3 CIRCUITS PHARE HIGHLIGHTED -->
  <!-- ========================================================================= -->
  <section class="py-20 sm:py-28 bg-[#f4efe6]/50 border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
        <div>
          <span class="inline-block text-xs font-black uppercase tracking-widest text-[#0e8354] bg-emerald-50 px-3.5 py-1 rounded-full border border-emerald-200 shadow-sm mb-2">
            Expéditions Coups de Cœur
          </span>
          <h2 class="font-black text-3xl sm:text-4xl text-slate-950 tracking-tight">
            Prêt pour l'aventure ? Nos 3 séjours phares
          </h2>
          <p class="text-slate-600 text-sm mt-1">
            Départs garantis en micro-groupes de 4 à 8 personnes avec Pawan, Kiran et nos équipes locales.
          </p>
        </div>
        <a href="/index.html#prochains-departs" class="inline-flex items-center gap-1.5 text-xs font-black text-[#0e8354] hover:underline shrink-0">
          <span>Explorer les 14 séjours</span>
          <span>→</span>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        {highlightedTours.map((tour) => (
          <div 
            class="bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-2xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col group cursor-pointer"
            onclick={`window.location.href='/tours/${tour.slug}.html'`}
          >
            <!-- Photo Hero -->
            <div class="relative h-60 overflow-hidden bg-slate-900">
              <img 
                src={tour.images[0]} 
                alt={tour.title} 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-transparent to-black/20"></div>

              <div class="absolute top-4 left-4 right-4 flex items-center justify-between">
                <span class="px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-amber-300 border border-amber-300/30 text-xs font-black">
                  {tour.badge}
                </span>
                <span class="px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-white text-xs font-bold">
                  4–8 pers.
                </span>
              </div>

              <div class="absolute bottom-4 left-4 right-4 text-white">
                <div class="flex items-center gap-2 text-xs font-bold text-slate-200">
                  <span>🕒 {tour.duration}</span>
                  <span>•</span>
                  <span class="text-amber-300">★ {tour.rating} ({tour.reviews} avis)</span>
                </div>
              </div>
            </div>

            <!-- Card Body -->
            <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
              <div>
                <span class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354]">{tour.style}</span>
                <h3 class="font-black text-xl text-slate-950 mt-1 leading-snug group-hover:text-[#0e8354] transition-colors">
                  {tour.title}
                </h3>
                <p class="text-xs text-slate-600 mt-2 line-clamp-2 leading-relaxed font-normal">
                  {tour.overview}
                </p>
              </div>

              <!-- Price & CTA -->
              <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                <div>
                  <span class="text-[10px] font-extrabold uppercase text-slate-400 block">À partir de</span>
                  <div class="flex items-baseline gap-2">
                    <span class="font-black text-2xl text-slate-950 tracking-tight">{tour.price}</span>
                    {tour.originalPrice && (
                      <span class="text-xs text-slate-400 line-through font-bold">{tour.originalPrice}</span>
                    )}
                  </div>
                </div>

                <a 
                  href={`/tours/${tour.slug}.html`}
                  class="px-5 py-2.5 rounded-2xl bg-gradient-to-r from-[#0e8354] to-[#109363] text-white font-extrabold text-xs shadow-md shadow-[#0e8354]/30 group-hover:shadow-lg hover:scale-105 transition-all"
                >
                  Voir le séjour →
                </a>
              </div>

            </div>
          </div>
        ))}
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 8. FOOTER -->
  <!-- ========================================================================= -->
  <Footer lang="fr" />
</Layout>
"""

# Replace from section 7 or footer till end
import re
fr_content = re.sub(r'<!-- ========================================================================= -->\s*<!-- 7\. CTA REJOINDRE L\'EXPÉDITION -->.*?</Layout>', highlighted_section_fr, fr_content, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(fr_content)

print("Updated src/pages/a-propos.astro with 3 highlighted tours!")

# Read English en/a-propos.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/a-propos.astro', 'r', encoding='utf-8') as f:
    en_content = f.read()

if 'import Header' not in en_content:
    en_content = en_content.replace("import Layout from '../../layouts/Layout.astro';", "import Layout from '../../layouts/Layout.astro';\nimport Header from '../../components/Header.astro';\nimport Footer from '../../components/Footer.astro';\nimport toursData from '../../data/tours.json';\n\nconst highlightedTours = toursData.filter(t => ['bardia-explorateur', 'nepal-sauvage', 'chitwan-culture'].includes(t.slug));")

en_content = en_content.replace("<Layout title=\"About Us | Jungle Nepal Adventure – Our Story & Master Trackers\" lang=\"en\">", "<Layout title=\"About Us | Jungle Nepal Adventure – Our Story & Master Trackers\" lang=\"en\">\n  <Header lang=\"en\" currentPath=\"/en/a-propos.html\" />")

highlighted_section_en = """
  <!-- ========================================================================= -->
  <!-- 7. 3 CIRCUITS PHARE HIGHLIGHTED -->
  <!-- ========================================================================= -->
  <section class="py-20 sm:py-28 bg-[#f4efe6]/50 border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
        <div>
          <span class="inline-block text-xs font-black uppercase tracking-widest text-[#0e8354] bg-emerald-50 px-3.5 py-1 rounded-full border border-emerald-200 shadow-sm mb-2">
            Featured Expeditions
          </span>
          <h2 class="font-black text-3xl sm:text-4xl text-slate-950 tracking-tight">
            Ready for Adventure? Our 3 Flagship Journeys
          </h2>
          <p class="text-slate-600 text-sm mt-1">
            Guaranteed small group departures of 4 to 8 travelers with Pawan, Kiran and our local tracking teams.
          </p>
        </div>
        <a href="/en/index.html#prochains-departs" class="inline-flex items-center gap-1.5 text-xs font-black text-[#0e8354] hover:underline shrink-0">
          <span>Explore all 14 expeditions</span>
          <span>→</span>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        {highlightedTours.map((tour) => (
          <div 
            class="bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-2xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col group cursor-pointer"
            onclick={`window.location.href='/en/tours/${tour.slug}.html'`}
          >
            <!-- Photo Hero -->
            <div class="relative h-60 overflow-hidden bg-slate-900">
              <img 
                src={tour.images[0]} 
                alt={tour.title} 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-transparent to-black/20"></div>

              <div class="absolute top-4 left-4 right-4 flex items-center justify-between">
                <span class="px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-amber-300 border border-amber-300/30 text-xs font-black">
                  {tour.badge}
                </span>
                <span class="px-3 py-1 rounded-full bg-black/60 backdrop-blur-md text-white text-xs font-bold">
                  4–8 pers.
                </span>
              </div>

              <div class="absolute bottom-4 left-4 right-4 text-white">
                <div class="flex items-center gap-2 text-xs font-bold text-slate-200">
                  <span>🕒 {tour.duration}</span>
                  <span>•</span>
                  <span class="text-amber-300">★ {tour.rating} ({tour.reviews} reviews)</span>
                </div>
              </div>
            </div>

            <!-- Card Body -->
            <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
              <div>
                <span class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354]">{tour.style}</span>
                <h3 class="font-black text-xl text-slate-950 mt-1 leading-snug group-hover:text-[#0e8354] transition-colors">
                  {tour.title}
                </h3>
                <p class="text-xs text-slate-600 mt-2 line-clamp-2 leading-relaxed font-normal">
                  {tour.overview}
                </p>
              </div>

              <!-- Price & CTA -->
              <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                <div>
                  <span class="text-[10px] font-extrabold uppercase text-slate-400 block">Starting from</span>
                  <div class="flex items-baseline gap-2">
                    <span class="font-black text-2xl text-slate-950 tracking-tight">{tour.price}</span>
                    {tour.originalPrice && (
                      <span class="text-xs text-slate-400 line-through font-bold">{tour.originalPrice}</span>
                    )}
                  </div>
                </div>

                <a 
                  href={`/en/tours/${tour.slug}.html`}
                  class="px-5 py-2.5 rounded-2xl bg-gradient-to-r from-[#0e8354] to-[#109363] text-white font-extrabold text-xs shadow-md shadow-[#0e8354]/30 group-hover:shadow-lg hover:scale-105 transition-all"
                >
                  View expedition →
                </a>
              </div>

            </div>
          </div>
        ))}
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 8. FOOTER -->
  <!-- ========================================================================= -->
  <Footer lang="en" />
</Layout>
"""

en_content = re.sub(r'<!-- ========================================================================= -->\s*<!-- 7\. CTA REJOINDRE L\'EXPÉDITION -->.*?</Layout>', highlighted_section_en, en_content, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(en_content)

print("Updated src/pages/en/a-propos.astro with 3 highlighted tours!")
