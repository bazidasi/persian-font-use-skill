# Persian Font Selection Guide

A decision framework for choosing the right Persian font for your project.

---

## Quick Decision Tree

```
What is your PRIMARY use case?
│
├─ 🌐 Modern Web UI / Dashboard / App
│   ├─ Need FREE commercial license? → **Vazirmatn** (default choice)
│   ├─ Need variable font? → **Vazirmatn** / **Sahel-VF** / **Estedad**
│   ├─ Need bilingual Persian+Latin? → **Vazirmatn** (best) / **Estedad**
│   ├─ Friendly/rounded UI? → **Sahel** / **Baloo Bhaijaan 2**
│   └─ Corporate Iran (budget)? → **IRANSansX** (paid)
│
├─ 📰 Long-form Reading / Articles / Books
│   ├─ Quranic / Classical / Literary → **Amiri** / **Amiri Quran**
│   ├─ Modern book body text → **Markazi Text** / **Tahrir**
│   ├─ Traditional Naskh → **Noto Naskh Arabic**
│   └─ Legacy compatibility → **Gandom** (archived)
│
├─ 🎭 Headlines / Posters / Branding / Display
│   ├─ Vintage Persian poster style → **Lalezar** (best)
│   ├─ Modern geometric Kufic → **Noto Kufi Arabic**
│   ├─ Bold heavy headlines → **Titr** (legacy)
│   └─ Friendly rounded → **Baloo Bhaijaan 2**
│
├─ ✍️ Poetry / Calligraphy / Literary
│   ├─ Authentic Nasta'liq → **IranNastaliq**
│   ├─ Typographic Nasta'liq → **Gulzar**
│   └─ Casual/handwritten → **Baloo Bhaijaan 2**
│
├─ 🏛️ Legacy / Government / Institutional (Iran)
│   ├─ Traditional documents → **B Nazanin**
│   ├─ Decorative titles → **B Lotus**
│   ├─ Heavy headlines → **B Titr**
│   └─ UI labels/wayfinding → **B Yekan**
│
└─ 🌍 Bilingual / Multilingual (Persian + Arabic + Latin)
    ├─ Best Latin integration → **Vazirmatn** (Roboto Latin)
    ├─ Full Noto family → **Noto Sans Arabic** + **Noto Serif** + **Noto Sans**
    ├─ Arabic-optimized → **Estedad** / **Noto Sans Arabic**
    └─ Variable font → **Vazirmatn** / **Estedad** / **Noto Kufi Arabic**
```

---

## By Category - Detailed Comparison

### 🏆 Modern Sans-Serif (UI/Body Text)

| Font | Weights | Variable | Latin | Farsi Digits | Best For | License |
|------|---------|----------|-------|--------------|----------|---------|
| **Vazirmatn** | 9 (100-900) | ✅ VF | ✅ Roboto | ✅ | **Default choice** | OFL |
| **Sahel** | 3 + VF | ✅ VF | ✅ DejaVu | ✅ (Sahel-FD) | Friendly UI | OFL |
| **Estedad** | 9 + VF | ✅ VF | ✅ Custom | ✅ | Bilingual UI | OFL |
| **Noto Sans Arabic** | 9 + VF | ✅ VF | ✅ Noto | ✅ | Google ecosystem | OFL |
| **Baloo Bhaijaan 2** | 9 + VF | ✅ VF | ✅ Full | ✅ | Playful UI | OFL |
| **IRANSans** | 5+ | ❌ | ✅ Custom | ✅ | Corporate Iran | Paid |

**Recommendation:** Start with **Vazirmatn**. It's the modern standard with best all-around support.

---

### 📖 Serif / Naskh (Long Reading)

| Font | Style | Weights | Best For | License |
|------|-------|---------|----------|---------|
| **Amiri** | Classical Naskh | 4 (R/B + Italic) | Quran, books, literary | OFL |
| **Markazi Text** | Open Naskh | 4 | Body text, magazines | OFL |
| **Tahrir** | Iranian-Arabic Naskh | 6 | Newspapers, print | Paid |
| **Noto Naskh Arabic** | Screen Naskh | 4 | Android/ChromeOS default | OFL |
| **Gandom** | Noto-based | 2 (archived) | Reading (legacy) | OFL |

