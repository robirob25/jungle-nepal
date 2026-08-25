# 🧭 État du Projet & Architecture Technique — Jungle Nepal Adventure

## 1. Vue d'ensemble & Stack Technique
- **Framework** : [Astro 5.4+](https://astro.build/) (Static Site Generation ultra-rapide & performant)
- **Styling** : Tailwind CSS 3.4+ (`@astrojs/tailwind`)
- **Icônes** : Lucide Icons (`lucide`, Lucide CDN / SVG natifs)
- **Typographie** : Plus Jakarta Sans (Google Fonts)
- **Serveur & Routage** :
  - Mode Build : `format: 'file'` (génère des URLs directes `.html` compatibles avec tous les hébergeurs statiques / Apache / Nginx / Hostinger)
  - Serveur Dev recommandé : `npm run dev` (port 8088, supporte le Hot-Reload automatique)

---

## 2. Structure des Dossiers

```
jungle-nepal/
├── src/
│   ├── layouts/
│   │   └── Layout.astro         # Layout global (SEO, OpenGraph, Header, Footer, Modale, WhatsApp)
│   ├── components/
│   │   ├── Header.astro         # Barre de navigation principale & dropdown destinations
│   │   ├── Footer.astro         # Pied de page unifié
│   │   └── ...
│   └── pages/
│       ├── index.astro          # Page d'accueil complète (Hero, Séjours, Carte interactive, Pisteurs, Avis)
│       ├── a-propos.astro       # Page À propos (Équipe, Pawan, Kiran, Robin, Charte éthique)
│       ├── contact.astro        # Page Contact & Devis sur-mesure
│       ├── destinations.astro   # Hub des destinations (Bardia, Chitwan, Annapurna, Suklaphanta, Katmandou)
│       ├── destinations/        # Pages spécifiques par destination (.astro)
│       └── tours/               # Les 14 pages détaillées des séjours (.astro)
│
├── public/                      # Assets statiques servis directement à la racine
│   ├── assets/                  # Images, logos, photos WebP optimisées
│   ├── nepal-map-illustrated.png
│   └── favicon.png
│
├── dist/                        # Dossier de build statique de production
└── scripts/
    └── audit_site.py            # Script d'audit automatique des liens et images
```

---

## 3. Règles d'Or pour la Stabilité (Single Source of Truth)

1. **Source Unique dans `src/`** :
   - Tout contenu (textes, images, composants, prix, liens) **doit être modifié dans `src/pages/*.astro` ou `src/components/*.astro`**.
   - Ne jamais modifier directement les fichiers générés dans `dist/` ou d'anciens `.html` à la racine qui sont écrasés au build.

2. **Format des Liens Internes** :
   - Toujours utiliser des liens absolus avec extension `.html` pour une compatibilité totale :
     - Accueil : `/index.html` ou `/`
     - Destinations : `/destinations.html`
     - Séjour spécifique : `/tours/bardia-explorateur.html`
     - Ancre : `/index.html#prochains-departs`

3. **Images et Médias** :
   - Placer les images dans `public/assets/` ou `public/`.
   - Utiliser des chemins absolus : `src="/assets/img_1.webp"` ou `src="/nepal-map-illustrated.png"`.

4. **Workflow de Vérification & Audit** :
   - Pour lancer le site en développement : `npm run dev`
   - Pour compiler le site : `npm run build`
   - Pour vérifier qu'aucun lien mort ou image manquante n'existe : `python3 scripts/audit_site.py`
