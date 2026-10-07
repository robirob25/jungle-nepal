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
    '/tours/dashain-immersion-culturelle': { fr: '/tours/dashain-immersion-culturelle', en: '/en/tours/dashain-festival-tharu-cultural-tour' },
    '/tours/tiji-mustang': { fr: '/tours/tiji-mustang', en: '/en/tours/tiji-festival-upper-mustang-trek' },

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

  // Fallback for general routes (/destinations, /tours/..., /blog/...)
  const cleanBase = base.replace(/\.html$/, '').replace(/\/$/, '');
  if (targetLang === 'en') {
    if (cleanBase === '' || cleanBase === '/') return '/en/';
    return `/en${cleanBase}`;
  } else {
    return cleanBase === '' ? '/' : cleanBase;
  }
}
