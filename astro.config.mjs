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
        const excluded = ['/merci', '/confirmation', '/thank-you', '/404'];
        return !excluded.some((p) => page.includes(p));
      }
    })
  ],
  redirects: {
    '/nos-offres': '/#prochains-departs',
    '/nos-offres/': '/#prochains-departs',
    '/offres': '/#prochains-departs',
    '/offres/': '/#prochains-departs',
    '/agence-de-safaris-au-nepal': '/a-propos',
    '/agence-de-safaris-au-nepal/': '/a-propos',
    '/nos-aventures': '/#prochains-departs',
    '/nos-aventures/': '/#prochains-departs',
    '/nos-destinations': '/destinations',
    '/nos-destinations/': '/destinations',
    '/safaris': '/tours/jungle-extreme',
    '/safaris/': '/tours/jungle-extreme',
    '/parc-national-de-bardia': '/destinations/bardia',
    '/parc-national-de-bardia/': '/destinations/bardia',
    '/parc-national-de-chitwan': '/destinations/chitwan',
    '/parc-national-de-chitwan/': '/destinations/chitwan',
    '/parc-national-de-suklaphanta': '/destinations/suklaphanta',
    '/parc-national-de-suklaphanta/': '/destinations/suklaphanta',
    '/annapurnas-pokhara': '/destinations/annapurna',
    '/annapurnas-pokhara/': '/destinations/annapurna',
    '/katmandou-vallee-des-rois': '/destinations/katmandou',
    '/katmandou-vallee-des-rois/': '/destinations/katmandou',
    '/contact-us': '/contact',
    '/contact-us/': '/contact',
    '/about-us': '/a-propos',
    '/about-us/': '/a-propos',
    '/about': '/a-propos',
    '/about/': '/a-propos',
    '/notre-histoire': '/a-propos',
    '/notre-histoire/': '/a-propos',
    // Circuits URL aliases
    '/circuits/bardia-explorateur': '/tours/bardia-explorateur',
    '/circuits/safari-bardia-5-jours': '/tours/bardia-explorateur',
    '/circuits/safari-bivouac-bardia': '/tours/bardia-nuit-sauvage',
    '/circuits/safari-faune-sauvage-15-jours': '/tours/jungle-extreme',
    '/circuits/jungle-extreme': '/tours/jungle-extreme',
    '/circuits/safari-pied-bardia': '/tours/safari-pied-bardia',
    '/circuits/safari-jeep-bardia': '/tours/safari-jeep-bardia'
  },
  i18n: {
    defaultLocale: 'fr',
    locales: ['fr', 'en'],
    routing: {
      prefixDefaultLocale: false
    }
  },
  build: {
    format: 'directory'
  },
  server: {
    port: 8088,
    host: true
  }
});
