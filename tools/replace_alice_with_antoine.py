import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

alice_card_pattern = r'<!-- AVIS 3 : Alice Palasti -->.*?<!-- Second Row'

antoine_card = """<!-- AVIS 3 : Antoine -->
        <article class="bg-white rounded-3xl p-7 sm:p-8 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div class="flex text-[#00b67a] text-base tracking-wider">★★★★★</div>
              <span class="text-[11px] font-bold text-slate-400 bg-slate-100 px-2.5 py-1 rounded-full flex items-center gap-1">
                <i data-lucide="check" class="w-3 h-3 text-[#00b67a]"></i> Avis Google
              </span>
            </div>
            <p class="text-slate-700 text-xs sm:text-[13px] leading-relaxed font-normal italic">
              « Une expérience et une aventure humaine tout simplement exceptionnelles. Voir les tigres et les rhinocéros en liberté avec des pisteurs aussi passionnés que Pawan et Robin est un privilège rare. L'organisation, les rencontres et le respect de la nature étaient parfaits du premier au dernier jour. Je recommande à 100% ! »
            </p>
          </div>
          <div class="mt-6 pt-5 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-amber-700 text-white font-black text-xs flex items-center justify-center shadow-sm">
              AN
            </div>
            <div>
              <p class="font-extrabold text-sm text-slate-900 leading-none">Antoine</p>
              <p class="text-[11px] text-slate-500 mt-1">Voyageur vérifié • Expédition Népal</p>
            </div>
          </div>
        </article>

      </div>

      <!-- Second Row"""

html = re.sub(alice_card_pattern, antoine_card, html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced Alice with Antoine in index.html successfully!")
