import json
import os
from tools.articles_fr import ARTICLES_FR
from tools.articles_en import ARTICLES_EN

# 1. Update FR
with open("src/data/blog_posts.json", "r", encoding="utf-8") as f:
    fr_posts = json.load(f)

existing_fr_slugs = {p["slug"] for p in fr_posts}
new_fr_posts = [p for p in ARTICLES_FR if p["slug"] not in existing_fr_slugs]
fr_posts = new_fr_posts + fr_posts

with open("src/data/blog_posts.json", "w", encoding="utf-8") as f:
    json.dump(fr_posts, f, ensure_ascii=False, indent=2)

print(f"FR posts: added {len(new_fr_posts)}, total is now {len(fr_posts)}")

# 2. Update EN
with open("src/data/blog_posts.en.json", "r", encoding="utf-8") as f:
    en_posts = json.load(f)

existing_en_slugs = {p["slug"] for p in en_posts}
new_en_posts = [p for p in ARTICLES_EN if p["slug"] not in existing_en_slugs]
en_posts = new_en_posts + en_posts

with open("src/data/blog_posts.en.json", "w", encoding="utf-8") as f:
    json.dump(en_posts, f, ensure_ascii=False, indent=2)

print(f"EN posts: added {len(new_en_posts)}, total is now {len(en_posts)}")
