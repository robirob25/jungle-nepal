import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Replace the single Cinema Hero Photo with 5-slide auto-slider
old_hero_bg = r'<!-- Cinema Hero Photo -->\s*<div class="absolute inset-0 z-0">.*?<\/div>\s*<\/div>'

new_hero_bg = """<!-- 5-PHOTO CINEMA HERO AUTO-SLIDER -->
    <div class="absolute inset-0 z-0 overflow-hidden" id="hero-slider-container">
      
      <!-- Slide 1: Tigre royal au bord de l'eau -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-100 scale-105" data-slide="0">
        <img 
          src="/assets/hero/hero_1_tiger_water.webp" 
          alt="Tigre du Bengale au point d'eau" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="eager"
        />
      </div>

      <!-- Slide 2: Rhinocéros unicorne dans la brume -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="1">
        <img 
          src="/assets/hero/hero_2_rhino_mist.webp" 
          alt="Rhinocéros unicorne au lever du soleil" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 3: Tigre en marche dans la jungle -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="2">
        <img 
          src="/assets/hero/hero_3_tiger_jungle.webp" 
          alt="Tigre royal en pleine jungle de Bardia" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 4: Cerfs des marais dans les plaines -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="3">
        <img 
          src="/assets/hero/hero_4_deer_plain.webp" 
          alt="Cerfs et faune sauvage du Terai" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 5: Nilgauts / antilopes sauvages -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="4">
        <img 
          src="/assets/hero/hero_5_nilgai_forest.webp" 
          alt="Antilopes Nilgaut en lisière de forêt" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Deep Atmospheric Gradients for Impeccable Text Contrast -->
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/40 to-slate-950/70 z-10"></div>
    </div>"""

c = re.sub(old_hero_bg, new_hero_bg, c, flags=re.DOTALL)

# 2. Add Indicator Dots below the Search Card inside the hero section
dots_html = """      <!-- Slider Indicator Dots -->
      <div class="relative z-20 mt-8 flex items-center justify-center gap-2" id="hero-slider-dots">
        <button onclick="setHeroSlide(0)" class="hero-dot w-8 h-1.5 rounded-full bg-amber-400 transition-all duration-300 cursor-pointer" aria-label="Slide 1 : Tigre au bord de l'eau"></button>
        <button onclick="setHeroSlide(1)" class="hero-dot w-2.5 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 2 : Rhinocéros unicorne"></button>
        <button onclick="setHeroSlide(2)" class="hero-dot w-2.5 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 3 : Tigre en jungle"></button>
        <button onclick="setHeroSlide(3)" class="hero-dot w-2.5 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 4 : Cerfs des marais"></button>
        <button onclick="setHeroSlide(4)" class="hero-dot w-2.5 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 5 : Nilgauts en forêt"></button>
      </div>"""

if 'id="hero-slider-dots"' not in c:
    c = c.replace('<!-- Trust badges below search -->', f'{dots_html}\n\n      <!-- Trust badges below search -->')

# 3. Add Slider Javascript in script block
slider_js = """  // AUTOMATIC HERO SLIDER
  var currentHeroSlide = 0;
  var totalHeroSlides = 5;
  var heroInterval = null;

  function showHeroSlide(index) {
    currentHeroSlide = (index + totalHeroSlides) % totalHeroSlides;
    var slides = document.querySelectorAll('.hero-slide');
    var dots = document.querySelectorAll('.hero-dot');
    
    slides.forEach(function(slide, idx) {
      if (idx === currentHeroSlide) {
        slide.classList.remove('opacity-0', 'scale-100', 'pointer-events-none');
        slide.classList.add('opacity-100', 'scale-105');
      } else {
        slide.classList.remove('opacity-100', 'scale-105');
        slide.classList.add('opacity-0', 'scale-100', 'pointer-events-none');
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
  }

  window.setHeroSlide = function(index) {
    showHeroSlide(index);
    startHeroSlider();
  };

  function startHeroSlider() {
    if (heroInterval) clearInterval(heroInterval);
    heroInterval = setInterval(nextHeroSlide, 4500);
  }

  startHeroSlider();
"""

if 'AUTOMATIC HERO SLIDER' not in c:
    c = c.replace('</Layout>', f'<script is:inline>\n{slider_js}\n</script>\n</Layout>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added 5-photo automatic Hero background slider with smooth cross-fades & indicator dots to index.astro!")
