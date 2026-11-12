import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://junglenepal.com',
  integrations: [
    tailwind(),
    sitemap({
      i18n: {
        defaultLocale: 'fr',
        locales: {
          fr: 'fr-FR',
          en: 'en-US'
        }
      },
      filter: (page) => {
        // Exclude thank-you / confirmation / private pages
        const excluded = ['/merci', '/booking-success', '/confirmation', '/thank-you', '/404'];
        return !excluded.some((p) => page.includes(p));
      }
    })
  ],
  i18n: {
    defaultLocale: 'fr',
    locales: ['fr', 'en'],
    routing: {
      prefixDefaultLocale: false
    }
  },
  build: {
    format: 'directory',
    inlineStylesheets: 'always'
  },
  server: {
    port: 8088,
    host: true
  }
});
