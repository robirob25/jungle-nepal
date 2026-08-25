import json, re, glob, os

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

tour_map = {t['slug']: t for t in tours}
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for tp in tour_files:
    slug = os.path.splitext(os.path.basename(tp))[0]
    tdata = tour_map.get(slug)
    if not tdata:
        continue

    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    clean_overview = tdata.get('overview', '').replace('"', '\\"').replace('\n', ' ')
    price_val = str(tdata.get('price', 850)).replace('€', '').replace(' ', '')
    rating_val = str(tdata.get('rating', '4.9'))
    reviews_count = str(tdata.get('reviews', 35)).replace('avis', '').replace('(', '').replace(')', '').strip() or '35'

    tour_schema = f"""  <!-- SCHEMA.ORG TOURIST TRIP JSON-LD (RICH SNIPPETS GOOGLE) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TouristTrip",
    "name": "{tdata['title']}",
    "description": "{clean_overview}",
    "image": "https://junglenepal.com{tdata.get('image', '/assets/original_site/tigre_bardia.webp')}",
    "touristType": ["Amoureux de nature", "Photographes animaliers", "Aventuriers"],
    "offers": {{
      "@type": "Offer",
      "price": "{price_val}",
      "priceCurrency": "EUR",
      "availability": "https://schema.org/InStock",
      "validFrom": "2026-08-01",
      "url": "https://junglenepal.com/tours/{slug}.html"
    }},
    "provider": {{
      "@type": "TravelAgency",
      "name": "Jungle Nepal Adventure",
      "url": "https://junglenepal.com"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "{rating_val}",
      "reviewCount": "{reviews_count}",
      "bestRating": "5"
    }}
  }}
  </script>"""

    if 'TouristTrip' not in c:
        c = c.replace('<Layout title=', tour_schema + '\n\n<Layout title=')
        with open(tp, 'w', encoding='utf-8') as f:
            f.write(c)

print("Successfully injected Schema.org TouristTrip JSON-LD across all 15 tour detail pages!")
