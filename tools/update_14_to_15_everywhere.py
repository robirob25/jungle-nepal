import os, re

files_updated = 0
total_replacements = 0

for root, dirs, files in os.walk('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src'):
    for fname in files:
        if fname.endswith(('.astro', '.html', '.json', '.js', '.ts')):
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content
            
            # French replacements
            content = re.sub(r'\bTous les 14 séjours\b', 'Tous les 15 séjours', content)
            content = re.sub(r'\bTous les 14 circuits\b', 'Tous les 15 circuits', content)
            content = re.sub(r'\bNos 14 Séjours\b', 'Nos 15 Séjours', content)
            content = re.sub(r'\bNos 14 séjours\b', 'Nos 15 séjours', content)
            content = re.sub(r'\bNos 14 circuits\b', 'Nos 15 circuits', content)
            content = re.sub(r'\bVoir les 14 séjours\b', 'Voir les 15 séjours', content)
            content = re.sub(r'\bVoir les 14 circuits\b', 'Voir les 15 circuits', content)
            content = re.sub(r'\b14 séjours d\'exception\b', '15 séjours d\'exception', content)
            content = re.sub(r'\b14 circuits d\'exception\b', '15 circuits d\'exception', content)
            content = re.sub(r'\b14 voyages au Népal\b', '15 voyages au Népal', content)
            content = re.sub(r'\b14 séjours au Népal\b', '15 séjours au Népal', content)

            # English replacements
            content = re.sub(r'\bAll 14 Expeditions\b', 'All 15 Expeditions', content)
            content = re.sub(r'\bAll 14 expeditions\b', 'All 15 expeditions', content)
            content = re.sub(r'\bAll 14 Tours\b', 'All 15 Tours', content)
            content = re.sub(r'\bAll 14 tours\b', 'All 15 tours', content)
            content = re.sub(r'\bAll 14 Trips\b', 'All 15 Trips', content)
            content = re.sub(r'\bAll 14 trips\b', 'All 15 trips', content)
            content = re.sub(r'\bOur 14 Expeditions\b', 'Our 15 Expeditions', content)
            content = re.sub(r'\bOur 14 expeditions\b', 'Our 15 expeditions', content)
            content = re.sub(r'\bView all 14 trips\b', 'View all 15 trips', content)
            content = re.sub(r'\bView all 14 expeditions\b', 'View all 15 expeditions', content)
            content = re.sub(r'\bView all 14 tours\b', 'View all 15 tours', content)
            content = re.sub(r'\bExplore all 14 expeditions\b', 'Explore all 15 expeditions', content)
            content = re.sub(r'\b14 exceptional tours\b', '15 exceptional tours', content)
            content = re.sub(r'\b14 exceptional trips\b', '15 exceptional trips', content)
            content = re.sub(r'\b14 exceptional expeditions\b', '15 exceptional expeditions', content)

            # Meta / Description
            content = re.sub(r'\b14 séjours\b', '15 séjours', content)

            if content != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_updated += 1

print(f"Updated {files_updated} files to '15 séjours / 15 expeditions' across the entire repository!")
