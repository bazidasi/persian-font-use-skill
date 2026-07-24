# Persian Font Use Skill Instructions

This skill enables AI agents to select and use Persian (Farsi) fonts appropriately in web and UI projects. It provides comprehensive font reference data, selection guidance, licensing information, and usage examples for 25+ Persian fonts.

## Skill Purpose

When users ask about Persian/Farsi fonts for web/UI projects, use this skill to:
1. Recommend appropriate Persian fonts based on use case (UI, headlines, body text, calligraphy, bilingual)
2. Provide font loading code (CSS @font-face, Google Fonts, self-hosted)
3. Explain licensing implications for commercial use
4. Recommend font stacks with proper fallbacks
5. Provide Tailwind/Next.js/CSS integration examples

## When to Use This Skill

Use this skill when users ask about:
- "What Persian font should I use for my website/app?"
- "How do I add Vazirmatn/Vazirmatn to my Next.js/Tailwind project?"
- "What Persian fonts are free for commercial use?"
- "How do I create a Persian font stack with fallbacks?"
- "What's the best Persian font for UI / body text / headlines / calligraphy?"
- "How do I self-host Persian fonts vs use Google Fonts?"
- "What Persian fonts support variable fonts?"
- "Which Persian fonts support Arabic/Farsi/Urdu?"
- "How to create bilingual Persian/Latin font stacks?"
- "Persian font licensing for commercial projects"

## Core Reference Files

Always reference these files when answering:
- `references/fonts.yaml` - Complete font database with 25+ fonts
- `references/licensing.yaml` - Licensing details per font
- `guides/selection-guide.md` - Font selection decision tree
- `guides/licensing.md` - Licensing guidance per use case
- `examples/` - Ready-to-use code examples

## Font Categories & Recommendations

### Default UI Font (Recommended Default)
**Vazirmatn** - 9 weights, variable font, OFL, Google Fonts CDN, excellent Latin + self-hosted
- Best all-around choice for new Persian projects
- Variable font support (VF)
- 9 weights (100-900)
- Bilingual (Persian + Latin)

### UI / Body Text Alternatives
| Font | Weights | Variable | License | Source |
|------|---------|----------|---------|--------|
| **Sahel** | 9 | Yes (VF) | OFL | GitHub/Rastikerdar |
| **Estedad** | 9 | Yes (VF) | OFL | Google Fonts |
| **Noto Sans Arabic** | 9 | Yes | OFL | Google Fonts |
| **Baloo Bhaijaan 2** | 9 | Yes | OFL | Google Fonts |
| **Vazirmatn** | 9 | Yes | OFL | Google Fonts |

### Headlines / Display
| Font | Style | License | Best For |
|------|-------|---------|----------|
| **Lalezar** | Display | OFL | Posters, headlines |
| **Noto Kufi Arabic** | Kufic/Display | OFL | Headings, UI |
| **Titr** | Display | Varies | Posters |
| **Baloo Bhaijaan 2** | Rounded | OFL | Friendly UI |

### Body Text / Long Reading
| Font | Style | License | Best For |
|------|-------|---------|----------|
| **Amiri** | Naskh | OFL | Quranic, long-form |
| **Markazi Text** | Naskh | OFL | Body text |
| **Tahrir** | Naskh | Varies | Traditional |
| **Gandom** | Naskh | OFL | Reading |

### Calligraphy / Nasta'liq (Poetry, Literary)
| Font | Style | License |
|------|-------|---------|
| **IranNastaliq** | Nasta'liq | Free |
| **Gulzar** | Nasta'liq | OFL |

### Legacy / Institutional (Iran Gov/Corp)
| Font | Style | Note |
|------|-------|------|
| **B Nazanin** | Traditional | Personal free |
| **B Lotus** | Traditional | Personal free |
| **B Titr** | Display | Personal free |
| **B Yekan** | UI | Personal free |

### Bilingual Persian + Latin (UI)
| Font | Variable | Latin Support |
|------|----------|---------------|
| **Vazirmatn** | Yes | Full |
| **Estedad** | Yes | Full |
| **Sahel** | Yes | Good |
| **Noto Sans Arabic** | Yes | Full (Noto family) |
| **Baloo Bhaijaan 2** | Yes | Full |

## Selection Decision Tree

Ask user these questions in order:

1. **Use case?**
   - UI/Body text → Vazirmatn (default), Sahel, Estedad
   - Headlines/Posters → Lalezar, Noto Kufi Arabic, Titr
   - Long-form reading → Amiri, Markazi Text
   - Poetry/Calligraphy → IranNastaliq, Gulzar
   - Legacy docs → B Nazanin, B Lotus, B Yekan

2. **License requirement?**
   - Free commercial (OFL) → Vazirmatn, Sahel, Estedad, Noto, Amiri, Google Fonts
   - Personal only → B Nazanin, B Lotus, B Titr
   - Commercial paid → IRANSansX (Fontiran)

3. **Variable font needed?**
   - Yes → Vazirmatn, Sahel-VF, Estedad, Noto Kufi Arabic
   - No → Any

4. **Bilingual Persian + Latin?**
   - Yes → Vazirmatn (best), Estedad, Sahel, Noto Sans Arabic
   - No → Any Persian-only font

