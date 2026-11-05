# 🧭 Carnet de Bord & Architecture Technique — Jungle Nepal Adventure

**Dernière mise à jour : 4 Novembre 2026**

---

## 🔒 Conformité Google Ads & Sécurité Forensic (Novembre 2026)
- **Motifs traités** : « Site infecté » (Compromised Site) et « Contournement des systèmes » (Circumventing Systems).
- **Hardening `.htaccess` en production** :
  - Blocage strict en HTTP 403 de tous les dossiers résiduels WordPress (`wp-includes_old_backup`, `wp-content_backup`, `wp-admin`, etc.).
  - Redirection 301 propre de `/conditions-generales` vers `/mentions-legales/` (résolution du 404).
  - En-têtes de sécurité renforcés : HSTS, CSP, X-Frame-Options, X-Content-Type-Options.
- **Assainissement des Avis Clients** :
  - **100% d'avis authentiques** issus des avis Google réels vérifiés (Eric Martin, Adrien Noat, Samantha Gonthier, Jean Tramoy, Alice Palasti, Justine Luçon, Nicole Cooper, Max Schlautmann, Matthew John).
  - Élimination intégrale des prénoms fictifs / placeholders.
  - Harmonisation du total à **22 avis vérifiés (note 5.0 / 5)** sur l'ensemble des fiches circuits (FR/EN) et dans les métadonnées Schema.org (`reviewCount: "22"`).
- **Conformité des Données Marchandes (Schema.org)** :
  - Suppression des champs `shippingDetails` et `ReturnByMail` inadaptés aux prestations de voyages et safaris.
  - Alignement des mentions légales et conditions d'acompte (MYWAY SAS / Pawan Thapa).

