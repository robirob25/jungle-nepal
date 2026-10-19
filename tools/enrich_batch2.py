import json

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

en_by_slug = {p['slug']: p for p in posts_en}

# 3. comment-aller-a-bardia-transport-avion-bus-guide
en_by_slug['comment-aller-a-bardia-transport-avion-bus-guide']['content'] = """<div class="bg-emerald-50/80 border border-emerald-200 rounded-2xl p-6 mb-8 text-slate-800 shadow-sm">
  <h3 class="text-lg font-black text-emerald-950 mb-3 flex items-center gap-2">📌 Quick Summary: How to Reach Bardia National Park</h3>
  <ul class="space-y-2 text-sm leading-relaxed">
    <li><strong>The Premier Route (Recommended):</strong> 50-minute domestic flight Kathmandu (KTM) &rarr; Nepalgunj (KEP) with <a href="https://www.buddhaair.com/" target="_blank" rel="noopener noreferrer" class="text-emerald-700 underline font-bold">Buddha Air</a> or Yeti Airlines, followed by a private 2-hour scenic taxi or 4x4 transfer to Thakurdwara (the park gateway). Total cost: $110 to $160.</li>
    <li><strong>From Pokhara:</strong> Direct domestic flight connecting via Kathmandu, or a private long-distance road drive (10 to 12 hours) across scenic rural hills and Terai plains.</li>
    <li><strong>The Budget Route (Overnight Bus):</strong> Deluxe AC tourist night bus departing Gongabu Bus Park in Kathmandu (15 to 18 hours, $18 to $25) to Ambassa Chowk on the East-West Highway.</li>
    <li><strong>Luggage & Gear Tips:</strong> Domestic airlines allow 15 kg checked baggage and 5 kg cabin baggage. Excess weight is roughly $1.50 per kg.</li>
  </ul>
</div>

<p class="text-lg leading-relaxed text-slate-700 font-medium">Situated in the remote southwestern corner of Nepal, <a href="/en/destinations/bardia" class="text-emerald-700 underline font-bold">Bardia National Park</a> is widely revered by international naturalists as Asia's premier wilderness sanctuary for tracking wild Bengal tigers on foot. While its geographical isolation protects it from mass tourism, reaching this pristine haven is straightforward with proper planning.</p>

<h2>Option 1: Domestic Flight to Nepalgunj + Private Ground Transfer (The Gold Standard)</h2>
<p>By far the most comfortable, reliable, and time-efficient route chosen by our expedition guests:</p>
<ul>
  <li><strong>Flight Route:</strong> Fly from Kathmandu Domestic Terminal to Nepalgunj Airport (KEP). Both Buddha Air and Yeti Airlines operate multiple daily morning and afternoon departures. Flight time is precisely 50 minutes, offering stunning panoramic views of the western Himalaya (Dhaulagiri, Annapurna and Kanjiroba ranges from the right-hand windows).</li>
  <li><strong>Nepalgunj to Thakurdwara by Private Vehicle:</strong> Upon touching down in Nepalgunj, our dedicated private driver greets you at arrivals. The journey to Thakurdwara covers approximately 85 kilometers along the paved East-West Mahendra Highway and takes between 2 hours and 2 hours 15 minutes.</li>
  <li><strong>Scenic Crossing:</strong> The drive passes through the protected forests of Banke National Park and crossing the Karnali River before entering the peaceful rural Tharu villages surrounding Bardia.</li>
</ul>

<h2>Option 2: Traveling to Bardia from Pokhara</h2>
<p>Connecting your Himalayan trek in the Annapurnas directly with a lowland tiger safari in Bardia is one of Nepal's finest journeys:</p>
<ul>
  <li><strong>By Air (Via Kathmandu):</strong> Take an early 25-minute flight from Pokhara to Kathmandu, followed by a short transit to catch the midday flight to Nepalgunj. You arrive at your Bardia lodge in time for an evening sundowner by the Geruwa river.</li>
  <li><strong>By Private Vehicle:</strong> A dedicated private 4x4 or Scorpio SUV can take you via the scenic Siddhartha Highway down through Butwal and westward along the Terai highway. Journey duration is 10 to 12 hours ($220 to $280 per vehicle). It is ideal for small groups wishing to explore rural villages at their own pace.</li>
</ul>

<h2>Option 3: The Deluxe Night Bus from Kathmandu (For Budget Travelers)</h2>
<p>For independent adventurers traveling on extended sabbaticals or strict budgets, overnight sleeper and AC buses run daily from Kathmandu:</p>
<ul>
  <li><strong>Departure:</strong> Gongabu New Bus Station in Kathmandu between 2:00 PM and 4:00 PM.</li>
  <li><strong>Route:</strong> The bus travels westward throughout the night along the Prithvi and East-West highways.</li>
  <li><strong>Drop-off Point (Crucial Detail):</strong> Do not book a ticket all the way to Mahendranagar; ask the driver to drop you off at <strong>Ambassa Chowk</strong> (the army checkpoint junction for Bardia). From Ambassa, Thakurdwara is located 13 kilometers south. Our lodge team will meet you directly at Ambassa with a private jeep or tuk-tuk.</li>
  <li><strong>Duration & Experience:</strong> 15 to 18 hours. Road conditions vary, and earplugs plus warm layers are strongly advised.</li>
</ul>

<div class="blog-cta-card my-10 p-6 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
  <div class="space-y-1">
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">1-Day Activity • Bardia</span>
    <h3 class="text-xl font-bold text-white">Full-Day Walking Tiger Safari in Bardia (50€)</h3>
    <p class="text-slate-300 text-xs">Arriving in Bardia? Step beyond standard safari jeeps and track wild Bengal tigers on foot with our veteran native master trackers. Jungle lunch, park permits, and safety briefing included.</p>
  </div>
  <div class="flex flex-wrap items-center gap-3 mt-4">
    <a href="/en/tours/bardia-walking-safari" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs shadow-md transition-all">Book Walking Safari (50€) →</a>
    <a href="https://wa.me/33695413227?text=Hello%20Robin,%20I%20am%20traveling%20to%20Bardia%20and%20want%20to%20book%20a%20walking%20safari" target="_blank" rel="noopener noreferrer" class="cta-btn-alt inline-block px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs border border-white/20 transition-all">Chat on WhatsApp</a>
  </div>
</div>

<h2>FAQ: Logistics & Reaching Bardia</h2>
<h3>Is it safe to travel to Bardia during the monsoon season?</h3>
<p>Domestic flights between Kathmandu and Nepalgunj operate year-round. However, during peak monsoon (July-August), river levels rise and certain jungle tracks in the park become inaccessible. The prime travel window is October through May.</p>

<h3>Can Jungle Nepal Adventure handle all domestic flights and transfers?</h3>
<p>Yes. All our multi-day expeditions include domestic flights, airport reception, and private vehicle transfers between Nepalgunj and your lodge in Bardia.</p>"""

