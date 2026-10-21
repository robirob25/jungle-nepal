import json
import re

# Comprehensive emoji regex
EMOJI_RE = re.compile(r'[\U00010000-\U0010ffff\u2600-\u27bf\u2300-\u23ff\u2b50\u200d\ufe0f]')

def clean_html_content(content):
    # 1. Convert markdown bold **text** to <strong>text</strong>
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)

    # 2. Specific replacements for common emoji patterns in headings / cards
    replacements = [
        ('🥇 ', '1. '),
        ('🥈 ', '2. '),
        ('📌 En résumé :', 'En résumé :'),
        ('📌 En bref :', 'En bref :'),
        ('📌 Quick Summary:', 'Quick Summary:'),
        ('📌 At a Glance:', 'At a Glance:'),
        ('💡 Le Conseil Photo', 'Conseil photo'),
        ('💡 Nos formules', 'Nos formules'),
        ('💡 Nos séjours', 'Nos séjours'),
        ('💡 Le Saviez-Vous ?', 'Le saviez-vous ?'),
        ('💡 Field Photography Tip', 'Field Photography Tip'),
        ('💡 Recommended Post-Trek', 'Recommended Post-Trek'),
        ('💡 Field Observation Note', 'Field Observation Note'),
        ('💡 Our Recommended', 'Our Recommended'),
        ('💡 Connect Directly', 'Connect Directly'),
        ('💡 Ready to Embark', 'Ready to Embark'),
        ('💡 Our Signature', 'Our Signature'),
        ('💡 Our Premier', 'Our Premier'),
        ('💡 Envie d\'échanger', "Envie d'échanger"),
        ('💡 Prêt à partir', 'Prêt à partir'),
        ('💡 Les séjours', 'Les séjours'),
        ('🚐 Évitez les tracas', 'Évitez les tracas'),
        ('🚐 Skip Transfer Headaches', 'Skip Transfer Headaches'),
        ('🐘 Découvrez Chitwan', 'Découvrez Chitwan'),
        ('🐘 Experience Ethical', 'Experience Ethical'),
        ('🐘 Les Tuskers', 'Les Tuskers'),
        ('🐘 Bardia\'s Legendary', "Bardia's Legendary"),
        ('🌿 Notre escapade', 'Notre escapade'),
        ('🌿 Our Top Recommended', 'Our Top Recommended'),
        ('🌿 Octobre à novembre', 'Octobre à novembre'),
        ('🌿 October to November', 'October to November'),
        ('🌿 Can\'t Decide?', "Can't Decide?"),
        ('🏔️ Expéditions', 'Expéditions'),
        ('🏔️ Préparer votre', 'Préparer votre'),
        ('🐾 Pistage', 'Pistage'),
        ('🐾 Plan Your', 'Plan Your'),
        ('🔥 Mars à mai', 'Mars à mai'),
        ('🔥 March to May', 'March to May'),
        ('❄️ Décembre à février', 'Décembre à février'),
        ('❄️ December to February', 'December to February'),
        ('📷 Wildlife Photography', 'Wildlife Photography'),
        ('💶 Transparent Safari', 'Transparent Safari'),
        ('🚶 Book Your Walking', 'Book Your Walking'),
    ]
    for old, new in replacements:
        content = content.replace(old, new)

    # 3. Strip any remaining leading emoji in <h1-6> tags
    def clean_heading(m):
        tag_open = m.group(1)
        inner = m.group(2)
        tag_close = m.group(3)
        # Strip leading emojis and whitespace
        cleaned = EMOJI_RE.sub('', inner).strip()
        # Clean any double space resulting from removal
        cleaned = re.sub(r'^\s*[-–—:]\s*', '', cleaned)
        return f'{tag_open}{cleaned}{tag_close}'

    content = re.sub(r'(<h[1-6][^>]*>)(.*?)(</h[1-6]>)', clean_heading, content, flags=re.IGNORECASE)

    # 4. Strip any leading emoji in span or p with bold/extrabold styling
    def clean_span_p(m):
        tag_open = m.group(1)
        inner = m.group(2)
        tag_close = m.group(3)
        cleaned = EMOJI_RE.sub('', inner).strip()
        cleaned = re.sub(r'^\s*[-–—:]\s*', '', cleaned)
        return f'{tag_open}{cleaned}{tag_close}'

    content = re.sub(r'(<(?:span|p)[^>]*class=\"[^\"]*font-(?:extra)?bold[^\"]*\"[^>]*>)(.*?)(</(?:span|p)>)', clean_span_p, content, flags=re.IGNORECASE)

    # 5. Fix green CTA button text visibility by adding cta-btn-primary and !text-white
    # Look for: <a href="..." class="... bg-[#0e8354] ...">
    def fix_button(m):
        full_tag = m.group(0)
        if 'cta-btn-primary' not in full_tag:
            full_tag = full_tag.replace('class="', 'class="cta-btn-primary !text-white no-underline ')
        elif '!text-white' not in full_tag:
            full_tag = full_tag.replace('class="', 'class="!text-white no-underline ')
        return full_tag

    content = re.sub(r'<a\s+href=\"[^\"]*\"[^>]*bg-\[#0e8354\][^>]*>', fix_button, content)
    content = re.sub(r'<a\s+href=\"[^\"]*\"[^>]*bg-emerald-[0-9]+[^>]*>', fix_button, content)

    # Also make sure spans inside cta buttons are !text-white
    def fix_btn_spans(m):
        btn_block = m.group(0)
        btn_block = re.sub(r'<span>(.*?)</span>', r'<span class="!text-white">\1</span>', btn_block)
        return btn_block

    content = re.sub(r'<a\s+[^>]*cta-btn-primary[^>]*>[\s\S]*?</a>', fix_btn_spans, content)

    return content

# Clean both JSON databases
for lang, fpath in [('fr', 'src/data/blog_posts.json'), ('en', 'src/data/blog_posts.en.json')]:
    with open(fpath, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    modified_count = 0
    for p in posts:
        orig = p.get('content', '')
        cleaned = clean_html_content(orig)
        if orig != cleaned:
            p['content'] = cleaned
            modified_count += 1
            
        # Also clean title if it has an emoji
        if EMOJI_RE.search(p.get('title', '')):
            p['title'] = EMOJI_RE.sub('', p['title']).strip()
            modified_count += 1
        if p.get('seo_title') and EMOJI_RE.search(p['seo_title']):
            p['seo_title'] = EMOJI_RE.sub('', p['seo_title']).strip()
            modified_count += 1

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print(f'Successfully updated {fpath}: {modified_count}/{len(posts)} posts cleaned.')

# Also clean tools/articles_fr.py and tools/articles_en.py
for fpath in ['tools/articles_fr.py', 'tools/articles_en.py']:
    with open(fpath, 'r', encoding='utf-8') as f:
        py_content = f.read()

    cleaned_py = clean_html_content(py_content)
    # Also clean the emoji in python strings directly
    cleaned_py = cleaned_py.replace('📌 ', '').replace('💡 ', '')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(cleaned_py)
    print(f'Successfully updated {fpath}.')