**Recommendation:** **Amiri** for traditional/classical, **Markazi Text** for modern books.

---

### 🎨 Display / Decorative (Headlines)

| Font | Style | Weights | Best For | License |
|------|-------|---------|----------|---------|
| **Lalezar** | Vintage poster | 1 (bold) | Posters, branding, cultural | OFL |
| **Noto Kufi Arabic** | Geometric Kufic | 9 + VF | Headings, signage, UI | OFL |
| **Titr** | Heavy bold | 1 | Posters, headlines | Personal |
| **Baloo Bhaijaan 2** | Rounded playful | 9 + VF | Kids, casual, marketing | OFL |

**Recommendation:** **Lalezar** for cultural/branding, **Noto Kufi Arabic** for modern UI headings.

---

### ✍️ Nasta'liq (Calligraphy/Poetry)

| Font | Style | Weights | Best For | License |
|------|-------|---------|----------|---------|
| **IranNastaliq** | Traditional cascading | 1 | Poetry, literary, decorative | Free* |
| **Gulzar** | Typographic Nasta'liq | 1 | Urdu/Persian reading, books | OFL |

*Verify IranNastaliq current terms at github.com/farsi-fonts/fonts-irannastaliq

**Recommendation:** **Gulzar** for OFL safety, **IranNastaliq** for authentic calligraphy.

---

### 🏛️ Legacy Iranian Classics (Borna Rayaneh)

| Font | Style | Weights | License | Note |
|------|-------|---------|---------|------|
| **B Nazanin** | Traditional serif | 2 | Personal* | Verify commercial |
| **B Lotus** | Compact calligraphic | 2 | Personal* | Verify commercial |
| **B Titr** | Heavy display | 1 | Personal* | Verify commercial |
| **B Yekan** | Rounded sans | 2 | Personal* | Verify commercial |

*Widely used in Iran but commercial license unclear. **Verify before commercial use.**

---

## By Technical Requirement

### Variable Font Support (Single file, all weights)
1. **Vazirmatn-VF** - Best all-around
2. **Sahel-VF** - Friendly alternative
3. **Estedad-VF** - Bilingual optimized
4. **Noto Kufi Arabic VF** - Display/Kufic
5. **Baloo Bhaijaan 2 VF** - Playful

### Google Fonts CDN (Zero config, fast)
```html
<!-- Vazirmatn -->
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap" rel="stylesheet">

<!-- Estedad -->
<link href="https://fonts.googleapis.com/css2?family=Estedad:wght@100..900&display=swap" rel="stylesheet">

<!-- Amiri -->
<link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">

<!-- Lalezar -->
<link href="https://fonts.googleapis.com/css2?family=Lalezar&display=swap" rel="stylesheet">

<!-- Noto Sans Arabic -->
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@100..900&display=swap" rel="stylesheet">
```

### Self-Hosted (WOFF2 via GitHub/jsDelivr)
```css
/* Vazirmatn */
@font-face {
  font-family: 'Vazirmatn';
  src: url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@latest/fonts/webfonts/Vazirmatn-VariableFont_wght.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
}

/* Sahel */
@font-face {
  font-family: 'Sahel';
  src: url('https://cdn.jsdelivr.net/npm/sahel-font@latest/dist/Sahel-VF.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
}
```

### Fontsource (npm, bundled with build tools)
```bash
npm install @fontsource/vazirmatn @fontsource/sahel @fontsource/estedad
```
```js
import "@fontsource/vazirmatn"; // CSS imported
import "@fontsource/vazirmatn/variable.css"; // Variable font
```

---

## Font Stacks (with Fallbacks)

### Modern Web App (Default)
```css
font-family: 'Vazirmatn', 'Sahel', 'Estedad', 'Noto Sans Arabic', system-ui, sans-serif;
```

### Long-form Reading
```css
font-family: 'Amiri', 'Markazi Text', 'Noto Naskh Arabic', Georgia, serif;
```

### Headlines/Display
```css
font-family: 'Lalezar', 'Noto Kufi Arabic', 'Titr', 'Baloo Bhaijaan 2', sans-serif;
```

