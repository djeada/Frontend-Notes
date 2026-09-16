## Additional Resources

### How to choose a resource without copying a polished mistake

This chapter is a **directory, not a certification program**. The sites below may offer free and paid assets, incompatible versions, or changing terms. When a resource looks useful, open its source and license, run the demo where possible, then test how it behaves in *your own* layout. Do not treat a beautiful screenshot as evidence of accessibility, performance or permission to redistribute its assets.

| Question | Check in practice | Document for future maintainers |
|---|---|---|
| Is reuse allowed? | Read the exact asset/template license and attribution conditions. | License URL and version/date. |
| Will it work in our stack? | Check peer dependencies, build output and supported framework version. | Package and version. |
| Can all users operate it? | Keyboard, focus, contrast, zoom, labels and errors. | Reproducible test notes. |
| Can it be modified? | Examine source, export format and component boundaries. | Local customization and owner. |
| Is it lightweight enough? | Inspect real transferred size and third-party requests. | Performance budget and tradeoffs. |
| Will it remain supported? | Review maintenance and update process. | Upgrade and replacement plan. |

**Mini case study:** choose a card design from an inspiration site. Rebuild its content with semantic `<article>`, a heading and real link. First inspect the [unstyled browser rendering](../assets/visual-examples/card-styling-browser.png), then apply its spacing and typography in the [live demo](../projects/visual-examples/index.html). Verify keyboard focus and mobile width. You may copy *ideas* while still needing permission to copy icons, photos, source code or trade dress.

**Suggested asset log:** `asset`, `source URL`, `author`, `license`, `attribution location`, `date checked`, `local filename`, `reason used`. This makes later audits and replacement feasible. Do not record “free” as a license: free price and reuse rights are different questions.


This directory collects tools for templates, components, typography, images, and design inspiration. **A link is a starting point, not an endorsement or a license grant.** Before adding an asset to a project, check its current price, license, attribution requirements, maintenance, accessibility, and compatibility with your stack. A free-to-view design is not necessarily free to copy or redistribute.

### 📄 Templates

