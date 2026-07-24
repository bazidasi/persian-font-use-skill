# Persian Font Usage Examples

Ready-to-use code examples for integrating Persian fonts in various frameworks.

---

## 1. Plain HTML/CSS (Google Fonts CDN)

```html
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Persian Font Demo</title>
  
  <!-- Preconnect for faster font loading -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  
  <!-- Vazirmatn (UI/Body) + Lalezar (Headlines) -->
  <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&family=Lalezar&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --font-ui: 'Vazirmatn', system-ui, sans-serif;
      --font-heading: 'Lalezar', sans-serif;
    }
    
    * {
      box-sizing: border-box;
    }
    
    body {
      font-family: var(--font-ui);
      font-weight: 400;
      line-height: 1.7;
      direction: rtl;
    }
    
    h1, h2, h3, h4 {
      font-family: var(--font-heading);
      font-weight: 400;
      line-height: 1.3;
    }
    
    .persian-digits {
      font-variant-numeric: diagonal-fractions;
    }
  </style>
</head>
<body>
  <h1>نمونه فونت فارسی</h1>
  <p>این یک متن نمونه با فونت <strong>Vazirmatn</strong> است.</p>
  <p class="persian-digits">ارقام فارسی: ۰۱۲۳۴۵۶۷۸۹</p>
</body>
</html>
```

---

## 2. Self-Hosted with @font-face (WOFF2)

```css
/* fonts.css - Include in your project */

/* Vazirmatn Variable Font */
@font-face {
  font-family: 'Vazirmatn';
  src: url('/fonts/Vazirmatn-VariableFont_wght.woff2') format('woff2-variations'),
       url('/fonts/Vazirmatn-VariableFont_wght.woff2') format('woff2');
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}

/* Sahel Variable Font */
@font-face {
  font-family: 'Sahel';
  src: url('/fonts/Sahel-VF.woff2') format('woff2-variations'),
       url('/fonts/Sahel.woff2') format('woff2');
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}

/* Lalezar (Display) */
@font-face {
  font-family: 'Lalezar';
  src: url('/fonts/Lalezar-Regular.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

/* Amiri (Reading) */
@font-face {
  font-family: 'Amiri';
  src: url('/fonts/Amiri-Regular.woff2') format('woff2'),
       url('/fonts/Amiri-Bold.woff2') format('woff2');
  font-weight: 400 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Amiri';
  src: url('/fonts/Amiri-Italic.woff2') format('woff2'),
       url('/fonts/Amiri-BoldItalic.woff2') format('woff2');
  font-weight: 400 700;
  font-style: italic;
  font-display: swap;
}

/* Usage */
:root {
  --font-ui: 'Vazirmatn', 'Sahel', system-ui, sans-serif;
  --font-heading: 'Lalezar', sans-serif;
  --font-reading: 'Amiri', Georgia, serif;
}
```

---

## 3. Tailwind CSS Configuration

```javascript
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{html,js,ts,jsx,tsx,vue}',
  ],
  theme: {
    extend: {
      fontFamily: {
        // Primary UI font stack
        persian: [
          'var(--font-persian)',
          'Vazirmatn',
          'Sahel',
          'Estedad',
          'system-ui',
          'sans-serif'
        ],
        // Headlines/Display
        'persian-heading': [
          'Lalezar',
          'Noto Kufi Arabic',
          'Baloo Bhaijaan 2',
          'sans-serif'
        ],
        // Long-form reading
        'persian-reading': [
          'Amiri',
          'Markazi Text',
          'Noto Naskh Arabic',
          'Georgia',
          'serif'
        ],
        // Calligraphy/Poetry
        'persian-calligraphy': [
          'IranNastaliq',
          'Gulzar',
          'cursive'
        ],
        // Bilingual (Persian + Latin)
        'persian-bilingual': [
          'Vazirmatn',
          'Estedad',
          'Noto Sans Arabic',
          'Inter',
          'Roboto',
          'system-ui',
          'sans-serif'
        ],
      },
      fontSize: {
        // Persian-optimized scale
        'persian-xs': ['0.75rem', { lineHeight: '1.6' }],
        'persian-sm': ['0.875rem', { lineHeight: '1.7' }],
        'persian-base': ['1rem', { lineHeight: '1.8' }],
        'persian-lg': ['1.125rem', { lineHeight: '1.8' }],
        'persian-xl': ['1.25rem', { lineHeight: '1.7' }],
        'persian-2xl': ['1.5rem', { lineHeight: '1.6' }],
        'persian-3xl': ['1.875rem', { lineHeight: '1.4' }],
        'persian-4xl': ['2.25rem', { lineHeight: '1.3' }],
      },
    },
  },
  plugins: [],
}
```

