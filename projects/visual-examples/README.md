# Rendered frontend teaching examples

Open [`index.html`](index.html) in a modern browser. This project has **no dependencies** and uses local HTML, CSS, and a small JavaScript form handler. Try the example pairs, narrow the viewport, move through the page with Tab, and submit an invalid email. The eight SVG illustrations are in [`assets/visual-examples`](../../assets/visual-examples) and linked from the [visual gallery](../../notes/visual-examples.md).

The SVGs are **illustrative wireframes**, not automated browser screenshots. The HTML project is the runnable implementation: use browser DevTools to inspect its actual rendered output, then compare the before/after scenes. The semantic pair consists of two separate full documents, [`semantic-before.html`](semantic-before.html) and [`semantic-after.html`](semantic-after.html), embedded in independent iframes so neither example nests a page-level `<main>` inside another.

The intentionally poor 'before' examples are comparisons, **not recommended accessible patterns**. JavaScript validation here is client-side only; a real server must validate submitted data. The form never sends or stores personal data.

To capture actual browser screenshots, open `index.html` and use your browser's screenshot action at the desired viewport. Alternatively, from the repository root run `python3 -m http.server 8000` and visit `http://localhost:8000/projects/visual-examples/`. No production website or account is necessary.
