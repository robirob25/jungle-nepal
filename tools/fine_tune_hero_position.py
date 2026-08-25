with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Fine-tune: adjust from pt-48 sm:pt-56 lg:pt-64 down slightly to pt-40 sm:pt-44 lg:pt-48
content = content.replace(
    'pt-48 sm:pt-56 lg:pt-64 pb-8 sm:pb-12',
    'pt-36 sm:pt-40 lg:pt-44 pb-6 sm:pb-8'
)

# And reduce the top margin of the search card slightly (from mt-10 to mt-8)
content = content.replace(
    '<div class="w-full max-w-3xl mt-10 bg-white rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.35)]',
    '<div class="w-full max-w-3xl mt-7 sm:mt-8 bg-white rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.35)]'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Hero position fine-tuned slightly higher!")
