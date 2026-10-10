import json
import re

def process_file(filepath, is_en=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        posts = json.load(f)

    # 1. Update featured images and content
    for p in posts:
        slug = p['slug']
        
        # Safari combiné Inde & Népal
        if slug == 'safari-combine-inde-nepal-corbett-dudhwa-suklaphanta-bardia':
            p['featuredImage'] = '/assets/drive_wildlife/Tigre_du_bengale_12.webp'
            print(f"[{'EN' if is_en else 'FR'}] Updated {slug} featuredImage -> /assets/drive_wildlife/Tigre_du_bengale_12.webp")

        # Safari Népal vs Inde
        elif slug == 'safari-nepal-ou-inde-comparatif-ranthambore-corbett-bardia':
            p['featuredImage'] = '/assets/drive_wildlife/Tigre_du_bengale_8.webp'
            if 'content' in p:
                p['content'] = p['content'].replace(
                    '/assets/curated_gallery/tigre_bengale_traversee_riviere.webp',
                    '/assets/drive_wildlife/Tigre_du_bengale_8.webp'
                )
            print(f"[{'EN' if is_en else 'FR'}] Updated {slug} featuredImage & content -> /assets/drive_wildlife/Tigre_du_bengale_8.webp")

        # Bardia post trek article: unique mountain cover + unique content tiger
        elif slug == 'comment-organiser-un-safari-a-bardia-apres-un-trek':
            p['featuredImage'] = '/assets/snow-leopard/annapurna_peaks.webp'
            if 'content' in p:
                p['content'] = p['content'].replace(
                    '/assets/curated_gallery/tigre_bengale_traversee_riviere.webp',
                    '/assets/drive_wildlife/Tigre_du_bengale_7.webp'
                )
            print(f"[{'EN' if is_en else 'FR'}] Updated {slug} featuredImage -> /assets/snow-leopard/annapurna_peaks.webp")

    # 2. Reorder so 'voir-des-tigres-au-nepal' is at index 0 (pinned flagship article)
    flagship_idx = next((i for i, p in enumerate(posts) if p['slug'] == 'voir-des-tigres-au-nepal'), None)
    if flagship_idx is not None and flagship_idx != 0:
        flagship_post = posts.pop(flagship_idx)
        posts.insert(0, flagship_post)
        print(f"[{'EN' if is_en else 'FR'}] Pinned 'voir-des-tigres-au-nepal' to index 0 (was at index {flagship_idx})")

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved {filepath}\n")

if __name__ == '__main__':
    process_file('src/data/blog_posts.json', is_en=False)
    process_file('src/data/blog_posts.en.json', is_en=True)
