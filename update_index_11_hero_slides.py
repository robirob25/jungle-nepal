import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Add slides 10 and 11 to hero background
slides_to_add = """      <!-- Slide 10: Marabout en plein vol -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="9">
        <img 
          src="/assets/wildlife_gallery/wildlife_marabout_flight.webp" 
          alt="Marabout chevelu en vol à l'aube" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>

      <!-- Slide 11: Paon bleu en parade -->
      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="10">
        <img 
          src="/assets/wildlife_gallery/wildlife_peacock_wheel.webp" 
          alt="Paon bleu en parade au Terai" 
          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"
          loading="lazy"
        />
      </div>"""

if 'Slide 10: Marabout' not in c:
    c = c.replace('<!-- Deep Atmospheric Gradients', f'{slides_to_add}\n\n      <!-- Deep Atmospheric Gradients')

# Update indicator dots to 11
new_11_dots = """      <!-- Slider Indicator Dots -->
      <div class="relative z-20 mt-8 flex items-center justify-center gap-1.5" id="hero-slider-dots">
        <button onclick="setHeroSlide(0)" class="hero-dot w-6 h-1.5 rounded-full bg-amber-400 transition-all duration-300 cursor-pointer" aria-label="Slide 1"></button>
        <button onclick="setHeroSlide(1)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 2"></button>
        <button onclick="setHeroSlide(2)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 3"></button>
        <button onclick="setHeroSlide(3)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 4"></button>
        <button onclick="setHeroSlide(4)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 5"></button>
        <button onclick="setHeroSlide(5)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 6"></button>
        <button onclick="setHeroSlide(6)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 7"></button>
        <button onclick="setHeroSlide(7)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 8"></button>
        <button onclick="setHeroSlide(8)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 9"></button>
        <button onclick="setHeroSlide(9)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 10"></button>
        <button onclick="setHeroSlide(10)" class="hero-dot w-2 h-1.5 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300 cursor-pointer" aria-label="Slide 11"></button>
      </div>"""

c = re.sub(r'<!-- Slider Indicator Dots -->\s*<div[^>]*id="hero-slider-dots"[^>]*>.*?<\/div>', new_11_dots, c, flags=re.DOTALL)

# Update totalHeroSlides to 11 in script
c = c.replace('var totalHeroSlides = 9;', 'var totalHeroSlides = 11;')
c = c.replace('var totalHeroSlides = 5;', 'var totalHeroSlides = 11;')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated Hero slider to 11 wildlife photos in index.astro!")
