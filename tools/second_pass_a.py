#!/usr/bin/env python3
"""One-time, anchored additions to the ORIGINAL chapters 01–07.

The companion-note experiment is not reinstated. This script runs in a one-time
workflow, validates its anchors, and is deleted by that workflow after use.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / 'notes'
modified = set()


def insert(filename, heading, body):
    path = NOTES / filename
    source = path.read_text(encoding='utf-8')
    assert source.count(heading + '\n') == 1, f'{filename}: missing or ambiguous heading {heading!r}'
    assert body.strip().splitlines()[0] not in source, f'{filename}: already inserted'
    result = source.replace(heading + '\n', heading + '\n\n' + body.strip() + '\n\n', 1)
    path.write_text(result, encoding='utf-8')
    modified.add(filename)


def correct(filename, old, new):
    path = NOTES / filename
    text = path.read_text(encoding='utf-8')
    assert old in text, f'{filename}: correction anchor missing: {old[:75]!r}'
    path.write_text(text.replace(old, new), encoding='utf-8')
    modified.add(filename)

# 01: original HTML note — retain its tag reference and put worked examples
# immediately beside the document structure, links, tables and form topics.
insert('01_html.md', '### Document Structure', """#### Worked page: structure, behavior, and visual output

The browser parses HTML into a document tree. CSS styles that tree; JavaScript can update it. A semantic page can be styled to look identical to a page made entirely of generic `<div>` elements, yet expose more useful navigation landmarks. Compare the [browser-rendered before/after screenshot](../assets/visual-examples/semantic-html-browser.png) with the [two runnable documents](../projects/visual-examples/semantic-before.html) and [semantic version](../projects/visual-examples/semantic-after.html). The screenshot demonstrates appearance, not an accessibility-test result.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Field notes — latest posts</title>
  <link rel="stylesheet" href="style.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a href="#content">Skip to content</a>
  <header>
    <a href="/">Field notes</a>
    <nav aria-label="Primary"><a href="/posts">Posts</a></nav>
  </header>
  <main id="content">
    <h1>Latest posts</h1>
    <article>
      <h2><a href="/posts/one">First experiment</a></h2>
      <p>What changed and what we learned.</p>
    </article>
  </main>
  <footer><p>© Field notes</p></footer>
</body>
</html>
```

The `defer` script runs after HTML parsing and before `DOMContentLoaded`, in document order relative to other deferred classic scripts; a module script is deferred by default. A heading describes content hierarchy, whereas `<header>`, `<nav>`, `<main>`, `<article>`, and `<footer>` communicate regions or content type. A skip link must lead to an existing ID. On a normal page, do not create multiple visible page-level `<main>` elements.

**Try it:** save the HTML as `index.html`, create an empty `style.css` and `app.js`, then open it in a browser. Check the document title, skip link, headings, and accessibility-tree landmarks. Disable CSS: the reading order should still make sense. Resize to 320 CSS pixels and 200% zoom: the viewport meta tag alone will not prevent overflow. Reference: [MDN document and website structure](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents).""")

insert('01_html.md', '#### Links', """##### Link behavior and accessible names: compare these examples

```html
<!-- Destination is clear when read out of context. -->
<a href="/pricing">View pricing plans</a>

<!-- Navigation uses a link; an action uses a button. -->
<a href="/account">Your account</a>
<button type="button" id="save">Save draft</button>

<!-- An icon-only link still needs a usable accessible name. -->
<a href="/search" aria-label="Search the site">
  <svg aria-hidden="true" viewBox="0 0 24 24" width="24" height="24">
    <circle cx="10" cy="10" r="6" fill="none" stroke="currentColor"/>
    <path d="m15 15 6 6" stroke="currentColor"/>
  </svg>
</a>
```

Avoid five identical links labeled “Read more”: screen-reader users may navigate by link name, so include the destination or surrounding context in the accessible name. The `download` attribute does not guarantee a download for arbitrary cross-origin URLs; server headers and browser behavior matter. `mailto:` invokes a configured email handler rather than sending email directly. If an external link deliberately opens a new tab, tell the reader when this matters and consider `rel="noopener"` (modern browsers implicitly apply this to `target="_blank"`, but explicit intent helps explain security).

**Exercise:** tab through the three examples with the browser's keyboard navigation. Replace the SVG with an image missing `alt`, inspect the accessible name, and correct it. Avoid putting a clickable button inside a clickable link: nested interactive controls have confusing activation behavior. Reference: [MDN links](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Creating_links).""")

insert('01_html.md', '#### Tables', """##### Data-table example: expose relationships, not only gridlines

A visual grid is not enough to express which header explains a data cell. Give a real data table a caption, mark headers with `<th>`, and use `scope` for straightforward row/column relationships. Do not use a `<table>` simply to create a two-column page layout: CSS Grid is designed for layout.

```html
<table>
  <caption>Course enrollment, autumn term</caption>
  <thead>
    <tr><th scope="col">Course</th><th scope="col">Students</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">HTML</th><td>24</td></tr>
    <tr><th scope="row">CSS</th><td>18</td></tr>
  </tbody>
