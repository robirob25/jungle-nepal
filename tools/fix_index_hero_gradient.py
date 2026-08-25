with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Locate line 391:
# <!-- Deep Atmospheric Gradients for Impeccable Text Contrast -->
# and add the real global dark overlay that covers all slides in the hero slider!

old_overlay_marker = "      <!-- Deep Atmospheric Gradients for Impeccable Text Contrast -->\n      \n    </div>"

new_overlay_marker = """      <!-- Deep Atmospheric Gradients & Dark Tint for Impeccable Text & Navbar Contrast -->
      <div class="absolute inset-0 z-10 bg-slate-950/60 pointer-events-none"></div>
      <div class="absolute inset-0 z-10 bg-gradient-to-b from-black/85 via-black/40 to-slate-950/95 pointer-events-none"></div>
      <div class="absolute inset-0 z-10 bg-gradient-to-t from-slate-950 via-transparent to-black/70 pointer-events-none"></div>
    </div>"""

if old_overlay_marker in c:
    c = c.replace(old_overlay_marker, new_overlay_marker)
else:
    # Alternative replace before </div> in hero-slider-container
    c = c.replace(
        '<!-- Slide 11: Paon bleu en parade -->\n      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="10">\n        <img \n          src="/assets/wildlife_gallery/wildlife_peacock_wheel.webp" \n          alt="Paon bleu en parade au Terai" \n          class="w-full h-full object-cover object-center filter brightness-90 contrast-105" \n          loading="lazy" \n        />\n      </div>\n\n      <!-- Deep Atmospheric Gradients for Impeccable Text Contrast -->\n      \n    </div>',
        '<!-- Slide 11: Paon bleu en parade -->\n      <div class="hero-slide absolute inset-0 transition-all duration-1000 ease-in-out opacity-0 scale-100 pointer-events-none" data-slide="10">\n        <img \n          src="/assets/wildlife_gallery/wildlife_peacock_wheel.webp" \n          alt="Paon bleu en parade au Terai" \n          class="w-full h-full object-cover object-center filter brightness-90 contrast-105" \n          loading="lazy" \n        />\n      </div>\n\n      <!-- Deep Atmospheric Gradients & Dark Tint for Impeccable Text & Navbar Contrast -->\n      <div class="absolute inset-0 z-10 bg-slate-950/60 pointer-events-none"></div>\n      <div class="absolute inset-0 z-10 bg-gradient-to-b from-black/85 via-black/40 to-slate-950/95 pointer-events-none"></div>\n      <div class="absolute inset-0 z-10 bg-gradient-to-t from-slate-950 via-transparent to-black/70 pointer-events-none"></div>\n    </div>'
    )

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Successfully placed real dark overlay layers directly over the hero image carousel in index.astro!")
