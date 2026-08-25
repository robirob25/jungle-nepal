import re, glob, os

# 1. Extract French cards
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    fr_index = f.read()

fr_cards_raw = re.findall(r'<article\s+class=\"[^\"]*trip-card[^\"]*\".*?</article>', fr_index, re.DOTALL)
fr_cards = {}
for a in fr_cards_raw:
    m = re.search(r'href=[\'\"]/tours/([^\'\"]+)\.html[\'\"]', a)
    if m:
        fr_cards[m.group(1)] = a

# 2. Extract English cards
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'r', encoding='utf-8') as f:
    en_index = f.read()

en_cards_raw = re.findall(r'<article\s+class=\"[^\"]*trip-card[^\"]*\".*?</article>', en_index, re.DOTALL)
en_cards = {}
for a in en_cards_raw:
    m = re.search(r'href=[\'\"]/en/tours/([^\'\"]+)\.html[\'\"]', a)
    if m:
        en_cards[m.group(1)] = a

# Related mapping
related_map = {
    "panthere-des-neiges": ["tiji-mustang", "nepal-sauvage", "rara-lake-bardia"],
    "tiji-mustang": ["panthere-des-neiges", "immersion-spirituelle", "carnet-de-voyage"],
    "bardia-explorateur": ["bardia-babai-camping", "babai-special", "chitwan-bardia-complete"],
    "bardia-babai-camping": ["babai-special", "jungle-extreme", "bardia-explorateur"],
    "babai-special": ["bardia-babai-camping", "bardia-nuit-sauvage", "chitwan-bardia-complete"],
    "bardia-nuit-sauvage": ["bardia-explorateur", "babai-special", "chitwan-culture"],
    "chitwan-culture": ["chitwan-bardia-complete", "bardia-explorateur", "nepal-immersion-totale"],
    "chitwan-bardia-complete": ["jungle-extreme", "nepal-immersion-totale", "rafting-safari"],
    "jungle-extreme": ["chitwan-bardia-complete", "rara-lake-bardia", "panthere-des-neiges"],
    "rafting-safari": ["nepal-immersion-totale", "chitwan-bardia-complete", "rara-lake-bardia"],
    "rara-lake-bardia": ["panthere-des-neiges", "rafting-safari", "nepal-sauvage"],
    "nepal-immersion-totale": ["chitwan-bardia-complete", "rafting-safari", "nepal-sauvage"],
    "nepal-sauvage": ["immersion-spirituelle", "carnet-de-voyage", "panthere-des-neiges"],
    "immersion-spirituelle": ["tiji-mustang", "carnet-de-voyage", "nepal-sauvage"],
    "carnet-de-voyage": ["immersion-spirituelle", "tiji-mustang", "nepal-sauvage"]
}

def inject_related(file_path, slug, is_en=False):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any existing related section
    content = re.sub(r'<!-- SECTION : AUTRES SÉJOURS.*?</section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- SECTION : DÉCOUVREZ AUSSI.*?</section>', '', content, flags=re.DOTALL)

    matching_slugs = related_map.get(slug, ["bardia-explorateur", "chitwan-bardia-complete", "tiji-mustang"])
    
    cards_pool = en_cards if is_en else fr_cards
    cards_html = []
    for s in matching_slugs:
        if s in cards_pool:
            cards_html.append(cards_pool[s])

    if not cards_html:
        print(f"Warning: No cards found for {slug} in {'EN' if is_en else 'FR'}")
        return

    cards_joined = '\n\n'.join(cards_html)

    if is_en:
        section_html = f"""
    <!-- SECTION : AUTRES SÉJOURS SIMILAIRES -->
    <section class="mt-20 pt-12 border-t border-slate-200">
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-8">
        <div>
          <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">Continue the adventure</span>
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight mt-1">You might also love these expeditions</h2>
        </div>
        <a href="/en/index.html#prochains-departs" class="inline-flex items-center gap-1.5 text-xs font-bold text-[#0e8354] hover:text-[#0c6d46] hover:underline">
          <span>Explore all 15 expeditions</span>
          <span>→</span>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
{cards_joined}
      </div>
    </section>
"""
    else:
        section_html = f"""
    <!-- SECTION : AUTRES SÉJOURS SIMILAIRES -->
    <section class="mt-20 pt-12 border-t border-slate-200">
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-8">
        <div>
          <span class="text-xs font-black uppercase tracking-widest text-[#0e8354]">Poursuivre l'exploration</span>
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight mt-1">Vous pourriez aussi aimer ces expéditions</h2>
        </div>
        <a href="/index.html#prochains-departs" class="inline-flex items-center gap-1.5 text-xs font-bold text-[#0e8354] hover:text-[#0c6d46] hover:underline">
          <span>Voir les 15 séjours au Népal</span>
          <span>→</span>
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
{cards_joined}
      </div>
    </section>
"""

    # Inject right before </main>
    if '</main>' in content:
        content = content.replace('</main>', section_html + '\n  </main>')
    else:
        print(f"Error: </main> not found in {file_path}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Injected 3 related tours into {os.path.basename(file_path)} ({'EN' if is_en else 'FR'})")

# Inject for all FR pages
for slug in related_map.keys():
    fr_path = f"/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/{slug}.astro"
    if os.path.exists(fr_path):
        inject_related(fr_path, slug, is_en=False)

# Inject for all EN pages
for slug in related_map.keys():
    en_path = f"/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/{slug}.astro"
    if os.path.exists(en_path):
        inject_related(en_path, slug, is_en=True)

print("Finished injecting related tours across all 30 tour pages!")
