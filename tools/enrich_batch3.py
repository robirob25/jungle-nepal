import json

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

en_by_slug = {p['slug']: p for p in posts_en}

# 5. animaux-bardia-faune-parc-national
en_by_slug['animaux-bardia-faune-parc-national']['content'] = """<div class="bg-emerald-50/80 border border-emerald-200 rounded-2xl p-6 mb-8 text-slate-800 shadow-sm">
  <h3 class="text-lg font-black text-emerald-950 mb-3 flex items-center gap-2">📌 Quick Summary: Wildlife of Bardia National Park</h3>
  <ul class="space-y-2 text-sm leading-relaxed">
    <li><strong>The King of the Jungle:</strong> Bengal tigers (~125 recorded adults, highest density and best sighting probability in Nepal).</li>
    <li><strong>Wild Asian Giants:</strong> Free-roaming migratory wild bull elephants and a flourishing population of reintroduced greater one-horned rhinos.</li>
    <li><strong>Rivers & Aquatic Life:</strong> Freshwater Gangetic dolphins (Platanista gangetica), marsh muggers, and fish-eating gharial crocodiles on the Karnali and Geruwa rivers.</li>
    <li><strong>Carnivores & Ungulates:</strong> Indian leopards, sloth bears, striped hyenas, dholes (wild dogs), spotted chital deer, swamp deer (barasingha), and the massive blue bull antelope (nilgai).</li>
    <li><strong>Birdwatching Haven:</strong> Over 400 recorded bird species including great hornbills, Bengal floricans, and sarus cranes.</li>
  </ul>
</div>

<p class="text-lg leading-relaxed text-slate-700 font-medium">Located in the remote southwestern Terai lowlands, <a href="/en/destinations/bardia" class="text-emerald-700 underline font-bold">Bardia National Park</a> spans 968 km² of pristine Sal hardwood forest, alluvial river islands, and savannah grasslands. It is globally recognized by conservationists as Nepal's most untouched wilderness sanctuary, offering unparalleled opportunities to observe apex predators on foot.</p>

<h2>1. The Bengal Tiger (Panthera tigris tigris): Undisputed Ruler of Bardia</h2>
<p>Bardia has become Asia's preeminent tiger tracking destination. While India's tiger reserves strictly restrict visitors to brief jeep corridors, Bardia allows travelers to track tigers silently on foot with senior naturalist guides. Over the past decade, rigorous anti-poaching enforcement and community-led buffer zone management have boosted Bardia's adult tiger population from just 18 individuals in 2009 to over <strong>125 resident tigers</strong> today. For an empirical breakdown of observation spots and success rates, read our study: <a href="/en/blog/tigre-bardia-observation-chances-spots" class="text-emerald-700 underline font-bold">Bardia tiger sightings: spots, seasons, and success rates</a>.</p>

<h2>2. Wild Asian Elephants (Elephas maximus): Roaming the Churia Hills</h2>
<p>Bardia serves as a vital cross-border transboundary corridor for wild Asian elephants migrating between Nepal and India's Katarniaghat Wildlife Sanctuary. Solitary massive bull tuskers—most famously legendary wanderers like <em>Shankar</em> and <em>Rajagaj</em>—roam the riverine forests. Spotting a wild bull emerging from the towering Sal trees to cross the Geruwa riverbed is an awe-inspiring spectacle.</p>

<h2>3. Greater One-Horned Rhinoceros (Rhinoceros unicornis)</h2>
<p>Following historical poaching pressures in the late 20th century, successful translocations from Chitwan have rebuilt a robust, thriving wild rhino population in Bardia's Baghaura and Babai river sectors. These solitary prehistoric giants thrive in riverine oxbow lakes and grassy floodplains, often encountered grazing peacefully at sunrise.</p>

<h2>4. Secondary Predators: Leopards, Sloth Bears, and Dholes</h2>
<p>Beyond the tiger, Bardia shelters an extraordinary community of sympatric carnivores:</p>
<ul>
  <li><strong>Indian Leopard (Panthera pardus):</strong> Highly adaptable and agile, leopards patrol the forest periphery and buffer zones, frequently resting high in the branches of large silk-cotton trees (Semal).</li>
  <li><strong>Sloth Bear (Melursus ursinus):</strong> Common in the termite-rich open Sal forests, actively foraging during early mornings and late afternoons.</li>
  <li><strong>Asiatic Wild Dog / Dhole (Cuon alpinus):</strong> Endangered pack hunters capable of exhausting large prey through coordinated tactical pursuits.</li>
</ul>

<h2>5. Aquatic Wildlife of the Karnali and Geruwa Rivers</h2>
<p>The braided channels of the Karnali river system provide vital sanctuary for rare aquatic species:</p>
<ul>
  <li><strong>Gangetic Dolphin:</strong> One of the world's few freshwater river dolphin species, surfacing for breath in deep river pools near the Chisapani gorge.</li>
  <li><strong>Gharial and Mugger Crocodiles:</strong> Basking on sunny pebble islands beside giant golden mahseer fish.</li>
</ul>

<div class="blog-cta-card my-10 p-6 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
  <div class="space-y-1">
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">1-Day Activity • Bardia</span>
    <h3 class="text-xl font-bold text-white">Full-Day Walking Tiger Safari in Bardia (50€)</h3>
    <p class="text-slate-300 text-xs">Join our senior native master trackers for an unforgettable full-day walking safari in Bardia National Park. Jungle bush lunch, entry permits, and safety gear included.</p>
  </div>
  <div class="flex flex-wrap items-center gap-3 mt-4">
    <a href="/en/tours/bardia-walking-safari" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs shadow-md transition-all">Book Day Walking Safari (50€) →</a>
    <a href="https://wa.me/33695413227?text=Hello%20Robin,%20I%20am%20interested%20in%20a%20wildlife%20safari%20in%20Bardia" target="_blank" rel="noopener noreferrer" class="cta-btn-alt inline-block px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs border border-white/20 transition-all">Chat on WhatsApp</a>
  </div>
</div>

<h2>Comparative Matrix: Wildlife Sightings in Bardia</h2>
<table class="my-8 w-full border-collapse border border-slate-200 text-sm">
  <thead>
    <tr class="bg-slate-100 text-slate-900 font-bold">
      <th class="p-3 border border-slate-200 text-left">Species</th>
      <th class="p-3 border border-slate-200 text-left">Bardia Population</th>
      <th class="p-3 border border-slate-200 text-left">Sighting Probability (3-Day Stay)</th>
      <th class="p-3 border border-slate-200 text-left">Best Safari Format</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Bengal Tiger</td>
      <td class="p-3 border border-slate-200">~125 adults</td>
      <td class="p-3 border border-slate-200 font-bold text-emerald-700">75% - 90% (Spring)</td>
      <td class="p-3 border border-slate-200">Full-Day Walking Safari / River Hide</td>
    </tr>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">One-Horned Rhino</td>
      <td class="p-3 border border-slate-200">~40-50 individuals</td>
      <td class="p-3 border border-slate-200">60% - 75%</td>
      <td class="p-3 border border-slate-200">Walking Safari & Open Jeep</td>
    </tr>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Wild Asian Elephant</td>
      <td class="p-3 border border-slate-200">Migratory herds + resident bulls</td>
      <td class="p-3 border border-slate-200">40% - 55%</td>
      <td class="p-3 border border-slate-200">Open Jeep & Karnali river banks</td>
    </tr>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Gangetic Dolphin</td>
      <td class="p-3 border border-slate-200">Isolated population</td>
      <td class="p-3 border border-slate-200">50% - 65%</td>
      <td class="p-3 border border-slate-200">Inflatable Rafting Expedition</td>
    </tr>
  </tbody>
</table>"""

