import { ui, defaultLang } from './ui';

export function getLangFromUrl(url: URL): 'fr' | 'en' {
  const [, lang] = url.pathname.split('/');
  if (lang === 'en') return 'en';
  return 'fr';
}

export function useTranslations(lang: 'fr' | 'en') {
  return function t(key: keyof typeof ui[typeof defaultLang]) {
    return ui[lang][key] || ui[defaultLang][key];
  };
}

export const BLOG_SLUG_MAP_FR_TO_EN: Record<string, string> = {
  'agence-safari-nepal-francophone': 'expert-local-safari-agency-nepal',
  'animaux-bardia-faune-parc-national': 'bardia-national-park-wildlife-animals-guide',
  'animaux-chitwan-faune-parc-national': 'chitwan-national-park-wildlife-animals-guide',
  'animaux-rares-safari-nepal-guide': 'rare-wildlife-nepal-secret-jungle-species-guide',
  'art-du-pistage-jungle-nepal-traces-cris-alarme': 'jungle-tracking-art-nepal-pugmarks-alarm-calls',
  'bardia-ou-chitwan-quel-parc-choisir': 'bardia-or-chitwan-which-park-to-choose-safari-nepal',
  'camping-safari-a-bardia-nuits-en-jungle-au-nepal': 'camping-safari-in-bardia-jungle-bivouac-nepal',
  'cerf-des-marais-suklaphanta-savanes-sauvages-ouest-nepalais': 'swamp-deer-suklaphanta-wild-savannas-western-nepal',
  'combien-de-jours-pour-un-safari-au-nepal': 'how-many-days-for-nepal-safari',
  'combiner-trek-et-safari-au-nepal-guide-complet': 'combining-trek-and-safari-in-nepal-complete-guide',
  'comment-aller-a-bardia-transport-avion-bus-guide': 'how-to-get-to-bardia-flights-buses-transfers',
  'comment-aller-a-chitwan-katmandou-pokhara-bus-avion': 'how-to-get-to-chitwan-bus-flights-private-car',
  'comment-organiser-un-safari-a-bardia-apres-un-trek': 'how-to-organize-bardia-safari-after-trek',
  'comment-organiser-un-safari-a-chitwan-apres-un-trek': 'how-to-organize-chitwan-safari-after-trek',
  'comment-organiser-un-safari-au-nepal': 'how-to-plan-a-safari-in-nepal-complete-guide',
  'comportement-du-rhinoceros-unicornis': 'greater-one-horned-rhino-behavior-guide-nepal',
  'comportement-du-tigre-du-bengale': 'bengal-tiger-behavior-king-of-nepal-jungle',
  'condition-physique-safari-a-pied-nepal': 'physical-fitness-walking-safari-nepal-guide',
  'culture-tharu-nepal-immersion-jungle': 'tharu-culture-nepal-jungle-traditions-village-life',
  'culture-tharu-traditions-cuisine-festival-dashain-bardia': 'tharu-cultural-immersion-bardia-traditions-cuisine-dashain',
  'ecologie-pistage-panthere-des-neiges-bharal-nepal': 'snow-leopard-blue-sheep-ecology-tracking-nepal',
  'elephant-sauvage-nepal-guide-safari': 'wild-asian-elephants-nepal-tracking-guide',
  'gavial-du-gange-crocodiles-nepal-guide': 'gharials-and-marsh-crocodiles-nepal-guide',
  'guide-complet-parc-national-de-bardia-nepal': 'bardia-national-park-complete-safari-guide',
  'guide-complet-parc-national-de-suklaphanta': 'suklaphanta-national-park-complete-safari-guide',
  'guide-ornithologique-nepal-oiseaux-bardia-suklaphanta': 'birdwatching-nepal-guide-bardia-suklaphanta',
  'guide-parc-national-de-chitwan-nepal': 'chitwan-national-park-complete-safari-guide',
  'le-safari-ethique-au-nepal-privilegier-la-marche': 'ethical-safari-nepal-why-walking-and-jeep-matter',
  'leopard-indien-panthere-nepal-guide-safari': 'indian-leopard-in-nepal-safari-guide',
  'nilgaut-cerfs-ongules-sauvages-nepal-guide': 'nilgai-blue-bulls-wild-deer-nepal-guide',
  'observer-les-oiseaux-au-nepal-guide-birdwatching': 'birdwatching-in-nepal-bardia-chitwan-guide',
  'oiseaux-bardia-calao-bicorne-rollier-indien-tchitrec-paradis': 'birds-of-bardia-hornbill-indian-roller-paradise-flycatcher',
  'ou-voir-panthere-des-neiges-nepal-dolpo-mustang': 'where-to-see-snow-leopard-nepal-dolpo-mustang',
  'panthere-des-neiges-au-nepal': 'snow-leopard-expedition-nepal-chances-reality',
  'pistage-a-pied-nepal-journee-type-pisteurs-tharu': 'walking-safari-nepal-tiger-tracking-tharu-guides',
  'pister-le-tigre-du-bengale-a-bardia': 'tracking-bengal-tigers-in-bardia-safari-story',
  'prix-dun-safari-au-nepal': 'cost-of-safari-in-nepal-prices-budget-guide',
  'prix-preparation-expedition-panthere-des-neiges-nepal': 'snow-leopard-expedition-nepal-cost-gear-preparation',
  'quand-partir-au-nepal-pour-un-safari-guide': 'best-time-for-safari-in-nepal-weather-seasons',
  'quels-animaux-voir-lors-dun-safari-au-nepal': 'what-animals-can-you-see-on-nepal-safari',
  'rapaces-chouettes-oiseaux-proie-nepal-guide': 'raptors-owls-birds-of-prey-nepal-guide',
  'reptiles-varans-agames-serpents-nepal-guide': 'reptiles-of-nepal-monitor-lizards-agamas-snakes-guide',
  'sac-safari-nepal': 'what-to-pack-for-nepal-safari-packing-list',
  'safari-a-pied-au-nepal-guide-complet': 'walking-safaris-in-nepal-complete-guide',
  'safari-a-pied-nepal-danger-regles-securite-guide': 'walking-safari-nepal-danger-safety-rules',
  'safari-bardia-prix-forfaits-et-ce-que-ca-inclut': 'bardia-safari-prices-packages-inclusions',
  'safari-combine-inde-nepal-corbett-dudhwa-suklaphanta-bardia': 'india-nepal-wildlife-safari-corbett-dudhwa-bardia',
  'safari-dos-elephant-nepal-pourquoi-refuser-cette-pratique': 'elephant-back-safari-nepal-ethical-reasons-to-avoid',
  'safari-nepal-en-famille-guide-securite': 'family-safari-in-nepal-safety-practical-guide',
  'safari-nepal-en-famille-securite-lodges-enfants': 'nepal-family-safari-safety-lodges-children',
  'safari-nepal-ou-afrique-que-choisir': 'nepal-vs-africa-safari-which-to-choose',
  'safari-nepal-ou-inde-comparatif-ranthambore-corbett-bardia': 'nepal-vs-india-safari-comparison-ranthambore-corbett-bardia',
  'safari-photo-au-nepal-spots-materiel-conseils': 'nepal-wildlife-photo-safari-gear-spots-tips',
  'safari-photo-tigre-nepal-bardia-guide-affut': 'bengal-tiger-photography-safari-bardia-nepal',
  'safari-pirogue-rafting-nepal-guide': 'canoe-safari-wildlife-rafting-nepal-guide',
  'sante-paludisme-vaccins-safari-nepal-conseils-medicaux': 'safari-health-malaria-vaccines-nepal-medical-guide',
  'singes-nepal-langurs-macaques-guide': 'monkeys-of-nepal-langurs-macaques-guide',
  'tigre-bardia-observation-chances-spots': 'tigers-in-bardia-sighting-chances-best-spots',
  'trek-jungle-nepal-safari-pied': 'jungle-trekking-nepal-walking-safari-guide',
  'voir-des-tigres-au-nepal': 'bengal-tigers-in-nepal-wildlife-safari-guide',
  'dauphin-du-gange-nepal-riviere-karnali-bardia': 'ganges-river-dolphin-nepal-karnali-bardia-guide'
};

