#!/usr/bin/env python3
"""
Persian Font Use Skill - Search & Query Script
Similar to ui-ux-pro-max search.py but for Persian fonts.
"""

import csv
import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict


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


@dataclass
class LicenseInfo:
    font_id: str
    license_type: str
    license_name: str
    license_url: str
    commercial_use: bool
    modification: bool
    distribution: bool
    sell_font: bool
    attribution_required: bool
    notes: str


class FontDatabase:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.fonts: List[Font] = []
        self.licenses: Dict[str, LicenseInfo] = {}
        self._load_data()

    def _load_data(self):
        # Load fonts
        fonts_path = self.data_dir / "fonts.csv"
        if fonts_path.exists():
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

        # Load licenses
        license_path = self.data_dir / "licensing.csv"
        if license_path.exists():
            with open(license_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.licenses[row['font_id']] = LicenseInfo(
                        font_id=row['font_id'],
                        license_type=row['license_type'],
                        license_name=row['license_name'],
                        license_url=row['license_url'],
                        commercial_use=row['commercial_use'].lower() == 'true',
                        modification=row['modification'].lower() == 'true',
                        distribution=row['distribution'].lower() == 'true',
                        sell_font=row['sell_font'].lower() == 'true',
                        attribution_required=row['attribution_required'].lower() == 'true',
                        notes=row['notes']
                    )

    def search(self, query: str, domain: Optional[str] = None, limit: int = 10) -> List[Font]:
        """Search fonts using simple text matching"""
        query_lower = query.lower()
        results = []

        for font in self.fonts:
            score = 0
            searchable = f"{font.name} {font.css_name} {font.category} {font.subcategory} {font.style} {font.description} {font.best_for}".lower()

            # Simple scoring
            for term in query_lower.split():
                if term in searchable:
                    score += 1
                if term in font.name.lower():
                    score += 3
                if term in font.category.lower():
                    score += 2

            if score > 0:
                results.append((score, font))

        # Sort by score then popularity
        results.sort(key=lambda x: (-x[0], -x[1].popularity))
        return [f for _, f in results[:limit]]

    def get_by_id(self, font_id: str) -> Optional[Font]:
        for font in self.fonts:
            if font.id == font_id:
                return font
        return None

    def get_by_category(self, category: str) -> List[Font]:
        return [f for f in self.fonts if f.category.lower() == category.lower()]

    def get_by_license(self, license_type: str) -> List[Font]:
        if license_type == "OFL":
            return [f for f in self.fonts if f.license == "OFL" and f.commercial_free]
        elif license_type == "commercial":
            return [f for f in self.fonts if not f.commercial_free and f.license != "OFL"]
        elif license_type == "personal":
            return [f for f in self.fonts if f.license == "Personal" and not f.commercial_free]
        elif license_type == "free":
            return [f for f in self.fonts if f.commercial_free]
        return []

    def get_variable_fonts(self) -> List[Font]:
        return [f for f in self.fonts if f.variable_font]

    def get_bilingual_fonts(self) -> List[Font]:
        return [f for f in self.fonts if f.latin_support and f.arabic_support]

    def get_recommendations(self, use_case: str) -> List[Font]:
        """Get font recommendations based on use case"""
        use_case_lower = use_case.lower()
        recommendations = []

        # Map use cases to font IDs
        recommendations_map = {
            "ui": ["vazirmatn", "sahel", "estedad", "noto_sans_arabic", "baloo_bhaijaan_2"],
            "body": ["vazirmatn", "estedad", "sahel", "parastoo", "noto_sans_arabic"],
            "heading": ["lalezar", "noto_kufi_arabic", "titr", "baloo_bhaijaan_2"],
            "reading": ["amiri", "markazi_text", "noto_naskh_arabic", "tahrir", "gandom"],
            "quranic": ["amiri", "markazi_text", "tahrir"],
            "calligraphy": ["irannastaliq", "gulzar"],
            "legacy": ["nazanin", "lotus", "titr", "yekan"],
            "bilingual": ["vazirmatn", "estedad", "sahel", "noto_sans_arabic", "baloo_bhaijaan_2"],
            "variable": ["vazirmatn", "sahel", "estedad", "noto_sans_arabic", "noto_kufi_arabic", "baloo_bhaijaan_2"],
            "free": ["vazirmatn", "sahel", "estedad", "parastoo", "amiri", "lalezar", "noto_sans_arabic", "noto_naskh_arabic", "noto_kufi_arabic", "markazi_text", "gulzar", "baloo_bhaijaan_2", "iranian_sans"],
            "commercial": ["iransans", "tahrir"],
            "persian_digits": ["sahel", "vazirmatn", "iransans"],
        }

        # Find matching use case
        for key, font_ids in recommendations_map.items():
            if key in use_case_lower:
                for fid in font_ids:
                    font = self.get_by_id(fid)
                    if font:
                        recommendations.append(font)
                break

        # If no match, return top popular fonts
        if not recommendations:
            recommendations = sorted(self.fonts, key=lambda f: -f.popularity)[:5]

        return recommendations

    def generate_design_system(self, project_name: str, use_case: str) -> str:
        """Generate a design system recommendation like ui-ux-pro-max"""
        fonts = self.get_recommendations(use_case)

        # Categorize recommendations
        ui_fonts = [f for f in fonts if f.category == "Sans-Serif" and f.subcategory == "Modern UI"]
        heading_fonts = [f for f in fonts if f.category == "Display" or f.subcategory == "Kufi"]
        reading_fonts = [f for f in fonts if f.category == "Serif" or f.subcategory == "Naskh"]
        calligraphy_fonts = [f for f in fonts if f.subcategory == "Nasta'liq"]

        output = []
        output.append(f"+{'-' * 86}+")
        output.append(f"|  TARGET: {project_name.upper():<76} |")
        output.append(f"+{'-' * 86}+")
        output.append("|                                                                                        |")

        # Pattern recommendation
        patterns = {
            "ui": "App-Centric + Clean UI",
            "body": "Content-First + Readability",
            "heading": "Hero-Centric + Visual Impact",
            "reading": "Article-Centric + Long-form",
            "calligraphy": "Artistic-Centric + Cultural",
            "bilingual": "Multilingual + Harmonized",
        }
        pattern = patterns.get(use_case.lower(), "General Purpose")
        output.append(f"|  PATTERN: {pattern:<75} |")
        output.append("|                                                                                        |")

        # Style recommendation
        style_keywords = {
            "ui": "Modern, clean, geometric, screen-optimized",
            "body": "Readable, balanced, professional",
            "heading": "Bold, distinctive, cultural, display",
            "reading": "Traditional, calligraphic, elegant, Naskh",
            "calligraphy": "Flowing, artistic, Nasta'liq, poetic",
            "bilingual": "Harmonized, matched weights, consistent rhythm",
        }
        style = style_keywords.get(use_case.lower(), "Modern, clean, accessible")
        output.append(f"|  STYLE: {style:<75} |")
        output.append("|                                                                                        |")

        # Colors placeholder
        output.append(f"|  COLORS:                                                                               |")
        output.append(f"|     Primary:    #1E3A5F (Deep Persian Blue)                                            |")
        output.append(f"|     Secondary:  #C8A951 (Persian Gold)                                                 |")
        output.append(f"|     CTA:        #E86C00 (Saffron Orange)                                               |")
        output.append(f"|     Background: #FAFAFA (Warm White)                                                   |")
        output.append(f"|     Text:       #1A1A2E (Near Black)                                                   |")
        output.append(f"|     Notes: Persian-inspired palette with cultural color meanings                       |")
        output.append("|                                                                                        |")

        # Typography section
        output.append(f"|  TYPOGRAPHY:                                                                           |")

        # Primary UI Font
        if ui_fonts:
            f = ui_fonts[0]
            weights = f.weights if f.weights else "Variable"
            output.append(f"|     UI Font:     {f.name} ({weights}) {'+ VF' if f.variable_font else ''} {'✅ OFL' if f.commercial_free else '💰 Paid'} |")
        else:
            output.append(f"|     UI Font:     Vazirmatn (100-900, VF) ✅ OFL                                        |")

        # Heading Font
        if heading_fonts:
            f = heading_fonts[0]
            weights = f.weights if f.weights else "Variable"
            output.append(f"|     Heading:     {f.name} ({weights}) {'+ VF' if f.variable_font else ''} {'✅ OFL' if f.commercial_free else '💰 Paid'} |")
        else:
            output.append(f"|     Heading:     Lalezar (Bold) ✅ OFL                                                 |")

        # Reading Font
        if reading_fonts:
            f = reading_fonts[0]
            weights = f.weights if f.weights else "Variable"
            output.append(f"|     Reading:     {f.name} ({weights}) {'✅ OFL' if f.commercial_free else '💰 Paid'} |")
        else:
            output.append(f"|     Reading:     Amiri (Regular, Bold + Italics) ✅ OFL                                |")

        # Calligraphy Font
        if calligraphy_fonts:
            f = calligraphy_fonts[0]
            output.append(f"|     Calligraphy: {f.name} (Regular) {'✅ OFL' if f.commercial_free else '🆓 Free'} |")
        else:
            output.append(f"|     Calligraphy: Gulzar (Regular) ✅ OFL                                               |")

        output.append("|                                                                                        |")

        # Key Effects
        effects = {
            "ui": "Smooth transitions (150-200ms) + Variable font weight interpolation + Subtle shadows",
            "body": "Optimal line-height (1.7-1.8) + Persian numerals + Justified text support",
            "heading": "Letter-spacing adjustments + Gradient text + Cultural ornamental accents",
            "reading": "OpenType features (ligatures, kerning) + Proper RTL line breaking + Footnotes",
            "calligraphy": "Baseline jitter + Swash alternates + Ink trap simulation + Organic flow",
            "bilingual": "Unified baseline + Matched x-height + Consistent weight mapping + Shared rhythm",
        }
        effect = effects.get(use_case.lower(), "Smooth transitions + Variable fonts + Cultural appropriateness")
        output.append(f"|  KEY EFFECTS: {effect:<72} |")
        output.append("|                                                                                        |")

        # Anti-patterns
        anti_patterns = {
            "ui": "AI purple/pink gradients + Over-animation + Thin weights at small sizes + Latin-only fonts",
            "body": "Display fonts for body + Tight line-height (<1.6) + Forced justification without hyphenation",
            "heading": "Body fonts for headlines + Excessive weights (more than 3) + Clashing Latin/Arabic weights",
            "reading": "Sans-serif for long Arabic text + Missing ligatures + Narrow columns + Small font sizes",
            "calligraphy": "Forced RTL on LTR fonts + Static fonts for dynamic text + Non-calligraphic Nasta'liq",
            "bilingual": "Mismatched weights + Different baseline grids + Unbalanced visual density + Fake bold/italic",
        }
        anti = anti_patterns.get(use_case.lower(), "Mismatched weights + Fake styles + Cultural insensitivity")
        output.append(f"|  AVOID (Anti-patterns): {anti:<62} |")
        output.append("|                                                                                        |")

        # Pre-delivery checklist
        output.append("|  PRE-DELIVERY CHECKLIST:                                                               |")
        output.append("|     [ ] No emojis as icons (use SVG: Heroicons/Lucide)                                 |")
        output.append("|     [ ] cursor-pointer on all clickable elements                                       |")
        output.append("|     [ ] Hover states with smooth transitions (150-300ms)                               |")
        output.append("|     [ ] Light mode: text contrast 4.5:1 minimum                                        |")
        output.append("|     [ ] Focus states visible for keyboard nav                                          |")
        output.append("|     [ ] prefers-reduced-motion respected                                               |")
        output.append("|     [ ] Responsive: 375px, 768px, 1024px, 1440px                                       |")
        output.append("|     [ ] RTL layout tested (mirrored icons, correct padding)                            |")
        output.append("|     [ ] Persian numerals rendering correctly                                           |")
        output.append("|     [ ] Font loading: preconnect + font-display: swap                                  |")
        output.append("|     [ ] OFL.txt included if self-hosting                                               |")
        output.append("+{}+\n".format('-' * 86))

        # Add source links
        output.append("SOURCES:")
        if ui_fonts:
            f = ui_fonts[0]
            if f.sources_google_fonts:
                output.append(f"  Google Fonts: {f.sources_google_fonts}")
            if f.sources_github:
                output.append(f"  GitHub: {f.sources_github}")
        output.append("  All fonts: https://github.com/YOUR_REPO/persian-font-use-skill")

        return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Persian Font Use Skill - Search & Design System Generator")
    parser.add_argument("query", nargs="?", help="Search query (e.g., 'modern UI', 'vazirmatn', 'calligraphy')")
    parser.add_argument("--domain", choices=["font", "license", "category", "use-case"], help="Search domain")
    parser.add_argument("--limit", type=int, default=10, help="Max results")
    parser.add_argument("--design-system", action="store_true", help="Generate design system")
    parser.add_argument("--project", "-p", default="My Project", help="Project name for design system")
    parser.add_argument("--format", choices=["text", "json", "markdown"], default="text", help="Output format")
    parser.add_argument("--list-categories", action="store_true", help="List all categories")
    parser.add_argument("--list-licenses", action="store_true", help="List license types")
    parser.add_argument("--variable", action="store_true", help="Show only variable fonts")
    parser.add_argument("--bilingual", action="store_true", help="Show only bilingual fonts")
    parser.add_argument("--commercial-free", action="store_true", help="Show only free commercial fonts")

    args = parser.parse_args()

    data_dir = Path(__file__).parent.parent / "data"
    db = FontDatabase(data_dir)

    if args.list_categories:
        categories = defaultdict(int)
        for f in db.fonts:
            categories[f.category] += 1
        if args.format == "json":
            print(json.dumps(dict(categories), ensure_ascii=False, indent=2))
        else:
            for cat, count in sorted(categories.items()):
                print(f"{cat}: {count} fonts")
        return

    if args.list_licenses:
        licenses = defaultdict(int)
        for f in db.fonts:
            licenses[f.license] += 1
        if args.format == "json":
            print(json.dumps(dict(licenses), ensure_ascii=False, indent=2))
        else:
            for lic, count in sorted(licenses.items()):
                print(f"{lic}: {count} fonts")
        return

    if args.variable:
        fonts = db.get_variable_fonts()
        if args.format == "json":
            print(json.dumps([asdict(f) for f in fonts], ensure_ascii=False, indent=2))
        else:
            for f in fonts:
                print(f"{f.name} ({f.weight_range}) - {f.license} - {'✅ Commercial' if f.commercial_free else '💰 Paid'}")
        return

    if args.bilingual:
        fonts = db.get_bilingual_fonts()
        if args.format == "json":
            print(json.dumps([asdict(f) for f in fonts], ensure_ascii=False, indent=2))
        else:
            for f in fonts:
                print(f"{f.name} - {f.category} - {f.latin_source} - {'✅' if f.commercial_free else '💰'}")
        return

    if args.commercial_free:
        fonts = db.get_by_license("free")
        if args.format == "json":
            print(json.dumps([asdict(f) for f in fonts], ensure_ascii=False, indent=2))
        else:
            for f in fonts:
                print(f"{f.name} - {f.category} - {f.license} - VF: {'Yes' if f.variable_font else 'No'}")
        return

    if args.design_system:
        output = db.generate_design_system(args.project, args.query or "general")
        if args.format == "markdown":
            print(f"```\n{output}\n```")
        else:
            print(output)
        return

    if not args.query:
        parser.print_help()
        return

    # Search
    results = db.search(args.query, args.domain, args.limit)

    if args.format == "json":
        print(json.dumps([asdict(f) for f in results], ensure_ascii=False, indent=2))
    elif args.format == "markdown":
        print(f"# Search Results for '{args.query}'\n")
        for f in results:
            print(f"## {f.name} (`{f.css_name}`)")
            print(f"- **Category**: {f.category} / {f.subcategory}")
            print(f"- **Style**: {f.style}")
            print(f"- **Weights**: {f.weights}{' + Variable Font' if f.variable_font else ''}")
            print(f"- **License**: {f.license} {'✅ Commercial Free' if f.commercial_free else '💰 Paid/Personal'}")
            print(f"- **Best For**: {f.best_for}")
            print(f"- **Sources**: Google Fonts: {'Yes' if f.sources_google_fonts else 'No'}, GitHub: {'Yes' if f.sources_github else 'No'}")
            print(f"- **Notes**: {f.notes}")
            print()
    else:
        # Text format (default)
        if not results:
            print(f"No fonts found for '{args.query}'")
            return

        print(f"Found {len(results)} font(s) for '{args.query}':\n")
        for i, f in enumerate(results, 1):
            print(f"{i}. {f.name} ({f.css_name})")
            print(f"   Category: {f.category} / {f.subcategory}")
            print(f"   Style: {f.style}")
            print(f"   Weights: {f.weights}{' + Variable Font' if f.variable_font else ''}")
            print(f"   License: {f.license} {'✅ Commercial Free' if f.commercial_free else '💰 Paid/Personal Only'}")
            print(f"   Best For: {f.best_for}")
            if f.sources_google_fonts:
                print(f"   Google Fonts: {f.sources_google_fonts}")
            if f.sources_github:
                print(f"   GitHub: {f.sources_github}")
            print(f"   Notes: {f.notes}")
            print()


if __name__ == "__main__":
    main()