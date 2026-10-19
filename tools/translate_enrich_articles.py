import json

with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

en_by_slug = {p['slug']: p for p in posts_en}

# 1. comment-aller-a-chitwan-katmandou-pokhara-bus-avion
en_by_slug['comment-aller-a-chitwan-katmandou-pokhara-bus-avion']['content'] = """<div class="bg-emerald-50/80 border border-emerald-200 rounded-2xl p-6 mb-8 text-slate-800 shadow-sm">
  <h3 class="text-lg font-black text-emerald-950 mb-3 flex items-center gap-2">📌 Quick Summary: How to Reach Chitwan (Nepal)</h3>
  <ul class="space-y-2 text-sm leading-relaxed">
    <li><strong>Tourist Bus (Most Popular):</strong> Daily morning departures at 7:00 AM from Shorakhutte / Kantipath in Kathmandu, or from Tourist Bus Park in Pokhara. Journey takes 5 to 7 hours depending on Prithvi Highway traffic. Cost: $10 to $15.</li>
    <li><strong>Express Domestic Flight:</strong> 20-minute flight from Kathmandu to Bharatpur (BHR) with Buddha Air or Yeti Airlines, followed by a 30-minute private vehicle transfer to your lodge in Sauraha. Total cost: $110 to $140 one-way.</li>
    <li><strong>Trishuli River Rafting Combo:</strong> Private road departure from Kathmandu, 3 hours of Class II-III+ river rafting on the Trishuli, riverside hot lunch, and road transfer onward to Chitwan before dusk.</li>
    <li><strong>Private AC Car / Jeep:</strong> Complete flexibility, door-to-door lodge pickup, ideal for families or photographers with heavy camera bodies and telephoto lenses. Cost: $100 to $140 per vehicle.</li>
  </ul>
</div>

<p class="text-lg leading-relaxed text-slate-700 font-medium">Located approximately 160 kilometers southwest of Kathmandu in the subtropical Terai lowlands, <a href="/en/destinations/chitwan" class="text-emerald-700 underline font-bold">Chitwan National Park</a> is Nepal's most readily accessible wilderness sanctuary. Whether you are seeking budget efficiency, optimal comfort, or an action-packed white-water river connection, here is everything you need to plan your route from Kathmandu or Pokhara.</p>

<h2>Option 1: The Tourist Bus (Kathmandu &rarr; Sauraha / Pokhara &rarr; Sauraha)</h2>
<p>The tourist bus remains the traditional choice favored by independent travelers and backpackers. Unlike local public buses, tourist coaches do not make random roadside stops, providing a much smoother, safer travel experience through the Trishuli and Narayani river valleys.</p>
<ul>
  <li><strong>Kathmandu Departure Point:</strong> Shorakhutte Tourist Bus Stop (just north of Thamel) or along Kantipath. All buses depart promptly between 6:45 AM and 7:15 AM. You must arrive 20 minutes prior to departure.</li>
  <li><strong>Pokhara Departure Point:</strong> Tourist Bus Park (Rashtra Bank Chowk / Lakeside area), with daily morning departures around 7:00 AM.</li>
  <li><strong>Arrival in Chitwan:</strong> Sauraha Tourist Bus Park (Bachhauli), located roughly 2 kilometers outside Sauraha village. If you have booked an expedition with Jungle Nepal Adventure, our lodge driver will meet you directly at the bus station with complimentary private transfer.</li>
  <li><strong>Travel Time:</strong> 5 to 7 hours. Travel times fluctuate depending on seasonal highway maintenance work along the Mugling and Narayanghat gorges.</li>
  <li><strong>Comfort & Amenities:</strong> Buses feature reclining seats, overhead luggage storage, and air conditioning (or forced air in budget versions). Two dedicated 20-minute comfort stops are scheduled at hygienic roadside restaurants for breakfast and lunch. Premium sofa-seater VIP buses (such as Swift Holidays) cost roughly $18 to $22 and provide extra legroom.</li>
</ul>

<h2>Option 2: Flight from Kathmandu &rarr; Bharatpur (The 20-Minute Aerial Shortcut)</h2>
<p>If your holiday time in Nepal is precious or you wish to bypass mountain road traffic entirely, flying is the ultimate high-efficiency option:</p>
<ul>
  <li><strong>Flight Route:</strong> Tribhuvan Domestic Airport (Kathmandu) &rarr; Bharatpur Airport (BHR). Daily scheduled flights operated by <a href="https://www.buddhaair.com/" target="_blank" rel="noopener noreferrer" class="text-emerald-700 underline font-bold">Buddha Air</a> and Yeti Airlines.</li>
  <li><strong>Flight Duration:</strong> Just 20 to 25 minutes of breathtaking aerial vistas over the Mahabharat ridge and the southern lowland plains.</li>
  <li><strong>Airport to Lodge Transfer:</strong> Bharatpur Airport is located 18 kilometers from Sauraha (a 30-minute private taxi drive) and 35 kilometers from Meghauli luxury properties (45 minutes).</li>
  <li><strong>Luggage Limits:</strong> Standard tickets include 15 kg of checked luggage and 5 kg of carry-on. Excess baggage is charged at approximately $1.50 per kilogram at the check-in desk.</li>
</ul>

<h2>Option 3: Trishuli River Rafting Combo En Route to Chitwan</h2>
<p>Why spend a travel day sitting passively on a bus when you can break up the journey with exhilarating Himalayan rapids? The Trishuli river connection is one of Nepal's most rewarding multi-sport experiences:</p>
<ul>
  <li><strong>Morning Departure:</strong> Depart your Kathmandu hotel by private car at 7:00 AM. A 3-hour drive down the Prithvi Highway brings you to the river entry point at Charaudi or Fishling.</li>
  <li><strong>3 Hours on the River:</strong> Run iconic Class II and III+ rapids such as <em>Ladies Delight</em>, <em>Monsoon</em>, and <em>Upset</em> under the guidance of certified river captains, surrounded by soaring canyon walls and suspension bridges.</li>
  <li><strong>Riverside Hot Lunch:</strong> Enjoy a hot freshly prepared buffet on a secluded sandy riverbank.</li>
  <li><strong>Afternoon Transfer:</strong> Change into dry clothes, re-board your vehicle, and complete the remaining 1.5 hours of smooth lowland road directly to the gates of Chitwan National Park before twilight.</li>
</ul>

<div class="blog-cta-card my-10 p-6 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
  <div class="space-y-1">
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">1-Day Activity • Chitwan</span>
    <h3 class="text-xl font-bold text-white">Full-Day Rhino Tracking Walking Safari in Chitwan (70€)</h3>
    <p class="text-slate-300 text-xs">Arriving in Sauraha? Experience the raw jungle on foot with certified senior naturalist guides. Track greater one-horned rhinos, sloth bears, and tropical birdlife far away from crowded tourist circuits.</p>
  </div>
  <div class="flex flex-wrap items-center gap-3 mt-4">
    <a href="/en/tours/chitwan-walking-safari" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs shadow-md transition-all">Book Day Walking Safari (70€) →</a>
    <a href="https://wa.me/33695413227?text=Hello%20Robin,%20I%20am%20heading%20to%20Chitwan%20and%20want%20to%20book%20a%20walking%20safari" target="_blank" rel="noopener noreferrer" class="cta-btn-alt inline-block px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs border border-white/20 transition-all">Chat on WhatsApp</a>
  </div>
</div>

<h2>Deciding Between Chitwan and Bardia?</h2>
<p>While Chitwan's immediate proximity to Kathmandu makes it unmatched for convenient 2 to 3-day itineraries, travelers seeking untamed solitude, pristine walking safaris, and vastly superior chances of observing wild Bengal tigers often combine both sanctuaries or choose Bardia. Read our comprehensive field comparison: <a href="/en/blog/bardia-ou-chitwan-quel-parc-choisir" class="text-emerald-700 underline font-bold">Bardia vs Chitwan: Which Safari Park Should You Choose?</a>.</p>

<h2>FAQ: Logistics & Getting to Chitwan</h2>
<h3>What is the fastest way to travel from Kathmandu to Chitwan?</h3>
<p>The fastest route is the 20-minute domestic flight from Kathmandu Domestic Airport (KTM) to Bharatpur Airport (BHR), followed by a 30-minute private taxi drive to your jungle lodge in Sauraha.</p>

<h3>Do I need to book tourist bus tickets in advance?</h3>
<p>During the peak autumn (October-November) and spring (March-April) seasons, tourist buses sell out several days in advance. We strongly recommend booking at least 3 to 5 days ahead, especially for premium sofa-seat coaches.</p>"""

