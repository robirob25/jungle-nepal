with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Increase top padding / margin to push the Hero text and search box down cleanly
content = content.replace(
    '<section class="relative min-h-[92vh] sm:min-h-screen flex flex-col justify-between items-center pt-36 sm:pt-40 pb-6 sm:pb-8 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950">',
    '<section class="relative min-h-[92vh] sm:min-h-screen flex flex-col justify-between items-center pt-48 sm:pt-56 lg:pt-64 pb-8 sm:pb-12 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950">'
)

content = content.replace(
    '<div class="relative z-10 max-w-5xl mx-auto text-center flex flex-col items-center w-full">',
    '<div class="relative z-10 max-w-5xl mx-auto text-center flex flex-col items-center w-full my-auto">'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Hero content positioned downwards cleanly!")