</table>
```

**Rendered expectation:** a caption above the table, two column headings and two labeled rows. Without CSS, it still reads as structured data. `scope="row"` associates “HTML” with 24; `scope="col"` associates “Students” with that column. For complex multi-level headers, consider explicit `id`/`headers` associations rather than assuming `scope` solves every arrangement. Avoid hiding essential table content on mobile; overflow scrolling may be preferable to discarding columns.

**Exercise:** add a third row and use a screen-reader table-navigation mode if available. Verify which row and column headers are announced. Reference: [MDN HTML table accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Table_accessibility).""")

insert('01_html.md', '### Interactive elements', """#### Complete accessible form: inputs, validation, and submission

![Actual browser before/after comparison of form validation](../assets/visual-examples/form-validation-browser.png)

HTML provides labels, input types, form ownership and submission semantics; CSS can expose states; JavaScript can add tailored feedback. `placeholder` is only an example hint, never a persistent label. The [runnable form](../projects/visual-examples/index.html) stays on the client for the exercise; the sample below illustrates a real POST endpoint, which needs server implementation and validation.

```html
<form action="/subscribe" method="post">
  <fieldset>
    <legend>Newsletter preferences</legend>
    <label for="address">Email address</label>
    <p id="address-help">We use this address for newsletter messages.</p>
    <input id="address" name="email" type="email"
           autocomplete="email" aria-describedby="address-help" required>
    <label><input type="checkbox" name="digest" value="weekly">
      Send a weekly digest</label>
  </fieldset>
  <button type="submit">Subscribe</button>
  <button type="reset">Clear form</button>
</form>
```

`name` determines the submitted field key; `id` connects a label to a control; `value` identifies a selected checkbox in form data; unchecked checkboxes normally contribute no field. `type="email"` and `required` perform constraint checks but do not guarantee that an address exists or that submissions are safe. `method="get"` places form data in the URL; avoid it for passwords and sensitive data. POST does not provide confidentiality unless the page and endpoint use HTTPS. A reset button discards input, so many production forms should omit it.

**Check it:** submit the blank form, enter `not-an-email`, then try a syntactically valid address. Observe native validation, inspect the Network panel on a controlled endpoint, and verify that server errors are also shown next to the relevant field. Reference: [MDN client-side form validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation).""")

# 02 CSS: teach *measured* layout rather than generic descriptions.
insert('02_css.md', '### Understanding Selectors', """#### Worked selector exercise: why the blue rule wins

```html
<p class="message" id="status">Saved successfully</p>
```

```css
p { color: green; }                  /* type selector: 0-0-1 */
.message { color: purple; }          /* class selector: 0-1-0 */
#status { color: blue; }             /* ID selector: 1-0-0 */
```

Assuming these normal declarations share an origin and cascade layer, the text is **blue**, despite the green rule appearing first and the purple rule appearing second. The ID selector is more specific. Specificity is not a universal score: origin, importance, cascade layers and other cascade stages can take precedence. Inline styles and declarations in transitions have special rules too. Use DevTools' Styles pane to see which rule wins and *why*, and the Computed pane for the final value.

**Try it:** replace `#status` with `.message`, then reverse the last two rules. When selector specificity ties at the same cascade stage, later source order wins. Add `@layer base, components;`, place one class rule in each named layer, and observe that layer order matters before specificity for normal declarations. Do not use `!important` as a routine override. Read the [MDN cascade guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction) before combining importance and layers: their precedence reverses for important declarations.""")

insert('02_css.md', '### Box Model', """#### Calculate the actual box size before debugging overflow

Imagine a product card with `width: 320px`, `padding: 24px` on both sides and a `2px` border on both sides. Under the default `box-sizing: content-box`, its border-box width is `320 + 48 + 4 = 372px`; margins are additional spacing outside the border. Under `border-box`, the *declared* 320px includes padding and border, so the content area is `268px` when dimensions can resolve. The original box diagram below is a conceptual illustration; actual measurements come from DevTools.

```css
/* Apply predictable sizing to elements and their pseudo-elements. */
*, *::before, *::after { box-sizing: border-box; }
.card {
  width: min(100%, 20rem);
  padding: 1.5rem;
  border: 2px solid #64748b;
  margin-inline: auto;
}
```

A fixed `width: 400px` on a 320px viewport will overflow regardless of a viewport meta tag. `width: min(100%, 20rem)` keeps this card within the parent's available width in the ordinary case. Long unbroken strings, min-content constraints and oversized media can still overflow: inspect the specific element rather than hiding all page overflow. `margin-inline: auto` distributes spare inline-axis space on a block with a definite used width; it does not vertically center an arbitrary element.

**Exercise:** add `overflow-wrap: anywhere` to a paragraph containing a long URL. Compare its computed width before and after, then toggle `box-sizing` in DevTools. Adjacent vertical margins of normal-flow blocks may collapse, but Flexbox/Grid item margins do not collapse in the same way. Reference: [MDN box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model).""")

