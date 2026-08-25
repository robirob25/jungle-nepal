import os, re, glob

src_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages'
astro_files = glob.glob(os.path.join(src_dir, '**/*.astro'), recursive=True)

print(f"Found {len(astro_files)} Astro pages to enrich with contextual internal links...")

# Let's inspect pages and enhance internal linking intelligently:

# 1. In Destination pages: add links to related tours in text, and reciprocal links
# 2. In Tour pages: add links to destination hubs, about page, and contact
# 3. In FAQ & Homepage narratives: add natural anchor links

enhanced_count = 0

for file_path in astro_files:
    rel = os.path.relpath(file_path, src_dir)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Enhancements for About Page
    if 'a-propos.astro' in rel:
        # Link Bardia mentions
        content = re.sub(r'(?<!>)(Parc National de Bardia)(?!</a>)', r'<a href="/destinations/bardia" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">Parc National de Bardia</a>', content, count=2)
        # Link Chitwan mentions
        content = re.sub(r'(?<!>)(Parc National de Chitwan)(?!</a>)', r'<a href="/destinations/chitwan" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">Parc National de Chitwan</a>', content, count=1)
        # Link circuits
        content = re.sub(r'(?<!>)(15 circuits et expéditions)(?!</a>)', r'<a href="/tours/carnet-de-voyage" class="text-amber-400 hover:text-amber-300 underline decoration-amber-500/30 underline-offset-2 transition-colors">15 circuits et expéditions</a>', content, count=1)

    # Enhancements for Destination Pages
    if 'destinations/' in rel:
        if 'bardia.astro' in rel:
            content = re.sub(r'(?<!>)(safaris à pied)(?!</a>)', r'<a href="/tours/bardia-explorateur" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">safaris à pied</a>', content, count=1)
            content = re.sub(r'(?<!>)(vallée secrète de la Babai)(?!</a>)', r'<a href="/tours/bardia-babai-camping" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">vallée secrète de la Babai</a>', content, count=1)
        if 'chitwan.astro' in rel:
            content = re.sub(r'(?<!>)(rhinocéros unicornes)(?!</a>)', r'<a href="/tours/chitwan-culture" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">rhinocéros unicornes</a>', content, count=1)
            content = re.sub(r'(?<!>)(combiner Chitwan et Bardia)(?!</a>)', r'<a href="/tours/chitwan-bardia-complete" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">combiner Chitwan et Bardia</a>', content, count=1)
        if 'suklaphanta.astro' in rel:
            content = re.sub(r'(?<!>)(grand chelem sauvage)(?!</a>)', r'<a href="/tours/nepal-sauvage" class="text-emerald-400 hover:text-emerald-300 underline decoration-emerald-500/30 underline-offset-2 transition-colors">grand chelem sauvage</a>', content, count=1)

    # Enhancements for Tour Pages
    if 'tours/' in rel:
        # In itinerary tabs or descriptions, link destination names to their destination guide
        content = re.sub(r'(?<![>/])(Parc National de Bardia)(?![<"a-zA-Z])', r'<a href="/destinations/bardia" class="text-emerald-400 hover:text-emerald-300 font-medium underline decoration-emerald-500/30 underline-offset-2 transition-colors">Parc National de Bardia</a>', content, count=1)
        content = re.sub(r'(?<![>/])(Parc National de Chitwan)(?![<"a-zA-Z])', r'<a href="/destinations/chitwan" class="text-emerald-400 hover:text-emerald-300 font-medium underline decoration-emerald-500/30 underline-offset-2 transition-colors">Parc National de Chitwan</a>', content, count=1)
        content = re.sub(r'(?<![>/])(vallée de Katmandou)(?![<"a-zA-Z])', r'<a href="/destinations/katmandou" class="text-emerald-400 hover:text-emerald-300 font-medium underline decoration-emerald-500/30 underline-offset-2 transition-colors">vallée de Katmandou</a>', content, count=1)

    if content != original_content:
        enhanced_count += 1
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Enhanced internal links in: {rel}")

print(f"\nInternal linking optimization applied to {enhanced_count} Astro template pages!")
