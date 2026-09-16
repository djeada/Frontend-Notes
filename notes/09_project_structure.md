## Project Structure

A useful project structure lets a developer locate a feature, change it, test it, and deploy it without guessing which files own which behavior. Organize a project for its **current requirements**, then refactor when responsibilities become unclear. There is no universally correct folder tree, and renaming folders alone does not improve runtime speed, security, or scalability.

### What to optimize for

- **Findability:** use consistent names so a new contributor can locate an entry point, component, stylesheet and test.
- **Maintainability:** keep related behavior together, isolate clear boundaries, and document unusual decisions.
- **Reusability:** extract common components when multiple consumers share genuine behavior; premature abstractions can make simple changes harder.
- **Modularity:** limit unrelated dependencies so a change can be understood and tested locally. A folder does not create isolation unless the code respects its boundaries.
- **Collaboration:** define ownership, contracts and review expectations. Separate directories may reduce conflicting edits, but do not guarantee conflict-free teamwork.
- **Performance:** measure actual assets, bundle size, loading behavior, caching and render work. A tidy file tree alone does not reduce bytes shipped to users.
- **Security:** put secrets in a secure server or hosting configuration, validate and authorize operations server-side, and restrict access in the deployed architecture. A `private/` directory in browser code does **not** make its contents private.

**Example:** moving an API key from `src/key.js` to `src/config/secret.js` changes its location but not its exposure when both are bundled for the browser. The fix is to move secret-dependent operations to an authenticated backend or an appropriate server-side function.

### Choosing technologies

HTML provides structure, CSS presentation, and JavaScript/TypeScript behavior. A plain HTML/CSS/JS site can be a good fit when the interaction is small; a framework may help with complex component composition, state or routing, but adds conventions and build dependencies. TypeScript adds static checking when configured, not automatic runtime validation or performance.

Choose based on real requirements: deployment model, accessibility support, team experience, ecosystem maintenance, testing, bundle budget and integration needs. Multiple frameworks in one application **can** be appropriate during migration or for isolated islands, but need deliberate integration boundaries; avoid combining them without a reason. Do not claim that plain JavaScript always outperforms every framework or that choosing an actively maintained dependency guarantees security.

### Example structure: a small multi-page site

The original CSS/JS/views/assets split is still a useful example. Here is a streamlined version that makes entry points and test ownership explicit:

```text
project/
├── index.html
├── about.html
├── contact.html
├── css/
│   ├── reset.css
│   ├── typography.css
│   ├── layout.css
│   ├── navigation.css
│   ├── forms.css
│   └── themes/
│       ├── dark.css
│       └── light.css
├── js/
│   ├── main.js
│   ├── utils.js
│   ├── components/
│   │   ├── header.js
│   │   └── sidebar.js
│   └── services/
│       └── api.js
├── assets/
│   ├── images/
│   ├── fonts/
│   └── videos/
├── data/
│   └── sample-data.json
├── tests/
│   └── navigation.test.js
├── docs/
│   └── decisions.md
└── README.md
```

- **HTML entry points:** `index.html`, `about.html`, and `contact.html` are separate pages. A template engine could instead compile shared `views/partials/` into these files; an HTML file does not automatically include another HTML file merely because they live in a `partials` folder.
- **CSS:** split reset, typography, layout, navigation, forms and themes only when each file has a clear purpose. Media queries can sit beside the component they adapt rather than in one large `media_queries.css`.
- **JavaScript:** `main.js` coordinates page startup, `components/` contains UI behavior, `services/` handles API boundaries, and `utils.js` should not become a dumping ground.
- **Assets:** organize images, fonts and videos for maintenance; optimize formats and delivery separately. Images need suitable dimensions and alternatives where meaningful.
- **Data and tests:** keep sample fixtures separate from production secrets, and test observable behavior rather than implementation details.
- **Documentation:** root `README.md` describes installation, scripts and examples; `docs/` can hold architecture decisions. A document nested in `docs/` does not replace an obvious root entry point by itself.