insert('02_css.md', '### Flexbox', """#### Build and test a wrapping toolbar

![Actual browser rendering: scattered controls versus an aligned wrapping toolbar](../assets/visual-examples/flex-alignment-browser.png)

```html
<div class="toolbar">
  <h2>My tasks</h2>
  <div class="toolbar__actions">
    <button type="button">Filter</button>
    <button type="button">New task</button>
  </div>
</div>
```

```css
.toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.75rem;
}
.toolbar__actions { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.toolbar h2 { margin: 0; }
```

`justify-content` has an effect when the flex line has distributable free space. `align-items` aligns across the main axis (the cross axis); `align-content` matters primarily when there are **multiple flex lines** and spare cross-axis space. `flex: 1` is a shorthand, not simply `flex-grow: 1`; check the computed grow, shrink and basis values. When a long label refuses to shrink, try `min-width: 0` on the appropriate flex item and allow text to wrap instead of clipping it.

**Before/after test:** compare the [runnable toolbar](../projects/visual-examples/index.html) at wide and narrow widths. Force 200% zoom, add a very long translated button label, and confirm that the controls remain visible. `order` changes visual arrangement but not necessarily reading or keyboard focus order, so do not use it to repair the DOM sequence. Reference: [MDN Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts).""")

insert('02_css.md', '### Integrating CSS with HTML', """#### Separate content from presentation, then verify the result

A small card is a useful controlled experiment: keep the **same HTML** before and after, then toggle only the CSS class. This isolates the effect of styling from changes in text, structure or JavaScript. The [actual Chromium screenshot](../assets/visual-examples/card-styling-browser.png) shows both rendered states side by side.

```html
<article class="course-card">
  <h2>Starter course</h2>
  <p>Learn to build a small web page.</p>
  <a href="/courses/starter">View course</a>
</article>
```

```css
.course-card {
  max-width: 28rem;
  padding: 1.5rem;
  border: 1px solid #cbd5e1;
  border-radius: 0.75rem;
  background: white;
  color: #0f172a;
}
.course-card h2 { margin-block: 0 0.5rem; line-height: 1.2; }
.course-card p { max-width: 60ch; }
.course-card a:focus-visible { outline: 3px solid #1d4ed8; outline-offset: 3px; }
```

**What changes:** padding creates interior breathing room; the border defines grouping; a constrained line length improves scanning; a visible focus indicator preserves keyboard discoverability. CSS does not confer HTML semantics on its own. If the source markup uses a `<div>` instead of `<article>`, simply making it look like a card does not change its semantic role. Try disabling the stylesheet and confirm that headings and links remain usable.""")

# 03 CSS tooling — runnable input/output, concrete distinction and migration path.
insert('03_css_frameworks.md', '### CSS Preprocessors', """#### Choose native CSS, a preprocessor, or a framework by problem

These solve *different* problems. Native CSS is what browsers parse. Sass/Less preprocess source into CSS before the browser sees it. Frameworks may supply design conventions, components, utility classes or build tooling; using Bootstrap or Tailwind does not mean the browser understands Sass variables or Tailwind directives. A small static site might need neither a preprocessor nor a framework.

| Requirement | First thing to try | Add a tool when… |
|---|---|---|
| Reusable runtime colors | `--accent` and `var(--accent)` | You need build-time theme generation or module conventions. |
| Nested selectors | Native CSS nesting | A project already has Sass or needs Sass-specific features. |
| Responsive components | Media/container queries and Grid/Flexbox | Shared component patterns justify a design system. |
| Repeated CSS declarations | Classes, selectors, custom properties | Mixins generate meaningfully different declarations. |
| Component libraries | Native accessible controls + your CSS | A maintained library meets verified requirements. |

A preprocessor's variables disappear or are substituted during compilation, while native CSS custom properties participate in the cascade at runtime. A CSS framework does not automatically provide accessibility, low bundle size or an appropriate design. Measure actual output and inspect generated styles rather than choosing tools based on a broad popularity claim.

**Practical experiment:** start with the [existing styled-card browser example](../projects/visual-examples/index.html), change a custom property in DevTools, then compile a separate Sass variable to CSS. A runtime CSS variable can respond to the cascade without rebuilding; editing `$accent` in Sass requires recompilation. Reference: [Sass variables](https://sass-lang.com/documentation/variables/) and [MDN custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/--*).""")

