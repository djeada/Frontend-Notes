# HTML: semantics, forms, and accessible content

[Original HTML chapter](../01_html.md) · [All chapter updates](README.md)

This companion chapter refines the existing introduction. HTML describes the *meaning and structure* of content; the browser constructs a DOM from the markup. CSS controls presentation and JavaScript adds behavior, but HTML alone should provide a usable reading order and functional links and forms.

## Corrections to the original

- An HTML element is not always represented by both an opening and closing tag: `img`, `input`, and `br` are **void elements**. A tag is the markup syntax; an element is the resulting document structure.
- `<!doctype html>` is not a version selector. Its practical purpose in HTML documents is to trigger **no-quirks (standards) mode**. Do not describe it as telling the browser to interpret a page specifically as HTML5.
- An image's `alt` is an *alternative* appropriate to its purpose, not necessarily a literal visual description. Use `alt=""` for purely decorative imagery; give meaningful images concise informative alternatives. Linked images need alternatives that convey the link's purpose.
- The `meta name="keywords"` example should not be presented as an SEO technique. Prefer a descriptive title, useful content, logical headings, and an appropriate description; search engines decide whether to show the description.
- A viewport meta tag enables a device-width viewport but **does not make a layout responsive on its own**. Flexible layouts, sensible image sizing, and testing at varied widths still matter.

## A complete, usable document

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Workshop registration</title>
  </head>
  <body>
    <a href="#content">Skip to main content</a>
    <header><nav aria-label="Main"><a href="/">Home</a></nav></header>
    <main id="content">
      <h1>Register for a workshop</h1>
      <form action="/register" method="post">
        <label for="email">Email address</label>
        <input id="email" name="email" type="email" autocomplete="email" required>
        <button type="submit">Register</button>
      </form>
    </main>
  </body>
</html>
```

The example uses a real label (a placeholder is not a substitute), a named form control so the server receives a field, a meaningful page title, and landmarks. The server must still validate input: `required` and `type="email"` help users but do not establish trust.

## Choosing elements by behavior

Use `<a href="...">` to **navigate** and `<button type="button">` for an **action**. A button inside a form defaults to submission unless its `type` says otherwise. Use `<section>` for a thematically grouped part of a document, generally with a heading; do not add `section` around everything. `<div>` and `<span>` are useful when no semantic element fits. Use tables for tabular data, not page layout, with `<th scope="col">` or `<th scope="row">` where appropriate.

## Practice

Build a two-page event site: one heading per page describing its subject, descriptive link text, an image with suitable alternative text, and a registration form. Navigate using only Tab, Shift+Tab, and Enter; then disable CSS and confirm the content still reads in order. Inspect the browser's accessibility tree and submit invalid form values to see what the browser checks versus what the server must check.

**References:** [HTML Living Standard](https://html.spec.whatwg.org/multipage/), [MDN: standards and quirks mode](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Quirks_mode_and_standards_mode), [MDN: images and alternative text](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img), [MDN: client-side validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation).