This is a **suggestion**, not a mandatory architecture. For a five-file learning example, five files in one directory may be easier to understand. A bundled app may have `src/`, `public/`, `dist/`, a lockfile, or a generated output directory instead; do not commit generated output unless deployment requires it.

### Alternative: organize by feature

As a component application grows, separating everything by file type can scatter one feature across multiple directories. Compare these simplified arrangements:

```text
# Type-first                        # Feature-first
src/components/CartButton.jsx        src/features/cart/CartButton.jsx
src/components/CheckoutForm.jsx      src/features/checkout/CheckoutForm.jsx
src/styles/cart.css                  src/features/cart/cart.css
src/styles/checkout.css              src/features/checkout/checkout.css
src/tests/cart.test.js               src/features/cart/cart.test.js
```

![Visual example comparing cluttered and purposeful content hierarchy](../assets/visual-examples/visual-hierarchy.svg)

**Actual browser-rendered before/after:**

![Browser screenshot of the visual hierarchy comparison](../assets/visual-examples/visual-hierarchy-browser.png)

A feature-first arrangement can simplify locating its tests and styles. Shared primitives (button, dialog, formatting functions) can still live in `src/shared/`. Use import boundaries to prevent cycles rather than expecting directory names to enforce architecture. The illustration teaches **interface hierarchy**, not a benchmark proving one file tree is faster.

### Best practices for a production build

- Bundle, split and minify assets **when measurements show a benefit**; modern project tooling often handles this automatically. Webpack, Parcel or another bundler is optional for small static examples. Gulp is a task runner, not a mandatory bundler.
- Use a template engine such as EJS, Handlebars or Pug for repeated server/build-time HTML only when duplication warrants it. Check the output HTML after compilation.
- Separate development, preview and production configuration. Never place server credentials in client-exposed environment variables.
- Use Git, a `.gitignore`, documented scripts and meaningful commits. Commit a lockfile where appropriate for reproducible dependency installation.
- Run a formatter and relevant linting tools (such as ESLint or Stylelint) consistently; tools catch selected problems, not all bugs.
- Write down decisions that future contributors cannot infer from code alone. Update the README when commands, environment variables or ownership change.

### Boilerplates

A boilerplate is a starting template containing some combination of files, dependencies, configurations, styles and example code. Its purpose is to remove repetitive setup, **not** to guarantee that every generated application is accessible, secure or fast. Review the generated project; delete unused example routes, dependencies and placeholder secrets before shipping it.

#### Why use one?

- Share a conventional entry point and scripts across a team.
- Reuse appropriate lint, formatting, test and build settings.
- Avoid repeating setup when building several projects with the same constraints.
- Make onboarding easier **if** the template is documented and maintained.

The drawbacks are important: a template can lock you to unsupported dependencies, introduce unnecessary features, or conceal how the tooling works. Check source, license, update frequency, and support for the target framework and Node.js version.

#### CSS in a boilerplate

Reusable base styles, typography, spacing tokens, and accessible form/button states can provide consistency. Responsive behavior is not guaranteed just because a template contains a media query; test narrow widths, long labels, 200% zoom, and keyboard focus. Naming methods such as BEM or OOCSS are options, not requirements for all projects.

**See what such a decision looks like:** the repository's [visual teaching project](../projects/visual-examples/README.md) has a shared stylesheet and minimal JavaScript. Inspect how its class names map to specific demonstrations and compare [unstyled versus styled cards](../assets/visual-examples/card-styling.svg). Change its spacing and color tokens in `styles.css` to see why predictable naming helps maintainability.

#### Finding and evaluating a boilerplate

Search the upstream project's real organization and documentation instead of copying placeholder URLs such as `https://github.com/username/boilerplate-html-css-js`; that address was an illustrative placeholder in the previous notes, **not a recommended repository**. Read the README, license, dependency versions, issue activity, and setup instructions. Test accessibility, performance and production output with *your application*, not only the template's screenshot.

