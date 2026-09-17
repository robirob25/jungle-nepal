#!/usr/bin/env python3
import os
import re

BASE_DIR = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages"

def fix_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Calculate depth relative to src/
    rel_path = os.path.relpath(file_path, os.path.join(BASE_DIR, ".."))
    depth = len(rel_path.split(os.sep)) - 1
    import_prefix = "../" * depth

    # 1. Ensure getLocalizedPath is imported in Astro frontmatter
    if "getLocalizedPath" not in content:
        import_stmt = f"import {{ getLocalizedPath }} from '{import_prefix}i18n/utils';\n"
        if content.startswith("---"):
            content = content.replace("---", f"---\n{import_stmt}", 1)
        else:
            content = f"---\n{import_stmt}---\n" + content

    # 2. Ensure frTargetUrl and enTargetUrl variables are calculated
    if "frTargetUrl" not in content:
        calc_stmt = "const frTargetUrl = getLocalizedPath(Astro.url, 'fr');\nconst enTargetUrl = getLocalizedPath(Astro.url, 'en');\n"
        parts = content.split("---", 2)
        if len(parts) >= 3:
            parts[1] += f"\n{calc_stmt}"
            content = "---".join(parts)

    # 3. Replace hardcoded dropdown links or button onclick="changeLanguage(...)"
    # Replace buttons or static <a> tags with dynamic frTargetUrl and enTargetUrl
    
    # Desktop Globe Menu replacement
    content = re.sub(
        r'<a href="[^"]*"\s+class="[^"]*">\s*<span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>.*?\n\s*</a>',
        '<a href={frTargetUrl} class={`w-full flex items-center justify-between px-3 py-2 rounded-xl ${Astro.url.pathname.startsWith("/en") ? "text-slate-300 hover:bg-white/10 hover:text-white" : "bg-white/20 text-white font-extrabold"} transition-colors text-left cursor-pointer`}>\n              <span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>\n            </a>',
        content,
        flags=re.DOTALL
    )

    content = re.sub(
        r'<a href="[^"]*"\s+class="[^"]*">\s*<span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>.*?\n\s*</a>',
        '<a href={enTargetUrl} class={`w-full flex items-center justify-between px-3 py-2 rounded-xl ${Astro.url.pathname.startsWith("/en") ? "bg-white/20 text-white font-extrabold" : "text-slate-300 hover:bg-white/10 hover:text-white"} transition-colors text-left cursor-pointer`}>\n              <span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>\n            </a>',
        content,
        flags=re.DOTALL
    )

    # Replace <button onclick="changeLanguage('fr')"> ... </button>
    content = re.sub(
        r'<button\s+onclick="changeLanguage\(\'fr\'\)"[^>]*>.*?</button>',
        '<a href={frTargetUrl} class="py-2 px-3 rounded-xl text-xs font-extrabold flex items-center justify-center gap-1.5 bg-white/10 hover:bg-white/20 text-white transition-all cursor-pointer"><span>🇫🇷</span> <span>FR</span></a>',
        content,
        flags=re.DOTALL
    )

    # Replace <button onclick="changeLanguage('en')"> ... </button>
    content = re.sub(
        r'<button\s+onclick="changeLanguage\(\'en\'\)"[^>]*>.*?</button>',
        '<a href={enTargetUrl} class="py-2 px-3 rounded-xl text-xs font-extrabold flex items-center justify-center gap-1.5 bg-white/10 hover:bg-white/20 text-white transition-all cursor-pointer"><span>🇬🇧</span> <span>EN</span></a>',
        content,
        flags=re.DOTALL
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed language switcher in: {file_path}")

def main():
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".astro"):
                fix_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
