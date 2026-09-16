# Quizzes: corrected answers and practice questions

[Original quiz chapter](../12_quizes.md) · [All chapter updates](README.md)

Use the original chapter as a question bank, with the following corrections when checking answers. Explanations should state a rule, then show what that rule means in a concrete example.

## Corrections to existing answers

**What is a doctype?** The answer should show the literal syntax `<!doctype html>` (including angle brackets) and say that it selects no-quirks mode in HTML documents. It is not a reliable signal of an HTML version.

**How do I remove a blue outline on linked images?** Do **not** recommend `a img { outline: none; }` as a blanket fix: interactive links must retain a visible keyboard focus indicator. If styling is necessary, apply an intentional focus style to the link itself, such as `a:focus-visible { outline: 3px solid currentColor; outline-offset: 3px; }`. Distinguish an image border from a link's focus outline.

**Will React run in any modern browser?** A browser does not need to install React separately; the app delivers compatible JavaScript and possibly server-rendered HTML. Browser support still depends on the framework/library version, build target, APIs, polyfills, and deployed assets. “Any browser” is not an unconditional guarantee.

**What is an object?** Object property keys can be **strings or symbols**, not just strings. Arrays are objects, but a `Map` is a separate built-in collection with distinct APIs and key semantics.

**What is JavaScript?** Avoid describing runtime execution only as line-by-line interpretation: engines may compile and optimize code.

## Five additional questions

<details><summary>1. Does fetch reject when the server responds 404?</summary>

Normally no. The Promise resolves with a Response; inspect `response.ok` or `response.status`. Network failures can reject.
</details>

<details><summary>2. Does a viewport meta element create a responsive design?</summary>

No. It adjusts viewport behavior, but layouts and media still need adaptable styles and testing.
</details>

<details><summary>3. Can a client-side required attribute replace server validation?</summary>

No. Clients can bypass or modify validation; the server must validate and authorize its inputs.
</details>

<details><summary>4. Is a select element always an ARIA combobox?</summary>

No. Native select controls have their own semantics and behavior; an autocomplete combobox is a distinct pattern.
</details>

<details><summary>5. Does CORS protect an API from unauthorized callers?</summary>

No. CORS controls which cross-origin responses browsers expose to scripts. Authentication and server-side authorization still protect resources.
</details>

## How to study

Answer without expanding each question; cite the relevant API or standard; build a ten-line reproduction; then explain a failure case. Revisit questions after changing dependencies or browser targets. Automated checks are useful, but include keyboard-only and screen-reader observations for UI questions.

**References:** [MDN: doctype](https://developer.mozilla.org/en-US/docs/Glossary/Doctype), [MDN: outline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline), [MDN: fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), [MDN: JavaScript objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects).