**Important dated guidance:** Create React App has been deprecated for new applications; don't recommend it as the default current React scaffold. React's documentation describes supported framework choices and building from scratch. Vue CLI is in maintenance mode; consult Vue's current tooling guide. Framework and CLI recommendations should link to current documentation and mention the version they were checked against.

#### Using HTML5 Boilerplate step by step

The following workflow uses an actual template repository, [HTML5 Boilerplate](https://github.com/h5bp/html5-boilerplate). Check its current prerequisites and license before running these commands:

```bash
git clone https://github.com/h5bp/html5-boilerplate.git my-new-project
cd my-new-project
```

Inspect `README.md`, `package.json`, and the existing scripts **before** installing dependencies. If the current version uses npm, install dependencies using the repository's documented command (for example, `npm install`, or `npm ci` when a compatible lockfile is present):

```bash
npm install  # only if supported by the template's current instructions
```

Customize the project title and description, fonts, CSS, markup and any interactions. Remove placeholder analytics identifiers, unused assets and example content. Make sure the generated page has meaningful headings and labels; a default appearance is not evidence of good accessibility.

If you intend to make an independent repository rather than contribute back to the template's history, the original `git clone` already created a repository with its own Git history. **Running `git init` alone does not remove that history.** Choose deliberately between preserving upstream history, using a template's “Use this template” action, or starting a fresh repository with the template files (and honoring its license):

```bash
# One possible fresh-history workflow after copying the permitted template files
# into a separately created directory (not inside the original clone):
git init
git add .
git commit -m "Start project from documented template"
```

Write a project-specific `README.md` covering purpose, prerequisites, installation, scripts, environment variables (names only, **not secret values**), testing and deployment. Run the build locally; test links, mobile layout and keyboard behavior before deploying.

### Reference directory: review maintenance before adopting

Some links below were part of the original chapter and are retained for historical context. **An older generator is not automatically a recommended choice today**; check the linked project's current support status and migration path.

- [Rapid Site Development](https://github.com/MWins/rapid-site-development)
- [A Minimal HTML Document](http://www.sitepoint.com/a-minimal-html-document-html5-edition/)
- [Reset Revisited by Eric Meyer](http://meyerweb.com/eric/thoughts/2011/01/03/reset-revisited/)
- [CSS Reset](http://www.cssreset.com/)
- [HTML5 Boilerplate](https://html5boilerplate.com/)
- [Node.js Boilerplate](https://github.com/sahat/hackathon-starter)
- [Express Generator](https://expressjs.com/en/starter/generator.html)
- [Create React App — deprecated for new apps](https://react.dev/blog/2025/02/14/sunsetting-create-react-app)
- [Vue CLI — maintenance mode](https://cli.vuejs.org/)
- [Angular CLI](https://angular.dev/tools/cli)
- [Next.js](https://nextjs.org/)
- [Nuxt](https://nuxt.com/)
- [Meteor](https://www.meteor.com/)
- [Webpack](https://webpack.js.org/)
- [Parcel](https://parceljs.org/)
- [Gulp](https://gulpjs.com/)
- [Yeoman](https://yeoman.io/)
- [Preact](https://preactjs.com/)
- [Sapper — historical; see SvelteKit](https://svelte.dev/docs/kit/introduction)
- [Quasar Framework](https://quasar.dev/start/quasar-cli)
- [Aurelia](https://aurelia.io/)
- [Gridsome](https://gridsome.org/)

**References:** [React: start a new React project](https://react.dev/learn/start-a-new-react-project), [React: sunsetting Create React App](https://react.dev/blog/2025/02/14/sunsetting-create-react-app), [Vue tooling](https://vuejs.org/guide/scaling-up/tooling.html), [MDN: deployment](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website), [OWASP cheat sheets](https://cheatsheetseries.owasp.org/).