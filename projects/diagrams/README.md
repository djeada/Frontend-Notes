# Frontend learning diagrams

Editable SVG diagrams used by the updated companion chapters live in [`../../assets/diagrams`](../../assets/diagrams). They are authored as standalone vector files: open them in a browser or vector editor and edit the source directly. Each has a `viewBox`, a descriptive `<title>`, and a `<desc>` so readers do not have to depend only on the drawing.

- [`css-cascade.svg`](../../assets/diagrams/css-cascade.svg): authoring checklist for CSS declaration precedence. Intentionally simplified; see the CSS cascade reference for animation, transition, and `!important` details.
- [`ux-loop.svg`](../../assets/diagrams/ux-loop.svg): research as an iterative process rather than a one-time handoff.
- [`request-lifecycle.svg`](../../assets/diagrams/request-lifecycle.svg): a request journey that marks caching and reuse as optional.

The SVG itself is the published asset; no raster export or third-party image dependency is required. For documentation systems requiring a PNG, export one from a vector editor at an appropriate resolution and keep the SVG as the source of truth. Check that diagram labels remain readable at narrow widths and that the surrounding Markdown explains the diagram in text.
