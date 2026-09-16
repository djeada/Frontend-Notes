# Frontend learning diagrams

Editable SVG diagrams embedded in the original [CSS](../../notes/02_css.md), [UX](../../notes/06_ux.md), and [protocols](../../notes/08_protocols.md) chapters live in [`../../assets/diagrams`](../../assets/diagrams). They are standalone vector files: open them in a browser or vector editor and edit the source directly. Each has a `viewBox`, a descriptive `<title>`, and a `<desc>` to supplement the surrounding prose.

- [`css-cascade.svg`](../../assets/diagrams/css-cascade.svg): a simplified checklist for diagnosing CSS declaration precedence; consult the specification for transitions, animations, layers and `!important` details.
- [`ux-loop.svg`](../../assets/diagrams/ux-loop.svg): research as an iterative process rather than a one-time handoff.
- [`request-lifecycle.svg`](../../assets/diagrams/request-lifecycle.svg): a conceptual request journey with caching and reuse as optional paths.

The SVG itself is the published asset; no raster export or third-party image dependency is required. For documentation systems requiring PNG, export one from a vector editor at an appropriate resolution and retain the SVG as source of truth. Verify label legibility at narrow widths and explain the diagram's teaching point in nearby Markdown.
