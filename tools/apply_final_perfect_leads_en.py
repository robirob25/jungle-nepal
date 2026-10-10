import re

BLOCKS_EN = {
    'src/pages/en/tours/bardia-jeep-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- ETHICS & WILD NATURE COMMITMENT -->)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Explore remote wilderness corridors of Bardia by private 4x4 Jeep
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Privatized exclusively for your group (up to 6 guests) at <strong>€190 for a full day</strong>, this 4x4 open-jeep safari is the ultimate way to reach the most secluded, untamed sectors of <strong>Bardia National Park</strong> (including Baghaura and the Karnali floodplains). Escorted by an expert driver and a certified senior naturalist, this all-inclusive expedition covers national park entry permits and a freshly prepared bush lunch, allowing you to cover vast distances and maximize encounters with wild Bengal tigers.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              Aboard a customized safari vehicle completely open to the wilderness, you navigate forest trails and alluvial grasslands alongside an elite tracking team, reading fresh night pugmarks and interpreting canopy alarm calls throughout the day.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              <strong>Primary objective:</strong> maximize your chances of encountering the apex ruler of Bardia, the <strong>Bengal tiger</strong>. The vehicle's swift mobility lets you access distant prime hotspots (such as the far banks of the Karnali River or deep jungle watchtowers), dramatically increasing opportunities to spot <strong>greater one-horned rhinos</strong>, <strong>wild elephants</strong>, <strong>leopards</strong>, herds of <strong>chital and sambar deer</strong>, and basking gharials along sandbanks.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              A bush lunch is shared in the wild, shaded inside a secured viewing machan overlooking a waterhole. Fully turn-key: all park permits and local entry permissions are fully handled.
            </p>
          </div>\n\n          """
    ),

    'src/pages/en/tours/bardia-walking-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- Wilderness Ethics Warning -->)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Head into the deep wilderness of Bardia National Park on foot
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Offered at <strong>€50 per person for a full day</strong> (6:30 AM – 6:00 PM), the <strong>walking safari in Bardia National Park</strong> is Nepal's purest, most thrilling wildlife encounter. Escorted by <strong>two licensed native Tharu trackers</strong> equipped with traditional fire-hardened bamboo staffs, this tour includes park permits, a jungle bush lunch, and boasts an <strong>85%+ sighting probability for wild Bengal tigers</strong> during the peak dry season.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Free from the noise of vehicle engines, you leave conventional tracks to tread quietly through towering Sal forests and elephant grasslands. Your guides read fresh pugmarks, scent markings, and canopy alarm calls to position you at strategic riverside watchpoints throughout the day.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              <strong>The primary quest: Bengal tigers.</strong> While sightings can never be 100% guaranteed in true wilderness, foot tracking also brings opportunities to observe <strong>greater one-horned Asian rhinos</strong>, <strong>wild elephant herds</strong>, chital and sambar deer, langur monkeys, and hundreds of bird species.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Bush lunch is enjoyed under ancient riverine canopy, maximizing every minute deep inside the national park.
            </p>
          </div>\n\n          """
    ),

    'src/pages/en/tours/bardia-rafting-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- AVERTISSEMENT ETHIQUE & NATURE SAUVAGE -->)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Float Down the Karnali River on a Private Rafting Safari in Bardia
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Available at <strong>€120 per person for a full day</strong>, this <strong>Karnali River rafting safari</strong> (a 35 km silent drift along Bardia National Park) is the quietest and most stealthy way to observe wild Asian wildlife. Guided by a certified whitewater captain, senior naturalist, and elite tracker, the tour includes complete safety equipment, 4x4 transfers, national park permits, and a freshly prepared picnic lunch on an isolated river island.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Carried by gentle, crystal-clear currents through the Karnali and Geruwa channels, your raft drifts silently alongside forested bluffs and gravel banks. This unique water-level vantage point offers rare views into the habitat of the endangered <strong>Gangetic river dolphin</strong>, as well as two prehistoric crocodilian species: the slender-snouted <strong>gharial</strong> and the marsh mugger.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              Along the shoreline, silent drifting often yields spectacular sightings of wild elephants bathing, greater one-horned rhinos grazing, deer herds, and occasionally a <strong>Bengal tiger</strong> crossing gravel bars in broad daylight. Includes bush stopovers for short tracking walks and an isolated beach lunch.
            </p>
          </div>\n\n          """
    ),

    'src/pages/en/tours/chitwan-walking-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="space-y-4">.*?</div>\s*(?=<!-- Ethical Wildlife Disclaimer -->)',
        """<section id="apercu" class="space-y-6">
          <div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Discover Chitwan differently: on foot
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Priced at <strong>€70 per person for a full day</strong>, the <strong>guided walking safari in Chitwan National Park</strong> gets you up close to the world's second-largest population of <strong>greater one-horned rhinos</strong> (>690 protected individuals). Led by two certified native naturalists, this expedition includes park permits, a wilderness picnic lunch, and boasts a near-guaranteed 95% rhino sighting rate year-round, far from motorized tourist routes.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              Setting off early in the morning to catch peak wildlife activity, your team tracks pugmarks, feeding traces, and primate alarm calls through Sal forests, tall grassland corridors, and quiet river bends in search of rhinos, sloth bears, Bengal tigers, and rare tropical birds.
            </p>
            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
              <strong>Bengal tigers remain the ultimate quest</strong>, while Chitwan's mosaic of riverbanks and community buffer zones also provides exceptional encounters with sloth bears, wild deer, marsh muggers, and endangered gharials. A hot picnic lunch is enjoyed directly in the jungle.
            </p>
          </div>\n\n          """
    ),

    'src/pages/en/tours/chitwan-jeep-safari.astro': (
        r'<section id="apercu"[^>]*>.*?<div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">.*?</div>\s*(?=<!-- Ethical & Wild Nature Commitment -->)',
        """<section id="apercu" class="scroll-mt-28 space-y-6">
          <div class="prose prose-slate max-w-none text-sm sm:text-base leading-relaxed text-slate-700">
            <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight not-prose mb-4">
              Explore the floodplains and wild jungles of Chitwan by private safari 4x4
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal not-prose">
              Privatized exclusively for your group (up to 6 passengers) at <strong>€190 for a full day</strong>, this open 4x4 expedition penetrates deep into the UNESCO World Heritage core sectors of <strong>Chitwan National Park</strong> (including Kasara and Sukhibhar). Guided by an expert driver and a certified senior naturalist, this all-inclusive tour covers national park permits and a bush lunch to maximize encounters with greater one-horned rhinos, sloth bears, gharials, and Bengal tigers.
            </p>
            <p>
              Immerse yourself into Nepal's oldest and most renowned national park for a full day of motorized exploration in total wilderness. A UNESCO World Heritage site, Chitwan National Park boasts an extraordinary mosaic of habitats: vast Sal tree forests, gigantic elephant-grass floodplains, and meandering river bends fostering remarkable wildlife density.
            </p>
            <p>
              Aboard a private, open-sided 4x4 safari vehicle, you are accompanied by a veteran driver, a senior naturalist guide specialized in the Terai biome, and an elite native tracker. Traveling by jeep allows you to escape standard tourist circuits, venture into the quietest sectors of the park, cross waterways, and watch for predator passages along primary forest corridors.
            </p>
            <p>
              Bush lunch is enjoyed deep in the jungle inside a secured observation watchtower overlooking a river curve or waterhole. Fully turn-key: all park permits, vehicle fees, and guide licenses are completely included.
            </p>
          </div>\n\n          """
    )
}

for path, (pattern, replacement) in BLOCKS_EN.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count == 1:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Perfectly rewritten aperçu in {path}")
    else:
        print(f"✗ Regex count {count} for {path}")
