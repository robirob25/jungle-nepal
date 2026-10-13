import json, re

with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

# Fix the 1 FR post: safari-photo-au-nepal-spots-materiel-conseils
for post in posts_fr:
    if post['slug'] == 'safari-photo-au-nepal-spots-materiel-conseils':
        if '/tours/safari-pied-bardia' not in post['content']:
            post['content'] += (
                '\n\n<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
                '<h4 class="text-base font-bold text-emerald-950 mb-2">Conseils Jungle Nepal pour photographes</h4>'
                '<p class="text-sm text-slate-700 leading-relaxed mb-2">Pour des prises de vue parfaites au ras du sol et un silence absolu, associez votre matériel à notre <a href="/tours/safari-pied-bardia" class="text-emerald-800 font-bold underline">safari à pied à Bardia (dès 50 €)</a> ou optez pour la mobilité maximale de notre <a href="/tours/safari-jeep-bardia" class="text-emerald-800 font-bold underline">jeep privatisée 4x4 (190 €/jour)</a>.</p>'
                '<p class="text-xs text-slate-600 font-medium">Pour un voyage photo complet de 5 jours : <a href="/tours/bardia-explorateur" class="text-emerald-800 font-bold underline">découvrez l\'expédition Bardia Explorateur</a>.</p>'
                '</div>'
            )
            print("Fixed FR: safari-photo-au-nepal-spots-materiel-conseils")

# Fix all remaining EN posts so that EVERY post has at least 2 to 4 tour links
for post in posts_en:
    slug = post['slug']
    content = post['content']
    
    # 1. Chitwan guide
    if slug == 'guide-parc-national-de-chitwan-nepal':
        content += (
            '\n\n<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
            '<h4 class="text-base font-bold text-emerald-950 mb-2">Explore Chitwan National Park</h4>'
            '<p class="text-sm text-slate-700 leading-relaxed mb-2">Track greater one-horned rhinos on our daily <a href="/en/tours/chitwan-walking-safari" class="text-emerald-800 font-bold underline">Chitwan Rhino Walking Safari (from €70)</a> or book an open-top <a href="/en/tours/chitwan-jeep-safari" class="text-emerald-800 font-bold underline">Private Chitwan Jeep Safari (€190/jeep)</a>.</p>'
            '<p class="text-xs text-slate-600 font-medium">Looking for a complete itinerary? Explore our <a href="/en/tours/chitwan-safari-cultural-tour" class="text-emerald-800 font-bold underline">4-Day Chitwan Cultural & Safari Tour</a> or combine both parks on our <a href="/en/tours/chitwan-bardia-combined-safari" class="text-emerald-800 font-bold underline">11-Day Chitwan + Bardia Safari</a>.</p>'
            '</div>'
        )
    # 2. Bardia tiger posts lacking secondary tour link
    elif any(k in slug for k in ['bardia', 'tigre', 'tiger', 'pistage', 'art-du-pistage', 'sac-safari', 'sante-paludisme', 'combien-de-jours', 'prix-dun-safari', 'le-safari-ethique', 'agence-safari', 'quels-animaux', 'nilgaut', 'singes', 'reptiles', 'rapaces', 'observer-les-oiseaux']):
        if '/en/tours/bardia-tiger-safari-5-days' not in content and '/en/tours/bardia-jeep-safari' not in content:
            content += (
                '\n\n<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
                '<h4 class="text-base font-bold text-emerald-950 mb-2">Recommended Bardia Experiences</h4>'
                '<p class="text-sm text-slate-700 leading-relaxed mb-2">Join our certified naturalists on a <a href="/en/tours/bardia-walking-safari" class="text-emerald-800 font-bold underline">Bardia Walking Tiger Safari (from €50)</a> or cover vast savannah territories in a <a href="/en/tours/bardia-jeep-safari" class="text-emerald-800 font-bold underline">Private 4x4 Jeep Safari (€190/vehicle)</a>.</p>'
                '<p class="text-xs text-slate-600 font-medium">For a complete 5-day lodge adventure: <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-800 font-bold underline">explore the Bardia Tiger Safari 5 Days (€690)</a>.</p>'
                '</div>'
            )
    # 3. Chitwan posts
    elif any(k in slug for k in ['chitwan', 'rhinoceros', 'elephant']):
        if '/en/tours/chitwan-jeep-safari' not in content and '/en/tours/chitwan-safari-cultural-tour' not in content:
            content += (
                '\n\n<div class="p-6 bg-emerald-50/70 border border-emerald-200/80 rounded-2xl my-8">'
                '<h4 class="text-base font-bold text-emerald-950 mb-2">Experience Chitwan with Native Guides</h4>'
                '<p class="text-sm text-slate-700 leading-relaxed mb-2">Track rhinos on foot with our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-800 font-bold underline">Chitwan Walking Safari (from €70)</a> or book a full-day <a href="/en/tours/chitwan-jeep-safari" class="text-emerald-800 font-bold underline">Private Jeep Safari (€190)</a>.</p>'
                '<p class="text-xs text-slate-600 font-medium">For an all-inclusive stay: <a href="/en/tours/chitwan-safari-cultural-tour" class="text-emerald-800 font-bold underline">discover the Chitwan Safari Cultural Tour (4 Days)</a>.</p>'
                '</div>'
            )
    # 4. Snow leopard posts
    elif 'panthere-des-neiges' in slug:
        if '/en/tours/tiji-festival-upper-mustang-trek' not in content:
            content += (
                '\n\n<div class="p-6 bg-slate-900 text-white rounded-2xl my-8 border border-white/10">'
                '<h4 class="text-base font-bold text-amber-300 mb-2">Himalayan High-Altitude Expeditions</h4>'
                '<p class="text-sm text-slate-300 leading-relaxed mb-2">Explore our flagship <a href="/en/tours/snow-leopard-expedition-nepal" class="text-emerald-400 font-bold underline">Snow Leopard Expedition in Dolpo & Mustang (17 Days)</a> or discover ancient cliff monasteries on our <a href="/en/tours/tiji-festival-upper-mustang-trek" class="text-emerald-400 font-bold underline">Tiji Festival Upper Mustang Trek</a>.</p>'
                '</div>'
            )
    # 5. Culture & combined posts
    elif any(k in slug for k in ['tharu', 'dashain', 'trek-jungle', 'afrique']):
        if '/en/tours/wild-nepal-safari-annapurna-trek' not in content:
            content += (
                '\n\n<div class="p-6 bg-amber-50/80 border border-amber-200 rounded-2xl my-8">'
                '<h4 class="text-base font-bold text-amber-950 mb-2">Authentic Nepal Experiences</h4>'
                '<p class="text-sm text-slate-700 leading-relaxed mb-2">Discover our cultural & wildlife tours: <a href="/en/tours/dashain-festival-tharu-cultural-tour" class="text-emerald-800 font-bold underline">Dashain Festival Tharu Tour</a> or combine mountain trekking and lowland safaris on our <a href="/en/tours/wild-nepal-safari-annapurna-trek" class="text-emerald-800 font-bold underline">Wild Nepal Safari & Annapurna Trek (15 Days)</a>.</p>'
                '</div>'
            )
    
    post['content'] = content

# Save both files
with open('src/data/blog_posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts_fr, f, ensure_ascii=False, indent=2)

with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print("Saved both 100% enriched JSON files!")
