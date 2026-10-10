import re

PATTERNS_EN_REMAINING = {
    'src/pages/en/tours/bardia-jeep-safari.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base text-slate-700 leading-relaxed font-normal">\s*Aboard a specially adapted open-top safari vehicle',
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Explore remote wilderness corridors of Bardia by private 4x4 Jeep
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Privatized exclusively for your group (up to 6 guests) at <strong>€190 for a full day</strong>, this 4x4 open-jeep safari is the ultimate way to reach the most secluded, untamed sectors of <strong>Bardia National Park</strong> (including Baghaura and the Karnali floodplains). Escorted by an expert driver and a certified senior naturalist, this all-inclusive expedition covers national park entry permits and a freshly prepared bush lunch, allowing you to cover vast distances and maximize encounters with wild Bengal tigers.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              Aboard a customized safari vehicle completely open to the wilderness, you navigate forest trails and alluvial grasslands alongside an elite tracking team, reading fresh night pugmarks and interpreting canopy alarm calls throughout the day."""
    ),
    'src/pages/en/tours/bardia-rafting-safari.astro': (
        r'<div class="space-y-4">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<p[^>]*>.*?</p>\s*<p class="text-base text-slate-700 leading-relaxed font-normal">\s*Aboard a private, fully certified inflatable raft',
        """<div class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-black text-slate-950 tracking-tight">
              Float Down the Karnali River on a Private Rafting Safari in Bardia
            </h2>
            <p class="text-base sm:text-lg text-slate-800 leading-relaxed font-normal">
              Available at <strong>€120 per person for a full day</strong>, this <strong>Karnali River rafting safari</strong> (a 35 km silent drift along Bardia National Park) is the quietest and most stealthy way to observe wild Asian wildlife. Guided by a certified whitewater captain, senior naturalist, and elite tracker, the tour includes complete safety equipment, 4x4 transfers, national park permits, and a freshly prepared picnic lunch on an isolated river island.
            </p>
            <p class="text-base text-slate-700 leading-relaxed font-normal">
              Carried by gentle, clear currents through the Karnali and Geruwa channels, your raft drifts silently alongside forested bluffs and gravel banks. This rare water-level perspective offers unmatched opportunities to witness freshwater Gangetic dolphins, critically endangered gharials, and wild elephants or Bengal tigers emerging to drink along the riverbanks."""
    )
}

for filepath, (pattern, replacement) in PATTERNS_EN_REMAINING.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count == 1:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Flawlessly updated {filepath}")
    else:
        print(f"✗ Regex count {count} for {filepath}")
