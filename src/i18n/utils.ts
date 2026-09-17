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
