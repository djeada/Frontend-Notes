# Rendered frontend teaching examples

Open [`index.html`](index.html) in any modern browser. This project has **no dependencies** and uses semantic HTML, local CSS, and a tiny JavaScript form handler. Try the example pairs, narrow the viewport, move through the page with Tab, and submit an invalid email. The lesson's eight SVG illustrations live in [`../../assets/visual-examples/`](../../assets/visual-examples/) and are linked from the [visual gallery](../../notes/visual-examples.md).

The SVGs are **illustrative wireframes**, not automated browser screenshots. This HTML project is the runnable implementation: use browser DevTools to inspect its actual rendered output, then compare the before/after scenes. Do not mistake the intentionally poor 'before' examples for recommended accessible patterns. JavaScript validation here is a client-side demo only; a real server must validate all submitted data. The form never sends or stores personal data.

To capture real screenshots, open `index.html` in a browser and use DevTools' screenshot action at the desired viewport. If using a local server, from the repository root run `python3 -m http.server 8000` and visit `http://localhost:8000/projects/visual-examples/`. No production website or account is necessary.