```css
/* globals.css */
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&family=Lalezar&family=Amiri:ital,wght@0,400;0,700;1,400;1,700&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html {
    @apply font-persian text-persian-base;
  }
  
  html[dir="rtl"] {
    @apply font-persian;
  }
  
  h1, h2, h3, h4, h5, h6 {
    @apply font-persian-heading;
  }
  
  .font-reading {
    @apply font-persian-reading;
  }
  
  .font-calligraphy {
    @apply font-persian-calligraphy;
  }
}
```

---

## 4. Next.js 14+ (App Router)

```javascript
// app/layout.js
import { Vazirmatn, Lalezar, Amiri } from 'next/font/google';
import './globals.css';

// Vazirmatn - Primary UI font
const vazirmatn = Vazirmatn({
  subsets: ['latin', 'arabic'],
  weight: ['100', '200', '300', '400', '500', '600', '700', '800', '900'],
  variable: '--font-vazirmatn',
  display: 'swap',
  preload: true,
});

// Lalezar - Headlines
const lalezar = Lalezar({
  subsets: ['latin', 'arabic'],
  weight: '400',
  variable: '--font-lalezar',
  display: 'swap',
});

// Amiri - Reading text
const amiri = Amiri({
  subsets: ['latin', 'arabic'],
  weight: ['400', '700'],
  style: ['normal', 'italic'],
  variable: '--font-amiri',
  display: 'swap',
});

export const metadata = {
  title: 'Persian Font Demo',
  metadataBase: new URL('https://your-domain.com'),
};

export default function RootLayout({ children }) {
  return (
    <html lang="fa" dir="rtl" className={`${vazirmatn.variable} ${lalezar.variable} ${amiri.variable}`}>
      <head>
        {/* Preconnect for self-hosted fonts if needed */}
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
      </head>
      <body className="font-sans antialiased">
        {children}
      </body>
    </html>
  );
}
```

```css
/* app/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --font-sans: var(--font-vazirmatn), system-ui, sans-serif;
  --font-heading: var(--font-lalezar), sans-serif;
  --font-reading: var(--font-amiri), Georgia, serif;
}

@layer base {
  html {
    font-family: var(--font-sans);
    line-height: 1.8;
  }
  
  h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    line-height: 1.3;
  }
  
  .font-reading {
    font-family: var(--font-reading);
  }
}

/* Persian numerals utility */
.persian-numerals {
  font-variant-numeric: diagonal-fractions;
  font-feature-settings: "cv02" 1;
}
```

```javascript
// app/page.js - Example usage
export default function HomePage() {
  return (
    <main className="p-8 max-w-4xl mx-auto">
      <h1 className="text-4xl md:text-5xl mb-6">
        خوش آمدید به پروژه فارسی
      </h1>
      
      <p className="text-lg mb-4 leading-relaxed">
        این متن با فونت <strong className="font-medium">Vazirmatn</strong> نمایش داده شده است.
        فونت پیش‌فرض مدرن برای پروژه‌های فارسی.
      </p>
      
      <h2 className="text-2xl md:text-3xl mb-4 font-heading">
        عناوین با Lalezar
      </h2>
      
      <article className="font-reading prose prose-rtl max-w-none">
        <p>
          برای متون طولانی و خواندن کتاب، فونت <strong>Amiri</strong> 
          گزینه کلاسیک و خوانا است.
        </p>
      </article>
      
      <div className="mt-8 p-4 bg-gray-100 rounded-lg persian-numerals">
        <p>ارقام فارسی: ۰۱۲۳۴۵۶۷۸۹</p>
        <p>قیمت: ۱۲۳،۴۵۶ تومان</p>
      </div>
    </main>
  );
}
```