- [Cruip](https://cruip.com/)
- [Bootswatch](https://bootswatch.com/)
- [Free HTML5](https://freehtml5.co/)
- [One Page Love](https://onepagelove.com/)
- [HTML5 UP](https://html5up.net/)
- [Colorlib Templates](https://colorlib.com/wp/templates/)
- [TemplateMo](https://templatemo.com/)
- [Start Bootstrap](https://startbootstrap.com/)
- [ThemeWagon](https://themewagon.com/)

**Evaluate a template:** inspect the HTML landmarks, heading order, keyboard navigation, small-screen behavior, bundled dependencies, and terms for commercial reuse. Run its build yourself instead of judging only the marketing preview.

### 🧩 Ready Components

- [Collect UI](https://collectui.com/)
- [Pure CSS](https://purecss.io/start/)
- [Free Frontend](https://freefrontend.com/)
- [Tailwind UI](https://tailwindui.com/)
- [MUI (Material UI)](https://mui.com/)
- [Chakra UI](https://chakra-ui.com/)
- [React Bootstrap](https://react-bootstrap.github.io/)
- [Flowbite](https://flowbite.com/)

These are **different kinds of resources**, not interchangeable component libraries. Collect UI is inspiration; a production component needs working interaction, focus management, semantics, documentation, and version compatibility. Check whether copied snippets require a framework, build step, icon package, or CSS reset.

### 🎨 CSS Generators

#### Inspect generated output and make it responsive

A generator may produce attractive declarations that behave poorly under different widths or color schemes. Rather than pasting a preset and stopping, rewrite the smallest reproducible test:

```html
<div class="generated-card">
  <h2>News</h2>
  <p>A very long translated description belongs here.</p>
  <a href="/news">Read the news</a>
</div>
```

```css
.generated-card {
  box-sizing: border-box;
  width: min(100%, 28rem);
  padding: clamp(1rem, 2vw, 1.5rem);
  border-radius: 1rem;
  background: #fff;
  color: #0f172a;
}
.generated-card a:focus-visible {
  outline: 3px solid #1d4ed8;
  outline-offset: 3px;
}
```

Compare the [actual styled-card capture](../assets/visual-examples/card-styling-browser.png). A generated blur or shadow may have contrast and performance costs; a CSS-only animation should respect reduced-motion preferences when motion is nonessential. Neumorphic controls sometimes lack clear boundaries, so check affordances and focus instead of selecting them purely by appearance. Test at 320px, zoom to 200%, add long text, and inspect computed styles. Keep the generated source and its original license where the tool provides one.


- [Fancy Border Radius](https://9elements.github.io/fancy-border-radius/)
- [CSS Separator Generator](https://wweb.dev/resources/css-separator-generator/)
- [Grid Layout It](https://grid.layoutit.com/)
- [Animista](https://animista.net/)
- [CSS Grid Generator](https://cssgrid-generator.netlify.app/)
- [Neumorphism.io](https://neumorphism.io/)
- [CSS Clip Path Maker](https://bennettfeely.com/clippy/)
- [Glassmorphism Generator](https://hype4.academy/tools/glassmorphism-generator)

**Try this:** generate a two-column grid, then resize the viewport and increase text size to 200%. Inspect the generated CSS; generators can produce fixed widths, overflow, low contrast, or motion that needs a reduced-motion alternative.

### 🎨 Graphical Elements

#### Images, icons and illustrations: use the right alternative text

The correct alternative depends on the **purpose in context**:

```html
<!-- Content image: describe information not otherwise present. -->
<img src="chart.png" alt="Revenue increased from January to March"
     width="640" height="360">

<!-- Decorative flourish: empty alternative, not the filename. -->
<img src="divider.svg" alt="" width="120" height="16">

<!-- An icon-only action still needs a name. -->
<button type="button" aria-label="Close dialog">
  <svg aria-hidden="true" viewBox="0 0 24 24" width="24" height="24">
    <path d="M5 5 19 19M19 5 5 19" stroke="currentColor"/>
  </svg>
</button>
```

Meaningful chart content often deserves an adjacent table or longer text explanation, not a 150-word `alt` attribute. Give content images dimensions or an aspect ratio to reserve layout space, and choose `loading="lazy"` for suitable below-the-fold images rather than applying it blindly to the hero image. An image's source URL, screenshot appearance and file extension do not establish its license.

**Try it:** take the [semantic browser screenshot](../assets/visual-examples/semantic-html-browser.png); write alternative text describing *the difference it teaches*, not every color or decorative rectangle. Compare this with an icon-only button's accessible name. Reference: [W3C image tutorial](https://www.w3.org/WAI/tutorials/images/).


#### UI Designs

- [UI Design Daily](https://uidesigndaily.com/)
- [Land Book](https://land-book.com/)
- [CSS Nectar](https://cssnectar.com/)
- [Dribbble](https://dribbble.com/)
- [Behance](https://www.behance.net/)
- [Mobbin](https://mobbin.com/)

Inspiration is useful for exploring layout ideas; do not copy someone else's brand, assets, or interface without permission. Evaluate whether a design still works with long translated labels, validation errors, and keyboard focus.

#### 🖼️ Icons

- [Swift Icons](https://www.swifticons.com)
- [Fontastic](https://fontastic.me/)
- [Flaticon](https://www.flaticon.com/)
- [Icon-Icons](https://icon-icons.com/)
- [Icon54](https://icon54.com/)
- [Font Awesome](https://fontawesome.com/)
- [Heroicons](https://heroicons.com/)
- [Feather Icons](https://feathericons.com/)

Decorative icons should be hidden from assistive technology; an icon-only button needs an accessible name describing its action. Confirm the icon-set license and avoid mixing incompatible visual styles without intent.

#### 📷 Stock Photos

- [Unsplash](https://unsplash.com/)
- [Burst Shopify](https://burst.shopify.com/)
- [Magdeleine](https://magdeleine.co/browse/)
- [Life of Pix](https://www.lifeofpix.com/)
- [Stocksnap](https://stocksnap.io/)
- [Pexels](https://www.pexels.com/)
- [Pixabay](https://pixabay.com/)
- [Reshot](https://www.reshot.com/)

Check the **specific image's** permitted uses, identifiable-person releases when relevant, and attribution terms. Compress images, give meaningful content images appropriate `alt` text, and use empty `alt=""` for decorative images.

#### Transparent Images

- [PNG Tree](https://pngtree.com/)
- [Pure PNG](https://purepng.com/)
- [Stick PNG](https://www.stickpng.com/)
- [PNGBarn](https://www.pngbarn.com/)
- [CleanPNG](https://www.cleanpng.com/)

Transparency does not mean an image is public domain. Verify licensing and whether a file actually has a transparent alpha channel.

#### 🛡️ Logos

- [Logo Inspirations](https://www.logoinspirations.co/)
- [LogoLynx](https://www.logolynx.com/)
- [LogoMakr](https://logomakr.com/)

Logos can involve trademarks as well as copyright. Inspiration or a download link is not permission to use another organization's mark as your own.

#### 🎡 Vectors

- [Scribbbles Design](https://www.scribbbles.design/)
- [Freepik Vectors](https://www.freepik.com/vectors)
- [Vecteezy](https://www.vecteezy.com/)

#### 3D Elements

- [Spline](https://spline.design/)
- [Shapefest](https://www.shapefest.com/)
- [Vectary](https://www.vectary.com/)
- [Shape](https://shape.so/)
- [Three.js Journey](https://threejs-journey.com/)

For animated 3D, check performance on modest devices, provide a static fallback when appropriate, and respect reduced-motion preferences.

#### 🌈 Gradients

- [Mesh Gradient](https://meshgradient.com/)
- [Grabient](https://www.grabient.com/)
- [Gradient Hunt](https://gradienthunt.com/)
- [Meshy](https://meshy.uxie.io/)
- [WebGradients](https://webgradients.com/)

#### 🌊 Animated Backgrounds

- [Animated Backgrounds](https://animatedbackgrounds.me/)
- [SVG Backgrounds](https://www.svgbackgrounds.com/)

#### 📊 Flow Charts

- [Excalidraw](https://excalidraw.com/)
- [Flowmapp](https://www.flowmapp.com/)
- [Lucidchart](https://www.lucidchart.com/)
- [Miro](https://miro.com/)

### 🎨 Mockups

- [Mockup Bro](https://mockupbro.com/)
- [Smartmockups](https://smartmockups.com/)
- [Mockup World](https://www.mockupworld.co/)

### 🎵 Font resources

- [Velvetyne](http://velvetyne.fr/)
- [Google Fonts](https://fonts.google.com/)
- [Font Squirrel](https://www.fontsquirrel.com/)
- [DaFont](https://www.dafont.com/)

Download only fonts with appropriate web-embedding rights, inspect weights and language coverage, and consider font-loading performance and fallbacks.

### 🔧 Utility

- [Remove Background](https://www.remove.bg/de)
- [PicWish](https://picwish.com)
- [Screens Tab](https://www.screenstab.com/editor/)
- [Let's Enhance](https://letsenhance.io/)
- [Auto Draw](https://www.autodraw.com/)
- [Colors and Fonts](https://www.colorsandfonts.com/)
- [TinyPNG](https://tinypng.com/)
- [SVGOMG](https://jakearchibald.github.io/svgomg/)
- [Figma](https://www.figma.com/)

Check the privacy policy before uploading private customer photos, unreleased brand materials, or proprietary designs to online utilities.

### 🎨 Color palettes

#### Test a palette on real interface states

A hex value must contain three, four, six or eight hexadecimal digits as supported by CSS; characters such as `K`, `S`, `G` or `%` are invalid in a hex color. The malformed codes in the older palette list were corrected in the earlier revision; do not assume that makes every remaining combination readable. A palette with five attractive swatches may fail when applied to small text, form errors, focus outlines and disabled controls.

```css
:root {
  --surface: #fff;
  --ink: #0f172a;
  --link: #1d4ed8;
  --focus: #0f172a;
}
body { background: var(--surface); color: var(--ink); }
a { color: var(--link); }
a:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

These are **example roles**, not a guarantee for every background or text size. Check actual foreground/background combinations against the applicable WCAG contrast criteria (commonly at least 4.5:1 for ordinary text and 3:1 for large text under WCAG 2.x AA), with separate evaluation for non-text UI boundaries and focus indicators. Test both light/dark variants, forced colors and invalid/disabled states. Color must not be the only way to identify a form error.

**Exercise:** choose one palette above, assign a surface, text, link, error and focus role, and test the [form and button browser screenshots](../assets/visual-examples/form-validation-browser.png) and [button states](../assets/visual-examples/button-states-browser.png). If a combination fails contrast, adjust the role value and document what changed. Reference: [WCAG contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).


- [Coolors](https://coolors.co/)
- [Color Hunt](https://colorhunt.co/)
- [Happy Hues](https://www.happyhues.co/)
- [Paletton](https://paletton.com/)
- [Adobe Color](https://color.adobe.com/)

A CSS hexadecimal color uses `#RGB`, `#RGBA`, `#RRGGBB`, or `#RRGGBBAA` with **hexadecimal digits only (0–9, A–F)**. Several palette codes in the previous version of this section contained invalid characters such as `K`, `O`, `S`, and `%`. Rather than silently guess the intended colors, those invalid entries are explicitly marked for replacement below. Valid samples are retained:

- **AI Takeover:** `#FD76CB #FFAC30 #000000 #FFFEFD`
- **Spaceship:** `#6B9FED #24F9F9 #A1A7C8 #FFFFFF`
- **Humanoid:** `#5AC994 #C0F7B7 #123143 #141B29`
- **Singularity:** second and subsequent recorded colors `#15265C #2EE09A #FFFFFF`; original first code `#EF84F%` is invalid and needs a designer-approved replacement.
- **Lake:** `#284445 #216A7E`; original repeated the second code four times. Choose additional intentional accents rather than treating the duplicates as distinct colors.
- **Rio:** original values `#298CK #DEBSA2 #597678 #24322E #BESA2E` include invalid codes; recover intended colors from the source design before using.
- **Tokyo:** original values `#DG0B3F #ODA6B5 #DOA4A4 #18CCCE #175F78` include invalid codes; keep only valid `#18CCCE #175F78` until the rest are verified.
- **Montreal:** `#1A9FAC #755822 #282422 #9F8668 #DDDEDD`
- **Berlin:** `#7B1B1E #AE7F31 #241B18 #F2EFE9 #807F6E`
- **New York:** `#E0372E #6B3620 #5D5765 #D7BFB4 #8696CF`

**Before choosing a palette**, test combinations for text contrast (typically 4.5:1 for normal text under WCAG AA), distinguish hover/focus/error states without relying on color alone, and preview light/dark modes. A palette is a starting point, not proof of accessibility.

### 🖋️ Font examples

- Ambit
- Helvetica Now
- Avenir Next Pro
- Plantin
- Futura PT
- TT Norms
- Brandon Grotesque
- Inter
- Manrope
- Space Grotesk

These are font names, not necessarily free or redistributable fonts. Check the exact family and license before embedding.

### 📚 Glossaries & Guides

- [Qualtrics UX Design Glossary](https://www.qualtrics.com/blog/ux-design-glossary/)
- [NNG UX Glossary](https://www.nngroup.com/articles/ux-glossary/)
- [UX Design.cc Glossary](https://uxdesign.cc/the-ux-glossary-5c30c4e2c8b6)
- [Usability.gov UX Basics](https://www.usability.gov/what-and-why/user-experience.html)
- [Smashing Magazine UX Guide](https://www.smashingmagazine.com/guides/ux-design/)
- [UX Design Institute Glossary](https://www.uxdesigninstitute.com/resources/ux-glossary/)
- [Interaction Design Foundation Glossary](https://www.interaction-design.org/literature/topics/ux-glossary)

Some older sites may have moved or disappeared. Before recommending an external link, confirm it loads, is maintained, and still covers the intended subject.

### A practical resource-selection checklist

1. **Purpose:** Does the tool solve a real requirement or merely add a dependency?
2. **License and cost:** Can you use, modify, redistribute, and deploy it under current terms?
3. **Accessibility:** Can the demo be operated by keyboard and at increased zoom? Are controls labeled?
4. **Maintenance:** When was it last updated, and what browsers/framework versions does it support?
5. **Performance and privacy:** What code, images, fonts, and third-party requests will ship to users?
6. **Reproducibility:** Can a teammate run the example from a documented dependency version?

**References:** [MDN: CSS hex colors](https://developer.mozilla.org/en-US/docs/Web/CSS/hex-color), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [MDN: alternative text](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img).