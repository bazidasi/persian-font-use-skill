---
name: persian-font-use
description: "Use this skill whenever the user asks about Persian (Farsi) fonts for web, UI, or design projects. Covers font selection, licensing, variable fonts, bilingual Persian+Latin stacks, and framework integration (Next.js, Tailwind, Vite, React Native, Flutter). Trigger on mentions of 'Persian font', 'Farsi font', 'Vazirmatn', 'Sahel', 'Estedad', 'Amiri', 'Lalezar', 'IranNastaliq', 'Gulzar', 'Noto Arabic', 'RTL font', 'Arabic font', 'bilingual font', 'Persian typography', 'font licensing Iran', 'web font Farsi'."
version: 1.0.0
license: MIT
platforms: [linux, macos, windows]
---

# Persian Font Use Skill

Select and use Persian (Farsi) fonts in web and UI projects. 25+ fonts with selection guidance, licensing info, and framework code examples.

## Quick Start

**Default recommendation:** Use **Vazirmatn** from Google Fonts for new Persian projects. OFL licensed, 9 weights + variable font, Persian + Latin support.

```
https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap
```

## Font Database

Reference files for detailed font data:
- `references/fonts.yaml` - Complete 25+ font database with weights, sources, licenses
- `guides/selection-guide.md` - Decision tree for font selection
- `guides/licensing.md` - Compliance guide per license type
- `examples/usage-examples.md` - Copy-paste code for 10+ frameworks

## Selection Decision Tree

1. **Use case?**
   - UI/Body text → Vazirmatn (default), Sahel, Estedad
   - Headlines/Display → Lalezar, Noto Kufi Arabic
   - Long-form reading → Amiri, Markazi Text
   - Poetry/Calligraphy → IranNastaliq, Gulzar
   - Legacy docs → B Nazanin, B Lotus, B Yekan

2. **License?**
   - Free commercial (OFL) → Vazirmatn, Sahel, Estedad, Noto, Amiri, Lalezar, Gulzar
   - Personal only → B Nazanin, B Lotus, B Titr, B Yekan
   - Commercial paid → IRANSansX (Fontiran), Tahrir (NoonFont)

3. **Variable font needed?**
   - Yes → Vazirmatn, Sahel-VF, Estedad, Noto Sans Arabic, Noto Kufi Arabic, Baloo Bhaijaan 2

4. **Bilingual Persian + Latin?**
   - Yes → Vazirmatn (best), Estedad, Sahel, Noto Sans Arabic

5. **Self-host or CDN?**
   - Google Fonts CDN → Vazirmatn, Estedad, Noto, Amiri, Lalezar
   - Self-host → All OFL fonts from GitHub releases (WOFF2)

## Framework Integration

### Google Fonts CDN
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap" rel="stylesheet">
```

### CSS @font-face (Self-hosted)
```css
@font-face {
  font-family: 'Vazirmatn';
  src: url('/fonts/Vazirmatn-VariableFont_wght.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
}
```

### Tailwind CSS
```js
// tailwind.config.js
fontFamily: {
  persian: ['Vazirmatn', 'Sahel', 'Estedad', 'system-ui', 'sans-serif'],
  'persian-heading': ['Lalezar', 'Noto Kufi Arabic', 'sans-serif'],
  'persian-reading': ['Amiri', 'Markazi Text', 'serif'],
}
```

### Next.js App Router
```js
import { Vazirmatn } from 'next/font/google';
const vazirmatn = Vazirmatn({
  subsets: ['latin', 'arabic'],
  variable: '--font-persian',
  display: 'swap',
});
```

### Fontsource (npm)
```bash
npm install @fontsource/vazirmatn @fontsource/lalezar @fontsource/amiri
```
```js
import "@fontsource/vazirmatn/variable.css";
```

### React Native / Expo
```bash
expo install expo-font @expo-google-fonts/vazirmatn
```

### Flutter
```yaml
flutter:
  fonts:
    - family: Vazirmatn
      fonts:
        - asset: fonts/Vazirmatn-VariableFont_wght.ttf
```

## Licensing Quick Reference

| License | Fonts | Commercial Use |
|---------|-------|----------------|
| **OFL** | Vazirmatn, Sahel, Estedad, Amiri, Lalezar, Noto*, Gulzar, Parastoo, Iranian Sans | Free (include OFL.txt) |
| **Free** | IranNastaliq | Free (verify terms) |
| **Commercial** | IRANSans/IRANSansX, Tahrir | Paid license required |
| **Personal** | B Nazanin, B Lotus, B Titr, B Yekan | Personal use only |

Always verify current license terms from official sources before commercial use.

## Key Principles

1. Default to **Vazirmatn** for new projects
2. Always mention licensing (OFL vs commercial vs personal)
3. Provide font stacks with system fallbacks
4. Use variable fonts for performance when multiple weights needed
5. Include `font-display: swap` on all @font-face
6. Note archived fonts (Samim, Shabnam, Tanha, Gandom) are still OFL but unmaintained
