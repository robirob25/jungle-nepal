import os
import re
import glob

def harmonize_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    is_en = '/en/' in filepath

    # 1. Schema.org reviewCount
    content = re.sub(r'("reviewCount":\s*)"?\d+"?', r'\g<1>"22"', content)
    content = re.sub(r"('reviewCount':\s*)'?\d+'?", r"\g<1>'22'", content)
    content = re.sub(r'("ratingValue":\s*)"?[0-9\.]+"?', r'\g<1>"5.0"', content)

    # 2. Hero and inline badges
    if is_en:
        # e.g. <span class="text-slate-500">(18 reviews)</span> -> (22 verified reviews)
        content = re.sub(r'\((\d+)\s+reviews\)', '(22 verified reviews)', content)
        content = re.sub(r'\((\d+)\s+verified reviews\)', '(22 verified reviews)', content)
        content = re.sub(r'5\.0\s*\(\d+\s+avis\)', '5.0 (22)', content)
        content = re.sub(r'5\.0\s*\(\d+\s+reviews\)', '5.0 (22)', content)
    else:
        # e.g. <span class="text-slate-500">(18 avis)</span> -> (22 avis vérifiés)
        content = re.sub(r'\((\d+)\s+avis\)', '(22 avis vérifiés)', content)
        content = re.sub(r'\((\d+)\s+avis vérifiés\)', '(22 avis vérifiés)', content)
        content = re.sub(r'5\.0\s*\(\d+\s+avis\)', '5.0 (22 avis vérifiés)', content)

    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

all_files = glob.glob('src/pages/**/*.astro', recursive=True)
count = 0
for f in all_files:
    if harmonize_file(f):
        count += 1

print(f"Harmonized {count} files to 22 verified reviews.")
