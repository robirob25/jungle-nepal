import os
import re
import urllib.parse

exact_google_url = "https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxK2MDA0NLY0MLYwNjUxMzMwMzMy3sDI-IpR2qs0Lz0nVcEvtSAxR8ExpSw1r6S0KFXBsSyzeBErPlkAWhIrKFYAAAA&rldimm=8011390383546606623&tbm=lcl&hl=fr-FR&sa=X&ved=2ahUKEwjW85Pw0bGWAxVfTaQEHX8wKpkQ9fQKegQIERAG&biw=1470&bih=798&dpr=2#lkt=LocalPoiReviews"

# 1. Overwrite review section in index.html precisely
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

real_reviews_section = f"""  <!-- ========================================================================= -->
  <!-- 9. SECTION AVIS GOOGLE VÉRIFIÉS (Avis Réels Verbatim) -->
  <!-- ========================================================================= -->
  <section id="avis" class="py-24 bg-safari-100/70 border-t border-slate-200 relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-16">
        <a href="{exact_google_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white border border-slate-200 shadow-sm text-xs font-black text-slate-900 mb-4 hover:border-[#0e8354] transition-colors">
          <span class="flex text-[#00b67a] text-sm">★★★★★</span>
          <span>Avis Google vérifiés • 5.0 / 5</span>
        </a>
        <h2 class="font-black text-3xl sm:text-5xl text-slate-950 tracking-tight leading-tight">
          Ce que disent nos voyageurs.
        </h2>
        <p class="mt-3 text-slate-600 text-sm sm:text-base font-normal">
          Note globale <strong>5.0 / 5</strong> basée sur les retours d'expérience vérifiés • 100% d'avis 5 étoiles ⭐
        </p>
      </div>

      <!-- Real Verbatim Review Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8">
        
        <!-- AVIS 1 : Adrien Noat -->
        <article class="bg-white rounded-3xl p-7 sm:p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div class="flex text-[#00b67a] text-base tracking-wider">★★★★★</div>
              <span class="text-[11px] font-bold text-slate-400 bg-slate-100 px-2.5 py-1 rounded-full flex items-center gap-1">
                <i data-lucide="check" class="w-3 h-3 text-[#00b67a]"></i> Avis Google
              </span>
            </div>
            <p class="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal italic">
              « Je reviens de 15 jours au Népal avec Jungle Nepal Adventure, et ce que je retiens avant tout, c’est l’humain. Au-delà des paysages, de la faune incroyable et des lieux traversés, il y a surtout une équipe profondément bienveillante, sincère et passionnée. On ne se sent jamais comme un simple client, mais réellement accompagné. Que ce soit à Chitwan, Bardia ou Katmandou, tout était pensé avec attention, sans jamais donner l’impression de quelque chose de formaté. Une expérience rare, que je recommande sincèrement ! »
            </p>
          </div>
          <div class="mt-6 pt-5 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-emerald-700 text-white font-black text-xs flex items-center justify-center shadow-sm">
              AN
            </div>
            <div>
              <p class="font-extrabold text-sm text-slate-900 leading-none">Adrien Noat</p>
              <p class="text-[11px] text-slate-500 mt-1">Voyageur vérifié • Circuit 15 jours</p>
            </div>
          </div>
        </article>

        <!-- AVIS 2 : Jean Tramoy -->
        <article class="bg-white rounded-3xl p-7 sm:p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div class="flex text-[#00b67a] text-base tracking-wider">★★★★★</div>
              <span class="text-[11px] font-bold text-slate-400 bg-slate-100 px-2.5 py-1 rounded-full flex items-center gap-1">
                <i data-lucide="check" class="w-3 h-3 text-[#00b67a]"></i> Avis Google
              </span>
            </div>
            <p class="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal italic">
              « Un voyage absolument inoubliable au Népal ! Bien plus qu’un simple séjour, c’est une véritable expérience humaine que j’ai vécue. Tout était parfaitement organisé du début à la fin. L’équipe est tout simplement exceptionnelle : disponible, bienveillante, à l’écoute et toujours prête à s’adapter. Les paysages sont à couper le souffle, entre montagnes majestueuses, jungle et villages authentiques. Un immense merci à toute l’équipe pour cette aventure hors du commun. Je recommande les yeux fermés ! 🙏 »
            </p>
          </div>
          <div class="mt-6 pt-5 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-slate-900 text-white font-black text-xs flex items-center justify-center shadow-sm">
              JT
            </div>
            <div>
              <p class="font-extrabold text-sm text-slate-900 leading-none">Jean Tramoy</p>
              <p class="text-[11px] text-slate-500 mt-1">Voyageur vérifié • Immersion Népal</p>
            </div>
          </div>
        </article>

        <!-- AVIS 3 : Alice Palasti -->
        <article class="bg-white rounded-3xl p-7 sm:p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div class="flex text-[#00b67a] text-base tracking-wider">★★★★★</div>
              <span class="text-[11px] font-bold text-slate-400 bg-slate-100 px-2.5 py-1 rounded-full flex items-center gap-1">
                <i data-lucide="check" class="w-3 h-3 text-[#00b67a]"></i> Avis Google
              </span>
            </div>
            <p class="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal italic">
              « Un voyage au Népal qui restera gravé à vie. Ce fut une expérience profondément humaine et pleine d'amour qui m'a ramenée à l'essentiel. Les paysages en montagne sont à couper le souffle. Séjourner chez l'habitant au milieu de la jungle de Bardia est une expérience hors du commun, sincèrement à vivre !! Merci à toute l'équipe, et surtout Agathe et Robin les organisateurs qui nous ont guidés avec tant de cœur et de soin pour vivre tout cela ! »
            </p>
          </div>
          <div class="mt-6 pt-5 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-amber-700 text-white font-black text-xs flex items-center justify-center shadow-sm">
              AP
            </div>
            <div>
              <p class="font-extrabold text-sm text-slate-900 leading-none">Alice Palasti</p>
              <p class="text-[11px] text-slate-500 mt-1">Voyageuse vérifiée • Jungle de Bardia</p>
            </div>
          </div>
        </article>

      </div>

      <!-- Second Row of Authentic Reviews -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 mt-6">
        
        <!-- AVIS 4 : Samantha Gonthier -->
        <article class="bg-white rounded-3xl p-7 sm:p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div class="flex text-[#00b67a] text-base tracking-wider">★★★★★</div>
              <span class="text-[11px] font-bold text-slate-400 bg-slate-100 px-2.5 py-1 rounded-full flex items-center gap-1">
                <i data-lucide="check" class="w-3 h-3 text-[#00b67a]"></i> Avis Google
              </span>
            </div>
            <p class="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal italic">
              « Choisir Jungle Nepal Adventure pour découvrir ce pays connu surtout pour ses montagnes, c'est la meilleure option pour l'apprécier sous un autre angle, celui de sa vie sauvage. J'ai vécu tant de moments uniques et incroyablement marquants grâce à l'équipe. J'ai été accompagnée tout au long de mon séjour par des personnes aussi bienveillantes que passionnées. »
            </p>
          </div>
          <div class="mt-6 pt-5 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-emerald-800 text-white font-black text-xs flex items-center justify-center shadow-sm">
              SG
            </div>
            <div>
              <p class="font-extrabold text-sm text-slate-900 leading-none">Samantha Gonthier</p>
              <p class="text-[11px] text-slate-500 mt-1">Voyageuse vérifiée • Vie sauvage</p>
            </div>
          </div>
        </article>

        <!-- AVIS 5 : Justine Luçon -->
        <article class="bg-white rounded-3xl p-7 sm:p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div class="flex text-[#00b67a] text-base tracking-wider">★★★★★</div>
              <span class="text-[11px] font-bold text-slate-400 bg-slate-100 px-2.5 py-1 rounded-full flex items-center gap-1">
                <i data-lucide="check" class="w-3 h-3 text-[#00b67a]"></i> Avis Google
              </span>
            </div>
            <p class="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal italic">
              « Le Népal a été bien plus qu’un voyage. Une expérience humaine profonde, riche en émotions, en amour et en découvertes. Un immense merci à toute l’équipe qui a organisé ce séjour : sans eux, rien de tout cela n’aurait été possible. Grâce à leur engagement, nous avons vécu chez l’habitant, partagé le quotidien local. On ne revient pas du Népal comme on est parti. »
            </p>
          </div>
          <div class="mt-6 pt-5 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-indigo-800 text-white font-black text-xs flex items-center justify-center shadow-sm">
              JL
            </div>
            <div>
              <p class="font-extrabold text-sm text-slate-900 leading-none">Justine Luçon</p>
              <p class="text-[11px] text-slate-500 mt-1">Voyageuse vérifiée • Immersion locale</p>
            </div>
          </div>
        </article>

        <!-- AVIS 6 : Max Schlautmann -->
        <article class="bg-white rounded-3xl p-7 sm:p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div class="flex text-[#00b67a] text-base tracking-wider">★★★★★</div>
              <span class="text-[11px] font-bold text-slate-400 bg-slate-100 px-2.5 py-1 rounded-full flex items-center gap-1">
                <i data-lucide="check" class="w-3 h-3 text-[#00b67a]"></i> Avis Google
              </span>
            </div>
            <p class="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal italic">
              « We had a 3-day safari adventure with our guide, Pawan, and it was truly one of the most memorable experiences of our lives. We were lucky to see one-horned rhinos, Asian elephants, Bengal tigers, and leopards. Bardia National Park feels truly wild and untouched. A special thank you to Pawan for his knowledge and patience! »
            </p>
          </div>
          <div class="mt-6 pt-5 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-teal-800 text-white font-black text-xs flex items-center justify-center shadow-sm">
              MS
            </div>
            <div>
              <p class="font-extrabold text-sm text-slate-900 leading-none">Max Schlautmann</p>
              <p class="text-[11px] text-slate-500 mt-1">Voyageur vérifié • Safari Bardia</p>
            </div>
          </div>
        </article>

      </div>

      <!-- Direct Link to Google Reviews -->
      <div class="mt-12 text-center">
        <a href="{exact_google_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-8 py-4 rounded-full bg-white hover:bg-slate-50 text-slate-900 font-extrabold text-xs sm:text-sm border border-slate-300 shadow-md hover:border-[#0e8354] hover:shadow-lg transition-all duration-300 hover:scale-105 active:scale-95">
          <span class="w-2.5 h-2.5 rounded-full bg-[#00b67a] animate-pulse"></span>
          <span>Consulter tous les 19 avis vérifiés sur Google (5.0 / 5)</span>
          <i data-lucide="external-link" class="w-4 h-4 text-slate-400"></i>
        </a>
      </div>

    </div>
  </section>"""

