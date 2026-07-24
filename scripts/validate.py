#!/usr/bin/env python3
"""
Validate Persian Font Use Skill data files
"""

import csv
import json
from pathlib import Path
from typing import List, Dict, Any


def validate_fonts_csv(filepath: Path) -> List[str]:
    """Validate fonts.csv structure and data"""
    errors = []
    required_fields = [
        'id', 'name', 'css_name', 'category', 'subcategory', 'style',
        'popularity', 'status', 'description', 'weights', 'variable_font',
        'variable_name', 'weight_range', 'latin_support', 'latin_source',
        'arabic_support', 'farsi_digits', 'farsi_digits_variant', 'best_for',
        'sources_google_fonts', 'sources_github', 'sources_cdn', 'sources_other',
        'license', 'commercial_free', 'notes'
    ]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Check headers
        if reader.fieldnames:
            missing = set(required_fields) - set(reader.fieldnames)
            extra = set(reader.fieldnames) - set(required_fields)
            if missing:
                errors.append(f"Missing columns: {missing}")
            if extra:
                errors.append(f"Extra columns: {extra}")

        # Check each row
        ids_seen = set()
        for i, row in enumerate(rows, start=2):
            # Check required fields not empty
            for field in ['id', 'name', 'css_name', 'category']:
                if not row.get(field, '').strip():
                    errors.append(f"Row {i}: Missing required field '{field}'")

            # Check duplicate IDs
            font_id = row.get('id', '').strip()
            if font_id in ids_seen:
                errors.append(f"Row {i}: Duplicate font ID '{font_id}'")
            ids_seen.add(font_id)

            # Validate popularity
            try:
                pop = int(row.get('popularity', 0))
                if pop < 0 or pop > 5:
                    errors.append(f"Row {i}: Popularity must be 0-5, got {pop}")
            except ValueError:
                errors.append(f"Row {i}: Popularity must be integer")

            # Validate boolean fields
            for field in ['variable_font', 'latin_support', 'arabic_support', 'farsi_digits', 'commercial_free']:
                val = row.get(field, '').strip().lower()
                if val and val not in ('true', 'false'):
                    errors.append(f"Row {i}: '{field}' must be 'true' or 'false', got '{val}'")

    except Exception as e:
        errors.append(f"Failed to read fonts.csv: {e}")

    return errors


def validate_licensing_csv(filepath: Path) -> List[str]:
    """Validate licensing.csv structure"""
    errors = []
    required_fields = [
        'font_id', 'license_type', 'license_name', 'license_url',
        'commercial_use', 'modification', 'distribution', 'sell_font',
        'attribution_required', 'notes'
    ]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if reader.fieldnames:
            missing = set(required_fields) - set(reader.fieldnames)
            extra = set(reader.fieldnames) - set(required_fields)
            if missing:
                errors.append(f"Missing columns: {missing}")
            if extra:
                errors.append(f"Extra columns: {extra}")

        font_ids = set()
        for i, row in enumerate(rows, start=2):
            fid = row.get('font_id', '').strip()
            if not fid:
                errors.append(f"Row {i}: Missing font_id")
            if fid in font_ids:
                errors.append(f"Row {i}: Duplicate font_id '{fid}'")
            font_ids.add(fid)

            for field in ['commercial_use', 'modification', 'distribution', 'sell_font', 'attribution_required']:
                val = row.get(field, '').strip().lower()
                if val and val not in ('true', 'false'):
                    errors.append(f"Row {i}: '{field}' must be 'true' or 'false', got '{val}'")

    except Exception as e:
        errors.append(f"Failed to read licensing.csv: {e}")

    return errors


def validate_skill_json(filepath: Path) -> List[str]:
    """Validate skill.json structure"""
    errors = []
    required_fields = [
        'name', 'displayName', 'description', 'version', 'author',
        'license', 'repository', 'homepage', 'keywords', 'platforms',
        'categories', 'entryPoints', 'scripts', 'dataFiles', 'templates',
        'skillType', 'requiresInternet', 'supportedFrameworks'
    ]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")

        # Validate platforms
        valid_platforms = ['claude-code', 'cursor', 'windsurf', 'vscode', 'copilot', 'adal', 'antigravity', 'kiro', 'qoder', 'trae', 'opencode']
        for p in data.get('platforms', []):
            if p not in valid_platforms:
                errors.append(f"Unknown platform: {p}")

    except Exception as e:
        errors.append(f"Failed to read skill.json: {e}")

    return errors


def validate_references_yaml(filepath: Path) -> List[str]:
    """Validate references/fonts.yaml exists and is readable"""
    errors = []
    try:
        import yaml
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if not data or 'fonts' not in data:
            errors.append("fonts.yaml missing 'fonts' key")
    except ImportError:
        errors.append("PyYAML not installed - cannot validate YAML")
    except Exception as e:
        errors.append(f"Failed to read fonts.yaml: {e}")
    return errors


def main():
    data_dir = Path(__file__).parent.parent / "data"
    ref_dir = Path(__file__).parent.parent / ".opencode" / "skill" / "persian-font-use" / "references"

    all_errors = []

    print("Validating fonts.csv...")
    all_errors.extend(validate_fonts_csv(data_dir / "fonts.csv"))

    print("Validating licensing.csv...")
    all_errors.extend(validate_licensing_csv(data_dir / "licensing.csv"))

    print("Validating skill.json...")
    all_errors.extend(validate_skill_json(Path(__file__).parent.parent / "skill.json"))

    print("Validating references/fonts.yaml...")
    all_errors.extend(validate_references_yaml(ref_dir / "fonts.yaml"))

    if all_errors:
        print("\n❌ VALIDATION FAILED:")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("\n✅ ALL VALIDATIONS PASSED")


if __name__ == "__main__":
    main()