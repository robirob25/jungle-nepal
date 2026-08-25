import os
import re

base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'

replacements = [
    (r'\bacompte de 20\s*%', 'acompte de 30%'),
    (r'\bAcompte de 20\s*%', 'Acompte de 30%'),
    (r'\b20\s*%\s*d\'acompte', '30% d\'acompte'),
    (r'\b20\s*%\s*seulement', '30% seulement'),
    (r'\b20\s*%\s*deposit\b', '30% deposit'),
    (r'\bdeposit of 20\s*%', 'deposit of 30%'),
    (r'Acompte de 30%', 'Acompte de 30%'),
    (r'acompte de 30%', 'acompte de 30%'),
    (r'30% d’acompte', '30% d’acompte'),
    (r'Acompte de 30%', 'Acompte de 30 %'),
    (r'acompte de 30%', 'acompte de 30 %'),
    (r'30% à l’inscription', '30% à l’inscription'),
    (r'20% à l\'inscription', '30% à l\'inscription'),
    (r'30% à la réservation', '30% à la réservation'),
]

modified_files = []

for root, dirs, files in os.walk(base_dir):
    for fname in files:
        if fname.endswith(('.html', '.js', '.py', '.json', '.md')):
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            new_content = content
            for pat, repl in replacements:
                new_content = re.sub(pat, repl, new_content)

            if new_content != content:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_files.append(os.path.relpath(fpath, base_dir))

print(f"Updated {len(modified_files)} files to 30% deposit:")
for f in sorted(modified_files):
    print(f" - {f}")
