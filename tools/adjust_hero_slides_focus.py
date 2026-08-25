with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Slide 1 (Tigre au bord de l'eau: hero_1_tiger_water.webp):
# The tiger head and gaze are on the right/top-right.
# Adjust object-position from object-center to object-[70%_25%] or object-[right_top] so the tiger's eyes/face are above the search box and to the right of the title!

c = c.replace(
    'src="/assets/hero/hero_1_tiger_water.webp" \n          alt="Tigre du Bengale au point d\'eau" \n          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"',
    'src="/assets/hero/hero_1_tiger_water.webp" \n          alt="Tigre du Bengale au point d\'eau" \n          class="w-full h-full object-cover object-[75%_30%] filter brightness-90 contrast-105"'
)

# 2. Slide 5 (Cerfs des marais: hero_4_deer_plain.webp):
# The heads and gaze of the two deer are in the upper center.
# Adjust object-position to object-[50%_15%] or object-[center_top] so their faces and eyes are placed higher up, clearly visible above the central title!

c = c.replace(
    'src="/assets/hero/hero_4_deer_plain.webp" \n          alt="Cerfs et faune sauvage du Terai" \n          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"',
    'src="/assets/hero/hero_4_deer_plain.webp" \n          alt="Cerfs et faune sauvage du Terai" \n          class="w-full h-full object-cover object-[50%_10%] filter brightness-90 contrast-105"'
)

# 3. Slide 4 (Tigre en approche: hero_7_tiger_stalk.webp):
c = c.replace(
    'src="/assets/hero/hero_7_tiger_stalk.webp" \n          alt="Tigre du Bengale en chasse" \n          class="w-full h-full object-cover object-center filter brightness-90 contrast-105"',
    'src="/assets/hero/hero_7_tiger_stalk.webp" \n          alt="Tigre du Bengale en chasse" \n          class="w-full h-full object-cover object-[50%_25%] filter brightness-90 contrast-105"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Adjusted object-position for hero slides to ensure animals' gaze and faces are fully visible!")