insert('03_css_frameworks.md', '##### Variables', """###### One theme implemented two ways — predict the generated CSS

```css
:root { --accent: #1d4ed8; }
.card { border-color: var(--accent); }
.card[data-tone="warning"] { --accent: #b45309; }
```

When `data-tone="warning"` is on the card, its own custom-property value wins through the cascade; the border updates without recompiling. Custom properties are not simple text macros: `var(--missing, red)` uses a fallback when the referenced property is invalid or absent as needed, and invalid computed values can invalidate an entire property declaration.

```scss
$accent: #1d4ed8;
.card { border-color: $accent; }
```

Compiling the Sass example emits an ordinary CSS color declaration. To change the theme in the browser after compilation, add native CSS custom properties or generate extra theme selectors. Sass modules use `@use`/`@forward`; avoid introducing new projects that depend on the old global `@import` workflow. **Exercise:** inspect the compiled output, then try changing `$accent` in browser DevTools (it is not a CSS property and has no effect). Reference: [Sass module system](https://sass-lang.com/documentation/at-rules/use/).""")

insert('03_css_frameworks.md', '##### Nesting', """###### Compare native nesting with compiled Sass output

```css
/* Native CSS: the browser parses the nested selector. */
.card {
  padding: 1rem;
  & .card__title { margin-block: 0; }
  &:focus-within { outline: 2px solid currentColor; }
}
```

```scss
/* Sass source: the build tool outputs regular CSS. */
.card {
  padding: 1rem;
  & .card__title { margin-block: 0; }
}
```

Both examples express the relationship, but they are processed by different systems. The first can be loaded directly in modern browsers supporting native nesting; the second must go through Sass when it uses `.scss` syntax and Sass-only features. Native nesting is not an excuse for deep selector chains: `.card .header .nav .item .label` is harder to override than a small explicit component class. `&` represents the parent selector, and changes such as `.card { &.featured { ... } }` match the *same element* with both classes, not a descendant.

**Exercise:** toggle `.card__title` and `.card.featured` classes in DevTools and explain which selector matches. Use the [browser card comparison](../assets/visual-examples/card-styling-browser.png) to connect the code to visible grouping. Reference: [MDN CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting).""")

insert('03_css_frameworks.md', '#### Step-by-step guide to creating LESS projects', """##### Prefer a reproducible project-local installation

The global installation described below is historically common, but a project-local compiler pins the dependency in `package.json` and makes onboarding and CI more predictable. For a new disposable example:

```bash
mkdir hello-less && cd hello-less
npm init -y
npm install --save-dev less
```

Create `src/theme.less`:

```less
@accent: #1d4ed8;
.card {
  border: 2px solid @accent;
  &__title { color: @accent; }
}
```

Compile it with `npx lessc src/theme.less dist/theme.css` **after creating `dist`** (`mkdir -p dist` on Unix-like systems). Add scripts such as `"build:css": "lessc src/theme.less dist/theme.css"` to `package.json` so a colleague can run `npm run build:css`; check the generated file into version control only if your deployment and repository policy require it. The HTML page must link to `dist/theme.css`, not directly to the `.less` source. **Verify:** open the output file and make sure it contains valid `.card` and `.card__title` rules; inspect the same styles on the rendered card. Reference: [Less command-line usage](https://lesscss.org/usage/).""")

# 04 JavaScript — types, event loop, DOM, fetch and testable code.
insert('04_javascript.md', '#### Numbers', """##### Numbers: precision, conversion, and input boundaries

JavaScript `Number` uses IEEE 754 binary floating-point. Most decimal fractions cannot be represented exactly, so `0.1 + 0.2 === 0.3` evaluates to `false`; avoid expecting exact decimal equality for currency. `Number.isNaN()` checks the actual `NaN` value without coercion, whereas global `isNaN()` first coerces its argument.

```js
console.log(0.1 + 0.2);                  // 0.30000000000000004
console.log(Number('12px'));              // NaN: entire string is invalid
console.log(parseInt('12px', 10));         // 12: accepts a numeric prefix
console.log(Number(''));                  // 0: perhaps not what a form wants
console.log(Number.isNaN('not a number')); // false: argument is a string
console.log(Number.isSafeInteger(2 ** 53)); // false
```

For money, represent integer cents when that is suitable for the domain, or use a properly specified decimal library. `BigInt` supports integers beyond Number's safe-integer range but cannot be mixed directly with `Number` in arithmetic. A form often needs both a **syntactic** check and a **domain** check (e.g., age must be a whole number within a defined range), not `parseInt()` alone.

```js
function parseQuantity(input) {
  const text = input.trim();
  if (!/^(0|[1-9]\d*)$/.test(text)) return null;
  const quantity = Number(text);
  return Number.isSafeInteger(quantity) && quantity <= 100 ? quantity : null;
}
console.log(parseQuantity('12px')); // null, not 12
console.log(parseQuantity('12'));   // 12
```

**Try it:** test `''`, `'01'`, `'-2'`, `'101'`, `'9007199254740993'` and `'12.5'`. Decide explicitly whether leading zeroes and negative numbers belong in *your* product before adapting the regular expression. Reference: [MDN Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number).""")

