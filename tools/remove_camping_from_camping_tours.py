import re

files_to_clean = [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/bardia-nuit-sauvage.astro',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/bardia-babai-camping.astro'
]

for fpath in files_to_clean:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the camping option card
    content = re.sub(
        r'\s*<!-- Option Camping Sauvage au Cœur du Parc de Bardia.*?</div>\s*</div>\s*(?=</div>\s*</section>)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove the toggleCampingOption script
    content = re.sub(
        r'\s*<script is:inline>\s*var baseTourPrice =.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove any extra badge element from sidebar
    content = re.sub(
        r'\s*<!-- Notification Badge: Option Camping incluse -->\s*<div id="camping-included-badge".*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Cleaned camping option from: {fpath}")

