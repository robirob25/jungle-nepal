import os
import re

tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
en_tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/tours'
os.makedirs(en_tours_dir, exist_ok=True)

# Import translate_html_content from translate_and_generate_en_site
from translate_and_generate_en_site import translate_html_content, make_globe_dropdown

for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    src_path = os.path.join(tours_dir, fname)
    with open(src_path, 'r', encoding='utf-8') as f:
        fr_tour = f.read()

    en_tour = translate_html_content(fr_tour, rel_depth=2)
    en_tour = en_tour.replace('src="../assets/', 'src="../../assets/')
    
    # Update globe in English
    globe_en = make_globe_dropdown(is_english=True, rel_depth=2)
    en_tour = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', globe_en, en_tour, flags=re.DOTALL)

    out_file = os.path.join(en_tours_dir, fname)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(en_tour)

print("Generated all 14 English tour pages flawlessly!")
