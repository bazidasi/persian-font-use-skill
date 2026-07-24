# Persian Font Use Skill

A comprehensive AI skill for selecting and using Persian (Farsi) fonts in web and UI projects. Provides font database, selection guidance, licensing info, and ready-to-use code examples for 25+ Persian fonts across multiple frameworks.

[![Version](https://img.shields.io/github/v/release/YOUR_USERNAME/persian-font-use-skill?style=for-the-badge&color=blue)](https://github.com/YOUR_USERNAME/persian-font-use-skill/releases)
[![License](https://img.shields.io/github/license/YOUR_USERNAME/persian-font-use-skill?style=for-the-badge&color=green)](https://github.com/YOUR_USERNAME/persian-font-use-skill/blob/main/LICENSE)
[![Fonts](https://img.shields.io/badge/Fonts-25%2B-purple?style=for-the-badge)](https://github.com/YOUR_USERNAME/persian-font-use-skill/tree/main/data)
[![Frameworks](https://img.shields.io/badge/Frameworks-12%2B-orange?style=for-the-badge)](https://github.com/YOUR_USERNAME/persian-font-use-skill/tree/main/data/frameworks.csv)
[![OFL Licensed](https://img.shields.io/badge/License-OFL%20%7C%20MIT-yellow?style=for-the-badge)](https://github.com/YOUR_USERNAME/persian-font-use-skill/blob/main/LICENSE)

**Compatible with:**  
![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-9333ea?style=for-the-badge&logo=anthropic&logoColor=white)
![Cursor](https://img.shields.io/badge/Cursor-compatible-000000?style=for-the-badge&logo=cursor&logoColor=white)
![Windsurf](https://img.shields.io/badge/Windsurf-compatible-00B4FF?style=for-the-badge&logo=windsurf&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-compatible-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![OpenCode](https://img.shields.io/badge/OpenCode-compatible-1A1A1A?style=for-the-badge&logo=opencode&logoColor=white)
![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-compatible-181717?style=for-the-badge&logo=github&logoColor=white)
![Continue](https://img.shields.io/badge/Continue-compatible-00D4AA?style=for-the-badge&logo=continue&logoColor=white)

---

## 🎯 Quick Start

### For AI Agents (Recommended)
The skill activates automatically when users ask about Persian fonts:
```
"Which Persian font should I use for my SaaS dashboard?"
"How do I add Vazirmatn to Next.js?"
"What Persian fonts are free for commercial use?"
"Best font for Persian + English bilingual site?"
```

### For Developers (CLI)
```bash
# Search fonts from command line
python3 scripts/search_fonts.py "vazirmatn" --verbose
python3 scripts/search_fonts.py "variable font" --domain category
python3 scripts/search_fonts.py "commercial free" --list-commercial-free

# Generate design system for a project
python3 scripts/search_fonts.py --design-system vazirmatn --project "MyApp"

# Validate data integrity
python3 scripts/validate_data.py
```

---

## 🏆 Top Recommendations

| Use Case | Font | Weights | Variable | License | Source |
|----------|------|---------|----------|---------|--------|
| **Default UI** | **Vazirmatn** | 9 (100-900) | ✅ | OFL | Google Fonts |
| **Friendly UI** | **Sahel** | 3 + VF | ✅ | OFL | GitHub/jsDelivr |
| **Bilingual** | **Estedad** | 9 + VF | ✅ | OFL | Google Fonts |
| **Headlines** | **Lalezar** | 1 (Bold) | ❌ | OFL | Google Fonts |
| **Reading** | **Amiri** | 4 (R/B + Italics) | ❌ | OFL | Google Fonts |
| **Calligraphy** | **Gulzar** / **IranNastaliq** | 1 | ❌ | OFL / Free | Google Fonts / GitHub |
| **Corporate Iran** | **IRANSansX** | 5+ | ❌ | **Paid** | Fontiran.com |

---

## 📁 Project Structure

```
persian-font-use-skill/
├── skill.json                    # Skill manifest (standard format)
├── README.md                     # This file
├── LICENSE                       # MIT License
├── CONTRIBUTING.md               # Contribution guide
├── SECURITY.md                   # Security policy
├── CODE_OF_CONDUCT.md            # Community guidelines
├── data/                         # Data files (CSV)
│   ├── fonts.csv                 # 25+ font database
│   ├── licensing.csv             # License reference
│   └── frameworks.csv            # 12+ framework integrations
├── scripts/                      # Python utilities
│   ├── search_fonts.py           # Search & design system generator
│   └── validate_data.py          # Data validation
├── templates/                    # Platform-specific templates
│   ├── claude-code/
│   ├── cursor/
│   ├── windsurf/
│   ├── vscode/
│   ├── opencode/
│   ├── adal/
│   └── antigravity/
└── .opencode/skill/persian-font-use/
    ├── skill.yaml                # OpenCode skill config
    ├── instructions.md           # Agent instructions
    ├── references/
    │   ├── fonts.yaml            # Font database (YAML)
    │   └── licensing.yaml        # License reference
    ├── guides/
    │   ├── selection-guide.md    # Decision trees
    │   └── licensing.md          # Compliance guide
    └── examples/
        └── usage-examples.md     # 10+ framework examples
```

---

## 🔧 Installation

### Option 1: CLI Installer (Recommended)
```bash
# Install for specific AI assistant
npx persian-font-use-cli init --ai claude-code    # Claude Code
npx persian-font-use-cli init --ai cursor         # Cursor
npx persian-font-use-cli init --ai windsurf       # Windsurf
npx persian-font-use-cli init --ai vscode         # VS Code
npx persian-font-use-cli init --ai opencode       # OpenCode
npx persian-font-use-cli init --ai copilot        # GitHub Copilot
npx persian-font-use-cli init --ai all            # All platforms

# Global install (available in all projects)
npx persian-font-use-cli init --ai claude-code --global
```

### Option 2: Manual Install
```bash
# Clone to your AI assistant's skill directory
git clone https://github.com/YOUR_USERNAME/persian-font-use-skill.git \
  ~/.claude/skills/persian-font-use     # Claude Code
git clone https://github.com/YOUR_USERNAME/persian-font-use-skill.git \
  ~/.cursor/skills/persian-font-use     # Cursor
git clone https://github.com/YOUR_USERNAME/persian-font-use-skill.git \
  ~/.windsurf/skills/persian-font-use   # Windsurf
git clone https://github.com/YOUR_USERNAME/persian-font-use-skill.git \
  ~/.vscode/skills/persian-font-use     # VS Code
git clone https://github.com/YOUR_USERNAME/persian-font-use-skill.git \
  ~/.opencode/skill/persian-font-use    # OpenCode
```

### Option 3: Direct Reference
Reference files directly in your prompts:
```
@.opencode/skill/persian-font-use/references/fonts.yaml
@.opencode/skill/persian-font-use/guides/selection-guide.md
```

---

## 🔍 Usage Examples

### Search & Compare Fonts
```bash
# Find UI fonts
python3 scripts/search_fonts.py "sans serif ui" --domain category

# Find variable fonts
python3 scripts/search_fonts.py --list-variable

# Find commercial-free fonts
python3 scripts/search_fonts.py --list-commercial-free

# Find bilingual fonts
python3 scripts/search_fonts.py --list-bilingual

# Get detailed info
python3 scripts/search_fonts.py "vazirmatn" --verbose
```

### Generate Design System
```bash
# For a SaaS dashboard
python3 scripts/search_fonts.py --design-system vazirmatn --project "SaaS Dashboard"

# For a poetry site
python3 scripts/search_fonts.py --design-system irannastaliq --project "Poetry Blog"

# Output as JSON for programmatic use
python3 scripts/search_fonts.py "headline display" --json
```

### Framework Integration

#### Next.js 14 (App Router)
```javascript
// app/layout.js
import { Vazirmatn, Lalezar, Amiri } from 'next/font/google';

const vazirmatn = Vazirmatn({
  subsets: ['latin', 'arabic'],
  variable: '--font-persian',
  display: 'swap',
  preload: true,
});

export default function RootLayout({ children }) {
  return (
    <html lang="fa" dir="rtl" className={vazirmatn.variable}>
      <body>{children}</body>
    </html>
  );
}
```

#### Tailwind CSS
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        persian: ['var(--font-persian)', 'Vazirmatn', 'Sahel', 'system-ui', 'sans-serif'],
        'persian-heading': ['Lalezar', 'Noto Kufi Arabic', 'sans-serif'],
        'persian-reading': ['Amiri', 'Markazi Text', 'serif'],
      },
    },
  },
};
```

#### Vite / React / Vue
```css
/* src/styles/fonts.css */
@import "@fontsource/vazirmatn/variable.css";
@import "@fontsource/lalezar/400.css";
@import "@fontsource/amiri/400.css";
@import "@fontsource/amiri/700.css";

:root {
  --font-persian: 'Vazirmatn', 'Sahel', system-ui, sans-serif;
}
```

#### React Native / Expo
```bash
expo install expo-font @expo-google-fonts/vazirmatn @expo-google-fonts/lalezar @expo-google-fonts/amiri
```
```javascript
import { Vazirmatn_400Regular, Vazirmatn_700Bold } from '@expo-google-fonts/vazirmatn';
import { useFonts } from 'expo-font';

const [fontsLoaded] = useFonts({
  'Vazirmatn-Regular': Vazirmatn_400Regular,
  'Vazirmatn-Bold': Vazirmatn_700Bold,
});
```

#### Flutter
```yaml
# pubspec.yaml
flutter:
  fonts:
    - family: Vazirmatn
      fonts:
        - asset: fonts/Vazirmatn-VariableFont_wght.ttf
    - family: Lalezar
      fonts:
        - asset: fonts/Lalezar-Regular.ttf
    - family: Amiri
      fonts:
        - asset: fonts/Amiri-Regular.ttf
        - asset: fonts/Amiri-Bold.ttf
          weight: 700
```

---

## 📊 Data-Driven Architecture

The skill uses CSV data files as the single source of truth:

### fonts.csv (25+ fonts)
```csv
id,name,css_name,category,subcategory,style,popularity,status,description,
weights,variable_font,variable_name,weight_range,latin_support,latin_source,
arabic_support,farsi_digits,farsi_digits_variant,best_for,
sources_google_fonts,sources_github,sources_cdn,sources_other,
license,commercial_free,notes
```

### licensing.csv
License reference for each font with compliance checklist.

### frameworks.csv
12+ framework integrations with install commands and config examples.

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Adding a New Font
1. Add row to `data/fonts.csv`
2. Add license info to `data/licensing.csv`
3. Run validation: `python3 scripts/validate_data.py`
4. Update framework examples if needed
5. Submit PR

### Adding a Framework
1. Add row to `data/frameworks.csv`
2. Add template to `templates/<platform>/`
3. Test with target AI assistant
4. Submit PR

---

## 🔒 Security

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

Font licensing information is for reference only. **Always verify current terms from official sources** before commercial use.

---

## 🔗 Resources

- [Vazirmatn GitHub](https://github.com/rastikerdar/vazirmatn)
- [Sahel GitHub](https://github.com/rastikerdar/sahel-font)
- [Estedad GitHub](https://github.com/aminabedi68/Estedad)
- [Google Fonts Persian](https://fonts.google.com/?subset=arabic)
- [Fontiran (IRANSans)](https://fontiran.com)
- [NoonFont (Tahrir)](https://noonfont.com/fonts/tahrir)

---

**Made for AI agents and developers working with Persian typography.** 🇮🇷