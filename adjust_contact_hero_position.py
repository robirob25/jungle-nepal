with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Position image to 'object-bottom' or 'object-[center_bottom]' and adjust height/padding
# so that the tiger in the bottom right is 100% visible and uncropped!

old_img = """      <img 
        src="/assets/drive_photos/adrien_bardia_sunset.webp" 
        alt="Coucher de soleil sauvage sur la rivière Karnali à Bardia Népal" 
        class="w-full h-full object-cover opacity-55 scale-105 filter brightness-80 contrast-105"
        loading="eager"
      />"""

new_img = """      <img 
        src="/assets/drive_photos/adrien_bardia_sunset.webp" 
        alt="Tigre du Bengale dans la végétation de Bardia au Népal" 
        class="w-full h-full object-cover object-[center_bottom] opacity-65 scale-100 filter brightness-90 contrast-105"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>"""

c = c.replace(old_img, new_img)

# Increase section min-height slightly so the lower part of the photo has full breathing room
c = c.replace(
    'class="relative min-h-[380px] sm:min-h-[440px] flex items-center bg-slate-950 text-white overflow-hidden py-16 sm:py-24 border-b border-white/10"',
    'class="relative min-h-[440px] sm:min-h-[500px] flex items-center bg-slate-950 text-white overflow-hidden py-20 sm:py-28 border-b border-white/10"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Positioned contact hero photo to object-[center_bottom] with larger viewport height!")
