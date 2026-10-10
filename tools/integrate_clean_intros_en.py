import re

EN_PAGES = {
    # 6. Safari Jeep Bardia EN
    'src/pages/en/tours/bardia-jeep-safari.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Explore remote wilderness corridors of Bardia by private 4x4 Jeep\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Explore remote wilderness corridors of Bardia by private 4x4 Jeep\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              A <strong>private full-day 4x4 open jeep safari in Bardia costs €190 per vehicle</strong> (accommodating up to 6 guests). It allows exploring remote park sectors inaccessible on foot (Baghaura, Karnali riverbanks). The tour includes the customized safari vehicle, expert driver, licensed senior naturalist guide, national park entry fees, and a freshly prepared bush lunch.\n            </p>'
    },

    # 7. Safari Pied Bardia EN
    'src/pages/en/tours/bardia-walking-safari.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Head into the deep wilderness of Bardia National Park on foot\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Head into the deep wilderness of Bardia National Park on foot\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              A <strong>full-day walking safari in Bardia National Park costs €50 per person</strong> with Jungle Nepal Adventure. Escorted by <strong>two certified native Tharu trackers</strong> equipped with traditional fire-hardened bamboo staffs, it runs from 6:30 AM to 6:00 PM and includes park permits, a jungle bush lunch, and an <strong>85%+ sighting probability for wild Bengal tigers</strong> during spring. Walking without two licensed guides is strictly illegal under Nepalese park law.\n            </p>'
    },

    # 8. Rafting Safari Bardia EN
    'src/pages/en/tours/bardia-rafting-safari.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Float Down the Karnali River on a Private Rafting Safari in Bardia\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Float Down the Karnali River on a Private Rafting Safari in Bardia\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              A <strong>full-day rafting safari on the Karnali River in Bardia costs €120 per person</strong>. This silent 35 km river drift offers rare views of freshwater Gangetic river dolphins, critically endangered gharial crocodiles, and riverbank tigers, accompanied by certified river guides with safety gear and riverside lunch included.\n            </p>'
    },

    # 9. Safari Pied Chitwan EN
    'src/pages/en/tours/chitwan-walking-safari.astro': {
        'target': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Discover Chitwan differently: on foot\n            </h2>',
        'insert': '<h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">\n              Discover Chitwan differently: on foot\n            </h2>\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              A <strong>guided walking safari in Chitwan National Park costs €70 per person</strong>. Led by two certified naturalists through community buffer forests, it offers a near-guaranteed <strong>95% sighting probability for greater one-horned rhinos</strong> (>690 recorded individuals), sloth bears, and river crocodilians without the disruption of motor vehicles.\n            </p>'
    },

    # 10. Safari Jeep Chitwan EN
    'src/pages/en/tours/chitwan-jeep-safari.astro': {
        'target': '<h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">\n              Explore the floodplains and wild jungles of Chitwan by private safari 4x4\n            </h2>',
        'insert': '<h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">\n              Explore the floodplains and wild jungles of Chitwan by private safari 4x4\n            </h2>\n            <p>\n              A <strong>full-day private jeep safari in Chitwan National Park costs €190 per vehicle</strong> (accommodating up to 6 passengers). The itinerary penetrates deep into the UNESCO World Heritage core sectors (Kasara and Sukhibhar) to track greater one-horned rhinos, sloth bears, wild elephants, and Bengal tigers alongside a licensed senior naturalist.\n            </p>'
    }
}

for path, data in EN_PAGES.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if data['target'] in content:
        content = content.replace(data['target'], data['insert'], 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated intro in {path}")
    else:
        print(f"✗ Target not found in {path}")