5. **Self-host or CDN?**
   - Google Fonts CDN → Vazirmatn, Estedad, Noto, Amiri, Lalezar
   - Self-host → All OFL fonts from GitHub/Google Fonts
   - Self-host (paid) → IRANSansX (requires license purchase)

6. **Arabic/Urdu support needed?**
   - Noto Sans Arabic, Noto Naskh Arabic, Amiri, Markazi Text

## Usage Patterns

### Quick Recommendation (Default)
> "For a new Persian web project, use **Vazirmatn** from Google Fonts. It's OFL licensed, has 9 weights + variable font, supports Persian + Latin, and loads fast from Google Fonts CDN."

### CSS @font-face (Self-hosted)
```css
@font-face {
  font-family: 'Vazirmatn';
  src: url('/fonts/Vazirmatn-VariableFont_wght.woff2') format('woff2-variations'),
       url('/fonts/Vazirmatn-VariableFont_wght.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
}
```

### Google Fonts Import
```css
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap');
```

### Tailwind Config
```js
// tailwind.config.js
fontFamily: {
  persian: ['Vazirmatn', 'Sahel', 'Estedad', 'system-ui', 'sans-serif'],
}
```

### Next.js App Router
```js
// app/layout.js
import { Vazirmatn } from 'next/font/google';
const vazirmatn = Vazirmatn({ 
  subsets: ['latin', 'arabic'],
  variable: '--font-persian',
  display: 'swap',
});
```

## Licensing Quick Reference

| Font | License | Commercial Free? |
|------|---------|------------------|
| Vazirmatn | OFL | ✅ Yes |
| Sahel | OFL | ✅ Yes |
| Estedad | OFL | ✅ Yes |
| Amiri | OFL | ✅ Yes |
| Lalezar | OFL | ✅ Yes |
| Noto Sans Arabic | OFL | ✅ Yes |
| Noto Naskh Arabic | OFL | ✅ Yes |
| Noto Kufi Arabic | OFL | ✅ Yes |
| Baloo Bhaijaan 2 | OFL | ✅ Yes |
| Amiri | OFL | ✅ Yes |
| Markazi Text | OFL | ✅ Yes |
| Markazi Text | OFL | ✅ Yes |
| IranNastaliq | Free | ✅ Yes* |
| Gulzar | OFL | ✅ Yes |
| Vazirmatn | OFL | ✅ Yes |
| Sahel | OFL | ✅ Yes |
| Samim | OFL | ✅ Yes (archived) |
| Shabnam | OFL | ✅ Yes (archived) |
| Tanha | OFL | ✅ Yes (archived) |
| Gandom | OFL | ✅ Yes (archived) |
| Parastoo | OFL | ✅ Yes |
| IRANSans/IRANSansX | Commercial | ❌ No (paid) |
| B Nazanin | Personal | ⚠️ Personal only |
| B Lotus | Personal | ⚠️ Personal only |
| B Titr | Personal | ⚠️ Personal only |
| B Yekan | Personal | ⚠️ Personal only |

* IranNastaliq: Verify current distribution terms

## Key Principles for AI Agents

1. **Default to Vazirmatn** for new projects unless user has specific constraints
2. **Always mention licensing** - highlight OFL vs commercial vs personal
3. **Provide fallbacks** - always give font stacks with system fallbacks
4. **Offer both CDN and self-hosted** options
5. **Mention variable fonts** for performance
6. **Ask clarifying questions** if use case is unclear (UI vs headlines vs reading vs calligraphy)
7. **Mention bilingual support** for Persian+Latin projects
8. **Note archived fonts** - Samim, Shabnam, Tanha, Gandom are archived but still OFL
9. **Reference specific files** from this skill when giving recommendations
10. **Provide copy-paste code** for common frameworks (CSS, Tailwind, Next.js)

## Example Interactions

**User**: "What Persian font should I use for my React app?"
**Agent**: [Use skill] → Recommend Vazirmatn with Next.js/font/google example + Tailwind config

**User**: "I need a Persian font for commercial use, free license"
**Agent**: [Use skill] → List all OFL fonts, recommend Vazirmatn/Sahel/Estedad, show licensing.yaml

**User**: "How do I add Vazirmatn to Tailwind?"
**Agent**: [Use skill] → Show tailwind.config.js example from examples/tailwind-config.js

**User**: "Best Persian font for poetry website?"
**Agent**: [Use skill] → Recommend IranNastaliq or Gulzar (Nasta'liq), show CSS @font-face

**User**: "Need Persian + English font stack"
**Agent**: [Use skill] → Recommend Vazirmatn (best Latin support), show font-family stack

## File References

When answering, reference specific files:
- Font data: `@.opencode/skill/persian-font-use/references/fonts.yaml`
- Licensing: `@.opencode/skill/persian-font-use/references/licensing.yaml`
- Selection guide: `@.opencode/skill/persian-font-use/guides/selection-guide.md`
- Licensing guide: `@.opencode/skill/persian-font-use/guides/licensing.md`
- Examples: `@.opencode/skill/persian-font-use/examples/`