### Bilingual Persian + Latin (Best Latin harmony)
```css
font-family: 'Vazirmatn', 'Estedad', 'Noto Sans Arabic', 'Roboto', system-ui, sans-serif;
```

### Corporate Iran (if budget allows)
```css
font-family: 'IRANSans', 'IRANSansX', 'Vazirmatn', 'Sahel', system-ui, sans-serif;
```

### Calligraphy/Poetry
```css
font-family: 'IranNastaliq', 'Gulzar', 'Amiri', cursive;
```

---

## Performance Checklist

- [ ] Use **WOFF2** only (modern browsers)
- [ ] Use **variable fonts** when multiple weights needed
- [ ] Add `font-display: swap` for FOUT
- [ ] Preconnect to font CDN: `<link rel="preconnect" href="https://fonts.gstatic.com">`
- [ ] Subset fonts if using few characters (Fontsource, pyftsubset)
- [ ] Set `font-weight` range in @font-face for variable fonts
- [ ] Use `font-synthesis: none` to prevent fake bold/italic

---

## Common Pitfalls

| Mistake | Fix |
|---------|-----|
| Using B Nazanin commercially without license | Verify license or use OFL alternative |
| Loading all 9 weights as separate files | Use variable font (single file) |
| No fallback fonts | Always add system-ui, sans-serif |
| Using Google Fonts without preconnect | Add preconnect links |
| Fake bold/italic on variable fonts | Set font-weight range, disable synthesis |
| Not including OFL.txt with self-hosted | Required by license |

---

## Project-Specific Recommendations

### E-commerce (Iran market)
- Primary: **IRANSansX** (if budget) or **Vazirmatn**
- Numbers: Ensure Farsi digits (Vazirmatn, Sahel-FD, IRANSansFaNum)

### News/Media Site
- Headlines: **Lalezar** / **Noto Kufi Arabic**
- Body: **Vazirmatn** / **Estedad** / **Noto Naskh Arabic**
- Arabic content: **Noto Sans Arabic** / **Amiri**

### Educational/Kids App
- UI: **Baloo Bhaijaan 2** / **Sahel**
- Friendly, rounded, readable

### Government/Institutional (Iran)
- Legacy compatibility: **B Nazanin** / **B Yekan** (verify license)
- Modern alternative: **Vazirmatn** / **IRANSansX**

### Multilingual (FA/AR/EN)
- **Vazirmatn** + **Noto Sans** (Latin)
- **Estedad** (designed for bilingual)
- Full **Noto family** (Sans/Arabic/Naskh/Kufi)

### Print/Book Publishing
- Body: **Amiri** / **Markazi Text** / **Tahrir**
- Headlines: **Lalezar** / **Noto Kufi Arabic**
- Ensure print license for commercial fonts

---

## Migration Guides

### From Vazir (legacy) → Vazirmatn
```css
/* Old */
font-family: 'Vazir', sans-serif;

/* New */
font-family: 'Vazirmatn', sans-serif;
/* Weights map 1:1, variable font available */
```

### From IRANSans → Vazirmatn (Free alternative)
```css
/* Map weights */
IRANSans Light     → Vazirmatn 300
IRANSans Regular   → Vazirmatn 400
IRANSans Medium    → Vazirmatn 500
IRANSans Bold      → Vazirmatn 700
IRANSans Black     → Vazirmatn 900
```

### From B Nazanin → Modern alternative
```css
/* For body text */
font-family: 'Amiri', 'Markazi Text', serif;

/* For UI */
font-family: 'Vazirmatn', 'Sahel', sans-serif;
```

---

## Testing Checklist

Before shipping:
- [ ] Test Persian, Arabic, English text together
- [ ] Test Farsi digits (۰۱۲۳۴۵۶۷۸۹) vs Latin (0123456789)
- [ ] Test all font weights used in design
- [ ] Test on Windows (DirectWrite), macOS (Core Text), Linux (FreeType)
- [ ] Test RTL layout with mixed LTR content
- [ ] Check font loading performance (DevTools Network)
- [ ] Verify OFL.txt included if self-hosting
- [ ] Test fallback fonts render acceptably