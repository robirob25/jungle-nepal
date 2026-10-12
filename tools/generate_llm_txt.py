# Generate /llms.txt and /llms-full.txt following strict llmstxt.org specification
import json, os

with open('public/llms.txt', 'r', encoding='utf-8') as f:
    llms_txt = f.read()

# Also generate public/llms-full.txt
with open('public/llms-full.txt', 'w', encoding='utf-8') as f:
    f.write(llms_txt)

print("Synchronized public/llms.txt and public/llms-full.txt according to llmstxt.org specification.")
