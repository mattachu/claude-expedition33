#!/usr/bin/env python3
"""Generate scripts/scripts.md — a readable listing of all pipeline scripts."""

import os

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPTS_DIR, "scripts.md")

def main():
    py_files = sorted(
        f for f in os.listdir(SCRIPTS_DIR) if f.endswith(".py")
    )

    lines = ["# Pipeline Scripts\n", "\n"]
    for filename in py_files:
        filepath = os.path.join(SCRIPTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        lines.append(f"## {filename}\n\n")
        lines.append(f"```python\n{content}\n```\n\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Written: {OUTPUT_FILE} ({len(py_files)} scripts)")

if __name__ == "__main__":
    main()
