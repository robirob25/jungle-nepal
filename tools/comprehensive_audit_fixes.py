#!/usr/bin/env python3
import json
import glob
import re
import os

print("=== AUDITING & UPDATING ALL FILES FOR 15 -> 16 SÉJOURS ===")

replacements = [
    # French
    (r"Tous les 15 séjours", "Tous les 16 séjours"),
    (r"tous les 15 séjours", "tous les 16 séjours"),
    (r"Tous les 15 Séjours", "Tous les 16 Séjours"),
    (r"Nos 15 Séjours", "Nos 16 Séjours"),
    (r"nos 15 séjours", "nos 16 séjours"),
    (r"Nos 15 séjours", "Nos 16 séjours"),
    (r"les 15 séjours", "les 16 séjours"),
    (r"Les 15 séjours", "Les 16 séjours"),
    (r"15 séjours d'exception", "16 séjours d'exception"),
    (r"15 séjours d’exception", "16 séjours d’exception"),
    (r"15 séjours 2026/2027", "16 séjours 2026/2027"),
    (r"15 séjours et départs", "16 séjours et départs"),
    (r"15 séjours au Népal", "16 séjours au Népal"),
    (r"15 voyages", "16 voyages"),
    (r"15 départs", "16 départs"),
    
    # English
    (r"All 15 Expeditions", "All 16 Expeditions"),
    (r"all 15 Expeditions", "all 16 Expeditions"),
    (r"All 15 expeditions", "All 16 expeditions"),
    (r"all 15 expeditions", "all 16 expeditions"),
    (r"All 15 journeys", "All 16 journeys"),
    (r"all 15 journeys", "all 16 journeys"),
    (r"All 15 Journeys", "All 16 Journeys"),
    (r"All 15 Tours", "All 16 Tours"),
    (r"all 15 tours", "all 16 tours"),
    (r"All 15 tours", "All 16 tours"),
    (r"All 15 trips", "All 16 trips"),
    (r"all 15 trips", "all 16 trips"),
    (r"All 15 Trips", "All 16 Trips"),
    (r"all 15 guaranteed departures", "all 16 guaranteed departures"),
    (r"15 exclusive itineraries", "16 exclusive itineraries"),
    (r"15 exceptional journeys", "16 exceptional journeys")
]

all_files = []
for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith((".astro", ".ts", ".js", ".json", ".html")):
            all_files.append(os.path.join(root, file))

all_files.append("public/llms.txt")

count_files_modified = 0
for filepath in all_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    for pattern, repl in replacements:
        new_content = re.sub(pattern, repl, new_content)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count_files_modified += 1
        print(f"Updated: {filepath}")

print(f"Total files updated with 16 tours count: {count_files_modified}")