# 6. tigre-bardia-observation-chances-spots
en_by_slug['tigre-bardia-observation-chances-spots']['content'] = """<div class="bg-emerald-50/80 border border-emerald-200 rounded-2xl p-6 mb-8 text-slate-800 shadow-sm">
  <h3 class="text-lg font-black text-emerald-950 mb-3 flex items-center gap-2">📌 Quick Summary: Bengal Tiger Sightings in Bardia</h3>
  <ul class="space-y-2 text-sm leading-relaxed">
    <li><strong>Exceptional Sighting Record:</strong> Bardia offers the highest success rates for observing wild tigers on foot in all of Asia (80% to 90% success during 3 to 4 full-day safaris in peak season).</li>
    <li><strong>Optimal Season:</strong> March through June. As temperature rises to 35-40°C, natural water sources dry up in the forest, forcing tigers to spend hours cooling off along the Geruwa and Khauraha rivers.</li>
    <li><strong>Top 3 Strategic Hides:</strong> Kingfisher Hide, Tinkuni (Three Corners), and Baleni on the Geruwa riverbed.</li>
    <li><strong>Foot vs. Jeep:</strong> Walking safaris allow silent, static vantage points overlooking watering holes without engine noise or vibrations scaring the cats away.</li>
  </ul>
</div>

<p class="text-lg leading-relaxed text-slate-700 font-medium">Tracking the Bengal tiger (<em>Panthera tigris tigris</em>) in its natural habitat is the ultimate dream of wildlife lovers worldwide. While many parks across the globe offer fleeting glimpses from noisy motorcades, <a href="/en/destinations/bardia" class="text-emerald-700 underline font-bold">Bardia National Park</a> remains the holy grail where patient naturalists can sit silently on a riverbank and watch a wild tiger emerge from the tall grass to drink. Here is the field-tested guide to maximizing your tiger sighting chances.</p>

<h2>1. Real Sighting Statistics: How Many Days Do You Need?</h2>
<p>Tiger tracking is an art of patience, sensory awareness, and timing. Based on our tracking logs over the past five seasons:</p>
<ul>
  <li><strong>1 Single Day Safari:</strong> ~40% to 50% probability of a visual sighting.</li>
  <li><strong>2 Full-Day Safaris:</strong> ~65% to 75% probability.</li>
  <li><strong>3 to 4 Full-Day Safaris:</strong> <strong>85% to 92% success rate</strong> (nearly guaranteed encounters during peak spring months).</li>
  <li><strong>Our Recommendation:</strong> Book a minimum of 3 full days inside the park. This allows your guides to adapt their strategy based on fresh pugmarks (footprints) and vocal alarm calls recorded the previous evening.</li>
</ul>

<h2>2. Secret Sighting Spots & Riverbank Hides in Bardia</h2>
<p>Bardia's geography features a network of braided rivers and natural watering holes where tigers regularly drink, bathe, and ambush prey. Our master trackers utilize several key strategic spots:</p>
<ul>
  <li><strong>Kingfisher Hide:</strong> A shaded natural vantage point positioned opposite a deep river oxbow where tigers regularly bathe during hot midday hours.</li>
  <li><strong>Tinkuni (The Three Corners):</strong> A major river junction surrounded by dense elephant grass and Sal woods. Resident dominant males and tigresses with cubs frequent this intersection daily.</li>
  <li><strong>Baleni & Khauraha Riverbank:</strong> Pristine gravel beds where tigers cross between river islands in search of spotted deer.</li>
</ul>

<h2>3. Why Walking Safaris Beat Jeeps for Tiger Tracking</h2>
<p>While an open 4x4 allows you to cover greater distances, experienced photographers and naturalists overwhelmingly favor walking safaris:</p>
<ul>
  <li><strong>Zero Engine Noise:</strong> Tigers possess extraordinary auditory sensitivity. A rumbling jeep engine alerts a tiger hundreds of meters away, causing it to slip silently into the thick brush. On foot, naturalists position themselves downwind without disturbing the ambient jungle soundscape.</li>
  <li><strong>Access to Intimate Game Trails:</strong> Jeeps are restricted to designated dirt tracks. On foot, trackers follow narrow game paths along secluded sandbars and dry riverbeds inaccessible to vehicles.</li>
  <li><strong>Uninterrupted Observation:</strong> Rather than driving constantly, walking safaris allow you to establish a discreet stakeout for several hours at prime watering spots, watching the jungle dramas unfold in real time.</li>
</ul>

<div class="blog-cta-card my-10 p-6 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
  <div class="space-y-1">
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">1-Day Activity • Bardia</span>
    <h3 class="text-xl font-bold text-white">Full-Day Tiger Tracking Walking Safari (50€)</h3>
    <p class="text-slate-300 text-xs">Maximize your chances of observing wild Bengal tigers with Bardia's premier tracking team. Dual licensed guides, entry permits, and lunch included.</p>
  </div>
  <div class="flex flex-wrap items-center gap-3 mt-4">
    <a href="/en/tours/bardia-walking-safari" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs shadow-md transition-all">Book Tiger Walking Safari (50€) →</a>
    <a href="https://wa.me/33695413227?text=Hello%20Robin,%20I%20want%20to%20track%20tigers%20in%20Bardia" target="_blank" rel="noopener noreferrer" class="cta-btn-alt inline-block px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs border border-white/20 transition-all">Chat on WhatsApp</a>
  </div>
</div>

<h2>FAQ: Tiger Sightings in Bardia</h2>
<h3>What is the absolute best month to see tigers in Bardia?</h3>
<p>April and May offer the highest statistical sighting rates of the entire year. Jungle foliage is dry and thin, temperatures exceed 35°C, and tigers spend hours immersed in the cool waters of the Geruwa River.</p>

<h3>Can I photograph tigers on foot safely?</h3>
<p>Yes. By maintaining safe observation distances (usually 40 to 80 meters across open riverbeds) and following strict silence protocols under the supervision of our two lead trackers, photographers regularly capture breathtaking images with 300mm to 600mm telephoto lenses.</p>"""