---

## 5. Vite / Vue 3 / React (CSS Modules)

```css
/* src/styles/fonts.css */
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&family=Sahel:wght@300;400;700;900&family=Lalezar&display=swap');

:root {
  --font-ui: 'Vazirmatn', 'Sahel', system-ui, sans-serif;
  --font-heading: 'Lalezar', sans-serif;
}

* {
  box-sizing: border-box;
}

html {
  font-family: var(--font-ui);
  direction: rtl;
  line-height: 1.7;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  font-weight: 400;
}
```

```javascript
// main.js (Vue) or index.js (React)
import './styles/fonts.css';
```

---

## 6. Fontsource (npm package, bundled)

```bash
# Install
npm install @fontsource/vazirmatn @fontsource/lalezar @fontsource/amiri @fontsource/noto-sans-arabic
```

```javascript
// main.js or layout.js
import "@fontsource/vazirmatn/variable.css"; // Variable font (100-900)
import "@fontsource/lalezar/400.css";
import "@fontsource/amiri/400.css";
import "@fontsource/amiri/700.css";
import "@fontsource/amiri/400-italic.css";
import "@fontsource/amiri/700-italic.css";
import "@fontsource/noto-sans-arabic/variable.css"; // Bilingual fallback
```

```css
/* global.css */
:root {
  --font-ui: 'Vazirmatn', 'Noto Sans Arabic', system-ui, sans-serif;
  --font-heading: 'Lalezar', sans-serif;
  --font-reading: 'Amiri', Georgia, serif;
}
```

---

## 7. React Native / Expo

```bash
# Install
expo install expo-font @expo-google-fonts/vazirmatn @expo-google-fonts/lalezar @expo-google-fonts/amiri
```

```javascript
// App.js
import { useFonts } from 'expo-font';
import { Vazirmatn_400Regular, Vazirmatn_700Bold, Vazirmatn_900Black } from '@expo-google-fonts/vazirmatn';
import { Lalezar_400Regular } from '@expo-google-fonts/lalezar';
import { Amiri_400Regular, Amiri_700Bold } from '@expo-google-fonts/amiri';

export default function App() {
  const [fontsLoaded] = useFonts({
    'Vazirmatn-Regular': Vazirmatn_400Regular,
    'Vazirmatn-Bold': Vazirmatn_700Bold,
    'Vazirmatn-Black': Vazirmatn_900Black,
    'Lalezar-Regular': Lalezar_400Regular,
    'Amiri-Regular': Amiri_400Regular,
    'Amiri-Bold': Amiri_700Bold,
  });

  if (!fontsLoaded) {
    return <LoadingScreen />;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>عنوان فارسی</Text>
      <Text style={styles.body}>متن بدنه با فازیرمتن</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20 },
  heading: { fontFamily: 'Lalezar-Regular', fontSize: 28, marginBottom: 16 },
  body: { fontFamily: 'Vazirmatn-Regular', fontSize: 16, lineHeight: 26 },
});
```

---

## 8. Flutter

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
        - asset: fonts/Amiri-Italic.ttf
          style: italic
        - asset: fonts/Amiri-BoldItalic.ttf
          weight: 700
          style: italic
