import re

for path in [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/index.html',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/destinations/index.html'
]:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace("""              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>
      </div>""", """              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>""")

    c = c.replace("""              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="../destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>
      </div>""", """              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="../destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>""")

    c = c.replace("""              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>
      </div>""", """              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>""")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

print("Fixed header tags in all index files!")
