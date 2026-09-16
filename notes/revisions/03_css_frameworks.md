# CSS frameworks and preprocessors: what runs where

[Original frameworks chapter](../03_css_frameworks.md) · [All chapter updates](README.md)

A **preprocessor** transforms source (such as SCSS or Less) into browser-readable CSS at build time. A **CSS framework** supplies styling conventions, components, or utility classes. Some tools combine these roles, but neither is required to use modern CSS.

## Corrections to the original

1. There is no single latest language release called **CSS4**. CSS is maintained in independently versioned modules, such as Selectors Level 4 and CSS Nesting Level 1.
2. `@apply .parent` is **not a standard CSS inheritance mechanism**. Tailwind has its own build-time `@apply` directive for utility classes; a browser must not be expected to expand it. Ordinary CSS can share declarations via a common class, custom properties, or an appropriate selector.
3. Native CSS **supports nesting**. The original claim that CSS lacks a direct equivalent to preprocessor nesting is outdated. Native nesting is parsed by the browser, while SCSS nesting is compiled.
4. CSS `calc()` is evaluated through the CSS value-processing pipeline in the browser; Sass arithmetic normally runs during compilation. These operations are not interchangeable in every context.
5. Sass `%placeholder` plus `@extend` is selector extension, not JavaScript-style prototype or class inheritance. The original `child` selector targets a literal HTML element named `child`; use `.child` for a class.

## Modern CSS first

```css
:root { --accent: rebeccapurple; }
.card {
  border: 2px solid var(--accent);
  & .card__title { color: var(--accent); }
  &:hover { box-shadow: 0 2px 12px #0002; }
}
```

This native CSS works without Sass. In SCSS, `$accent` is a compile-time variable; in CSS, `--accent` is a custom property that can participate in inheritance and change at runtime. The syntaxes look similar but have different semantics.

```scss
@use 'sass:math';
$spacing: 1rem;
.card {
  padding: $spacing;
  &__title { margin-block-end: math.div($spacing, 2); }
}
```

SCSS allows selector concatenation with `&__title`, and the Sass `math.div()` function performs arithmetic without relying on deprecated slash division. Native CSS nesting does **not** support concatenating `&` into a class name in that way. Choose a preprocessor when its specific build-time features justify another dependency; choose a framework when its conventions and maintenance costs fit the project.

## Exercise

Build the same small card twice: once in plain CSS with custom properties and native nesting, and once with a utility framework. Compare source size, generated output, clarity, keyboard focus, and whether a build step is necessary. Do not infer performance from framework popularity alone.

**References:** [W3C: CSS Snapshot](https://www.w3.org/TR/css-2026/), [MDN: nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting), [Tailwind: directives](https://tailwindcss.com/docs/functions-and-directives), [Sass: breaking changes to slash division](https://sass-lang.com/documentation/breaking-changes/slash-div/).
