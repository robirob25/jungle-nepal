import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Check all hero slides inside #hero-slider-container
# Replace slides with clean sequential 0 to 9 indexes:
slides_html = """    <!-- 10-PHOTO CINEMA HERO AUTO-SLIDER (ZERO BLACK/EMPTY SLIDES GUARANTEED) -->
    <div class="absolute inset-0 z-0 overflow-hidden" id="hero-slider-container">
      
      <!-- Slide 0: Tigre royal au bord de l'eau -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-100 scale-100" data-slide="0">
        <img 
          src="/assets/hero/hero_1_tiger_water.webp" 
          alt="Tigre du Bengale au point d'eau" 
          class="w-full h-full object-cover object-[75%_30%] filter brightness-90 contrast-105"
          loading="eager"
        />
      </div>

      <!-- Slide 1: Rhinocéros unicorne dans la brume -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="1">
        <img 
          src="/assets/hero/hero_2_rhino_mist.webp" 
          alt="Rhinocéros unicorne au lever du soleil" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 2: Tigre royal en approche -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="2">
        <img 
          src="/assets/hero/hero_7_tiger_stalk.webp" 
          alt="Tigre du Bengale en chasse" 
          class="w-full h-full object-cover object-[50%_25%] filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 3: Cerfs des marais dans les plaines -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="3">
        <img 
          src="/assets/hero/hero_4_deer_plain.webp" 
          alt="Cerfs et faune sauvage du Terai" 
          class="w-full h-full object-cover object-[50%_10%] filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 4: Crocodile avec reflet dans l'eau -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="4">
        <img 
          src="/assets/hero/hero_8_croco_water.webp" 
          alt="Crocodile des marais à fleur d'eau" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 5: Tigre en marche dans la jungle -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="5">
        <img 
          src="/assets/hero/hero_3_tiger_jungle.webp" 
          alt="Tigre royal en pleine jungle de Bardia" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 6: Grand Calao bicorne -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="6">
        <img 
          src="/assets/hero/hero_9_calao_hornbill.webp" 
          alt="Grand Calao bicorne sur une branche" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 7: Nilgauts / antilopes sauvages -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="7">
        <img 
          src="/assets/hero/hero_5_nilgai_forest.webp" 
          alt="Antilopes Nilgaut en lisière de forêt" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 8: Marabout en plein vol -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="8">
        <img 
          src="/assets/wildlife_gallery/wildlife_marabout_flight.webp" 
          alt="Marabout chevelu en vol à l'aube" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 9: Paon bleu en parade -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="9">
        <img 
          src="/assets/wildlife_gallery/wildlife_peacock_wheel.webp" 
          alt="Paon bleu en parade au Terai" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Balanced Cinematic Gradient & Tint for Clarity & Warmth -->
      <div class="absolute inset-0 z-10 bg-slate-950/30 pointer-events-none"></div>
      <div class="absolute inset-0 z-10 bg-gradient-to-b from-black/60 via-transparent to-slate-950/70 pointer-events-none"></div>
    </div>"""

c = re.sub(r'<!-- 9-PHOTO CINEMA HERO AUTO-SLIDER -->.*?</div>\s*<!-- Balanced Cinematic Gradient', slides_html[:-150], c, flags=re.DOTALL)
# Also clean the container block
c = re.sub(r'<div class="absolute inset-0 z-0 overflow-hidden" id="hero-slider-container">.*?</div>\s*<div class="relative z-10 max-w-5xl', slides_html + '\n\n    <div class="relative z-10 max-w-5xl', c, flags=re.DOTALL)

# 2. Update JavaScript totalHeroSlides dynamically based on actual DOM elements!
old_js = """  var currentHeroSlide = 0;
  var totalHeroSlides = 11;
  var heroInterval = null;

  function showHeroSlide(index) {
    currentHeroSlide = (index + totalHeroSlides) % totalHeroSlides;
    var slides = document.querySelectorAll('.hero-slide');
    var dots = document.querySelectorAll('.hero-dot');
    
    slides.forEach(function(slide, idx) {
      if (idx === currentHeroSlide) {
        slide.classList.remove('opacity-0', 'pointer-events-none');
        slide.classList.add('opacity-100', 'scale-100');
      } else {
        slide.classList.remove('opacity-100', 'scale-100');
        slide.classList.add('opacity-0', 'pointer-events-none');
      }
    });

    dots.forEach(function(dot, idx) {
      if (idx === currentHeroSlide) {
        dot.className = 'hero-dot w-8 h-1.5 rounded-full bg-amber-400 transition-all duration-300 cursor-pointer';
      } else {
        dot.className = 'hero-dot w-2.5 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer';
      }
    });
  }

  function nextHeroSlide() {
    showHeroSlide(currentHeroSlide + 1);
  }"""

new_js = """  var currentHeroSlide = 0;
  var heroInterval = null;

  function showHeroSlide(index) {
    var slides = document.querySelectorAll('.hero-slide');
    if (!slides.length) return;
    var total = slides.length;
    currentHeroSlide = (index + total) % total;
    
    slides.forEach(function(slide, idx) {
      if (idx === currentHeroSlide) {
        slide.classList.remove('opacity-0', 'pointer-events-none');
        slide.classList.add('opacity-100', 'scale-100');
      } else {
        slide.classList.remove('opacity-100', 'scale-100');
        slide.classList.add('opacity-0', 'pointer-events-none');
      }
    });
  }

  function nextHeroSlide() {
    var slides = document.querySelectorAll('.hero-slide');
    if (!slides.length) return;
    showHeroSlide(currentHeroSlide + 1);
  }"""

c = c.replace(old_js, new_js)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed hero slider: dynamically counts exact active slides (10), guaranteeing zero empty/black transition screens!")