export const BLOG_SLUG_MAP_EN_TO_FR: Record<string, string> = Object.entries(BLOG_SLUG_MAP_FR_TO_EN).reduce(
  (acc, [fr, en]) => {
    acc[en] = fr;
    return acc;
  },
  {} as Record<string, string>
);

export function getLocalizedPath(url: URL, targetLang: 'fr' | 'en'): string {
  let path = url.pathname;
  const isEnCurrent = path.startsWith('/en/') || path === '/en';

  // Normalize path without leading /en
  let base = path.replace(/^\/en(\/|$)/, '/');
  if (!base.startsWith('/')) base = '/' + base;

  // Clean trailing .html or / for mapping
  let norm = base.replace(/\.html$/, '').replace(/\/$/, '');

  // Exact route translation map between FR and EN
  const routeMap: Record<string, { fr: string; en: string }> = {
    '': { fr: '/', en: '/en/' },
    '/index': { fr: '/', en: '/en/' },
    '/a-propos': { fr: '/a-propos', en: '/en/about' },
    '/about': { fr: '/a-propos', en: '/en/about' },
    '/mentions-legales': { fr: '/mentions-legales', en: '/en/legal-mentions' },
    '/legal-mentions': { fr: '/mentions-legales', en: '/en/legal-mentions' },
    // Tours & Expeditions Mapping FR <-> EN (Strict SEO Slugs)
    '/tours/safari-pied-bardia': { fr: '/tours/safari-pied-bardia', en: '/en/tours/bardia-walking-safari' },
    '/tours/safari-jeep-bardia': { fr: '/tours/safari-jeep-bardia', en: '/en/tours/bardia-jeep-safari' },
    '/tours/safari-pied-chitwan': { fr: '/tours/safari-pied-chitwan', en: '/en/tours/chitwan-walking-safari' },
    '/tours/safari-jeep-chitwan': { fr: '/tours/safari-jeep-chitwan', en: '/en/tours/chitwan-jeep-safari' },
    '/tours/rafting-safari-bardia': { fr: '/tours/rafting-safari-bardia', en: '/en/tours/bardia-rafting-safari' },
    '/tours/bardia-explorateur': { fr: '/tours/bardia-explorateur', en: '/en/tours/bardia-tiger-safari-5-days' },
    '/tours/jungle-extreme': { fr: '/tours/jungle-extreme', en: '/en/tours/nepal-wildlife-safari-15-days' },
    '/tours/bardia-nuit-sauvage': { fr: '/tours/bardia-nuit-sauvage', en: '/en/tours/bardia-bivouac-camping-safari' },
    '/tours/chitwan-culture': { fr: '/tours/chitwan-culture', en: '/en/tours/chitwan-safari-cultural-tour' },
    '/tours/chitwan-bardia-complete': { fr: '/tours/chitwan-bardia-complete', en: '/en/tours/chitwan-bardia-combined-safari' },
    '/tours/nepal-sauvage': { fr: '/tours/nepal-sauvage', en: '/en/tours/wild-nepal-safari-annapurna-trek' },
    '/tours/bardia-babai-camping': { fr: '/tours/bardia-babai-camping', en: '/en/tours/babai-valley-wild-camping-safari' },
    '/tours/babai-special': { fr: '/tours/babai-special', en: '/en/tours/babai-valley-tiger-tracking-5-days' },
    '/tours/rafting-safari': { fr: '/tours/rafting-safari', en: '/en/tours/karnali-rafting-and-wildlife-safari' },
    '/tours/panthere-des-neiges': { fr: '/tours/panthere-des-neiges', en: '/en/tours/snow-leopard-expedition-nepal' },
    '/tours/rara-lake-bardia': { fr: '/tours/rara-lake-bardia', en: '/en/tours/rara-lake-bardia-expedition' },
    '/tours/nepal-immersion-totale': { fr: '/tours/nepal-immersion-totale', en: '/en/tours/nepal-wildlife-culture-immersion' },
    '/tours/carnet-de-voyage': { fr: '/tours/carnet-de-voyage', en: '/en/tours/nepal-sketching-travel-journal-tour' },
    '/tours/immersion-spirituelle': { fr: '/tours/immersion-spirituelle', en: '/en/tours/himalaya-spiritual-immersion-tour' },
    '/tours/safari-chitwan-3-jours': { fr: '/tours/safari-chitwan-3-jours', en: '/en/tours/chitwan-3-days-safari-post-trek' },
    '/tours/pokhara-chitwan-safari-transfert-katmandou': { fr: '/tours/pokhara-chitwan-safari-transfert-katmandou', en: '/en/tours/pokhara-to-chitwan-safari-transfer-kathmandu' },
    '/tours/chitwan-3-days-safari-post-trek': { fr: '/tours/safari-chitwan-3-jours', en: '/en/tours/chitwan-3-days-safari-post-trek' },
    '/tours/pokhara-to-chitwan-safari-transfer-kathmandu': { fr: '/tours/pokhara-chitwan-safari-transfert-katmandou', en: '/en/tours/pokhara-to-chitwan-safari-transfer-kathmandu' },

    // EN reverse entries
    '/tours/bardia-walking-safari': { fr: '/tours/safari-pied-bardia', en: '/en/tours/bardia-walking-safari' },
    '/tours/bardia-jeep-safari': { fr: '/tours/safari-jeep-bardia', en: '/en/tours/bardia-jeep-safari' },
    '/tours/chitwan-walking-safari': { fr: '/tours/safari-pied-chitwan', en: '/en/tours/chitwan-walking-safari' },
    '/tours/chitwan-jeep-safari': { fr: '/tours/safari-jeep-chitwan', en: '/en/tours/chitwan-jeep-safari' },
    '/tours/bardia-rafting-safari': { fr: '/tours/rafting-safari-bardia', en: '/en/tours/bardia-rafting-safari' },
    '/tours/bardia-tiger-safari-5-days': { fr: '/tours/bardia-explorateur', en: '/en/tours/bardia-tiger-safari-5-days' },
    '/tours/nepal-wildlife-safari-15-days': { fr: '/tours/jungle-extreme', en: '/en/tours/nepal-wildlife-safari-15-days' },
    '/tours/bardia-bivouac-camping-safari': { fr: '/tours/bardia-nuit-sauvage', en: '/en/tours/bardia-bivouac-camping-safari' },
    '/tours/chitwan-safari-cultural-tour': { fr: '/tours/chitwan-culture', en: '/en/tours/chitwan-safari-cultural-tour' },
    '/tours/chitwan-bardia-combined-safari': { fr: '/tours/chitwan-bardia-complete', en: '/en/tours/chitwan-bardia-combined-safari' },
    '/tours/wild-nepal-safari-annapurna-trek': { fr: '/tours/nepal-sauvage', en: '/en/tours/wild-nepal-safari-annapurna-trek' },
    '/tours/babai-valley-wild-camping-safari': { fr: '/tours/bardia-babai-camping', en: '/en/tours/babai-valley-wild-camping-safari' },
    '/tours/babai-valley-tiger-tracking-5-days': { fr: '/tours/babai-special', en: '/en/tours/babai-valley-tiger-tracking-5-days' },
    '/tours/karnali-rafting-and-wildlife-safari': { fr: '/tours/rafting-safari', en: '/en/tours/karnali-rafting-and-wildlife-safari' },
    '/tours/snow-leopard-expedition-nepal': { fr: '/tours/panthere-des-neiges', en: '/en/tours/snow-leopard-expedition-nepal' },
    '/tours/rara-lake-bardia-expedition': { fr: '/tours/rara-lake-bardia', en: '/en/tours/rara-lake-bardia-expedition' },
    '/tours/nepal-wildlife-culture-immersion': { fr: '/tours/nepal-immersion-totale', en: '/en/tours/nepal-wildlife-culture-immersion' },
    '/tours/nepal-sketching-travel-journal-tour': { fr: '/tours/carnet-de-voyage', en: '/en/tours/nepal-sketching-travel-journal-tour' },
    '/tours/himalaya-spiritual-immersion-tour': { fr: '/tours/immersion-spirituelle', en: '/en/tours/himalaya-spiritual-immersion-tour' },
    '/dashain-festival-tharu-cultural-tour': { fr: '/tours/dashain-immersion-culturelle', en: '/en/tours/dashain-festival-tharu-cultural-tour' },
    '/tours/dashain-festival-tharu-cultural-tour': { fr: '/tours/dashain-immersion-culturelle', en: '/en/tours/dashain-festival-tharu-cultural-tour' },
    '/tours/tiji-festival-upper-mustang-trek': { fr: '/tours/tiji-mustang', en: '/en/tours/tiji-festival-upper-mustang-trek' },
  };

  if (routeMap[norm]) {
    return routeMap[norm][targetLang];
  }

  // Blog dynamic post mapping between FR and EN
  if (norm.startsWith('/blog/')) {
    const slug = norm.replace('/blog/', '');
    if (targetLang === 'en') {
      const enSlug = BLOG_SLUG_MAP_FR_TO_EN[slug] || (BLOG_SLUG_MAP_EN_TO_FR[slug] ? slug : slug);
      return `/en/blog/${enSlug}`;
    } else {
      const frSlug = BLOG_SLUG_MAP_EN_TO_FR[slug] || (BLOG_SLUG_MAP_FR_TO_EN[slug] ? slug : slug);
      return `/blog/${frSlug}`;
    }
  }

  // Fallback for general routes (/destinations, /tours/..., /blog)
  const cleanBase = base.replace(/\.html$/, '').replace(/\/$/, '');
  if (targetLang === 'en') {
    if (cleanBase === '' || cleanBase === '/') return '/en/';
    return `/en${cleanBase}`;
  } else {
    return cleanBase === '' ? '/' : cleanBase;
  }
}
