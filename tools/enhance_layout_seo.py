with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

schema_org_agency = """  <!-- SCHEMA.ORG TRAVEL AGENCY JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "TravelAgency",
    "name": "Jungle Nepal Adventure",
    "url": "https://junglenepal.com",
    "logo": "https://junglenepal.com/assets/logo_nav_white.png",
    "image": "https://junglenepal.com/assets/original_site/tigre_bardia.webp",
    "description": "Agence locale d'écotourisme d'exception et de safaris immersifs au Népal. Traque à pied du tigre du Bengale, panthère des neiges et expéditions sauvages.",
    "telephone": "+33695413227",
    "email": "contact@junglenepal.com",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Bardia & Katmandou",
      "addressCountry": "NP"
    },
    "priceRange": "450€ - 3890€",
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "142",
      "bestRating": "5"
    }
  }
  </script>"""

if 'TravelAgency' not in c:
    c = c.replace('<!-- Plus Jakarta Sans Font -->', schema_org_agency + '\n\n  <!-- Plus Jakarta Sans Font -->')
    with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Enhanced Layout.astro with Schema.org TravelAgency JSON-LD!")
else:
    print("Schema.org already in Layout.astro")
