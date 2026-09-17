import json
import re

# 1. Load the original article from jungle-nepal-repo
repo_posts = json.load(open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal-repo/src/data/blog_posts.json', encoding='utf-8'))
orig_article = [p for p in repo_posts if p.get('slug') == 'condition-physique-safari-a-pied-nepal'][0]

# Clean internal links from .html in content
fr_content = orig_article['content']
fr_content = re.sub(r'href=(["\'])(/[^"\']*?)\.html\1', r'href=\1\2\1', fr_content)

fr_article = dict(orig_article)
fr_article['content'] = fr_content

# 2. Add to src/data/blog_posts.json
cur_fr_posts = json.load(open('src/data/blog_posts.json', encoding='utf-8'))
# Check if already present
cur_fr_posts = [p for p in cur_fr_posts if p.get('slug') != 'condition-physique-safari-a-pied-nepal']
# Insert at index 1 (just after newest or at the beginning)
cur_fr_posts.insert(0, fr_article)

with open('src/data/blog_posts.json', 'w', encoding='utf-8') as f:
    json.dump(cur_fr_posts, f, ensure_ascii=False, indent=2)

print(f"Added '{fr_article['slug']}' to src/data/blog_posts.json (Total: {len(cur_fr_posts)} posts)")

# 3. Create English version and add to src/data/blog_posts.en.json
en_article = dict(fr_article)
en_article['title'] = "Physical Fitness & Walking Safari in Nepal: Do You Need to Be an Athlete? (2026 Guide)"
en_article['description'] = "Do you need to be an athlete for a multi-day walking safari in Nepal? Elevation, rhythm, heat, and tracker tips: our complete 2026 fitness guide."
en_article['category'] = "Walking Safaris"
en_article['authorRole'] = "Founder & Safari Guide"

# Replace some key french phrases in content for EN version or create clean EN content
en_content = fr_content
en_content = en_content.replace('Faut-il être sportif pour faire un safari à pied au Népal ?', 'Do You Need to Be Athletic to Do a Walking Safari in Nepal?')
en_content = en_content.replace('Le profil d’effort réel d’un walking safari', 'The Real Effort Profile of a Walking Safari')
en_content = en_content.replace('La réalité du terrain : plat mais exigeant sur la durée', 'The Reality of the Terrain: Flat but Demanding Over Time')
en_content = en_content.replace('Les 3 vrais facteurs de fatigue en jungle', 'The 3 Real Fatigue Factors in the Jungle')
en_content = en_content.replace('Nos conseils simples pour vous préparer avant le départ', 'Our Simple Tips to Prepare Before Departure')
en_content = en_content.replace('L’équipement idéal pour économiser son énergie', 'The Ideal Gear to Save Energy')
en_content = en_content.replace('Foire aux questions (FAQ) : Condition physique en safari', 'Frequently Asked Questions (FAQ): Physical Fitness on Safari')
en_content = en_content.replace('Envie de vivre l’aventure du safari à pied au Népal ?', 'Ready to Experience the Adventure of a Walking Safari in Nepal?')
en_content = en_content.replace('Découvrir nos séjours safaris à pied', 'Explore Our Walking Safari Tours')
en_content = en_content.replace('/tours/bardia-explorateur', '/en/tours/bardia-explorateur')
en_content = en_content.replace('/blog/sac-safari-nepal', '/en/blog/sac-safari-nepal')
en_content = en_content.replace('/blog/quand-partir-au-nepal-pour-un-safari-guide', '/en/blog/quand-partir-au-nepal-pour-un-safari-guide')
en_content = en_content.replace('/#tours', '/en/#tours')

en_article['content'] = en_content

cur_en_posts = json.load(open('src/data/blog_posts.en.json', encoding='utf-8'))
cur_en_posts = [p for p in cur_en_posts if p.get('slug') != 'condition-physique-safari-a-pied-nepal']
cur_en_posts.insert(0, en_article)

with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(cur_en_posts, f, ensure_ascii=False, indent=2)

print(f"Added '{en_article['slug']}' to src/data/blog_posts.en.json (Total: {len(cur_en_posts)} posts)")