## 1. Vue d'Ensemble & Stack Technique
- **Framework** : [Astro 5.4+](https://astro.build/) (Static Site Generation ultra-performant)
- **Styling** : Tailwind CSS 3.4+ (`@tailwindcss/typography`)
- **Typographie** : Plus Jakarta Sans (Google Fonts & Webfonts locales)
- **Hébergement & CDN** : Hostinger VPS / Cloudflare CDN
- **Déploiement** : Script de synchronisation atomique multithread FTP (`tools/sync_tours_robust.py`)
- **Internationalisation (i18n)** : Bilingue strict **Français (FR 🇫🇷)** et **Anglais (EN 🇬🇧)**
  - Pas de traduction automatique tierce (Google Translate éliminé)
  - Balises `hreflang` réciproques complètes (`fr`, `en`, `x-default`)

---

## 2. État du Référencement Naturel (Audit 360° 100% Validé)

### Scores de Santé Technique & Sémantique
- **Score Technique Global** : 100 / 100
- **Liens Internes Cassés (404)** : **0** (toutes les pages, destinations et redirections 301 vérifiées)
- **Balises Canoniques** : 188 / 188 pages indexables couvertes (100%)
- **Structure H1 Unique** : 188 / 188 pages (0 manquant, 0 multiple)
- **Meta Descriptions & Titles** : 188 / 188 pages avec meta description unique calibrée (135-165 caractères, 0 doublon)
- **Données Structurées Schema.org JSON-LD** : 188 / 188 pages (`TravelAgency`, `["TouristTrip", "Product"]`, `FAQPage`, `BlogPosting`, `BreadcrumbList` — 0 bloc dupliqué)
- **Accessibilité des Médias** : 100% des images avec balise `alt` renseignée et 0 image cassée
- **Sitemap XML (`sitemap.xml`)** : 188 URLs actives (couverture 100%, 0 redirection 301, syntaxe XML conforme)
- **LLM Knowledge Base (`llms.txt` & `llms-full.txt`)** : Synchronisé avec les 18 circuits et 5 activités à la journée
- **Robots.txt** : Déclaration propre pointant sur `https://junglenepal.com/sitemap.xml`

---

## 3. Stratégie d'Offre & Monétisation SEO

### A. Les 10 Activités à la Journée (Ciblage « Day Tours » Haute Intention)
Ces fiches captent les touristes déjà au Népal ou préparant leur voyage depuis l'étranger pour réserver immédiatement :
1. **Safari à pied à Bardia (Walking Safari)** : 50 €
   - FR : `/tours/safari-pied-bardia`
   - EN : `/en/tours/bardia-walking-safari`
2. **Safari en Jeep à Bardia** : 190 € (privatif)
   - FR : `/tours/safari-jeep-bardia`
   - EN : `/en/tours/bardia-jeep-safari`
3. **Safari à pied à Chitwan (Traque des rhinocéros)** : 70 €
   - FR : `/tours/safari-pied-chitwan`
   - EN : `/en/tours/chitwan-walking-safari`
4. **Safari en Jeep à Chitwan** : 190 €
   - FR : `/tours/safari-jeep-chitwan`
   - EN : `/en/tours/chitwan-jeep-safari`
5. **Rafting & Safari sur la rivière Karnali** : 120 €
   - FR : `/tours/rafting-safari-bardia`
   - EN : `/en/tours/bardia-rafting-safari`

### B. Circuits Majeurs & Séjours Longs
- **Immersion Spirituelle en Himalaya** : Prix actualisé à **2 190 €**
  - FR : `/tours/immersion-spirituelle`
  - EN : `/en/tours/himalaya-spiritual-immersion-tour`
- **Jungle Extrême (15 jours)** : 2 490 €
- **Bardia Explorateur (5 jours)** : 690 €
- **Expédition Panthère des Neiges** : 4 190 €

---

## 4. Maillage Interne & Siloing Blog ➔ Fiches Tours & Activités
- **120 articles de blog audités et 100% optimisés (60 FR + 60 EN)** :
  - **Taux de couverture tours : 100%** (zéro article orphelin ou sans lien d'activité).
  - Moyenne de **3,02 liens tours par article en FR** et **3,88 liens tours par article en EN**.
  - Chaque article intègre désormais 2 à 4 ancres contextuelles et naturelles dans le corps du texte (reliées aux safaris à la journée à 50€/70€/120€/190€ et aux expéditions multi-jours 5j/11j/15j/17j).
  - Remplacement de 75 liens génériques vagues (`/#prochains-departs`) par les URLs exactes des fiches d'activités.
  - Cartes d'appel à l'action contextuelles en fin d'article adaptées à chaque thématique animale ou géographique.

---

## 5. Procédure de Déploiement & Sécurité Cache
À chaque exécution de `npm run build`, la chaîne automatique s'exécute :
1. `generate_perfect_sitemap.py` : régénère `sitemap.xml` avec toutes les URLs actives et les alternates hreflang.
2. `astro build` : compile le code statique dans `dist/`.
3. `ensure_dual_routes.py` : garantit le double routage (support des URLs avec et sans slash).
4. `sync_tours_robust.py` : déploie par FTP de façon atomique vers Hostinger.

> **Règle d'or de cache** : En cas de modification CSS/JS, toujours s'assurer que les fichiers `dist/_astro/` sont bien téléversés et ajouter si nécessaire un query parameter de cache buster (`?v=...`) pour éviter que le CDN ne serve une version antérieure.

---

## 6. Architecture Réseau, DNS & Optimisation Vitesse (Octobre 2026)
- **Résolution DNS & TTFB (0,15s - 0,20s)** :
  - Le domaine apex `junglenepal.com` et `admin` pointent directement en IPv4 (`A`) vers l'adresse réelle de l'origin Hostinger LiteSpeed (`213.130.145.177`) avec proxy Cloudflare actif.
  - Les enregistrements AAAA obsolètes / hors-service et les relais tiers défaillants ont été éliminés pour supprimer tout timeout de 20s.
  - Le CNAME `www` pointe proprement vers `junglenepal.com`.
- **Core Web Vitals & Google PageSpeed** :
  - Seule la slide visible (Slide 0) est chargée en priorité haute (`fetchpriority="high"`, `loading="eager"`). Les 9 slides suivantes sont différées en `loading="lazy"`, réduisant le poids initial de ~2 Mo.
  - Bibliothèque d'icônes `Lucide` auto-hébergée localement dans `/assets/js/lucide.min.js` avec chargement `defer`, éliminant l'appel tiers à `unpkg.com`.
  - Google Analytics 4 (`gtag.js`) différé au chargement de la page (`window.onload`) pour éliminer le blocage du thread principal et le reflow forcé.

---

## 7. Initiative Conservation & Communautés (NAGA Conservation Project — Novembre 2026)
- **Nouvelles routes bilingues intégrées** :
  - FR : `/conservation/` (`src/pages/conservation.astro`)
  - EN : `/en/conservation/` (`src/pages/en/conservation.astro`)
- **Partenariat de terrain** : Jungle Nepal Adventure × Nature Guide Association (NAGA) de Bardia (fondée en 2054 BS / 1997-1998 CE).
- **Gouvernance & Acteurs** :
  - Krisna Saha (Président actuel de la NAGA)
  - Pawan Thapa (Co-fondateur & Directeur des Opérations Terrain de Jungle Nepal Adventure, membre actif de la NAGA)
  - Robin Rozier (Fondateur de Jungle Nepal Adventure)
- **Storytelling de terrain & Réalité des Risques** :
  - Conflits réels hommes-faune à Bardia (éléphants, tigres, léopards, rhinocéros) et rôle central des guides comme médiateurs locaux.
  - Accidents graves vécus (attaque de tigre subie par Krisna Saha, chute d'arbre de Pawan Thapa, décès d'un guide par rhinocéros).
  - Engagement de don fixe par participant à chaque tour avec pour objectif une couverture assurance privée complète pour tous les guides de Bardia d'ici 2027.
- **Direction artistique & UX Mobile-First** :
  - Grille éditoriale responsive 2 colonnes sur les 6 missions statutaires de la NAGA.
  - Diptyque grand angle avec photo de tigre dans les hautes herbes et texte immersif.
  - Optimisation responsive mobile complète (paddings fluidifiés `p-5 sm:p-8 lg:p-12`, boutons pleine largeur en colonne sur smartphone, tailles typographiques calibrées pour éviter les retours à la ligne disgracieux, espacements et zones tactiles >= 44px).
  - Suppression de tout artifice IA (suppression des puces/bulles décoratives, micro-chiffres et jauges factices).
- **Sitemap & SEO** : 202 URLs indexées avec balises `hreflang` bidirectionnelles FR/EN/x-default.

---

## 8. Moteur de Réservation Directe Stripe (Activités à la Journée — Novembre 2026)
- **Objectif Business & Juridique** :
  - Vente directe sans intermédiaire des 5 excursions à la journée (< 24h, sans nuitée obligatoire) dispensées d'agrément Atout France.
  - Taux de conversion maximal : sélection de date, nombre de participants, options locales, paiement CB / Apple Pay / Google Pay direct via Stripe Checkout hébergé.
- **Les 10 fiches tours équipées du module interactif** :
  1. `safari-pied-bardia` (FR: 50€/pers) & `bardia-walking-safari` (EN: 50€/pers)
  2. `safari-jeep-bardia` (FR: 190€ forfait) & `bardia-jeep-safari` (EN: 190€ forfait)
  3. `safari-pied-chitwan` (FR: 70€/pers) & `chitwan-walking-safari` (EN: 70€/pers)
  4. `safari-jeep-chitwan` (FR: 190€ forfait) & `chitwan-jeep-safari` (EN: 190€ forfait)
  5. `rafting-safari-bardia` (FR: 190€ forfait) & `bardia-rafting-safari` (EN: 190€ forfait)
- **Architecture Technique & Sécurité** :
  - `src/components/DayTourBookingWidget.astro` : Calendrier interactif (sélecteur date HTML5 avec date min = demain, raccourcis Demain / +2j / +1semaine), compteur voyageurs avec désactivation automatique aux bornes min/max, option nuitée chez Pawan (+12€/pers), coordonnées de prise en charge hôtel, recalcul dynamique du prix, soumission asynchrone sécurisée.
  - `public/api/stripe-config.php` : Clés API Stripe (actuellement en mode Test `pk_test_...` et `sk_test_...`), email de notification, URL racine.
  - `public/api/.htaccess` : Protection 403 Forbidden sur `stripe-config.php` et tout fichier `.env*`.
  - `public/api/create-checkout-session.php` : Endpoint PHP natif cURL sans dépendances Composer. Validation stricte côté serveur des tarifs du catalogue (EUR cents), gestion dynamique des devises et moyens de paiement (Cards, Apple Pay, Google Pay), métadonnées complètes passées à Stripe (date, participants, WhatsApp, hôtel, langue).
  - Support des alias d'URL FR et EN.
  - `src/pages/merci-reservation.astro` (FR) & `src/pages/en/booking-success.astro` (EN) : Pages de confirmation après paiement réussi avec étapes suivantes, numéro WhatsApp direct et récapitulatif.
  - Permissions-Policy mise à jour dans `public/.htaccess` : `payment=*` pour autoriser Apple Pay et Google Pay.
  - CSP dans `src/layouts/Layout.astro` configuré pour autoriser `*.stripe.com`.

