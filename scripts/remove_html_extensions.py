import os
import re
import glob

base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'

# 1. Update astro.config.mjs
astro_config_path = os.path.join(base_dir, 'astro.config.mjs')
if os.path.exists(astro_config_path):
    with open(astro_config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("format: 'file'", "format: 'directory'")
    with open(astro_config_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated astro.config.mjs to format: 'directory'")

# 2. Update src/i18n/utils.ts
utils_path = os.path.join(base_dir, 'src/i18n/utils.ts')
new_utils_content = '''import { ui, defaultLang } from './ui';

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
  let base = path.replace(/^\\/en(\\/|$)/, '/');
  if (!base.startsWith('/')) base = '/' + base;

  // Clean trailing .html or / for mapping
  let norm = base.replace(/\\.html$/, '').replace(/\\/$/, '');

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
  const cleanBase = base.replace(/\\.html$/, '').replace(/\\/$/, '');
  if (targetLang === 'en') {
    if (cleanBase === '' || cleanBase === '/') return '/en/';
    return `/en${cleanBase}`;
  } else {
    return cleanBase === '' ? '/' : cleanBase;
  }
}
'''
with open(utils_path, 'w', encoding='utf-8') as f:
    f.write(new_utils_content)
print("Updated src/i18n/utils.ts")

# 3. Replace .html in all .astro, .ts, .js files under src/
files = glob.glob(os.path.join(base_dir, 'src/**/*.*'), recursive=True)
count = 0
for filepath in files:
    if not (filepath.endswith('.astro') or filepath.endswith('.ts') or filepath.endswith('.js') or filepath.endswith('.json')):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # Replace href="/blog/...html" with "/blog/..."
    new_content = re.sub(r'href=(["\'])(/(?:en/)?(?:blog|tours|destinations|a-propos|contact|about|mentions-legales|legal-mentions)[^"\']*?)\.html\1', r'href=\1\2\1', new_content)
    
    # Template string replacements e.g. `/blog/${slug}.html` -> `/blog/${slug}`
    new_content = re.sub(r'`(/(?:en/)?(?:blog|tours|destinations|a-propos|contact)[^`]*?)\.html`', r'`\1`', new_content)
    
    # Header.astro variable assignments
    new_content = new_content.replace("'/destinations.html'", "'/destinations'")
    new_content = new_content.replace("'/en/destinations.html'", "'/en/destinations'")
    new_content = new_content.replace("'/a-propos.html'", "'/a-propos'")
    new_content = new_content.replace("'/en/a-propos.html'", "'/en/a-propos'")
    new_content = new_content.replace("'/blog.html'", "'/blog'")
    new_content = new_content.replace("'/en/blog.html'", "'/en/blog'")
    new_content = new_content.replace("'/contact.html'", "'/contact'")
    new_content = new_content.replace("'/en/contact.html'", "'/en/contact'")
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated: {os.path.relpath(filepath, base_dir)}")

print(f"Updated {count} files in src/")