insert('04_javascript.md', '#### Comparison Operators', """##### Coercion and truthiness: predict the output first

```js
console.log(0 == false);    // true: loose equality coerces operands
console.log(0 === false);   // false: different types
console.log('5' + 1);       // '51': string concatenation
console.log('5' - 1);       // 4: numeric coercion
console.log(Boolean('0'));  // true: nonempty string
console.log(Boolean(''));   // false
console.log(null == undefined);  // true
console.log(null === undefined); // false
```

`===` is usually the clearer default, but object comparisons still test **identity**, not structural equality: `{x:1} === {x:1}` is false because the two literals construct separate objects. `NaN === NaN` is false; `Number.isNaN()` tests for it explicitly. `&&` and `||` return operands, not necessarily booleans: `'' || 'Fallback'` returns `'Fallback'`. To default only when a value is `null` or `undefined`, use nullish coalescing (`??`): `0 ?? 10` remains 0.

**Exercise:** before running each line, write its result and identify where coercion occurs. Compare `value || 10` with `value ?? 10` for `0`, `false`, `''`, `null` and `undefined`. Reference: [MDN equality comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness).""")

insert('04_javascript.md', '### Functions', """#### Events, microtasks, and a responsive browser

Asynchronous JavaScript does **not** mean that one synchronous event handler runs several JavaScript statements at the same instant on a typical single main thread. Promise reactions run in a microtask queue after the current JavaScript job completes; timers schedule later tasks and are subject to delays. Browsers may have workers and multiple processes, but a long synchronous loop on the main thread can still block interaction and paint.

```js
console.log('A');
setTimeout(() => console.log('D: timer'), 0);
Promise.resolve().then(() => console.log('C: promise'));
console.log('B');
// A, B, C: promise, D: timer
```

Why? The synchronous job logs A and B; the promise callback executes as a microtask when that job finishes; the timer is a later task. A `0` delay is not a guarantee of zero elapsed time. `await` pauses the **async function** and lets other work proceed; it does not turn a CPU-heavy synchronous function into nonblocking work.

```js
async function loadProducts(signal) {
  const response = await fetch('/api/products', { signal });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}
```

This snippet requires a real `/api/products` endpoint and illustrates error handling, not a runnable standalone request. `fetch` generally rejects for network failures and aborts, **not** merely for an HTTP 404 or 500. See the [form's browser before/after](../assets/visual-examples/form-validation-browser.png) for a visible result of an event handler. **Exercise:** change a button's text via `textContent`, then insert a heavy loop and watch interaction freeze; remove it and compare. Reference: [MDN event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model) and [using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).""")

# 05 React — state and effects with executable modern API, comparisons and caveats.
insert('05_javascript_frameworks.md', '## What are frameworks?', """### Decide whether a framework earns its complexity

A static portfolio, a content website with minimal interactivity, and a client-heavy dashboard have different requirements. Begin with an explicit feature inventory: navigation/routing, persistence, data fetching, authentication boundaries, search requirements, accessibility, localization, bundle constraints, deployment environment, and team experience. Libraries and frameworks solve some of these, but none automatically supplies good information architecture or security.

| Example | Possible starting point | What to investigate before choosing |
|---|---|---|
| Static documentation | HTML, CSS, optional build-time generator | Editing workflow, accessibility, search and hosting. |
| Small interactive widget | Native JavaScript or a small component library | DOM ownership, reusability, testing and bundle cost. |
| Multi-route application | An appropriate app framework | Routing, server/client data, error pages and deployment. |
| Embedded widget in a legacy site | An isolated component | CSS isolation, integration, versioning and cleanup. |

**Comparison experiment:** implement the [same button and form behavior](../projects/visual-examples/index.html) in vanilla JavaScript first. Add a framework only after identifying which duplication or state complexity it actually removes. Measure page size and runtime behavior in your own application; framework marketing and survey popularity are not performance tests. A framework may provide conventions for routes and data loading, whereas React by itself is a UI library: distinguish its API from the surrounding toolchain.

**Accessibility contract:** whichever stack is chosen, a button should remain a button, a label should still name its input, keyboard focus must be visible, and API authorization still belongs on the server. Reference: [React project options](https://react.dev/learn/start-a-new-react-project).""")

