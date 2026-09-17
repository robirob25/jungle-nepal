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
  const isEnCurrent = path.startsWith('/en/') || path === '/en' || path === '/en.html';

  // Normalize path without leading /en
  let base = path.replace(/^\/en(\.html|\/|$)/, '/');
  if (!base.startsWith('/')) base = '/' + base;

  // Clean trailing .html or / for mapping
  let norm = base.replace(/\.html$/, '').replace(/\/$/, '');

  // Exact route translation map between FR and EN
  const routeMap: Record<string, { fr: string; en: string }> = {
    '': { fr: '/', en: '/en/' },
    '/index': { fr: '/', en: '/en/' },
    '/a-propos': { fr: '/a-propos.html', en: '/en/about.html' },
    '/about': { fr: '/a-propos.html', en: '/en/about.html' },
    '/mentions-legales': { fr: '/mentions-legales.html', en: '/en/legal-mentions.html' },
    '/legal-mentions': { fr: '/mentions-legales.html', en: '/en/legal-mentions.html' },
  };

  if (routeMap[norm]) {
    return routeMap[norm][targetLang];
  }

  // Fallback for general routes (/destinations, /tours/..., /blog/...)
  if (targetLang === 'en') {
    if (base === '/' || base === '') return '/en/';
    return `/en${base.endsWith('.html') || base.includes('/tours/') || base.includes('/destinations/') || base.includes('/blog/') ? base : base + '.html'}`;
  } else {
    return base === '' ? '/' : base;
  }
}
