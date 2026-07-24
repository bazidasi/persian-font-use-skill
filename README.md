# Persian Font Use Skill

A comprehensive skill for AI agents to select and use Persian (Farsi) fonts appropriately in web and UI projects. Provides font reference data, selection guidance, licensing information, and ready-to-use code examples for 25+ Persian fonts.

## 🎯 What This Skill Provides

- **25+ Persian fonts** cataloged with complete metadata
- **Smart selection guide** - decision trees for use cases
- **Licensing reference** - OFL, personal-use, commercial
- **Framework examples** - Next.js, Tailwind, Vite, React Native, Flutter, CSS
- **Font stacks** - ready-to-copy fallback chains
- **Variable font support** - performance optimization

## 📦 Quick Start

### For AI Agents
This skill is designed for AI assistants. When users ask about Persian fonts, the agent will:

1. Ask clarifying questions (use case, license, bilingual needs, framework)
2. Recommend appropriate fonts from the catalog
3. Provide copy-paste code for their stack
4. Explain licensing implications

### For Developers
Browse the references directly:

| File | Description |
|------|-------------|
| [`references/fonts.yaml`](.opencode/skill/persian-font-use/references/fonts.yaml) | Complete font database (25+ fonts) |
| [`guides/selection-guide.md`](.opencode/skill/persian-font-use/guides/selection-guide.md) | Decision trees & comparisons |
| [`guides/licensing.md`](.opencode/skill/persian-font-use/guides/licensing.md) | License compliance guide |
| [`examples/usage-examples.md`](.opencode/skill/persian-font-use/examples/usage-examples.md) | 10+ framework integrations |

## 🏆 Top Recommendations

### Default Choice: **Vazirmatn**
```html
<!-- Google Fonts CDN -->
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap" rel="stylesheet">
```
- 9 weights + variable font (100-900)
- OFL license - free commercial
- Roboto Latin companion
- Persian + Arabic support
- Google Fonts CDN + self-hosted

### Alternatives by Use Case

| Need | Font | Why |
|------|------|-----|
| Friendly UI | **Sahel** | Rounded, Sahel-FD has Persian digits |
| Bilingual UI | **Estedad** | Designed for Arabic+Latin harmony |
| Headlines | **Lalezar** | Vintage Persian poster style |
| Long reading | **Amiri** | Classical Naskh, Quranic optimized |
| Calligraphy | **Gulzar** / **IranNastaliq** | Nasta'liq script |
| Corporate Iran | **IRANSansX** | Paid, industry standard in Iran |

## 📁 Skill Structure

```
.opencode/skill/persian-font-use/
├── skill.yaml              # Skill metadata
├── instructions.md         # Agent instructions
├── references/
│   ├── fonts.yaml          # 25+ font database
│   └── licensing.yaml      # License reference
├── guides/
│   ├── selection-guide.md  # Decision trees
│   └── licensing.md        # Compliance guide
└── examples/
    └── usage-examples.md   # 10 framework examples
```

## 🛠️ Framework Examples Included

- **Next.js 14** (App Router + `next/font/google`)
- **Tailwind CSS** (font-family config)
- **Vite / React / Vue** (CSS @import + self-hosted)
- **Fontsource** (npm packages)
- **React Native / Expo** (expo-font)
- **Flutter** (pubspec.yaml fonts)
- **Plain HTML/CSS** (Google Fonts + self-hosted)
- **CSS Utilities** (copy-paste classes)

## 📋 Font Catalog Summary

### Modern Sans-Serif (UI)
- **Vazirmatn** ⭐ - 9 weights, VF, OFL
- **Sahel** - 3 weights + VF, OFL, Persian digits variant
- **Estedad** - 9 weights, VF, OFL, bilingual optimized
- **Noto Sans Arabic** - 9 weights, VF, OFL, 1642 glyphs
- **Baloo Bhaijaan 2** - VF, OFL, playful rounded

### Serif / Naskh (Reading)
- **Amiri** - Classical Naskh, 4 files, OFL
- **Markazi Text** - Open Naskh, 4 weights, OFL
- **Noto Naskh Arabic** - Screen Naskh, 4 weights, OFL
- **Tahrir** - Iranian Naskh, 6 weights, **Paid**

### Display / Decorative
- **Lalezar** - Vintage poster, OFL
- **Noto Kufi Arabic** - Geometric Kufic, 9 weights + VF, OFL
- **Titr** - Heavy bold, legacy, personal use

### Calligraphy / Nasta'liq
- **IranNastaliq** - Traditional cascading, free
- **Gulzar** - Typographic Nasta'liq, OFL

### Legacy Iranian (Borna Rayaneh)
- **B Nazanin**, **B Lotus**, **B Titr**, **B Yekan** - Personal use only

## ⚖️ Licensing Quick Reference

| License | Fonts | Commercial Free? |
|---------|-------|------------------|
| **OFL** | Vazirmatn, Sahel, Estedad, Amiri, Lalezar, Noto family, Baloo 2, Gulzar, Parastoo, Samim, Shabnam, Tanha, Gandom, Iranian Sans | ✅ Yes |
| **Personal Only** | B Nazanin, B Lotus, B Titr, B Yekan | ⚠️ Verify |
| **Paid** | IRANSans/IRANSansX, Tahrir | ❌ Purchase required |

## 🔧 Installation as opencode Skill

```bash
# Clone to your opencode skills directory
git clone https://github.com/YOUR_USERNAME/persian-font-use-skill.git \
  ~/.config/opencode/skill/persian-font-use
```

Or copy the `.opencode/skill/persian-font-use` folder to your project.

## 🤝 Contributing

1. Fork the repository
2. Update `references/fonts.yaml` with new font data
3. Update `guides/selection-guide.md` if categories change
4. Add framework examples to `examples/usage-examples.md`
5. Submit PR

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

Font licensing information is for reference only. Always verify current terms from official sources before commercial use.

## 🔗 Useful Links

- [Vazirmatn GitHub](https://github.com/rastikerdar/vazirmatn)
- [Sahel GitHub](https://github.com/rastikerdar/sahel-font)
- [Estedad GitHub](https://github.com/aminabedi68/Estedad)
- [Google Fonts Persian](https://fonts.google.com/?subset=arabic)
- [Fontiran (IRANSans)](https://fontiran.com)
- [NoonFont (Tahrir)](https://noonfont.com/fonts/tahrir)

---

**Made for AI agents and developers working with Persian typography.** 🇮🇷