insert('05_javascript_frameworks.md', '#### Component', """##### Modern functional component: props, state, and an observable outcome

The class component below demonstrates an older component style. For a new small component, a function with hooks is often simpler. This is an illustrative module for an app whose HTML contains `<div id="root"></div>` and whose build tool supports JSX:

```jsx
import { useState } from 'react';
import { createRoot } from 'react-dom/client';

function QuantityPicker({ productName, max = 5 }) {
  const [quantity, setQuantity] = useState(1);
  return (
    <section aria-label={`Quantity for ${productName}`}>
      <p>{productName}: {quantity}</p>
      <button type="button" disabled={quantity === 1}
              onClick={() => setQuantity(q => q - 1)}>Decrease</button>
      <button type="button" disabled={quantity === max}
              onClick={() => setQuantity(q => q + 1)}>Increase</button>
    </section>
  );
}

createRoot(document.getElementById('root')).render(
  <QuantityPicker productName="Notebook" max={4} />
);
```

**What the user sees:** initially “Notebook: 1,” with Decrease unavailable. Each Increase click updates the number; at 4, Increase becomes disabled. State lives in the component; `productName` and `max` are inputs from its parent. The functional state updater `q => q + 1` uses the queued previous state, which matters when several updates occur in one event. React normally batches updates, so reading state immediately after calling a setter still yields the snapshot for that render.

**Test cases:** initial value 1; clicking Increase twice displays 3; Decrease returns to 2; the maximum cannot be exceeded. Check the disabled state's explanation and color contrast against the [button-states browser screenshot](../assets/visual-examples/button-states-browser.png). Reference: [React state as a snapshot](https://react.dev/learn/state-as-a-snapshot).""")

insert('05_javascript_frameworks.md', '### Hooks', """#### Effects synchronize with external systems; derived values usually do not need one

An effect should connect React to something *outside* its pure rendering model, such as an event subscription, timer or network resource. Do not copy a prop into state with an effect merely to calculate a full name or filtered list; compute those values during rendering when possible. Cleanup runs when dependencies change and when a component unmounts, helping prevent leaks and stale subscriptions.

```jsx
import { useEffect, useState } from 'react';

function WindowWidth() {
  const [width, setWidth] = useState(() => window.innerWidth);
  useEffect(() => {
    const update = () => setWidth(window.innerWidth);
    window.addEventListener('resize', update);
    return () => window.removeEventListener('resize', update);
  }, []);
  return <output>Viewport: {width} CSS pixels</output>;
}
```

This is a **client-only teaching example**: directly accessing `window` in state initialization is not safe during server rendering. In an SSR app, choose a server-safe initial value and handle hydration deliberately, or use a suitable external-store abstraction. Development Strict Mode may run an extra setup/cleanup cycle to expose bugs; do not “fix” duplicate-looking development logs by suppressing cleanup or lying about dependencies.

**Compare:** computing `const doubled = count * 2` in render needs no effect. Starting a timer inside rendering, by contrast, creates a new timer on each render and is incorrect. For network requests, cancel or ignore stale results when a dependency changes, handle loading/error/empty states, and do not put authentication secrets in browser bundles. Reference: [React synchronizing with effects](https://react.dev/learn/synchronizing-with-effects) and [you might not need an effect](https://react.dev/learn/you-might-not-need-an-effect).""")

# 06 UX — research plan, measurable iteration, evidence vs assumption.
insert('06_ux.md', '### The UX Design Process', """#### Worked case study: finding shipping costs

**Scenario:** visitors say delivery fees are difficult to find. That statement is a research lead, not yet proof that a particular menu label is at fault. Define an observable task: “Find the delivery cost for a standard order without placing an order.” Recruit participants who reasonably represent the product's relevant tasks, contexts and accessibility needs; avoid treating one colleague's preferences as general evidence.

| Stage | Question | Evidence to capture | Decision |
|---|---|---|---|
| Discover | Where do users expect the fee? | Task paths and participant explanations. | Form competing hypotheses. |
| Baseline | Can they find it with the current UI? | Completion, wrong turns, time and confusion. | Describe specific observed issues. |
| Prototype | Does clearer labeling change the path? | Side-by-side annotated prototypes. | Pick what to test, not an assumed winner. |
| Evaluate | Can users now complete the task? | Same task definition and documented conditions. | Iterate or investigate remaining problems. |
| Monitor | Does behavior hold after launch? | Support tickets and appropriately aggregated metrics. | Revisit when content or audience changes. |

![Browser-rendered illustration: competing CTAs versus clearer visual hierarchy](../assets/visual-examples/visual-hierarchy-browser.png)

A more prominent “Shipping and returns” link may be a hypothesis, but visually attractive wireframes do not prove a task is easier. Compare a working prototype, record what changed, and ask a second person to attempt the same task without coaching. Do not quietly switch tasks or count success differently between versions. Even if completion improves in a small study, report **observed participants and conditions**, not a population-wide percentage or causal guarantee.

**Practical deliverable:** write a one-page research note with the task, recruitment criteria, prototype version, observed failures, quotations labeled as participant reports, and next iteration. Use the [iterative UX diagram](../assets/diagrams/ux-loop.svg) to map where the next round begins. Reference: [NN/g usability testing](https://www.nngroup.com/articles/usability-testing-101/).""")

