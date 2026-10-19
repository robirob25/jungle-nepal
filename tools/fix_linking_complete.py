import json, re

with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

# French additions for the 4 remaining posts
FR_EXTRA = {
    'safari-photo-au-nepal-spots-materiel-conseils': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">📸 Conseils Jungle Nepal pour les photographes</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed mb-3">Pour optimiser vos prises de vue animalières, nous recommandons de combiner notre <a href="/tours/safari-jeep-bardia" class="text-emerald-800 font-bold underline">safari en jeep privatisée à Bardia (190 €/véhicule)</a> pour transporter vos téléobjectifs et notre <a href="/tours/safari-pied-bardia" class="text-emerald-800 font-bold underline">affût à pied (dès 50 €)</a> pour les angles rasants.</p>'
        '<p class="text-xs text-slate-600 font-medium">Pour une immersion photo complète de 5 jours : <a href="/tours/bardia-explorateur" class="text-emerald-800 font-bold underline">consultez notre séjour Bardia Explorateur</a>.</p>'
        '</div>'
    ),
    'ou-voir-panthere-des-neiges-nepal-dolpo-mustang': (
        '<div class="p-6 bg-slate-900 text-white rounded-2xl my-8 border border-white/10">'
        '<h4 class="text-base font-bold text-amber-300 mb-2">🏔️ Expéditions haute altitude Jungle Nepal</h4>'
        '<p class="text-sm text-slate-300 leading-relaxed mb-3">Pour partir sur les traces de l\'once au cœur de l\'Himalaya sauvage, explorez notre <a href="/tours/panthere-des-neiges" class="text-emerald-400 font-bold underline">Expédition officielle Panthère des Neiges (17 jours)</a> ou découvrez les falaises sacrées lors de notre trek du <a href="/tours/tiji-mustang" class="text-emerald-400 font-bold underline">Tiji Festival en Haut Mustang</a>.</p>'
        '</div>'
    ),
    'prix-preparation-expedition-panthere-des-neiges-nepal': (
        '<div class="p-6 bg-slate-900 text-white rounded-2xl my-8 border border-white/10">'
        '<h4 class="text-base font-bold text-amber-300 mb-2">🏔️ Préparer votre expédition avec nos guides</h4>'
        '<p class="text-sm text-slate-300 leading-relaxed mb-3">Consultez notre programme clé en main <a href="/tours/panthere-des-neiges" class="text-emerald-400 font-bold underline">Expédition Panthère des Neiges (17 jours)</a> incluant permis DNPWC, campings d\'altitude et pisteurs natifs, ou découvrez notre trek d\'altitude <a href="/tours/tiji-mustang" class="text-emerald-400 font-bold underline">Tiji Festival Haut Mustang</a>.</p>'
        '</div>'
    ),
    'ecologie-pistage-panthere-des-neiges-bharal-nepal': (
        '<div class="p-6 bg-slate-900 text-white rounded-2xl my-8 border border-white/10">'
        '<h4 class="text-base font-bold text-amber-300 mb-2">🐾 Pistage sur le terrain</h4>'
        '<p class="text-sm text-slate-300 leading-relaxed mb-3">Vivez cette traque éthique en haute montagne lors de notre <a href="/tours/panthere-des-neiges" class="text-emerald-400 font-bold underline">Expédition Panthère des Neiges (17 jours)</a> ou explorez les contrastes du Népal sur notre combiné <a href="/tours/nepal-sauvage" class="text-emerald-400 font-bold underline">Népal Sauvage : Trek des Annapurnas & Safari</a>.</p>'
        '</div>'
    )
}

for post in posts_fr:
    slug = post['slug']
    if slug in FR_EXTRA:
        if '📸' not in post['content'] and '🏔️' not in post['content'] and '🐾' not in post['content']:
            post['content'] += "\n\n" + FR_EXTRA[slug]
            print(f"Added extra rich box to FR: {slug}")

