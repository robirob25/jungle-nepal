import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

new_hero_bg = """<!-- 9-PHOTO CINEMA HERO AUTO-SLIDER -->
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

      <!-- Slide 2: Éléphant sauvage en jungle -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="1">
        <img 
          src="/assets/hero/hero_6_elephant_jungle.webp" 
          alt="Éléphant d'Asie sauvage en jungle de Bardia" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 3: Rhinocéros unicorne dans la brume -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="2">
        <img 
          src="/assets/hero/hero_2_rhino_mist.webp" 
          alt="Rhinocéros unicorne au lever du soleil" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 4: Tigre royal en approche -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="3">
        <img 
          src="/assets/hero/hero_7_tiger_stalk.webp" 
          alt="Tigre du Bengale en chasse" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 5: Cerfs des marais dans les plaines -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="4">
        <img 
          src="/assets/hero/hero_4_deer_plain.webp" 
          alt="Cerfs et faune sauvage du Terai" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 6: Crocodile avec reflet dans l'eau -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="5">
        <img 
          src="/assets/hero/hero_8_croco_water.webp" 
          alt="Crocodile des marais à fleur d'eau" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 7: Tigre en marche dans la jungle -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="6">
        <img 
          src="/assets/hero/hero_3_tiger_jungle.webp" 
          alt="Tigre royal en pleine jungle de Bardia" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 8: Grand Calao bicorne -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="7">
        <img 
          src="/assets/hero/hero_9_calao_hornbill.webp" 
          alt="Grand Calao bicorne sur une branche" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 9: Nilgauts / antilopes sauvages -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="8">
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

# Replace hero bg
c = re.sub(r'<!-- (?:5|9)-PHOTO CINEMA HERO AUTO-SLIDER -->.*?<\/div>\s*<\/div>', new_hero_bg, c, flags=re.DOTALL)

# Replace indicator dots
new_dots = """      <!-- Slider Indicator Dots -->
      <div class="relative z-20 mt-8 flex items-center justify-center gap-1.5" id="hero-slider-dots">
        <button onclick="setHeroSlide(0)" class="hero-dot w-7 h-1.5 rounded-full bg-amber-400 transition-all duration-300 cursor-pointer" aria-label="Slide 1"></button>
        <button onclick="setHeroSlide(1)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 2"></button>
        <button onclick="setHeroSlide(2)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 3"></button>
        <button onclick="setHeroSlide(3)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 4"></button>
        <button onclick="setHeroSlide(4)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 5"></button>
        <button onclick="setHeroSlide(5)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 6"></button>
        <button onclick="setHeroSlide(6)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 7"></button>
        <button onclick="setHeroSlide(7)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 8"></button>
        <button onclick="setHeroSlide(8)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 9"></button>
      </div>"""

c = re.sub(r'<!-- Slider Indicator Dots -->\s*<div[^>]*id="hero-slider-dots"[^>]*>.*?<\/div>', new_dots, c, flags=re.DOTALL)

# Update total slides in script
c = c.replace('var totalHeroSlides = 5;', 'var totalHeroSlides = 9;')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated Hero slider to 9 wildlife photos in index.astro!")