insert('06_ux.md', '### Conducting User Interviews', """#### Interview script: separate behaviors from leading questions

A semi-structured interview uses open questions and consistent goals, not a rigid list of suggested answers. Ask for permission before recording, explain how notes will be used, and avoid collecting unnecessary personal data. If the participant is under pressure, paid by a sponsor or already knows the product, record that context rather than treating the session as neutral evidence.

**Suggested sequence for a 20-minute discovery session:**

1. Explain the purpose and recording choice; make it clear there are no right answers.
2. “Tell me about the last time you checked shipping costs before ordering.”
3. “What information were you looking for, and where did you look first?”
4. “Can you show or describe the steps you took?”
5. “What, if anything, surprised you?”
6. “What happened after you found—or failed to find—the information?”
7. Ask whether anything important was missed, then thank the participant.

Avoid “You found the checkout confusing, didn't you?”: it supplies the judgment and encourages agreement. Follow a surprise with “What were you expecting to happen?” rather than immediately explaining the design. Observe actions separately from claimed intentions; neither source is infallible. Include verbatim quotations only when permitted, and remove identifying details from widely shared research artifacts.

**Analysis exercise:** make three columns labeled *observation*, *interpretation* and *follow-up question*. “Three participants clicked Help first” is an observation; “the Shipping label is unclear” is a hypothesis; “What did Help mean to you?” is a follow-up. Don't convert a handful of qualitative participants into representative percentages. Reference: [NN/g interview guidance](https://www.nngroup.com/articles/user-interviews/).""")

insert('06_ux.md', '## What to Avoid in UX Design?', """#### Evaluate outcomes without confusing aesthetics with usability

Before/after mockups can clarify a design hypothesis, but neither appearance nor a single engagement metric defines user experience. People may complete a checkout faster because they understand it, because they were pressured, or because important explanations were removed. Define guardrail measures alongside a primary task outcome.

| UX goal | Observable signal | Common confounder |
|---|---|---|
| Find an answer | Task completion and path taken | Prior familiarity with the site. |
| Understand an error | Can the user explain and recover? | Researcher coaching. |
| Complete checkout | Successful, informed purchase | Hidden charges or defaults. |
| Navigate by keyboard | Can all controls be reached and used? | Tester used mouse during the task. |
| Read at high zoom | No clipped critical controls | Only desktop width was tested. |

**Experiment:** with the [visual hierarchy demo](../projects/visual-examples/index.html), compare the layouts at 320px, 200% zoom and with CSS disabled. Ask a participant to locate the primary task. The screenshot illustrates the proposed change but cannot establish user preference, performance, or accessibility on its own. Record the viewport, browser, whether assistance was given, and any incomplete steps. Aim for understandable, reversible actions rather than maximizing clicks regardless of user intent.""")

# 07 UI — concrete interaction contracts, design tokens and keyboard tests.
insert('07_ui.md', '### UI Components', """#### Interaction contract: visuals are only one state of a control

A reusable component needs a specification of *behavior* as well as colors and spacing. For a button, record its label, purpose, activation behavior, default/hover/focus/disabled/busy states, available input methods, and how errors are shown. The [actual browser comparison](../assets/visual-examples/button-states-browser.png) is a starting point; it is not a substitute for keyboard or assistive-technology testing.

| Control | Native semantic choice | Minimum functional check |
|---|---|---|
| Navigate to another page | `<a href="...">` | Activates with Enter, exposes destination. |
| Perform an action | `<button type="button">` | Activates with Enter and Space, focus visible. |
| Submit form data | `<button type="submit">` | Validates/submits intended form. |
| Choose one of several choices | Radio group with a shared name | Arrow-key behavior, descriptive legend. |
| Choose independent options | Checkboxes | Space toggles each option. |
| Choose from a compact fixed list | Native `<select>` | Works with keyboard and touch. |

An element with `onclick` does not automatically acquire button semantics, focusability, Space activation or accessible naming. Prefer HTML controls rather than rebuilding their entire interaction model with ARIA. Do not disable a working submit control as the *only* explanation of why a form is incomplete: give a discoverable explanation. A `loading` state must prevent accidental duplicate actions where necessary, while exposing progress and preserving a usable focus strategy.

**Audit exercise:** start from the [live demo](../projects/visual-examples/index.html), unplug the mouse and traverse controls with Tab, Shift+Tab, Enter and Space. Check whether the visible focus location corresponds to the action, and test with forced colors as available. Reference: [WAI-ARIA first rule](https://www.w3.org/TR/using-aria/#rule1).""")

