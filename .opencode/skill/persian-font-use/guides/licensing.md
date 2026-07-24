# Persian Font Licensing Guide

Complete licensing reference for 25+ Persian (Farsi) fonts. **Always verify current terms from official sources before commercial use.**

---

## License Categories

### ✅ SIL Open Font License (OFL) - Free Commercial Use

**Permits:**
- Commercial use, modification, distribution
- Bundling with software/products
- Selling products that use the font
- Must include license file
- Cannot sell font alone
- Must rename if modified

**Fonts (17 fonts):**

| Font | Source | Version/Notes |
|------|--------|---------------|
| **Vazirmatn** | Google Fonts / GitHub | v14+, 9 weights + VF |
| **Sahel** | GitHub (Rastikerdar) | 3 weights + VF, includes Sahel-FD |
| **Estedad** | GitHub / Google Fonts | 9 weights + VF |
| **Parastoo** | Google Fonts / GitHub | 2 weights |
| **Amiri** | Google Fonts | 4 files (Regular, Bold, Italics) |
| **Markazi Text** | Google Fonts | 4 weights |
| **Noto Sans Arabic** | Google Fonts | 9 weights + VF, 1642 glyphs |
| **Noto Naskh Arabic** | Google Fonts | 4 weights |
| **Noto Kufi Arabic** | Google Fonts | 9 weights + VF |
| **Lalezar** | Google Fonts / Adobe Fonts | 1 weight (display) |
| **Baloo Bhaijaan 2** | Google Fonts | Variable 400-800 |
| **Gulzar** | Google Fonts / GitHub | 1 weight (Nasta'liq) |
| **Samim** | GitHub (archived) | 2 weights, OFL |
| **Shabnam** | GitHub (archived) | 2 weights, OFL |
| **Tanha** | GitHub (archived) | 1 weight, OFL |
| **Gandom** | GitHub (archived) | 2 weights, OFL |
| **Iranian Sans** | Font Library / GitHub | 2 weights |

**⚠️ Archived fonts (Samim, Shabnam, Tanha, Gandom):** Still OFL licensed, but no longer maintained. Use Vazirmatn/Sahel/Estedad for new projects.

---

### ⚠️ Free for Personal Use Only - Commercial License Required

**Traditional Borna Rayaneh fonts** - widely used in Iranian government/corporate documents.

| Font | Also Known As | Commercial License |
|------|---------------|-------------------|
| **Nazanin** | B Nazanin | Verify per source (MyFonts/Linotype) |
| **Lotus** | B Lotus | Verify per source |
| **Titr** | B Titr | Verify per source (Font Library) |
| **Yekan** | B Yekan | Verify per source |

**Sources claiming "free for personal use":**
- `arabicfonts.net`
- `fontlibrary.org`
- `github.com/rahatool/persian-fonts`
- `cdnfonts.com`
- `myfonts.com` (Linotype - paid)

**⚠️ Action Required:** Contact font vendor or check MyFonts/Linotype for commercial license pricing before using in:
- Commercial websites
- Mobile apps (App Store/Play Store)
- Printed materials for sale
- Client work
- Any revenue-generating use

---

### 💰 Commercial Licenses Required

| Font | Vendor | License Type | Notes |
|------|--------|--------------|-------|
| **IRANSans / IRANSansX** | Fontiran.com | Paid commercial | Most popular commercial Persian font in Iran. npm wrapper only provides CSS, not font files. |
| **Tahrir** | NoonFont.com | Paid commercial | 6 weights (v4.3), newspaper optimized |
| **Nazanin (Linotype)** | MyFonts/Monotype | Paid commercial | Professional version |

**IRANSans Details:**
- Official: `https://fontiran.com` (Persian)
- Pricing: Contact Fontiran (varies by usage: web, app, print, TV)
- Variants: IRANSans, IRANSansX (Persian digits), IRANSansFN (Latin), IRANSansDN
- npm wrapper: `github.com/akiarostami/iransans` (CSS only - you must provide font files)

**Tahrir Details:**
- Official: `https://noonfont.com/fonts/tahrir`
- 6 weights, optimized for newspaper text

---

## License Compliance Checklist

### For OFL Fonts (Vazirmatn, Sahel, etc.):
- [ ] Include `OFL.txt` in your project/font folder
- [ ] Don't sell the font file by itself
- [ ] If modified: rename font (e.g., "MyVazirmatn") and update license
- [ ] Credit original authors in documentation (optional but recommended)

### For Personal-Use Fonts (B Nazanin, etc.):
- [ ] Verify commercial license from official vendor
- [ ] Purchase appropriate license (web, app, print, broadcast)
- [ ] Keep license documentation
- [ ] Don't assume "free download" = "free commercial use"

### For Commercial Fonts (IRANSans, Tahrir):
- [ ] Purchase license before launch
- [ ] Match license to usage (web vs app vs print vs broadcast)
- [ ] Track page views/app installs if license has limits
- [ ] Renew license if subscription-based

---

## Quick Decision Matrix

| Your Project | Recommended Fonts | License Action |
|--------------|-------------------|----------------|
| **Personal portfolio** | Any font | Personal use OK for all |
| **Open source project** | OFL fonts only | Include OFL.txt |
| **Commercial website** | Vazirmatn, Sahel, Estedad, Noto, Lalezar, Amiri | OFL - no cost |
| **Mobile app (App Store)** | Vazirmatn, Sahel, Estedad, Noto | OFL - include license |
| **Client work (agency)** | OFL fonts or IRANSans (if client pays) | Verify client has license for paid fonts |
| **E-commerce site** | Vazirmatn, Sahel, Estedad | OFL - free commercial |
| **Government/Iran corp** | IRANSans (standard in Iran) | Purchase from Fontiran |
| **Printed book/magazine** | Amiri, Markazi Text, Tahrir | Amiri/Markazi: OFL; Tahrir: buy license |
| **Poetry/literary site** | IranNastaliq, Gulzar | OFL (Gulzar) / Free (IranNastaliq) |

---

## Font Attribution Examples

### OFL Font (Vazirmatn)
```css
/* In your CSS or credits page */
/*
Vazirmatn - Persian/Arabic typeface
Copyright (c) 2015-2024, Saber Rastikerdar (saber@rastikerdar.com)
Licensed under SIL Open Font License 1.1
https://scripts.sil.org/OFL
Source: https://github.com/rastikerdar/vazirmatn
*/
```

### Google Fonts (Standard attribution)
```html
<!-- In HTML head or credits page -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<!-- Fonts served by Google Fonts - no additional attribution required per Google Fonts ToS -->
```

### Commercial Font (IRANSans)
```css
/*
IRANSans - Commercial Persian Font
Licensed from Fontiran.com
License: [Your License Number/Type]
Usage: [Web/App/Print - per your license]
*/
```

---

## Risk Assessment

| Risk Level | Scenario | Mitigation |
|------------|----------|------------|
| **Low** | Using Vazirmatn from Google Fonts | OFL, Google hosts, no tracking |
| **Low** | Self-hosting OFL fonts from GitHub releases | Include OFL.txt, verify checksum |
| **Medium** | Using B Nazanin from GitHub repo "free fonts" | **Verify license** - many repos redistribute without commercial rights |
| **High** | Using IRANSans without license in production | **Purchase license** - Fontiran actively enforces |
| **High** | Client provides "licensed" font files | **Get written confirmation** of license scope |

---

## Official License Texts

### SIL OFL 1.1 Summary
- **Full text:** `https://scripts.sil.org/OFL`
- **FAQ:** `https://scripts.sil.org/OFL_faq`
- **Key point:** "The fonts may be used, studied, modified and redistributed freely as long as they are not sold by themselves."

### Google Fonts ToS
- **Full text:** `https://fonts.google.com/attribution`
- **Key point:** Fonts served by Google Fonts API require no additional attribution beyond the standard embed code.

### Fontiran (IRANSans)
- **Persian:** `https://fontiran.com/license`
- **Contact:** `info@fontiran.com`

---

## Resources

- **OFL License:** https://scripts.sil.org/OFL
- **Google Fonts Attribution:** https://fonts.google.com/attribution
- **Fontiran Licensing:** https://fontiran.com/license
- **NoonFont (Tahrir):** https://noonfont.com/fonts/tahrir
- **MyFonts (Nazanin Linotype):** https://www.myfonts.com/collections/nazanin-lt-font-linotype

---

## Disclaimer

This guide is for reference only. **Not legal advice.** Font licenses can change. Always:
1. Check the official vendor website
2. Read the actual license file included with font download
3. Consult legal counsel for commercial projects
4. Keep records of license purchases

*Last updated: 2024. Verify current terms before production use.*