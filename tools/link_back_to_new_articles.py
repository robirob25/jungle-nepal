import json

def update_posts(path, is_en=False):
    with open(path, 'r', encoding='utf-8') as f:
        posts = json.load(f)

    target_slug = "combiner-trek-et-safari-au-nepal-guide-complet"
    for p in posts:
        if p.get('slug') == target_slug:
            content = p.get('content', '')
            if "comment-organiser-un-safari-a-bardia-apres-un-trek" not in content:
                if not is_en:
                    addition = """
<div class="my-8 p-6 rounded-2xl bg-emerald-950/80 border border-emerald-500/30 text-white">
  <h3 class="text-lg font-bold text-emerald-300 mb-2">Guides pratiques d'organisation après votre trek :</h3>
  <p class="text-sm text-slate-200 mb-3">Vous terminez un trek aux Annapurnas, à l'Everest ou au Manaslu et cherchez la logistique détaillée (transports, lodges, budget) ?</p>
  <ul class="space-y-1.5 text-xs font-semibold text-emerald-200">
    <li>👉 <a href="/blog/comment-organiser-un-safari-a-bardia-apres-un-trek" class="underline hover:text-white">Comment organiser un safari à Bardia après un trek au Népal (avion, bus, faune sauvage)</a></li>
    <li>👉 <a href="/blog/comment-organiser-un-safari-a-chitwan-apres-un-trek" class="underline hover:text-white">Comment organiser un safari à Chitwan après un trek (liaison Pokhara, pirogue, rhinocéros)</a></li>
  </ul>
</div>
"""
                else:
                    addition = """
<div class="my-8 p-6 rounded-2xl bg-emerald-950/80 border border-emerald-500/30 text-white">
  <h3 class="text-lg font-bold text-emerald-300 mb-2">Practical post-trek extension guides:</h3>
  <p class="text-sm text-slate-200 mb-3">Wrapping up a trek in the Annapurnas, Everest, or Manaslu and looking for detailed logistics (transports, lodges, budgets)?</p>
  <ul class="space-y-1.5 text-xs font-semibold text-emerald-200">
    <li>👉 <a href="/en/blog/comment-organiser-un-safari-a-bardia-apres-un-trek" class="underline hover:text-white">How to organize a safari in Bardia after trekking in Nepal (flights, buses, wildlife)</a></li>
    <li>👉 <a href="/en/blog/comment-organiser-un-safari-a-chitwan-apres-un-trek" class="underline hover:text-white">How to organize a safari in Chitwan after trekking (Pokhara buses, river canoes, rhinos)</a></li>
  </ul>
</div>
"""
                p['content'] = content + addition
                print(f"Updated {path} post {target_slug} with cross-links!")

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

update_posts('src/data/blog_posts.json', is_en=False)
update_posts('src/data/blog_posts.en.json', is_en=True)
