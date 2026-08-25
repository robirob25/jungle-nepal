with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/index.html', 'r', encoding='utf-8') as f:
    fr = f.read()

from translate_and_generate_en_site import translate_html_content, make_globe_dropdown
import re

en = translate_html_content(fr, rel_depth=2)
en = en.replace('src="../assets/', 'src="../../assets/')
globe_en = make_globe_dropdown(is_english=True, rel_depth=2)
en = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', globe_en, en, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/destinations/index.html', 'w', encoding='utf-8') as f:
    f.write(en)

print("Regenerated en/destinations/index.html cleanly!")
