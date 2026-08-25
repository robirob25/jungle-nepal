with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

# Add core animation utility CSS classes in Layout.astro <style>
anim_css = """
  /* High-End Motion & Interaction Primitives */
  @keyframes subtleRadarPulse {
    0% { transform: scale(1); opacity: 0.8; }
    50% { transform: scale(1.8); opacity: 0.2; }
    100% { transform: scale(2.2); opacity: 0; }
  }

  @keyframes heroFadeUp {
    from { opacity: 0; transform: translateY(22px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .animate-hero-1 { animation: heroFadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.1s both; }
  .animate-hero-2 { animation: heroFadeUp 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.25s both; }
  .animate-hero-3 { animation: heroFadeUp 1.0s cubic-bezier(0.16, 1, 0.3, 1) 0.4s both; }

  /* Scroll Reveal Helper Classes */
  .reveal-on-scroll {
    opacity: 0;
    transform: translateY(24px);
    transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    will-change: opacity, transform;
  }

  .reveal-on-scroll.revealed {
    opacity: 1;
    transform: translateY(0);
  }

  .map-pin-radar::after {
    content: '';
    position: absolute;
    inset: -4px;
    border-radius: 9999px;
    background-color: rgba(16, 185, 129, 0.6);
    animation: subtleRadarPulse 2.8s cubic-bezier(0, 0, 0.2, 1) infinite;
    pointer-events: none;
    z-index: -1;
  }

  /* Smooth FAQ spring animation */
  details summary {
    transition: color 0.2s ease;
  }
  details[open] summary svg {
    transform: rotate(180deg);
  }
"""

if "/* High-End Motion" not in layout:
    layout = layout.replace('</style>', anim_css + '\n</style>')

# Add Universal Scroll-Observer script right before </body> in Layout.astro
scroll_script = """
  <!-- Universal Performance-Optimized Scroll Observer -->
  <script is:inline>
    document.addEventListener('DOMContentLoaded', function() {
      if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function(entries) {
          entries.forEach(function(entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('revealed');
              observer.unobserve(entry.target);
            }
          });
        }, {
          threshold: 0.08,
          rootMargin: '0px 0px -40px 0px'
        });

        document.querySelectorAll('.reveal-on-scroll').forEach(function(el) {
          observer.observe(el);
        });
      } else {
        document.querySelectorAll('.reveal-on-scroll').forEach(function(el) {
          el.classList.add('revealed');
        });
      }
    });
  </script>
"""

if "Universal Performance-Optimized Scroll Observer" not in layout:
    layout = layout.replace('</body>', scroll_script + '\n</body>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)

print("✓ Added animation CSS & universal IntersectionObserver to Layout.astro")

# 2. Update index.astro to apply the animations to Hero, Bento, 15 Séjours, Map, Gallery, Video, Trackers and FAQ
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# 2.1 Hero section stagger
idx = idx.replace(
    '<h1 class="text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-black tracking-tight text-white mb-6 leading-none">',
    '<h1 class="animate-hero-1 text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-black tracking-tight text-white mb-6 leading-none">'
)
idx = idx.replace(
    '<p class="text-lg sm:text-xl md:text-2xl text-slate-100 max-w-3xl mx-auto mb-10 font-normal leading-relaxed text-balance">',
    '<p class="animate-hero-2 text-lg sm:text-xl md:text-2xl text-slate-100 max-w-3xl mx-auto mb-10 font-normal leading-relaxed text-balance">'
)
idx = idx.replace(
    '<div class="max-w-4xl mx-auto backdrop-blur-xl bg-white/95 p-3 sm:p-4 rounded-3xl shadow-2xl border border-white/40">',
    '<div class="animate-hero-3 max-w-4xl mx-auto backdrop-blur-xl bg-white/95 p-3 sm:p-4 rounded-3xl shadow-2xl border border-white/40 hover:shadow-[0_20px_50px_rgba(0,0,0,0.3)] transition-all duration-300">'
)

# 2.2 Category bento cards smooth scroll reveal & subtle hover
idx = idx.replace(
    '<section id="categories" class="relative z-20 -mt-10 sm:-mt-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">',
    '<section id="categories" class="reveal-on-scroll relative z-20 -mt-10 sm:-mt-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">'
)

# 2.3 Trip cards smooth staggered reveal
idx = idx.replace(
    'class="trip-card group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-[0_4px_20px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_40px_rgba(10,50,30,0.18)] hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between"',
    'class="trip-card reveal-on-scroll group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-[0_4px_20px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_40px_rgba(10,50,30,0.18)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between"'
)

# 2.4 Interactive Map Radar Pulses on pins
idx = idx.replace(
    'class="map-pin relative group cursor-pointer"',
    'class="map-pin relative group cursor-pointer map-pin-radar"'
)

# 2.5 Wildlife Gallery smooth reveal
idx = idx.replace(
    '<section id="galerie-faune" class="scroll-mt-20 sm:scroll-mt-24 py-12 sm:py-16 lg:py-20 bg-slate-950 text-white relative overflow-hidden">',
    '<section id="galerie-faune" class="reveal-on-scroll scroll-mt-20 sm:scroll-mt-24 py-12 sm:py-16 lg:py-20 bg-slate-950 text-white relative overflow-hidden">'
)

# 2.6 Video cinema section reveal
idx = idx.replace(
    '<section id="concept" class="scroll-mt-20 sm:scroll-mt-24 py-12 sm:py-16 lg:py-20 bg-[#072418] text-white relative overflow-hidden">',
    '<section id="concept" class="reveal-on-scroll scroll-mt-20 sm:scroll-mt-24 py-12 sm:py-16 lg:py-20 bg-[#072418] text-white relative overflow-hidden">'
)

# 2.7 Trackers section reveal
idx = idx.replace(
    '<section id="pisteurs" class="scroll-mt-20 sm:scroll-mt-24 py-12 sm:py-16 lg:py-20 bg-[#faf8f5]">',
    '<section id="pisteurs" class="reveal-on-scroll scroll-mt-20 sm:scroll-mt-24 py-12 sm:py-16 lg:py-20 bg-[#faf8f5]">'
)

# 2.8 FAQ & Reviews reveal
idx = idx.replace(
    '<section id="avis" class="scroll-mt-20 sm:scroll-mt-24 py-12 sm:py-16 lg:py-20 bg-[#f4f0ea]">',
    '<section id="avis" class="reveal-on-scroll scroll-mt-20 sm:scroll-mt-24 py-12 sm:py-16 lg:py-20 bg-[#f4f0ea]">'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

print("✓ Applied refined animations across all homepage sections!")
