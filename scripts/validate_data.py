#!/usr/bin/env python3
"""
Validate data files for Persian Font Use Skill
"""

import csv
import json
import sys
from pathlib import Path


def validate_fonts_csv(data_dir: Path):
    """Validate fonts.csv"""
    path = data_dir / "fonts.csv"
    if not path.exists():
        print(f"ERROR: {path} not found")
        return False

    required_fields = [
        'id', 'name', 'css_name', 'category', 'subcategory', 'style',
        'popularity', 'status', 'description', 'weights', 'variable_font',
        'variable_name', 'weight_range', 'latin_support', 'latin_source',
        'arabic_support', 'farsi_digits', 'farsi_digits_variant', 'best_for',
        'sources_google_fonts', 'sources_github', 'sources_cdn', 'sources_other',
        'license', 'commercial_free', 'notes'
    ]

    errors = []
    ids_seen = set()

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 2):
            # Check required fields
            for field in required_fields:
                if field not in row:
                    errors.append(f"Row {i}: Missing field '{field}'")

            # Check unique ID
            if row['id'] in ids_seen:
                errors.append(f"Row {i}: Duplicate ID '{row['id']}'")
            ids_seen.add(row['id'])

            # Validate popularity
            try:
                pop = int(row['popularity'])
                if not 1 <= pop <= 5:
                    errors.append(f"Row {i}: Popularity must be 1-5, got {pop}")
            except ValueError:
                errors.append(f"Row {i}: Invalid popularity '{row['popularity']}'")

            # Validate boolean fields
            for field in ['variable_font', 'latin_support', 'arabic_support', 'farsi_digits', 'commercial_free']:
                val = row[field].lower()
                if val not in ('true', 'false'):
                    errors.append(f"Row {i}: {field} must be 'true' or 'false', got '{val}'")

            # Validate status
            if row['status'] not in ('active', 'superseded', 'archived', 'legacy'):
                errors.append(f"Row {i}: Invalid status '{row['status']}'")

    if errors:
        for err in errors:
            print(f"  {err}")
        return False
    else:
        print(f"  ✅ fonts.csv: {len(ids_seen)} fonts valid")
        return True


def validate_licensing_csv(data_dir: Path):
    """Validate licensing.csv"""
    path = data_dir / "licensing.csv"
    if not path.exists():
        print(f"ERROR: {path} not found")
        return False

    required_fields = ['font_id', 'license_type', 'license_name', 'license_url',
                       'commercial_free', 'modification_allowed', 'distribution_allowed',
                       'sell_font_allowed', 'credit_required', 'notes']

    errors = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 2):
            for field in required_fields:
                if field not in row:
                    errors.append(f"Row {i}: Missing field '{field}'")

            for field in ['commercial_free', 'modification_allowed', 'distribution_allowed', 'sell_font_allowed', 'credit_required']:
                val = row[field].lower()
                if val not in ('true', 'false'):
                    errors.append(f"Row {i}: {field} must be 'true' or 'false'")

    if errors:
        for err in errors:
            print(f"  {err}")
        return False
    else:
        print(f"  ✅ licensing.csv: valid")
        return True


def validate_frameworks_csv(data_dir: Path):
    """Validate frameworks.csv"""
    path = data_dir / "frameworks.csv"
    if not path.exists():
        print(f"ERROR: {path} not found")
        return False

    required_fields = ['framework', 'name', 'description', 'install_command', 'config_example', 'font_import_method']

    errors = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 2):
            for field in required_fields:
                if field not in row:
                    errors.append(f"Row {i}: Missing field '{field}'")

    if errors:
        for err in errors:
            print(f"  {err}")
        return False
    else:
        print(f"  ✅ frameworks.csv: valid")
        return True


def validate_skill_json(root_dir: Path):
    """Validate skill.json"""
    path = root_dir / "skill.json"
    if not path.exists():
        print(f"ERROR: {path} not found")
        return False

    try:
        with open(path, 'r', encoding='utf-8') as f:
            skill = json.load(f)

        required = ['name', 'displayName', 'description', 'version', 'author', 'license', 'repository', 'homepage',
                    'keywords', 'platforms', 'categories', 'entryPoints', 'scripts', 'dataFiles', 'templates',
                    'skillType', 'requiresInternet', 'supportedFrameworks']

        for field in required:
            if field not in skill:
                print(f"  ERROR: Missing required field '{field}'")
                return False

        print(f"  ✅ skill.json: valid")
        return True
    except json.JSONDecodeError as e:
        print(f"  ERROR: Invalid JSON: {e}")
        return False


def main():
    root_dir = Path(__file__).parent.parent
    data_dir = root_dir / "data"

    print("Validating Persian Font Use Skill data files...\n")

    all_valid = True
    all_valid &= validate_fonts_csv(data_dir)
    all_valid &= validate_licensing_csv(data_dir)
    all_valid &= validate_frameworks_csv(data_dir)
    all_valid &= validate_skill_json(root_dir)

    print()
    if all_valid:
        print("✅ All validations passed!")
        return 0
    else:
        print("❌ Validation failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())