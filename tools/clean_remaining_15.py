#!/usr/bin/env python3
import os
import re

patterns = [
    (r"\b15\s+séjours\b", "16 séjours"),
    (r"\b15\s+Séjours\b", "16 Séjours"),
    (r"\b15\s+expeditions\b", "16 expeditions"),
    (r"\b15\s+Expeditions\b", "16 Expeditions"),
    (r"\b15\s+tours\b", "16 tours"),
    (r"\b15\s+Tours\b", "16 Tours"),
    (r"\b15\s+trips\b", "16 trips"),
    (r"\b15\s+Trips\b", "16 Trips"),
    (r"\b15\s+journeys\b", "16 journeys"),
    (r"\b15\s+Journeys\b", "16 Journeys"),
    (r"\b15\s+voyages\b", "16 voyages"),
    (r"\b15\s+Voyages\b", "16 Voyages"),
]

all_files = []
for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith((".astro", ".ts", ".js", ".json", ".html")):
            all_files.append(os.path.join(root, file))

for filepath in all_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    for pat, rep in patterns:
        new_content = re.sub(pat, rep, new_content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Cleaned: {filepath}")

print("Cleaned all remaining 15s!")
