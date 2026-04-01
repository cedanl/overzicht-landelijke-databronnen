#!/usr/bin/env python3
"""
Parse README.md markdown tables into JSON for the GitHub Pages website.
Run: python3 scripts/parse_readme.py README.md docs/data.json
"""
import re
import json
import sys
from pathlib import Path


def extract_links(cell):
    """Extract all [text](url) links from a markdown cell."""
    return [
        {"tekst": m.group(1), "url": m.group(2)}
        for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', cell)
    ]


def plain_text(cell):
    """Strip markdown links, return plain text."""
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', cell).strip()


def parse_onderwijstype(cell):
    """Split 'HBO, WO' into ['HBO', 'WO']."""
    text = plain_text(cell)
    if not text:
        return []
    return [t.strip() for t in text.split(',') if t.strip()]


def parse_table(header_line, data_lines):
    """Parse a markdown table given the header line and subsequent data lines."""
    headers = [h.strip() for h in header_line.split('|')[1:-1]]
    rows = []
    for line in data_lines:
        if not line.strip().startswith('|'):
            break
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if len(cells) < len(headers):
            continue
        row = {headers[i]: cells[i] for i in range(len(headers))}
        rows.append(row)
    return rows


def normalize_row(row, categorie, sectie):
    """Normalize a raw table row to a consistent structure."""
    entry = {
        'leverancier': plain_text(row.get('Leverancier', '')),
        'bron': plain_text(row.get('Bron', '')),
        'onderwijstype': parse_onderwijstype(row.get('Onderwijstype', '')),
        'doel': plain_text(row.get('Doel', '')),
        'frequentie': plain_text(row.get('Frequentie', '')),
        'categorie': categorie,
        'sectie': sectie,
        'documentatie': None,
        'repositories': [],
        'publieke_producten': [],
    }

    # Documentatie URL
    doc_cell = row.get('Documentatie URL', row.get('Documentatie', ''))
    doc_links = extract_links(doc_cell)
    if doc_links:
        entry['documentatie'] = doc_links[0]
    elif doc_cell.strip():
        entry['documentatie'] = {'tekst': 'Documentatie', 'url': doc_cell.strip()}

    # Repository links (CEDA or VusaVerse)
    repo_cell = row.get('CEDA repository', row.get('VusaVerse repository', ''))
    entry['repositories'] = extract_links(repo_cell)
    if not entry['repositories'] and repo_cell.strip():
        entry['repositories'] = [{'tekst': 'Repository', 'url': repo_cell.strip()}]

    # Publieke informatieproducten
    pub_cell = row.get('Publieke informatieproducten', '')
    entry['publieke_producten'] = extract_links(pub_cell)

    return entry


def parse_readme(filepath):
    """Parse all markdown tables from README.md into a list of bronnen."""
    content = Path(filepath).read_text(encoding='utf-8')
    lines = content.split('\n')

    bronnen = []
    current_section = None
    current_subsection = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # H1 section heading (skip main title)
        if re.match(r'^# [^#]', line):
            title = line[2:].strip()
            if title != 'Landelijke data bronnen':
                current_section = title
                current_subsection = None

        # H2 subsection heading (skip inhoudsopgave)
        elif re.match(r'^## ', line):
            subsection = line[3:].strip()
            if subsection != 'Inhoudsopgave':
                current_subsection = subsection

        # Table header row
        elif line.startswith('|') and 'Leverancier' in line:
            data_lines = []
            j = i + 2  # skip separator line
            while j < len(lines) and lines[j].strip().startswith('|'):
                data_lines.append(lines[j])
                j += 1

            rows = parse_table(line, data_lines)
            categorie = current_subsection or current_section

            for row in rows:
                entry = normalize_row(row, categorie, current_section)
                if entry['leverancier'] or entry['bron']:
                    bronnen.append(entry)

            i = j
            continue

        i += 1

    return bronnen


if __name__ == '__main__':
    readme = sys.argv[1] if len(sys.argv) > 1 else 'README.md'
    output = sys.argv[2] if len(sys.argv) > 2 else 'docs/data.json'

    Path(output).parent.mkdir(parents=True, exist_ok=True)
    bronnen = parse_readme(readme)
    Path(output).write_text(
        json.dumps(bronnen, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    print(f"Parsed {len(bronnen)} bronnen -> {output}")
