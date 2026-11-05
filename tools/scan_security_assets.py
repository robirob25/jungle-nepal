import os, re

script_srcs = set()
fetch_urls = set()
iframes = set()
evals = set()

for root, dirs, files in os.walk('.'):
    if any(ign in root for ign in ['.git', 'node_modules', '.astro', 'dist']):
        continue
    for f in files:
        if f.endswith(('.astro', '.html', '.js', '.ts')):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                for s in re.findall(r'<script[^>]*src=[\'"]([^\'"]+)[\'"]', content, re.I):
                    script_srcs.add((s, p))
                for fu in re.findall(r'fetch\([\'"`]([^\'"`]+)[\'"`]', content, re.I):
                    fetch_urls.add((fu, p))
                for ifr in re.findall(r'<iframe[^>]*src=[\'"]([^\'"]+)[\'"]', content, re.I):
                    iframes.add((ifr, p))
                for ev in re.findall(r'(\beval\s*\(|\bdocument\.write\s*\(|\bfromCharCode\s*\(|\bwindow\.location\s*=)', content, re.I):
                    evals.add((ev, p))

print('=== SCRIPT SRCS ===')
for s, p in sorted(script_srcs):
    print(f'{s}  ->  {p}')

print('\n=== FETCH URLS ===')
for fu, p in sorted(fetch_urls):
    print(f'{fu}  ->  {p}')

print('\n=== IFRAMES ===')
for ifr, p in sorted(iframes):
    print(f'{ifr}  ->  {p}')

print('\n=== DANGEROUS PATTERNS (eval, document.write, etc.) ===')
for ev, p in sorted(evals):
    print(f'{ev}  ->  {p}')
