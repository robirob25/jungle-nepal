import os, glob, re

tour_badges_fr = {
    "tiji-mustang": "🏔️ Himalaya, Mustang & Spiritualité",
    "immersion-spirituelle": "🏔️ Himalaya, Mustang & Spiritualité",
    "carnet-de-voyage": "🏔️ Himalaya, Mustang & Spiritualité",
    "rara-lake-bardia": "🏔️ Himalaya, Mustang & Spiritualité",
    "nepal-sauvage": "🏔️ Himalaya, Mustang & Spiritualité",
    "rafting-safari": "🚣 Rafting & Expédition Rivière",
    "nepal-immersion-totale": "🇳🇵 Grand Tour Immersion 360°",
    "chitwan-bardia-complete": "🦏 Chitwan & Bardia Sauvage",
    "bardia-explorateur": "🐅 Safari & Pistage Tigre",
    "bardia-nuit-sauvage": "⛺ Bivouac & Nuit Sauvage",
    "bardia-babai-camping": "⛺ Bivouac & Nuit Sauvage",
    "babai-special": "⛺ Bivouac & Vallée Secrète",
    "jungle-extreme": "🐅 Safari & Faune Extrême",
    "chitwan-culture": "🦏 Rhinocéros & Culture Tharu"
}

tour_badges_en = {
    "tiji-mustang": "🏔️ Himalayas, Mustang & Spirituality",
    "immersion-spirituelle": "🏔️ Himalayas, Mustang & Spirituality",
    "carnet-de-voyage": "🏔️ Himalayas, Mustang & Spirituality",
    "rara-lake-bardia": "🏔️ Himalayas, Mustang & Spirituality",
    "nepal-sauvage": "🏔️ Himalayas, Mustang & Spirituality",
    "rafting-safari": "🚣 Rafting & River Expedition",
    "nepal-immersion-totale": "🇳🇵 Grand 360° Immersion Tour",
    "chitwan-bardia-complete": "🦏 Chitwan & Wild Bardia",
    "bardia-explorateur": "🐅 Safari & Tiger Tracking",
    "bardia-nuit-sauvage": "⛺ Wild Camping & Night Safari",
    "bardia-babai-camping": "⛺ Wild Camping & Night Safari",
    "babai-special": "⛺ Wild Bivouac & Secret Valley",
    "jungle-extreme": "🐅 Safari & Extreme Wildlife",
    "chitwan-culture": "🦏 One-Horned Rhinos & Tharu Culture"
}

# Update FR tour pages
for slug, badge in tour_badges_fr.items():
    fpath = f'/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/{slug}.astro'
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        
        # Replace badge in header
        c = re.sub(
            r'<span class="text-xs font-bold bg-slate-900 text-amber-300 px-3 py-1 rounded-full border border-amber-300/30">.*?</span>',
            f'<span class="text-xs font-bold bg-slate-900 text-amber-300 px-3 py-1 rounded-full border border-amber-300/30">\n            {badge}\n          </span>',
            c,
            flags=re.DOTALL
        )
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

# Update EN tour pages
for slug, badge in tour_badges_en.items():
    fpath = f'/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/{slug}.astro'
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        
        c = re.sub(
            r'<span class="text-xs font-bold bg-slate-900 text-amber-300 px-3 py-1 rounded-full border border-amber-300/30">.*?</span>',
            f'<span class="text-xs font-bold bg-slate-900 text-amber-300 px-3 py-1 rounded-full border border-amber-300/30">\n            {badge}\n          </span>',
            c,
            flags=re.DOTALL
        )
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print("Updated badges across all 14 FR & EN tour pages!")
