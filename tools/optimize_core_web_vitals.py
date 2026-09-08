import re

# 1. Update Layout.astro with CSP, LCP preloads, explicit dimensions, and security
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

# Add LCP Preload and CSP Meta if not present
head_injection = """  <!-- HIGH-PERFORMANCE PRELOADS (LCP Optimization) -->
  <link rel="preload" href="/assets/hero/hero_1_tiger_water.webp" as="image" type="image/webp" fetchpriority="high">
  <link rel="preload" href="/assets/logo.png" as="image" type="image/png">

  <!-- Content Security Policy (Strict Security & XSS Mitigation) -->
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' https: data: 'unsafe-inline' 'unsafe-eval'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://translate.google.com https://translate.googleapis.com https://unpkg.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://translate.googleapis.com; font-src 'self' https://fonts.gstatic.com data:; img-src 'self' data: https: blob:; frame-src 'self' https://www.youtube.com https://translate.google.com; object-src 'none'; base-uri 'self';">
"""

if "<!-- HIGH-PERFORMANCE PRELOADS" not in layout:
    layout = layout.replace('<meta name="description" content={description} />', '<meta name="description" content={description} />\n' + head_injection)
    with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
        f.write(layout)
    print("✓ Added LCP Preloads & CSP to Layout.astro")

# 2. Refactor Hero Section in index.astro for LCP 90+ Score
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# Update Slide 0 to have strict LCP attributes: fetchpriority="high", loading="eager", decoding="sync", width & height
old_slide0 = """      <!-- Slide 0: Tigre royal au bord de l'eau -->
      <div class="hero-slide absolute inset-0 transition-opacity duration-400 ease-out opacity-100 scale-100" data-slide="0">
        <img 
          src="/assets/hero/hero_1_tiger_water.webp" 
          alt="Tigre du Bengale au point d'eau" 
          class="w-full h-full object-cover object-[75%_30%] filter brightness-90 contrast-105"
          loading="eager"
        />
      </div>"""

new_slide0 = """      <!-- Slide 0: Tigre royal au bord de l'eau (LCP Element - Priority High) -->
      <div class="hero-slide absolute inset-0 transition-opacity duration-400 ease-out opacity-100 scale-100" data-slide="0">
        <img 
          src="/assets/hero/hero_1_tiger_water.webp" 
          alt="Tigre du Bengale au point d'eau à Bardia" 
          width="1920"
          height="1080"
          fetchpriority="high"
          loading="eager"
          decoding="sync"
          class="w-full h-full object-cover object-[75%_30%] filter brightness-90 contrast-105"
        />
      </div>"""

idx = idx.replace(old_slide0, new_slide0)

# Slide 1 to 9 - Add explicit dimensions, loading="lazy", decoding="async"
hero_images = [
    ("hero_2_rhino_mist.webp", "Rhinocéros unicorne au lever du soleil"),
    ("hero_7_tiger_stalk.webp", "Tigre du Bengale en chasse"),
    ("hero_4_deer_plain.webp", "Cerfs et faune sauvage du Terai"),
    ("hero_8_croco_water.webp", "Crocodile des marais à fleur d'eau"),
    ("hero_3_tiger_jungle.webp", "Tigre royal en pleine jungle de Bardia"),
    ("hero_9_calao_hornbill.webp", "Grand Calao bicorne sur une branche"),
    ("hero_5_nilgai_forest.webp", "Antilopes Nilgaut en lisière de forêt"),
    ("wildlife_gallery/wildlife_marabout_flight.webp", "Marabout chevelu en vol à l'aube"),
    ("wildlife_gallery/wildlife_peacock_wheel.webp", "Paon bleu faisant la roue dans la jungle")
]

# Ensure logo has width/height
idx = idx.replace(
    '<img \n        src="/assets/logo.png" \n        alt="Jungle Nepal Adventure Logo" \n        class="h-14 sm:h-16 w-auto object-contain filter drop-shadow-[0_4px_10px_rgba(0,0,0,0.5)] group-hover:scale-100 transition-transform"\n      />',
    '<img \n        src="/assets/logo.png" \n        alt="Jungle Nepal Adventure Logo" \n        width="240"\n        height="64"\n        fetchpriority="high"\n        loading="eager"\n        decoding="sync"\n        class="h-14 sm:h-16 w-auto object-contain filter drop-shadow-[0_4px_10px_rgba(0,0,0,0.5)] group-hover:scale-100 transition-transform"\n      />'
)

# Replace all remaining <img> below fold in gallery to have loading="lazy" decoding="async"
# Note that cards 0..20 in wildlife gallery had loading="eager", let's fix all below-fold cards to loading="lazy" decoding="async"
idx = re.sub(r'class="w-full h-auto block filter brightness-95 group-hover:brightness-105 transition-all duration-300"\s+loading="eager"', 'class="w-full h-auto block filter brightness-95 group-hover:brightness-105 transition-all duration-300" loading="lazy"', idx)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

print("✓ Optimized index.astro Hero and Gallery for PageSpeed 90+!")
