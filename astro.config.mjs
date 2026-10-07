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
    // 1. Navigation, offres & sitelinks
    '/nos-offres': { status: 301, destination: '/#prochains-departs' },
    '/offres': { status: 301, destination: '/#prochains-departs' },
    '/nos-aventures': { status: 301, destination: '/#prochains-departs' },
    '/nos-tours-a-venir': { status: 301, destination: '/#prochains-departs' },
    '/nos-recommandations': { status: 301, destination: '/#prochains-departs' },
    '/voyage-nature-au-nepal-safari-et-aventures-hors-sentiers-battus': { status: 301, destination: '/#prochains-departs' },

    // 2. Entreprise / Contact / À propos
    '/agence-de-safaris-au-nepal': { status: 301, destination: '/a-propos' },
    '/about-us': { status: 301, destination: '/a-propos' },
    '/about': { status: 301, destination: '/a-propos' },
    '/notre-histoire': { status: 301, destination: '/a-propos' },
    '/contact-us': { status: 301, destination: '/contact' },

    // 3. Destinations
    '/nos-destinations': { status: 301, destination: '/destinations' },
    '/parc-national-de-bardia': { status: 301, destination: '/destinations/bardia' },
    '/parc-national-de-chitwan': { status: 301, destination: '/destinations/chitwan' },
    '/parc-national-de-suklaphanta': { status: 301, destination: '/destinations/suklaphanta' },
    '/annapurnas-pokhara': { status: 301, destination: '/destinations/annapurna' },
    '/annapurna-region': { status: 301, destination: '/destinations/annapurna' },
    '/katmandou-vallee-des-rois': { status: 301, destination: '/destinations/katmandou' },
    '/katmandou': { status: 301, destination: '/destinations/katmandou' },

    // 4. Anciens endpoints WordPress /tour/...
    '/tour/jungle-extreme-special-faune-sauvage': { status: 301, destination: '/tours/jungle-extreme' },
    '/tour/nepal-sauvage-de-la-jungle-aux-montagnes-sacrees': { status: 301, destination: '/tours/nepal-sauvage' },
    '/tour/chitwan-bardia-laventure-jungle-complete': { status: 301, destination: '/tours/chitwan-bardia-complete' },
    '/tour/bardia-explorateur-5-jours-dans-la-jungle': { status: 301, destination: '/tours/bardia-explorateur' },
    '/tour/chitwan-culture-et-jungle-sauvage': { status: 301, destination: '/tours/chitwan-culture' },
    '/tour/rivieres-sauvages-et-patrimoines-caches-expedition-et-rafting': { status: 301, destination: '/tours/rafting-safari' },
    '/tour/bardia-aventure-immersive-en-jungle-et-camping-sauvage': { status: 301, destination: '/tours/bardia-nuit-sauvage' },
    '/tour/rara-lake-bardia-expedition-lultime-aventure-hors-sentiers-battus': { status: 301, destination: '/tours/rara-lake-bardia' },
    '/tour/bardia-babai-vallee-camping-sauvage-au-coeur-dune-nature-vierge-et-isolee': { status: 301, destination: '/tours/bardia-babai-camping' },
    '/tour/nepal-immersion-totale-culture-vie-sauvage-et-aventure': { status: 301, destination: '/tours/nepal-immersion-totale' },
    '/tour/deep-into-the-wild-babai-special-experience-5-jours': { status: 301, destination: '/tours/babai-special' },
    '/tour/tiji-festival-tour-upper-mustang': { status: 301, destination: '/tours/tiji-mustang' },
    '/tour/nepal-special-carnet-de-voyage': { status: 301, destination: '/tours/carnet-de-voyage' },
    '/tour/immersion-spirituelle-en-himalaya': { status: 301, destination: '/tours/immersion-spirituelle' },
    '/tour/dashain-immersion-culturelle-special-festival': { status: 301, destination: '/tours/dashain-immersion-culturelle' },

    // 5. Alias /circuits/
    '/circuits/bardia-explorateur': { status: 301, destination: '/tours/bardia-explorateur' },
    '/circuits/safari-bardia-5-jours': { status: 301, destination: '/tours/bardia-explorateur' },
    '/circuits/safari-bivouac-bardia': { status: 301, destination: '/tours/bardia-nuit-sauvage' },
    '/circuits/safari-faune-sauvage-15-jours': { status: 301, destination: '/tours/jungle-extreme' },
    '/circuits/jungle-extreme': { status: 301, destination: '/tours/jungle-extreme' },
    '/circuits/safari-pied-bardia': { status: 301, destination: '/tours/safari-pied-bardia' },
    '/circuits/safari-jeep-bardia': { status: 301, destination: '/tours/safari-jeep-bardia' },
    '/circuits/safari-pied-chitwan': { status: 301, destination: '/tours/safari-pied-chitwan' },
    '/circuits/safari-jeep-chitwan': { status: 301, destination: '/tours/safari-jeep-chitwan' },
    '/safaris': { status: 301, destination: '/tours/jungle-extreme' },

    // 6. Anciens articles de blog WordPress
    '/babai-valley-la-vallee-oubliee-du-nepal-sauvage': { status: 301, destination: '/blog/babai-valley-vallee-oubliee-safari-sauvage' },
    '/bardia-ou-chitwan-safari-nepal': { status: 301, destination: '/blog/bardia-ou-chitwan-quel-parc-choisir' },
    '/camping-jungle-nepal': { status: 301, destination: '/blog/camping-safari-a-bardia-nuits-en-jungle-au-nepal' },
    '/culture-tharu-a-bardia-traditions-villages-et-vie-locale': { status: 301, destination: '/blog/culture-tharu-nepal-immersion-jungle' },
    '/la-faune-du-nepal-a-la-rencontre-du-big-5-de-bardia': { status: 301, destination: '/blog/animaux-bardia-faune-parc-national' },
    '/quand-partir-au-nepal': { status: 301, destination: '/blog/quand-partir-au-nepal-pour-un-safari-guide' },
    '/safari-a-pied-au-nepal-est-ce-dangereux': { status: 301, destination: '/blog/safari-a-pied-nepal-danger-regles-securite-guide' },
    '/safari-au-nepal-vivre-la-jungle-autrement-loin-des-circuits-touristiques': { status: 301, destination: '/blog/comment-organiser-un-safari-au-nepal' },
    '/safari-dans-le-parc-national-de-bardia-au-nepal': { status: 301, destination: '/blog/guide-complet-parc-national-de-bardia-nepal' },
    '/safari-tigre-nepal': { status: 301, destination: '/blog/voir-des-tigres-au-nepal' }
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
