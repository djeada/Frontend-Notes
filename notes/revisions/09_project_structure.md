# Project structure: start with boundaries, not folders

[Original project-structure chapter](../09_project_structure.md) · [All chapter updates](README.md)

A directory layout is a communication tool, not a performance optimization in itself. Choose a structure that helps maintainers locate code, understand ownership, test changes, and deploy reliably. A small static page and a multi-team application do not need the same architecture.

## Corrections to the original

- **Folder names do not automatically improve load time, scalability, or security.** Delivery depends on asset size, caching, rendering and network behavior; security depends on enforcement and deployment boundaries. Files in a frontend bundle can be read by users regardless of where they lived in source control.
- Plain JavaScript is not inherently faster than a framework. Measure relevant interactions, bundle size, and rendering rather than promising better performance from a technology label.
- Multiple frameworks in one product are not categorically forbidden; micro-frontends and incremental migrations can justify them, but add integration and maintenance costs.
- Do not prescribe bundling and minifying for *every* deployment. A few static files may not need a build step, while a large application may benefit from code splitting and modern toolchains.
- The original Create React App recommendation and `reactjs.org` scaffolding link are outdated. CRA is deprecated for new projects; follow React's current project guidance.
- The placeholder `github.com/username/boilerplate-html-css-js` is not a verified template. Replace it with a real maintained example or remove it.

## Two reasonable starting points

**A static site:**

```text
site/
├── index.html
├── about.html
├── styles.css
├── script.js
└── assets/
```

Avoid introducing a framework merely to organize five files. For a larger component-based application, organize around features with explicit shared modules:

```text
app/
├── src/
│   ├── features/
│   │   └── search/
│   │       ├── SearchView.jsx
│   │       └── SearchView.test.jsx
│   ├── shared/
│   │   └── Button.jsx
│   └── main.jsx
├── public/
├── package.json
└── README.md
```

This is an example, not a universal standard. Keep feature-specific code near its consumer; move code to `shared` only when there is genuine reuse. Keep secrets and server-only operations **outside the client build**. Document environment variables and explicitly distinguish public build-time configuration from credentials.

## Definition of done for structure

Someone new should be able to answer: How do I run the app? Where does a feature live? Where are tests? Which files ship to browsers? How do I build and deploy? What is the rollback path? Validate the proposed structure by adding a feature and tracing its dependencies, rather than counting folders.

**References:** [React: start a new project](https://react.dev/learn/start-a-new-react-project), [React: CRA deprecation](https://react.dev/blog/2025/02/14/sunsetting-create-react-app), [OWASP: client-side security](https://owasp.org/www-project-top-ten-client-side-security-risks/), [web.dev: performance](https://web.dev/learn/performance).
