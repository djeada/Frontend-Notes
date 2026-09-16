# Frontend Notes 🚀

A practical collection of notes and small projects for learning how the web works: semantic HTML, adaptable CSS, JavaScript, UI architecture, accessible design, network requests, testing, and deployment.

![Frontend illustration](https://github.com/djeada/Frontend-Notes/assets/37275728/562de86d-66f1-42c0-991b-82c4cbe74255)

Frontend development builds the parts of websites and web applications that people encounter in a browser. **HTML** provides meaningful content and structure, **CSS** styles and lays out that content, and **JavaScript** can add interaction and communicate with services. Good frontend work also considers accessibility, performance, security, and the full user experience.

## Start here

You will need a modern browser and a text editor. Some projects run directly from an `index.html` file; others use Node.js and a package manager such as npm. **Read each project's README or package scripts before running it.** A local development server is often preferable to opening a file with `file://`, especially for JavaScript modules, routing, and network requests.

```sh
git clone https://github.com/djeada/Frontend-Notes.git
cd Frontend-Notes
```

Choose a chapter below, read its original long-form notes, then open its **correction and expansion companion**. Work through the related directory under [`projects/`](projects) where one exists. For a plain HTML example, open [`projects/01_html/image/index.html`](projects/01_html/image/index.html) in a browser; do not assume that the same command works for framework applications.

## Learning path

Each companion is an additive editorial pass: it clarifies specific mistakes, shows a modern working pattern, suggests practice, and links to primary references. The original chapters are retained, rather than silently replaced or claimed to be exhaustively fact-checked.

| # | Original notes | Corrections and practical expansion |
| --- | --- | --- |
| 1 | [HTML](notes/01_html.md) | [Semantics, doctype, and accessible forms](notes/revisions/01_html.md) |
| 2 | [CSS](notes/02_css.md) | [Cascade, responsive layout, and focus styling](notes/revisions/02_css.md) |
| 3 | [CSS frameworks and preprocessors](notes/03_css_frameworks.md) | [Native nesting, Sass, and nonstandard directives](notes/revisions/03_css_frameworks.md) |
| 4 | [JavaScript](notes/04_javascript.md) | [Type pitfalls, runtime behavior, and fetch](notes/revisions/04_javascript.md) |
| 5 | [JavaScript frameworks](notes/05_javascript_frameworks.md) | [React 19, project tooling, and tradeoffs](notes/revisions/05_javascript_frameworks.md) |
| 6 | [User experience](notes/06_ux.md) | [Research, observation, and iteration](notes/revisions/06_ux.md) |
| 7 | [User interface](notes/07_ui.md) | [Accessible components and validation](notes/revisions/07_ui.md) |
| 8 | [Protocols](notes/08_protocols.md) | [HTTPS lifecycle, caching, and CORS](notes/revisions/08_protocols.md) |
| 9 | [Project structure](notes/09_project_structure.md) | [Scalable boundaries and safe configuration](notes/revisions/09_project_structure.md) |
| 10 | [Testing](notes/10_testing.md) | [Test boundaries and reliable examples](notes/revisions/10_testing.md) |
| 11 | [Hosting websites](notes/11_hosting_websites.md) | [DNS, deployment, and operational checks](notes/revisions/11_hosting_websites.md) |
| 12 | [Quizzes](notes/12_quizes.md) | [Corrected answers and new questions](notes/revisions/12_quizzes.md) |
| 13 | [Additional resources](notes/13_additional_resources.md) | [How to evaluate tools, licensing, and maintenance](notes/revisions/13_additional_resources.md) |

For an overview of the revision scope and a per-chapter change list, see the [revision index](notes/revisions/README.md). Three editable, locally hosted SVG diagrams explain the [CSS cascade](assets/diagrams/css-cascade.svg), [UX iteration](assets/diagrams/ux-loop.svg), and [HTTPS request lifecycle](assets/diagrams/request-lifecycle.svg). Their source and editing guidance are in the [diagram project](projects/diagrams/README.md).

## How to study effectively

1. Read a topic and restate its main concept in your own words.
2. Run a small example, then change one variable and predict the result.
3. Inspect browser DevTools: Elements, Styles, Console, Network, and accessibility information.
4. Test with the keyboard, on a narrow viewport, and at increased zoom.
5. Verify uncertain claims in the linked standards or current tool documentation. A framework version, hosting price, or API may have changed since a note was written.

For network-backed projects, serve the files using the project's documented development server. Do not embed production secrets into client-side code. Keep example credentials and API endpoints separate from real accounts.

## Reference starting points

- [MDN Web Docs](https://developer.mozilla.org/): HTML, CSS, JavaScript, and browser APIs.
- [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/): HTML behavior and markup rules.
- [W3C CSS Snapshot](https://www.w3.org/TR/css-2026/): the current modular CSS specification landscape.
- [ECMAScript specification](https://tc39.es/ecma262/): JavaScript language semantics.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): accessibility success criteria.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): practical application-security guidance.
- [web.dev](https://web.dev/): frontend performance and quality.
- [The Odin Project](https://www.theodinproject.com/) and [freeCodeCamp](https://www.freecodecamp.org/): project-based learning.

The [additional-resources chapter](notes/13_additional_resources.md) contains a broader directory of templates, images, components, and inspiration. Always verify current licensing, pricing, and maintenance before reuse.

## Contributing

Contributions that correct an inaccurate example or improve accessibility are especially welcome. Fork the repository, create a focused branch, document what changed and why, and open a pull request. Include a runnable reproduction for code changes and a primary source for factual corrections. Update both an original chapter and its companion when you resolve an outstanding discrepancy; avoid letting two versions of the same guidance contradict each other.

## License

This repository is licensed under the [MIT License](LICENSE). Individual third-party images, fonts, libraries, and linked resources may have separate terms: inspect their licenses before redistribution.
