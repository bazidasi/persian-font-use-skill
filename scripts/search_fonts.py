#!/usr/bin/env python3
"""
Persian Font Use Skill - Search & Query Script
Usage: python3 scripts/search_fonts.py "query" [options]
"""

import csv
import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class Font:
    id: str
    name: str
    css_name: str
    category: str
    subcategory: str
    style: str
    popularity: int
    status: str
    description: str
    weights: str
    variable_font: bool
    variable_name: str
    weight_range: str
    latin_support: bool
    latin_source: str
    arabic_support: bool
    farsi_digits: bool
    farsi_digits_variant: str
    best_for: str
    sources_google_fonts: str
    sources_github: str
    sources_cdn: str
    sources_other: str
    license: str
    commercial_free: bool
    notes: str


class FontDatabase:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.fonts: List[Font] = []
        self._load_fonts()

    def _load_fonts(self):
        fonts_path = self.data_dir / "fonts.csv"
        if not fonts_path.exists():
            print(f"Error: {fonts_path} not found", file=sys.stderr)
            return

        with open(fonts_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                font = Font(
                    id=row['id'],
                    name=row['name'],
                    css_name=row['css_name'],
                    category=row['category'],
                    subcategory=row['subcategory'],
                    style=row['style'],
                    popularity=int(row['popularity']) if row['popularity'] else 0,
                    status=row['status'],
                    description=row['description'],
                    weights=row['weights'],
                    variable_font=row['variable_font'].lower() == 'true',
                    variable_name=row['variable_name'],
                    weight_range=row['weight_range'],
                    latin_support=row['latin_support'].lower() == 'true',
                    latin_source=row['latin_source'],
                    arabic_support=row['arabic_support'].lower() == 'true',
                    farsi_digits=row['farsi_digits'].lower() == 'true',
                    farsi_digits_variant=row['farsi_digits_variant'],
                    best_for=row['best_for'],
                    sources_google_fonts=row['sources_google_fonts'],
                    sources_github=row['sources_github'],
                    sources_cdn=row['sources_cdn'],
                    sources_other=row['sources_other'],
                    license=row['license'],
                    commercial_free=row['commercial_free'].lower() == 'true',
                    notes=row['notes']
                )
                self.fonts.append(font)

    def search(self, query: str, domain: Optional[str] = None, limit: int = 10) -> List[Font]:
        """Search fonts using text matching"""
        query_lower = query.lower()
        results = []

        for font in self.fonts:
            if domain == "font" and query_lower not in font.name.lower() and query_lower not in font.css_name.lower():
                continue
            if domain == "category" and query_lower not in font.category.lower() and query_lower not in font.subcategory.lower():
                continue
            if domain == "license" and query_lower not in font.license.lower():
                continue

            score = 0
            searchable = f"{font.name} {font.css_name} {font.category} {font.subcategory} {font.style} {font.description} {font.best_for}".lower()

            for term in query_lower.split():
                if term in searchable:
                    score += 1
                if term in font.name.lower():
                    score += 3
                if term in font.category.lower():
                    score += 2

            if score > 0:
                results.append((score, font))

        results.sort(key=lambda x: (-x[0], -x[1].popularity))
        return [f for _, f in results[:limit]]

    def get_by_id(self, font_id: str) -> Optional[Font]:
        for font in self.fonts:
            if font.id == font_id:
                return font
        return None

    def get_by_category(self, category: str) -> List[Font]:
        return [f for f in self.fonts if f.category.lower() == category.lower()]

    def get_variable_fonts(self) -> List[Font]:
        return [f for f in self.fonts if f.variable_font]

    def get_commercial_free(self) -> List[Font]:
        return [f for f in self.fonts if f.commercial_free]

    def get_bilingual(self) -> List[Font]:
        return [f for f in self.fonts if f.latin_support and f.arabic_support]


def format_font(font: Font, verbose: bool = False) -> str:
    """Format a font for display"""
    vf = " ✓" if font.variable_font else ""
    cf = " ✓" if font.commercial_free else ""
    lines = [
        f"  {font.name} ({font.css_name}){vf}{cf}",
        f"    Category: {font.category} / {font.subcategory}",
        f"    Style: {font.style}",
        f"    Weights: {font.weights} {'(Variable: ' + font.weight_range + ')' if font.variable_font else ''}",
        f"    Popularity: {'★' * font.popularity}",
        f"    Status: {font.status}",
        f"    License: {font.license} {'(Commercial Free)' if font.commercial_free else '(Paid/Restricted)'}",
        f"    Latin: {font.latin_source if font.latin_support else 'No'} | Arabic: {'Yes' if font.arabic_support else 'No'} | Farsi Digits: {'Yes' if font.farsi_digits else 'No'}",
        f"    Best for: {font.best_for}",
    ]

    if verbose:
        lines.extend([
            f"    Description: {font.description}",
            f"    Sources:",
            f"      Google Fonts: {font.sources_google_fonts or 'N/A'}",
            f"      GitHub: {font.sources_github or 'N/A'}",
            f"      CDN: {font.sources_cdn or 'N/A'}",
            f"      Other: {font.sources_other or 'N/A'}",
            f"    Notes: {font.notes}",
        ])

    return "\n".join(lines)


def format_design_system(font: Font, project_name: str = "MyProject") -> str:
    """Generate a design system recommendation for a font"""
    return f"""╔═══════════════════════════════════════════════════════════════════════════════╗
║  DESIGN SYSTEM RECOMMENDATION: {project_name.upper():<40} ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  PRIMARY FONT: {font.name} ({font.css_name}){" " * (40 - len(font.name) - len(font.css_name))}║
║  Category: {font.category} / {font.subcategory:<50}║
║  Style: {font.style:<62}║
║                                                                              ║
║  WEIGHTS: {font.weights} {'(Variable: ' + font.weight_range + ')' if font.variable_font else ''}║
║  LICENSE: {font.license} {'(Commercial Free ✓)' if font.commercial_free else '(⚠️ Check License)'}║
║                                                                              ║
║  RECOMMENDED USAGE:                                                          ║
║  {'  • ' + chr(10).join('  • '.join(font.best_for.split(';'))).ljust(60)} ║
║                                                                              ║
║  FONT STACKS:                                                                ║
║  UI/Body:    '{font.css_name}', {font.css_name.lower().replace(' ', '-') if font.variable_font else ('Vazirmatn' if font.category == 'Sans-Serif' else 'Amiri')}, system-ui, sans-serif║
║  Heading:    '{font.css_name if font.category == 'Display' else 'Lalezar'}, {font.css_name}', sans-serif║
║  Reading:    'Amiri', 'Markazi Text', 'Noto Naskh Arabic', serif║
║  Bilingual:  '{font.css_name}', 'Estedad', 'Noto Sans Arabic', 'Roboto', sans-serif║
║                                                                              ║
║  IMPLEMENTATION:                                                             ║
║  Google Fonts: <link href="{font.sources_google_fonts or 'https://fonts.googleapis.com/css2?family=' + font.css_name + ':wght@100..900&display=swap'}" rel="stylesheet">║
║  Self-hosted: @font-face {{ font-family: '{font.css_name}'; src: url('/fonts/{font.variable_name or font.css_name + '-VF'}.woff2') format('woff2-variations'); font-weight: {font.weight_range if font.variable_font else '400'}; font-display: swap; }}║
║                                                                              ║
║  PRE-DELIVERY CHECKLIST:                                                     ║
║  [ ] font-display: swap on all @font-face                                    ║
║  [ ] preconnect to fonts.gstatic.com (if using Google Fonts)                 ║
║  [ ] WOFF2 format only                                                       ║
║  [ ] Variable font used when >2 weights needed                               ║
║  [ ] OFL.txt included if self-hosting OFL fonts                              ║
║  [ ] RTL lang="fa" dir="rtl" on html element                                 ║
║  [ ] Fallback fonts specified                                                ║
║                                                                              ║
╚═══════════════════════════════════════════════════════════════════════════════╝"""


def main():
    parser = argparse.ArgumentParser(description="Search Persian Font Database")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--domain", choices=["font", "category", "license", "style", "use-case"],
                        help="Search domain")
    parser.add_argument("--limit", type=int, default=10, help="Max results")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--design-system", "-d", help="Generate design system for font ID")
    parser.add_argument("--project", "-p", default="MyProject", help="Project name for design system")
    parser.add_argument("--list-categories", action="store_true", help="List all categories")
    parser.add_argument("--list-variable", action="store_true", help="List variable fonts")
    parser.add_argument("--list-commercial-free", action="store_true", help="List commercial-free fonts")
    parser.add_argument("--list-bilingual", action="store_true", help="List bilingual fonts")

    args = parser.parse_args()

    data_dir = Path(__file__).parent.parent / "data"
    db = FontDatabase(data_dir)

    if not db.fonts:
        print("Error: No fonts loaded", file=sys.stderr)
        return 1

    # Special list commands
    if args.list_categories:
        categories = {}
        for f in db.fonts:
            cat = f.category
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(f)
        for cat, fonts in sorted(categories.items()):
            print(f"{cat}: {len(fonts)} fonts")
            for f in fonts:
                print(f"  - {f.name} ({f.css_name})")
        return 0

    if args.list_variable:
        for f in db.get_variable_fonts():
            print(f"{f.name} ({f.css_name}) - {f.weight_range} - {f.license}")
        return 0

    if args.list_commercial_free:
        for f in db.get_commercial_free():
            print(f"{f.name} ({f.css_name}) - {f.license} - {f.category}")
        return 0

    if args.list_bilingual:
        for f in db.get_bilingual():
            print(f"{f.name} ({f.css_name}) - Latin: {f.latin_source} - {f.category}")
        return 0

    # Design system generation
    if args.design_system:
        font = db.get_by_id(args.design_system)
        if not font:
            print(f"Error: Font '{args.design_system}' not found", file=sys.stderr)
            return 1
        print(format_design_system(font, args.project))
        return 0

    # Search
    if not args.query:
        parser.print_help()
        return 1

    results = db.search(args.query, args.domain, args.limit)

    if not results:
        print(f"No results for '{args.query}'")
        return 0

    if args.json:
        print(json.dumps([asdict(f) for f in results], indent=2, ensure_ascii=False))
    else:
        print(f"Found {len(results)} result(s) for '{args.query}':\n")
        for font in results:
            print(format_font(font, args.verbose))
            print()

    return 0


if __name__ == "__main__":
    sys.exit(main())