# 1. src/pages/destinations/[slug].astro
dest_astro = """---
import Layout from '../../layouts/Layout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import destinationsData from '../../data/destinations.json';
import toursData from '../../data/tours.json';

export async function getStaticPaths() {
  return destinationsData.map((dest) => ({
    params: { slug: dest.slug },
    props: { dest },
  }));
}

const { dest } = Astro.props;
const { slug } = Astro.params;

// Associated tours
const matchingTours = toursData.filter((t) => {
  if (slug === 'bardia') return t.slug.includes('bardia') || t.slug.includes('babai') || t.slug.includes('nepal-sauvage');
  if (slug === 'chitwan') return t.slug.includes('chitwan');
  if (slug === 'suklaphanta') return t.slug.includes('nepal-sauvage') || t.slug.includes('immersion-totale');
  if (slug === 'annapurna') return t.slug.includes('rara') || t.slug.includes('spirituelle') || t.slug.includes('carnet');
  return true;
}).slice(0, 3);
---

<Layout 
  title={`${dest.name} – Safaris & Guide`}
  description={dest.desc}
  image={dest.heroImage}
  lang="fr"
  isDarkHeader={true}
>
  <Header lang="fr" currentPath={`/destinations/${slug}`} />

  <!-- HERO DESTINATION -->
  <div class="relative min-h-[55vh] flex items-center justify-center pt-24 pb-16 px-4 bg-slate-950 text-white overflow-hidden">
    <div class="absolute inset-0 z-0">
      <img src={dest.heroImage} alt={dest.name} class="w-full h-full object-cover opacity-35 scale-105" />
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/60 to-transparent"></div>
    </div>

    <div class="relative z-10 max-w-4xl mx-auto text-center space-y-4">
      <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-500/20 text-[#10b981] border border-emerald-500/30 text-xs font-black uppercase tracking-widest">
        <span>{dest.icon}</span> Destination sauvage d'exception
      </span>
      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black tracking-tight text-white leading-tight">
        {dest.name}
      </h1>
      <p class="text-base sm:text-xl text-slate-300 max-w-2xl mx-auto font-normal leading-relaxed">
        {dest.tagline}
      </p>
    </div>
  </div>

  <!-- CONTENT -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 font-sans space-y-16">
    
    <!-- Presentation Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      <div class="lg:col-span-7 space-y-6">
        <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
          L'immersion grandeur nature à {dest.name}
        </h2>
        <p class="text-base sm:text-lg text-slate-700 leading-relaxed">
          {dest.desc}
        </p>

        <div class="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/90 shadow-sm space-y-4">
          <h3 class="font-bold text-lg text-slate-950 flex items-center gap-2">
            <span class="text-amber-500">✨</span>
            <span>Les incontournables de cette destination</span>
          </h3>
          <ul class="space-y-3 text-sm text-slate-700">
            {dest.highlights.map((h: string) => (
              <li class="flex items-start gap-3">
                <span class="w-2 h-2 rounded-full bg-[#0e8354] mt-2 shrink-0"></span>
                <span>{h}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div class="lg:col-span-5">
        <div class="relative rounded-3xl overflow-hidden shadow-2xl border border-slate-200">
          <img src={dest.heroImage} alt={dest.name} class="w-full h-[400px] object-cover hover:scale-105 transition-transform duration-700" />
        </div>
      </div>
    </div>

    <!-- SÉJOURS QUI EXPLORENT CETTE DESTINATION -->
    <div class="pt-8 border-t border-slate-200 space-y-8">
      <div class="flex items-end justify-between">
        <div>
          <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">Circuits recommandés</span>
          <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight mt-1">
            Séjours passant par {dest.name}
          </h2>
        </div>
        <a href="/#prochains-departs" class="hidden sm:inline-flex items-center gap-1.5 text-xs font-extrabold text-[#0e8354] hover:text-[#0c6d46]">
          <span>Voir les 14 séjours</span>
          <span>→</span>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {matchingTours.map((t) => (
          <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col group">
            <div class="relative h-48 overflow-hidden">
              <img src={t.images[0]} alt={t.title} class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
              <span class="absolute top-3 left-3 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-amber-300 text-xs font-bold">
                {t.badge}
              </span>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
              <div>
                <p class="text-xs font-bold text-slate-500">{t.duration} • ★ {t.rating} ({t.reviews} avis)</p>
                <h3 class="font-bold text-base text-slate-900 mt-1 leading-snug">
                  {t.title}
                </h3>
              </div>
              <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
                <div>
                  <span class="text-[10px] text-slate-400 block font-bold">À PARTIR DE</span>
                  <span class="font-black text-lg text-slate-950">{t.price}</span>
                </div>
                <a href={`/tours/${t.slug}`} class="px-4 py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white text-xs font-bold transition-colors">
                  Découvrir →
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>

  </main>

  <Footer lang="fr" />
</Layout>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/[slug].astro', 'w', encoding='utf-8') as f:
    f.write(dest_astro)

# English version
en_dest_astro = dest_astro.replace('lang="fr"', 'lang="en"').replace('currentPath={`/destinations/${slug}`}', 'currentPath={`/en/destinations/${slug}`}')
en_dest_astro = en_dest_astro.replace('<span>Accueil</span>', '<span>Home</span>')
en_dest_astro = en_dest_astro.replace('Destination sauvage d\'exception', 'Exceptional Wild Sanctuary')
en_dest_astro = en_dest_astro.replace('Les incontournables de cette destination', 'Highlights of this destination')
en_dest_astro = en_dest_astro.replace('Circuits recommandés', 'Recommended Expeditions')
en_dest_astro = en_dest_astro.replace('Séjours passant par', 'Trips visiting')
en_dest_astro = en_dest_astro.replace('Voir les 14 séjours', 'View all 14 trips')
en_dest_astro = en_dest_astro.replace('Découvrir →', 'Explore →')
en_dest_astro = en_dest_astro.replace('À PARTIR DE', 'STARTING FROM')
en_dest_astro = en_dest_astro.replace('/#prochains-departs', '/en#prochains-departs')
en_dest_astro = en_dest_astro.replace('href={`/tours/${t.slug}`}', 'href={`/en/tours/${t.slug}`}')
en_dest_astro = en_dest_astro.replace('<Footer lang="fr" />', '<Footer lang="en" />')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/destinations/[slug].astro', 'w', encoding='utf-8') as f:
    f.write(en_dest_astro)

print("Created src/pages/destinations/[slug].astro and English mirror!")
