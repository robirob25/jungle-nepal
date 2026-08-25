import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's add subtle links in key editorial spots:
# In story section
content = content.replace(
    'dans le Parc National de Bardia,',
    'dans le <a href="/destinations/bardia" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">Parc National de Bardia</a>,'
)

content = content.replace(
    'Parc National de Chitwan et de Suklaphanta',
    '<a href="/destinations/chitwan" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">Parc National de Chitwan</a> et de <a href="/destinations/suklaphanta" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">Suklaphanta</a>'
)

# In pisteur section
content = content.replace(
    'Pawan & Kiran vous guident en micro-groupe',
    '<a href="/a-propos" class="text-emerald-400 hover:text-emerald-300 font-semibold underline decoration-emerald-500/30 underline-offset-2 transition-colors">Pawan & Kiran</a> vous guident en micro-groupe'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("Enhanced internal linking in index.astro!")