# Replace the review section with regex
html = re.sub(r'<section id=\"avis\".*?</section>', real_reviews_section, html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Overwrote review section in index.html successfully!")

# 2. Comprehensive Link Audit across all files
base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'
all_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            all_files.append(os.path.join(root, f))

print(f"Auditing links across {len(all_files)} HTML files...")

broken_links = []
total_links = 0

for file_path in all_files:
    rel_file = os.path.relpath(file_path, base_dir)
    file_dir = os.path.dirname(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check all hrefs
    hrefs = re.findall(r'href=[\"\']([^\"\']+)[\"\']', content)
    for h in hrefs:
        total_links += 1
        # Skip external, anchor, mailto, tel
        if h.startswith(('http://', 'https://', 'mailto:', 'tel:', '#', 'javascript:')):
            continue
        
        # Parse path without query/hash
        clean_path = h.split('?')[0].split('#')[0]
        if not clean_path:
            continue
        
        # Check resolved path
        resolved = os.path.normpath(os.path.join(file_dir, clean_path))
        if not os.path.exists(resolved):
            broken_links.append((rel_file, h, resolved))

print(f"Total links audited: {total_links}")
if broken_links:
    print(f"Found {len(broken_links)} broken links:")
    for src, href, res in broken_links:
        print(f"  In {src}: href='{href}' -> NOT FOUND: {res}")
else:
    print("ALL INTERNAL LINKS ARE 100% VALID!")

