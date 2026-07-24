# Contributing to Persian Font Use Skill

Thank you for your interest in contributing! This skill helps AI agents and developers select and use Persian fonts correctly.

## 🚀 Quick Start

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/persian-font-use-skill.git
cd persian-font-use-skill

# 3. Create a feature branch
git checkout -b feat/add-new-font

# 4. Make changes
# 5. Validate
python3 scripts/validate_data.py

# 6. Commit and push
git commit -m "feat: add new Persian font XYZ"
git push origin feat/add-new-font

# 7. Open a Pull Request
```

## 📋 Contribution Types

### 🔤 Adding a New Font

1. **Add to `data/fonts.csv`** - Follow existing format:
   ```csv
   id,name,css_name,category,subcategory,style,popularity,status,description,
   weights,variable_font,variable_name,weight_range,latin_support,latin_source,
   arabic_support,farsi_digits,farsi_digits_variant,best_for,
   sources_google_fonts,sources_github,sources_cdn,sources_other,
   license,commercial_free,notes
   ```

2. **Add to `data/licensing.csv`** - Include license details

3. **Run validation**: `python3 scripts/validate_data.py`

4. **Test search**: `python3 scripts/search_fonts.py "new font name" --verbose`

### 🌐 Adding Framework Integration

1. **Add to `data/frameworks.csv`** with:
   - Framework identifier
   - Display name
   - Description
   - Install command
   - Config example
   - Font import method

2. **Add template** to `templates/<platform>/` if needed

### 📝 Improving Documentation

- Update guides in `.opencode/skill/persian-font-use/guides/`
- Add examples to `examples/usage-examples.md`
- Improve README.md

### 🐛 Bug Reports

Use the issue template with:
- Skill version
- Platform (Claude Code, Cursor, etc.)
- Steps to reproduce
- Expected vs actual behavior
- Relevant font/framework

---

## ✅ Validation Checklist

Before submitting PR, ensure:

- [ ] `python3 scripts/validate_data.py` passes
- [ ] `python3 scripts/search_fonts.py "your font"` works
- [ ] CSV formatting is consistent (no trailing commas, proper escaping)
- [ ] New font has complete source URLs
- [ ] License info matches official source
- [ ] No duplicate font IDs
- [ ] Popularity is 1-5 integer

---

## 📏 Code Style

### CSV Files
- UTF-8 encoding
- Semicolon-separated values in multi-value fields (weights, best_for)
- Boolean fields: `true`/`false` lowercase
- URLs without trailing slashes

### Python Scripts
- Type hints for public functions
- Docstrings for modules and classes
- Standard library only (no external dependencies)
- Error handling with clear messages

### Markdown
- GitHub-flavored markdown
- Consistent heading hierarchy
- Code blocks with language tags
- Tables for structured data

---

## 🔄 Release Process

Releases use semantic versioning:
- **Patch** (1.0.x): Bug fixes, data corrections
- **Minor** (1.x.0): New fonts, frameworks, features
- **Major** (x.0.0): Breaking changes to data format

---

## 🤝 Community

- Be respectful and inclusive
- Help others with font selection questions
- Share real-world usage examples
- Report licensing discrepancies

---

## 📞 Questions?

Open a [Discussion](https://github.com/YOUR_USERNAME/persian-font-use-skill/discussions) or [Issue](https://github.com/YOUR_USERNAME/persian-font-use-skill/issues).