# 2. animaux-chitwan-faune-parc-national
en_by_slug['animaux-chitwan-faune-parc-national']['content'] = """<div class="bg-emerald-50/80 border border-emerald-200 rounded-2xl p-6 mb-8 text-slate-800 shadow-sm">
  <h3 class="text-lg font-black text-emerald-950 mb-3 flex items-center gap-2">📌 Quick Summary: Wildlife of Chitwan National Park</h3>
  <ul class="space-y-2 text-sm leading-relaxed">
    <li><strong>The Star Species:</strong> Over 690 greater one-horned rhinos (Rhinoceros unicornis) – the second-largest wild population on Earth.</li>
    <li><strong>Apex Predators:</strong> ~128 adult Bengal tigers, dense populations of sloth bears (Melursus ursinus) and Indian leopards.</li>
    <li><strong>River Giants:</strong> Critically endangered fish-eating gharials (Gavialis gangeticus) and marsh mugger crocodiles on the Rapti and Narayani rivers.</li>
    <li><strong>Avian & Ungulate Richness:</strong> 540+ bird species, golden jackals, mongooses, spotted chital deer, barking deer and giant sambar.</li>
  </ul>
</div>

<p class="text-lg leading-relaxed text-slate-700 font-medium">Inscribed as a UNESCO World Heritage Site in 1984, <a href="/en/destinations/chitwan" class="text-emerald-700 underline font-bold">Chitwan National Park</a> is Nepal's oldest, most celebrated wildlife sanctuary. Nestled within an expansive subtropical inner Terai river valley bordered by the Rapti, Narayani and Reu rivers, its mosaic of dense Sal hardwood forests, riverine marshes, and soaring elephant grasslands provides a thriving habitat for Asia's most iconic megafauna.</p>

<h2>1. Greater One-Horned Rhinoceros (Rhinoceros unicornis): The Pride of Chitwan</h2>
<p>With more than <strong>690 individuals recorded</strong> in the official <a href="https://dnpwc.gov.np/" target="_blank" rel="noopener noreferrer" class="text-emerald-700 underline font-bold">National Rhino Count Nepal</a>, Chitwan shelters the second-largest population of greater one-horned rhinos in the world, surpassed only by Kaziranga in Assam. Unlike elusive predators, rhinos are frequently encountered grazing in riverbeds at dawn, wallowing in mud pools during hot afternoons, or quietly strolling through community forests bordering Sauraha village at dusk. To understand their biology and survival strategies, explore our guide on <a href="/en/blog/comportement-du-rhinoceros-unicornis" class="text-emerald-700 underline font-bold">greater one-horned rhino behavior</a>.</p>
<p>Weighing between 1.8 and 2.2 metric tons and armored with thick folds of tuberculated skin resembling riveted plates, these magnificent herbivores can be safely observed on ethical private <a href="/en/tours/chitwan-jeep-safari" class="text-emerald-700 underline font-bold">Chitwan jeep safaris</a> and guided walking safaris in community buffer zones.</p>

<h2>2. Bengal Tigers in Chitwan: Magnificent yet Challenging</h2>
<p>Chitwan is home to an impressive population of approximately <strong>128 adult Bengal tigers</strong>. However, spotting a tiger in Chitwan is notoriously more demanding than in Bardia National Park (see our in-depth comparison: <a href="/en/blog/animaux-bardia-faune-parc-national" class="text-emerald-700 underline font-bold">wildlife of Bardia National Park</a>):</p>
<ul>
  <li>Chitwan's grasslands feature elephant grass reaching towering heights of 6 to 8 meters after the monsoon, providing almost impenetrable natural camouflage.</li>
  <li>Heavier tourist volume around eastern Sauraha prompts resident tigers to patrol deep interior sectors far from routine tracks. For travelers obsessed with seeing a tiger, check our statistical guide: <a href="/en/blog/tigre-bardia-observation-chances-spots" class="text-emerald-700 underline font-bold">Bardia tiger tracking success rates and hides</a>.</li>
  <li><strong>Expert Tip from Our Naturalists:</strong> Focus your safari between March and May when winter grass fires have cleared undergrowth and water scarcity concentrates feline activity near permanent river oxbows. Opt for full-day jeep expeditions reaching remote sectors like Kasara, Sukhibhar and Meghauli.</li>
</ul>

<h2>3. River Crocodilians of Rapti and Narayani: Gharials and Muggers</h2>
<p>Drifting silently aboard a hand-carved wooden canoe down the Rapti River offers intimate views of two of the planet's most fascinating crocodilian species (read more in our guide on the <a href="/en/blog/gavial-du-gange-crocodiles-nepal-guide" class="text-emerald-700 underline font-bold">Gharials and crocodiles of Nepal</a>):</p>
<ul>
  <li><strong>The Gharial (Gavialis gangeticus):</strong> Critically endangered on the <a href="https://www.iucnredlist.org/" target="_blank" rel="noopener noreferrer" class="text-emerald-700 underline font-bold">IUCN Red List</a>, unmistakable with its needle-thin elongated jaws lined with over 100 interlocking teeth and the bulbous nasal boss (ghara) on mature males. They feed exclusively on river fish. A world-renowned captive breeding and conservation center operates at park headquarters in Kasara.</li>
  <li><strong>The Marsh Mugger (Crocodylus palustris):</strong> A robust, broad-snouted apex ambush predator thriving in still oxbow lakes, muddy creeks, and sunny sandbars.</li>
</ul>

<h2>4. Sloth Bears (Melursus ursinus): Record Densities in Chitwan</h2>
<p>Chitwan is widely recognized by field zoologists as one of the finest refuges in South Asia for the nocturnal, insectivorous sloth bear. Often active around sunrise and late afternoon, they excavate subterranean termite mounds with enormous curved ivory claws, producing vacuuming snorts audible from dozens of meters away. They frequently cross sandy tracks between Sal forests and riverbanks.</p>

<div class="blog-cta-card my-10 p-6 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
  <div class="space-y-1">
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">1-Day Activity • Chitwan</span>
    <h3 class="text-xl font-bold text-white">Full-Day Private Jeep Safari in Chitwan (190€)</h3>
    <p class="text-slate-300 text-xs">Venture deep into the pristine core sectors of Chitwan National Park aboard our customized open-top safari 4x4. Dedicated naturalist guide, park permits, and lunch included.</p>
  </div>
  <div class="flex flex-wrap items-center gap-3 mt-4">
    <a href="/en/tours/chitwan-jeep-safari" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs shadow-md transition-all">Book Full-Day Jeep Safari (190€) →</a>
    <a href="https://wa.me/33695413227?text=Hello%20Robin,%20I%20would%20like%20to%20book%20a%20full-day%20jeep%20safari%20in%20Chitwan" target="_blank" rel="noopener noreferrer" class="cta-btn-alt inline-block px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs border border-white/20 transition-all">Chat on WhatsApp</a>
  </div>
</div>

<h2>Comparative Matrix: Iconic Wildlife of Chitwan</h2>
<table class="my-8 w-full border-collapse border border-slate-200 text-sm">
  <thead>
    <tr class="bg-slate-100 text-slate-900 font-bold">
      <th class="p-3 border border-slate-200 text-left">Species</th>
      <th class="p-3 border border-slate-200 text-left">Chitwan Population</th>
      <th class="p-3 border border-slate-200 text-left">Sighting Probability</th>
      <th class="p-3 border border-slate-200 text-left">Recommended Activity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Greater One-Horned Rhino</td>
      <td class="p-3 border border-slate-200">> 690 individuals</td>
      <td class="p-3 border border-slate-200">Near-Guaranteed (95-100%)</td>
      <td class="p-3 border border-slate-200">Jeep safari & buffer walking safari</td>
    </tr>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Gharial Crocodile</td>
      <td class="p-3 border border-slate-200">~200 individuals</td>
      <td class="p-3 border border-slate-200">Very High (90%)</td>
      <td class="p-3 border border-slate-200">Rapti River traditional canoe safari</td>
    </tr>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Sloth Bear</td>
      <td class="p-3 border border-slate-200">Dense healthy population</td>
      <td class="p-3 border border-slate-200">Good (40-60%)</td>
      <td class="p-3 border border-slate-200">Late afternoon open jeep safari</td>
    </tr>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Bengal Tiger</td>
      <td class="p-3 border border-slate-200">~128 adults</td>
      <td class="p-3 border border-slate-200">Challenging (25-35%)</td>
      <td class="p-3 border border-slate-200">Full-day deep jeep safari (Kasara/Sukhibhar)</td>
    </tr>
  </tbody>
</table>"""

with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print("Batch 1 (Chitwan Transport & Chitwan Wildlife) written successfully.")
