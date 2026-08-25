# Jungle Nepal Adventure 🇳🇵🌿

Site officiel de **Jungle Nepal Adventure** – Agence d'éco-safaris à pied, d'expéditions naturalistes et de retraites spirituelles au Népal (Bardia, Chitwan, Suklaphanta, Annapurna, Katmandou).

## 🚀 Stack Technique Moderne (2026)
- **Framework :** [Astro 5](https://astro.build/) (Static Site Generation ultra-rapide)
- **Styles :** [Tailwind CSS](https://tailwindcss.com/)
- **Icons :** [Lucide React / Inline SVG](https://lucide.dev/)
- **SEO & Structured Data :** Schema.org (`TouristTrip`, `LocalBusiness`, `FAQPage`), OpenGraph, Sitemap XML & Canonical tags.
- **Routage :** Dual Routing System (`/route` & `/route.html`) pour compatibilité serveur universelle.

## 📁 Structure du Projet
```
├── public/                 # Assets statiques (photos Drive WebP, logos, sitemap, robots.txt)
├── src/
│   ├── components/         # Header & Footer modulaires
│   ├── data/               # Données JSON (15 tours, 5 destinations, avis, galerie)
│   ├── layouts/            # Layout principal avec SEO, favicons dynamiques & modal devis
│   └── pages/              # Pages Astro (Accueil, À propos, Contact, Destinations, Tours)
├── .github/workflows/      # Déploiement automatique GitHub Actions
└── ensure_dual_routes.py   # Script de garantie de double routage statique
```

## 🛠️ Développement Local
```bash
# Installation des dépendances
npm install

# Lancer le serveur de développement
npm run dev

# Compiler pour la production
npm run build
```