insert('07_ui.md', '#### Buttons', """##### State implementation: not just four colored rectangles

```html
<button class="save-button" type="button">Save draft</button>
<button class="save-button" type="button" disabled>
  Save unavailable
</button>
<p id="save-help">Enter a title before saving.</p>
```

```css
.save-button { background: #1d4ed8; color: white; border: 2px solid transparent; }
.save-button:hover:not(:disabled) { background: #1e40af; }
.save-button:focus-visible { outline: 3px solid #0f172a; outline-offset: 3px; }
.save-button:disabled { background: #e2e8f0; color: #334155; cursor: not-allowed; }
@media (forced-colors: active) {
  .save-button:focus-visible { outline: 3px solid Highlight; }
}
```

The disabled control will usually be skipped by sequential Tab navigation. If people must discover *why* an action is unavailable, provide associated visible text, a status message, or a design where an enabled button explains the validation error on activation. For a pending network request, distinguish *busy* from *disabled* and expose the result on success/failure. Do not remove the browser focus outline without an equivalent replacement.

**Try it:** compare the [browser screenshot](../assets/visual-examples/button-states-browser.png) with real hover and Tab behavior in the [project](../projects/visual-examples/index.html). Simulate a monochrome view and verify that text, border and shape still distinguish states. Reference: [MDN `:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible).""")

insert('07_ui.md', '#### Inputs', """##### Form errors: a concrete four-state specification

![Chromium rendering of initial and invalid form states](../assets/visual-examples/form-validation-browser.png)

| State | Visible presentation | Accessible/behavioral requirement |
|---|---|---|
| Empty, untouched | Persistent label and optional hint | Input has a programmatic name. |
| Editing | Text remains legible; hint stays available | Don't erase the label. |
| Invalid after submit | Specific error next to the field | Message connected with `aria-describedby`; focus strategy. |
| Valid/submitted | Clear result or next step | Server errors still handled; no false success promise. |

```html
<label for="email-signup">Email address</label>
<p id="email-hint">For example: name@example.com</p>
<input id="email-signup" name="email" type="email" required
       aria-describedby="email-hint email-error">
<p id="email-error" role="status"></p>
```

JavaScript can populate the error element with `textContent`, set `aria-invalid="true"` *after* validation fails, and focus the invalid field if appropriate. Avoid `role="alert"` on every keystroke: overly aggressive announcements are distracting. Native browser validation can be a useful baseline; a fully custom system must reproduce helpful messages and focus behavior. Client-side checks improve guidance but are not a security boundary. Reference: [W3C form instructions and validation](https://www.w3.org/WAI/tutorials/forms/validation/).""")

insert('07_ui.md', '#### Menus', """##### Responsive navigation: width, semantics, and keyboard testing

![Actual wide and narrow browser views of the same navigation](../assets/visual-examples/responsive-navigation-browser.png)

![Actual narrow-screen navigation capture](../assets/visual-examples/responsive-navigation-mobile.png)

The two screenshots show that **reflow** can make the same set of links usable at different widths. The simplest implementation needs no custom popup: allow a `<nav>` to wrap or stack its links. A container query is useful when a component appears in both a narrow sidebar and a wide page, because the component responds to its available space rather than to the viewport alone.

```css
.navigation-container { container-type: inline-size; }
.navigation { display: flex; flex-wrap: wrap; gap: 0.75rem; }
@container (max-width: 24rem) {
  .navigation { flex-direction: column; align-items: flex-start; }
}
```

The query targets descendants of `.navigation-container`; setting a query on an element does not allow that element's own dimensions to be styled by its own container query. For a collapsible design, implement a real button with `aria-expanded`, `aria-controls` and a clearly named panel. Closing must not strand keyboard focus inside hidden content. **Test:** a 320px viewport, 200% zoom, Tab through all links, open/close behavior, and browser Back navigation. Reference: [MDN container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries).""")

assert modified == {'01_html.md', '02_css.md', '03_css_frameworks.md', '04_javascript.md', '05_javascript_frameworks.md', '06_ux.md', '07_ui.md'}, modified
print('Second-pass A: expanded seven ORIGINAL chapters, retaining existing content.')