# 7. safari-dos-elephant-nepal-pourquoi-refuser-cette-pratique
en_by_slug['safari-dos-elephant-nepal-pourquoi-refuser-cette-pratique']['content'] = """<div class="bg-emerald-50/80 border border-emerald-200 rounded-2xl p-6 mb-8 text-slate-800 shadow-sm">
  <h3 class="text-lg font-black text-emerald-950 mb-3 flex items-center gap-2">📌 Quick Summary: Why We Reject Elephant-Back Riding</h3>
  <ul class="space-y-2 text-sm leading-relaxed">
    <li><strong>Anatomy & Spine Damage:</strong> An elephant's spine consists of upward-pointing bony protrusions (spinous processes) that are not evolved to support heavy wooden saddles (howdahs) or human weight.</li>
    <li><strong>The Brutal "Phajaan" Training:</strong> Captive riding elephants undergo psychological crushing through restraint, sensory deprivation, and pain to force obedience to the bullhook (ankush).</li>
    <li><strong>Ethical Alternatives Exist:</strong> Experience the jungle ethically through silent walking safaris on foot, open-top 4x4 jeep expeditions, and traditional river canoe patrols.</li>
    <li><strong>Our Unwavering Commitment:</strong> Jungle Nepal Adventure strictly refuses to sell, promote, or facilitate elephant-back safaris.</li>
  </ul>
</div>

<p class="text-lg leading-relaxed text-slate-700 font-medium">For decades, commercial travel agencies in South Asia marketed riding atop a captive elephant as the quintessential jungle experience. However, growing global awareness of animal ethology and veterinary science has pulled back the curtain on this outdated practice. At <a href="/en/about" class="text-emerald-700 underline font-bold">Jungle Nepal Adventure</a>, we believe true wildlife travel must never come at the cost of animal exploitation.</p>

<h2>1. The Anatomy Myth: An Elephant's Spine Is Fragile</h2>
<p>Despite their massive physical power, Asian elephants are anatomically unsuited for carrying heavy loads on their backs:</p>
<ul>
  <li><strong>Delicate Skeletal Structure:</strong> Unlike horses or camels whose vertebrae evolved horizontally to bear weight, an elephant's backbone features tall, delicate vertical dorsal spines covered by a thin layer of muscle and tissue.</li>
  <li><strong>Chronic Injuries from Saddles:</strong> Heavy wooden saddles (howdahs) carrying four adult tourists plus a handler weigh upwards of 300 kilograms. Over years of daily riding, this causes chronic spinal lesions, permanent tissue necrosis, and severe arthritis.</li>
</ul>

<h2>2. The Invisible Cruelty of the "Phajaan"</h2>
<p>Wild elephants are naturally wild creatures with strong family bonds and high intelligence. To compel an elephant to accept human riders and tolerate sudden movements without retaliating, young calves are subjected to a traditional breaking process known as the <em>Phajaan</em> ("crushing the spirit"):</p>
<ul>
  <li>Separation from their mothers at a young age.</li>
  <li>Confinement in small wooden crushes with tight ropes.</li>
  <li>Deprivation of sleep, food, and water alongside physical punishment with metal-tipped bullhooks until their natural defensive instincts are extinguished.</li>
</ul>

<h2>3. Life Outside the Safari: Short Chains and Isolation</h2>
<p>When tourists return to their lodges, captive riding elephants often spend up to 18 hours chained by their feet to concrete posts, unable to socialize, graze naturally, or bathe in river waters. Elephants in commercial riding camps frequently exhibit repetitive stress behaviors (weaving and swaying), clear indicators of deep psychological distress.</p>

<div class="blog-cta-card my-10 p-6 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
  <div class="space-y-1">
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">Ethical Safari • Bardia</span>
    <h3 class="text-xl font-bold text-white">Experience the Raw Jungle on Foot (50€)</h3>
    <p class="text-slate-300 text-xs">Say NO to captive elephant exploitation. Walk the wild trails of Bardia National Park with our certified native naturalists for an authentic, respectful wildlife encounter.</p>
  </div>
  <div class="flex flex-wrap items-center gap-3 mt-4">
    <a href="/en/tours/bardia-walking-safari" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs shadow-md transition-all">Book Ethical Walking Safari (50€) →</a>
    <a href="https://wa.me/33695413227?text=Hello%20Robin,%20I%20support%20ethical%20safaris%20and%20want%20to%20learn%20more" target="_blank" rel="noopener noreferrer" class="cta-btn-alt inline-block px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs border border-white/20 transition-all">Chat on WhatsApp</a>
  </div>
</div>

<h2>Ethical Alternatives: How to Experience the Jungle Responsibly</h2>
<p>Choosing responsible tourism sends a direct economic signal to local communities and park operators:</p>
<ul>
  <li><strong>Guided Walking Safaris:</strong> The most intimate and low-impact way to explore the wilderness, leaving zero carbon footprint and zero disturbance to wildlife.</li>
  <li><strong>Open 4x4 Jeep Safaris:</strong> Cover expansive territory safely, allowing ethical observations from a respectful distance.</li>
  <li><strong>Traditional River Canoes:</strong> Silent drift safaris on river systems that do not stress resident animals.</li>
</ul>"""

with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print("Batch 3 (Bardia Wildlife, Tiger Spots & Elephant Ethics) written successfully.")
