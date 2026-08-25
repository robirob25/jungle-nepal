import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. In Hero Slider: remove scale-105 / scale transforms
c = re.sub(r'scale-105', 'scale-100', c)
c = c.replace("slide.classList.add('opacity-100', 'scale-105');", "slide.classList.add('opacity-100');")
c = c.replace("slide.classList.remove('opacity-100', 'scale-105');", "slide.classList.remove('opacity-100');")
c = c.replace("slide.classList.remove('opacity-0', 'scale-100', 'pointer-events-none');", "slide.classList.remove('opacity-0', 'pointer-events-none');")
c = c.replace("slide.classList.add('opacity-0', 'scale-100', 'pointer-events-none');", "slide.classList.add('opacity-0', 'pointer-events-none');")

# 2. In Wildlife Bento Gallery: remove group-hover:scale-108 and hover zoom
c = c.replace('group-hover:scale-108 transition-transform duration-700 ease-out', 'transition-opacity duration-300')
c = c.replace('hover:scale-105', '')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Removed all artificial photo zoom and scaling effects from index.astro!")
