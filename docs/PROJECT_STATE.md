# 🧭 Carnet de Bord & Architecture Technique — Jungle Nepal Adventure

**Dernière mise à jour : 8 Octobre 2026**

---

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

## 2. État du Référencement Naturel (Audit 100% Validé)

### Scores de Santé Technique & Sémantique
- **Score Technique Global** : 99 / 100
- **Liens Internes Cassés (404)** : **0** (tous les liens reliquats WP corrigés)
- **Balises Canoniques** : 183 / 183 pages de contenu couvertes (100%)
- **Structure H1 Unique** : 183 / 183 pages (0 manquant, 0 multiple)
- **Meta Descriptions & Titles** : 183 / 183 pages
- **Données Structurées Schema.org JSON-LD** : 183 / 183 pages (`TravelAgency`, `TouristTrip`, `FAQPage`, `BlogPosting`, `BreadcrumbList`)
- **Accessibilité des Médias** : 100% des images avec balise `alt` renseignée
- **Sitemap XML (`sitemap.xml`)** : 178 URLs actives, **0 redirection 301**, syntaxe XML conforme
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
