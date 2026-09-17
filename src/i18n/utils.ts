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

  // Normalize: strip leading /en if present (including /en.html or /en/)
  path = path.replace(/^\/en(\.html|\/|$)/, '/');

  if (!path.startsWith('/')) {
    path = '/' + path;
  }

  // Handle root homepage
  if (path === '/' || path === '/index.html' || path === '') {
    return targetLang === 'en' ? '/en/' : '/';
  }

  if (targetLang === 'en') {
    return `/en${path}`;
  }

  return path;
}