# 4. safari-a-pied-nepal-danger-regles-securite-guide
en_by_slug['safari-a-pied-nepal-danger-regles-securite-guide']['content'] = """<div class="bg-emerald-50/80 border border-emerald-200 rounded-2xl p-6 mb-8 text-slate-800 shadow-sm">
  <h3 class="text-lg font-black text-emerald-950 mb-3 flex items-center gap-2">📌 Quick Summary: Walking Safari Safety in Nepal</h3>
  <ul class="space-y-2 text-sm leading-relaxed">
    <li><strong>Strict Two-Guide Regulation:</strong> By national park law in Bardia, entering the wilderness on foot requires two certified government-licensed naturalists at all times.</li>
    <li><strong>The Bamboo Staff:</strong> Guides do not carry firearms. They use traditional seasoned bamboo staffs, relying on deep animal ethology, wind orientation, and non-violent deterrence.</li>
    <li><strong>Golden Rule:</strong> Never run in front of a predator. Running instinctively triggers the chase response of apex carnivores.</li>
    <li><strong>Dress Code:</strong> Neutral earth tones (khaki, olive, beige, dark green). Strict ban on bright colors, white, and scented deodorants or perfumes.</li>
  </ul>
</div>

<p class="text-lg leading-relaxed text-slate-700 font-medium">Entering the dense subtropical jungle of <a href="/en/destinations/bardia" class="text-emerald-700 underline font-bold">Bardia National Park</a> on foot is arguably the most electrifying wildlife encounter on the Asian continent. Yet for first-time visitors, walking through territory ruled by wild Bengal tigers, greater one-horned rhinos, and wild bull elephants naturally sparks legitimate questions about danger and safety. Here is an authentic breakdown of how safety is guaranteed in the field.</p>

<h2>1. The Mandatory Two-Tracker Rule: Eyes in Front and Behind</h2>
<p>In Bardia, independent walking inside the park is strictly illegal. Every walking safari must be escorted by a minimum of <strong>two certified senior guides</strong>:</p>
<ul>
  <li><strong>Lead Tracker:</strong> Walks at the head of the single-file line, scanning fresh tracks, reading broken branches, checking wind direction, and observing alarm calls from langurs and chital deer.</li>
  <li><strong>Rear Tracker:</strong> Closes the line, ensuring that no guest falls behind and continuously scanning the flanks and rear perimeter. Tigers are stealth ambush hunters that rarely approach from the front; having a dedicated professional guarding the rear eliminates surprise encounters.</li>
  <li><strong>Decades of Indigenous Heritage:</strong> Our guides belong predominantly to the indigenous Tharu community. They have lived beside the jungle for generations, possessing an intuitive understanding of animal vocalizations, tail flicks, and body posturing.</li>
</ul>

<h2>2. Why Bamboo Staffs Instead of Firearms?</h2>
<p>Many travelers coming from African safaris are surprised to find that Nepalese park rangers and safari guides carry sturdy, fire-hardened bamboo sticks rather than rifles. There are philosophical and practical reasons for this:</p>
<ul>
  <li><strong>Non-Lethal Conservation Philosophy:</strong> National parks in Nepal prioritize strict non-violence. Guides do not enter the wilderness to dominate nature, but to observe as respectful guests.</li>
  <li><strong>The Acoustic Weapon:</strong> Striking a hard seasoned bamboo staff firmly against the trunk of a Sal tree produces an echoing, sharp acoustic crack that instantly alarms rhinos and bears, causing them to turn and retreat without physical harm.</li>
  <li><strong>Physical Deterrence:</strong> In rare close-quarters encounters with an irritated mother rhino, a firmly planted staff creates a visual and physical barrier that guides use to deflect charges toward nearby trees.</li>
</ul>

<h2>3. Survival Protocols Facing the "Big Four" of the Jungle</h2>
<p>Before stepping across the park boundary, your lead guide will deliver an intensive 15-minute tactical briefing covering how to react depending on the species encountered:</p>
<table class="my-6 w-full border-collapse border border-slate-200 text-sm">
  <thead>
    <tr class="bg-slate-100 text-slate-900 font-bold">
      <th class="p-3 border border-slate-200 text-left">Animal Encountered</th>
      <th class="p-3 border border-slate-200 text-left">Immediate Action</th>
      <th class="p-3 border border-slate-200 text-left">What You Must NEVER Do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Bengal Tiger</td>
      <td class="p-3 border border-slate-200">Freeze immediately. Maintain calm, unbroken eye contact. Slowly back away step-by-step behind the guides.</td>
      <td class="p-3 border border-slate-200 text-rose-700 font-bold">NEVER run or turn your back. Running triggers an instant predatory chase reflex.</td>
    </tr>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">One-Horned Rhino</td>
      <td class="p-3 border border-slate-200">Run in a zigzag pattern behind large Sal trees or climb a tree (rhinos cannot climb). Drop your backpack to distract its poor eyesight.</td>
      <td class="p-3 border border-slate-200 text-rose-700 font-bold">Do not run in a straight line; rhinos charge straight at up to 45 km/h.</td>
    </tr>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Sloth Bear</td>
      <td class="p-3 border border-slate-200">Group closely together with the guides. Wave arms high, bang sticks, and make loud commanding human voices to intimidate it.</td>
      <td class="p-3 border border-slate-200 text-rose-700 font-bold">Never stay silent or crouch. Sloth bears have poor eyesight and attack out of panic.</td>
    </tr>
    <tr>
      <td class="p-3 border border-slate-200 font-semibold">Wild Asian Elephant</td>
      <td class="p-3 border border-slate-200">Quietly retreat downwind immediately. Give solitary bull elephants at least 100 meters of clearance.</td>
      <td class="p-3 border border-slate-200 text-rose-700 font-bold">Never approach upwind or block an elephant's path to water.</td>
    </tr>
  </tbody>
</table>

<div class="blog-cta-card my-10 p-6 rounded-2xl bg-emerald-950 text-white border border-emerald-500/30">
  <div class="space-y-1">
    <span class="text-[10px] uppercase font-bold text-emerald-400 tracking-wider">1-Day Activity • Bardia</span>
    <h3 class="text-xl font-bold text-white">Full-Day Walking Tiger Safari in Bardia (50€)</h3>
    <p class="text-slate-300 text-xs">Experience the ultimate thrill of tracking wild tigers on foot under the safest, most professional conditions in Nepal. Dual licensed trackers, permits, and bush lunch included.</p>
  </div>
  <div class="flex flex-wrap items-center gap-3 mt-4">
    <a href="/en/tours/bardia-walking-safari" class="cta-btn inline-block px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs shadow-md transition-all">Book Day Walking Safari (50€) →</a>
    <a href="https://wa.me/33695413227?text=Hello%20Robin,%20I%20have%20questions%20about%20safety%20on%20walking%20safaris" target="_blank" rel="noopener noreferrer" class="cta-btn-alt inline-block px-4 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs border border-white/20 transition-all">Chat on WhatsApp</a>
  </div>
</div>

<h2>Essential Gear and Etiquette for Walking Safaris</h2>
<p>To maximize your safety and avoid spooking sensitive wildlife:</p>
<ul>
  <li><strong>Footwear:</strong> Broken-in lightweight trekking shoes or trail runners with quiet soles. Avoid loud squeaking rubber or heavy mountaineering boots.</li>
  <li><strong>Hydration:</strong> At least 2 liters of water in a reusable thermos or canteen (plastic bottles are banned inside the park).</li>
  <li><strong>Silence:</strong> Complete discipline. Whispering is reserved exclusively for vital instructions from your lead tracker.</li>
</ul>"""

with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print("Batch 2 (Bardia Transport & Walking Safari Safety) written successfully.")
