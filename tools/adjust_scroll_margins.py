import re, glob, os

src_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages'
astro_files = glob.glob(os.path.join(src_dir, '**/*.astro'), recursive=True)

section_ids = [
    'pisteurs',
    'galerie-faune',
    'prochains-departs',
    'circuits',
    'concept',
    'avis',
    'faq',
    'histoire',
    'recit-terrain',
    'itineraire',
    'dates-prix',
    'inclus',
    'equipement',
    'guide',
    'carte',
    'infos-pratiques'
]

count = 0

for file_path in astro_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    for sid in section_ids:
        pattern = rf'(<(?:section|div)\s+[^>]*id=["\']{sid}["\'][^>]*class=["\'])([^"\']*)(["\'])'
        
        def repl(m):
            prefix = m.group(1)
            classes = m.group(2)
            suffix = m.group(3)
            classes_cleaned = re.sub(r'scroll-mt-\S+', '', classes).strip()
            new_classes = f"scroll-mt-16 sm:scroll-mt-20 {classes_cleaned}"
            return f"{prefix}{new_classes}{suffix}"

        content = re.sub(pattern, repl, content)

    if content != orig:
        count += 1
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated scroll offset in: {os.path.basename(file_path)}")

print(f"Total files updated: {count}")