# Now English Posts: ensure every EN post has natural in-text tour links
EN_SNIPPETS = {
    'safari-nepal-en-famille-securite-lodges-enfants': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">🌿 Family Safari Recommendations</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">For safe, comfortable wildlife watching with kids, book our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-800 font-bold underline">Private 4x4 Jeep Safari in Bardia (€190/jeep)</a>, our <a href="/en/tours/chitwan-jeep-safari" class="text-emerald-800 font-bold underline">Private Chitwan Jeep Safari</a>, or join our gentle <a href="/en/tours/chitwan-safari-cultural-tour" class="text-emerald-800 font-bold underline">Chitwan Safari Cultural Tour (4 Days)</a>.</p>'
        '</div>'
    ),
    'culture-tharu-traditions-cuisine-festival-dashain-bardia': (
        '<div class="p-6 bg-amber-50/80 border border-amber-200 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-amber-950 mb-2">🏮 Authentic Tharu Village Immersions</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Experience living indigenous traditions on our <a href="/en/tours/dashain-festival-tharu-cultural-tour" class="text-emerald-800 font-bold underline">Dashain Festival & Tharu Cultural Tour</a> or combine cultural villages and wildlife on our <a href="/en/tours/chitwan-safari-cultural-tour" class="text-emerald-800 font-bold underline">Chitwan Safari Cultural Tour (4 Days)</a>.</p>'
        '</div>'
    ),
    'safari-combine-inde-nepal-corbett-dudhwa-suklaphanta-bardia': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">🐅 Grand Wildlife Circuits</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Discover our ultimate multi-park expedition <a href="/en/tours/nepal-wildlife-safari-15-days" class="text-emerald-800 font-bold underline">Nepal Wildlife Safari (15 Days)</a> exploring Suklaphanta, Bardia, and Chitwan, or book our daily <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Walking Tiger Safari in Bardia (from €50)</a>.</p>'
        '</div>'
    ),
    'guide-ornithologique-nepal-oiseaux-bardia-suklaphanta': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">🦅 Birdwatching Safaris in Nepal</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Spot over 500 species on our <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Bardia Birdwatching Walking Safari (from €50)</a>, our gentle <a href="/en/tours/bardia-rafting-safari" class="text-emerald-800 font-bold underline">Karnali River Rafting Drift Safari (€120)</a>, or our all-inclusive <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-800 font-bold underline">Bardia Tiger Safari 5 Days</a>.</p>'
        '</div>'
    ),
    'safari-dos-elephant-nepal-pourquoi-refuser-cette-pratique': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">🐘 Ethical Wildlife Watching Alternatives</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">We strictly boycott captive elephant riding. Choose 100% ethical observation on foot with our <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Bardia Walking Safari (from €50)</a>, our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-800 font-bold underline">Chitwan Walking Safari (from €70)</a>, or in an open <a href="/en/tours/bardia-jeep-safari" class="text-emerald-800 font-bold underline">Private 4x4 Jeep Safari</a>.</p>'
        '</div>'
    ),
    'comment-aller-a-bardia-transport-avion-bus-guide': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">✈️ Hassle-Free Transfer & Lodge Packages</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Save the stress of independent travel with our all-inclusive package including Nepalgunj airport transfers: <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-800 font-bold underline">Bardia Tiger Safari 5 Days (€690)</a> or book our day activities: <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Walking Safari (from €50)</a> and <a href="/en/tours/bardia-jeep-safari" class="text-emerald-800 font-bold underline">Private 4x4 Jeep Safari (€190)</a>.</p>'
        '</div>'
    ),
    'comment-aller-a-chitwan-katmandou-pokhara-bus-avion': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">🦏 Explore Chitwan with Native Naturalists</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Arriving from Kathmandu or Pokhara? Book our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-800 font-bold underline">Chitwan Rhino Walking Safari (from €70)</a>, our <a href="/en/tours/chitwan-jeep-safari" class="text-emerald-800 font-bold underline">Private Chitwan Jeep Safari (€190)</a>, or our 4-day <a href="/en/tours/chitwan-safari-cultural-tour" class="text-emerald-800 font-bold underline">Chitwan Safari Cultural Tour</a>.</p>'
        '</div>'
    ),
    'tigre-bardia-observation-chances-spots': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">🐅 Maximize Your Tiger Sighting Chances</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Book our daily <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Bardia Walking Tiger Safari (from €50)</a> with two certified naturalists, explore distant river branches on our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-800 font-bold underline">Private 4x4 Jeep Safari (€190)</a>, or choose our flagship 5-day package <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-800 font-bold underline">Bardia Tiger Safari 5 Days (€690)</a>.</p>'
        '</div>'
    ),
    'safari-photo-tigre-nepal-bardia-guide-affut': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">📷 Wildlife Photography in Bardia</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">For telephoto flexibility, reserve our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-800 font-bold underline">Private 4x4 Jeep Safari (€190/vehicle)</a> and pair it with our silent <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Walking Tiger Safari (from €50)</a> or our immersive <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-800 font-bold underline">5-Day Bardia Tiger Safari</a>.</p>'
        '</div>'
    ),
    'prix-dun-safari-au-nepal': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">💶 Transparent Safari Rates</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Book directly with local transparent pricing: <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Walking Safari in Bardia (from €50)</a>, <a href="/en/tours/bardia-jeep-safari" class="text-emerald-800 font-bold underline">Private 4x4 Jeep Safari (€190)</a>, <a href="/en/tours/chitwan-walking-safari" class="text-emerald-800 font-bold underline">Chitwan Walking Safari (from €70)</a>, or our all-inclusive 5-day package <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-800 font-bold underline">Bardia Tiger Safari 5 Days (€690)</a>.</p>'
        '</div>'
    ),
    'bardia-ou-chitwan-quel-parc-choisir': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">🌿 Can\'t Decide? Compare or Combine Both!</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Choose our <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Bardia Walking Safari (from €50)</a> for raw wild tiger tracking, our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-800 font-bold underline">Chitwan Walking Safari (from €70)</a> for rhinos, or enjoy the complete experience with our <a href="/en/tours/chitwan-bardia-combined-safari" class="text-emerald-800 font-bold underline">Chitwan + Bardia Combined Safari (11 Days)</a>.</p>'
        '</div>'
    ),
    'comment-organiser-un-safari-au-nepal': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">🐾 Plan Your Nepal Safari with Local Experts</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Explore our flexible options: <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Walking Safari in Bardia (from €50)</a>, <a href="/en/tours/bardia-jeep-safari" class="text-emerald-800 font-bold underline">Private 4x4 Jeep Safari (€190)</a>, our 5-day package <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-800 font-bold underline">Bardia Tiger Safari (€690)</a>, or our grand <a href="/en/tours/nepal-wildlife-safari-15-days" class="text-emerald-800 font-bold underline">Nepal Wildlife Safari 15 Days</a>.</p>'
        '</div>'
    ),
    'safari-a-pied-au-nepal-guide-complet': (
        '<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
        '<h4 class="text-base font-bold text-emerald-950 mb-2">🚶 Book Your Walking Safari</h4>'
        '<p class="text-sm text-slate-700 leading-relaxed">Experience on-foot predator tracking on our daily <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Bardia Walking Safari (from €50)</a>, our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-800 font-bold underline">Chitwan Walking Safari (from €70)</a>, or across multiple days with our <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-800 font-bold underline">Bardia Tiger Safari 5 Days (€690)</a>.</p>'
        '</div>'
    )
}

for post in posts_en:
    slug = post['slug']
    if slug in EN_SNIPPETS:
        snippet = EN_SNIPPETS[slug]
        # Check if already added
        if 'border-emerald-200' not in post['content'] and 'border-amber-200' not in post['content']:
            post['content'] += "\n\n" + snippet
            print(f"Added rich snippet to EN: {slug}")

# Also replace any remaining /#prochains-departs in EN posts
for post in posts_en:
    post['content'] = re.sub(r'href=[\"\'](/#prochains-departs|https://junglenepal\.com/#prochains-departs)[\"\']', r'href="/en/tours/bardia-tiger-safari-5-days"', post['content'])

# Save both
with open('src/data/blog_posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts_fr, f, ensure_ascii=False, indent=2)

with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print("Saved both src/data/blog_posts.json and src/data/blog_posts.en.json with 100% complete linking!")