```

```dart
// main.dart
MaterialApp(
  theme: ThemeData(
    fontFamily: 'Vazirmatn',
    textTheme: const TextTheme(
      displayLarge: TextStyle(fontFamily: 'Lalezar', fontWeight: FontWeight.normal),
      bodyLarge: TextStyle(fontFamily: 'Vazirmatn', height: 1.7),
      bodyMedium: TextStyle(fontFamily: 'Vazirmatn', height: 1.8),
    ),
  ),
  home: Directionality(
    textDirection: TextDirection.rtl,
    child: Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('عنوان با لالازار', style: Theme.of(context).textTheme.displayLarge),
            SizedBox(height: 16),
            Text('متن با فازیرمتن', style: Theme.of(context).textTheme.bodyLarge),
          ],
        ),
      ),
    ),
  ),
);
```

---

## 9. CSS Utility Classes (Copy-Paste)

```css
/* persian-fonts-utilities.css */

/* Font Families */
.font-persian { font-family: 'Vazirmatn', 'Sahel', 'Estedad', system-ui, sans-serif; }
.font-persian-heading { font-family: 'Lalezar', 'Noto Kufi Arabic', sans-serif; }
.font-persian-reading { font-family: 'Amiri', 'Markazi Text', 'Noto Naskh Arabic', serif; }
.font-persian-calligraphy { font-family: 'IranNastaliq', 'Gulzar', cursive; }
.font-persian-bilingual { font-family: 'Vazirmatn', 'Estedad', 'Noto Sans Arabic', 'Inter', system-ui, sans-serif; }

/* Font Weights (for variable fonts) */
.font-thin { font-weight: 100; }
.font-extralight { font-weight: 200; }
.font-light { font-weight: 300; }
.font-normal { font-weight: 400; }
.font-medium { font-weight: 500; }
.font-semibold { font-weight: 600; }
.font-bold { font-weight: 700; }
.font-extrabold { font-weight: 800; }
.font-black { font-weight: 900; }

/* Persian Numerals */
.persian-numerals {
  font-variant-numeric: diagonal-fractions;
  font-feature-settings: "cv02" 1, "cv03" 1;
}

/* RTL Support */
.rtl { direction: rtl; }
.ltr { direction: ltr; }

/* Text Optimization */
.optimize-persian {
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-synthesis: none; /* Prevent fake bold/italic */
}
```

---

## 10. Performance: Preload Critical Fonts

```html
<!-- In <head> for critical fonts -->
<link rel="preload" as="font" type="font/woff2" crossorigin 
      href="https://fonts.gstatic.com/s/vazirmatn/v14/...woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin 
      href="/fonts/Vazirmatn-VariableFont_wght.woff2">

<!-- Preconnect for Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Font-display swap is handled by Google Fonts automatically -->
<!-- For self-hosted, ensure @font-face has font-display: swap -->
```

---

## Font File Download Links

| Font | WOFF2 Variable | WOFF2 Static | GitHub Releases |
|------|----------------|--------------|-----------------|
| Vazirmatn | [VF](https://github.com/rastikerdar/vazirmatn/releases/latest/download/Vazirmatn-VariableFont_wght.ttf) | [Static](https://github.com/rastikerdar/vazirmatn/releases/latest) | [Releases](https://github.com/rastikerdar/vazirmatn/releases) |
| Sahel | [VF](https://github.com/rastikerdar/sahel-font/releases/latest/download/Sahel-VF.ttf) | [Static](https://github.com/rastikerdar/sahel-font/releases/latest) | [Releases](https://github.com/rastikerdar/sahel-font/releases) |
| Estedad | [VF](https://github.com/aminabedi68/Estedad/releases/latest/download/Estedad-VariableFont_wght.ttf) | [Static](https://github.com/aminabedi68/Estedad/releases/latest) | [Releases](https://github.com/aminabedi68/Estedad/releases) |
| Lalezar | - | [Google Fonts](https://fonts.google.com/specimen/Lalezar) | [GitHub](https://github.com/googlefonts/lalezar) |
| Amiri | - | [Google Fonts](https://fonts.google.com/specimen/Amiri) | [GitHub](https://github.com/alif-type/amiri) |

**Convert TTF to WOFF2:**
```bash
# Using woff2_compress (Google's tool)
woff2_compress Vazirmatn-VariableFont_wght.ttf

# Or use Fonttools
pip install fonttools
fonttools ttf2woff2 Vazirmatn-VariableFont_wght.ttf
```