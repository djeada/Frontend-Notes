# JavaScript UI libraries and frameworks: current mental models

[Original chapter](../05_javascript_frameworks.md) · [All chapter updates](README.md)

A UI library supplies reusable rendering and component APIs; an application framework may also prescribe routing, data loading, server rendering, and build/deployment conventions. The boundary varies by product, so compare actual capabilities instead of assuming a framework automatically supplies a style guide or an app skeleton.

## Corrections to the original

- The claim that *most* web apps use a JavaScript framework needs a dated survey and a clearly defined population. Do not present it as a universal fact.
- React is a **UI library**. Its ecosystem offers routers and application frameworks, but React itself does not choose one for you. A framework does not inherently guarantee speed, longevity, or accessibility.
- `ReactDOM.render()` in the class-component example was removed in **React 19**. For a client-rendered app use `createRoot()` from `react-dom/client`; for HTML rendered on the server use `hydrateRoot()` instead.
- **Create React App is deprecated for new projects**. The React team recommends an appropriate framework for new applications, or a modern build tool for a from-scratch learning project. Do not describe CRA as an up-to-date starting point.
- Component APIs, routing, state, and browser support vary by library, configuration, and version. Validate claims against their current documentation, not static popularity rankings.

## A minimal React component

```jsx
import { useState } from 'react';
import { createRoot } from 'react-dom/client';

function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount((previous) => previous + 1)}>
    Count: {count}
  </button>;
}

createRoot(document.getElementById('root')).render(<Counter />);
```

`useState` stores a value between renders. Passing an updater function handles changes based on the previous value without relying on a potentially stale closure. `createRoot()` is for an empty client root; a server-rendered root needs hydration to reuse existing markup. Build tooling must transform JSX before browsers can run this example.

## Choosing architecture by requirements

Start with the tasks: static marketing pages, an interactive dashboard, or an application needing authentication and server data. Write down rendering strategy, routing, hosting constraints, team familiarity, accessibility needs, dependency upkeep, and deployment options. Then test one representative route and interactive component. A plain HTML/CSS/JS site remains a legitimate solution for many jobs.

## Practice

Turn a vanilla JavaScript counter into the component above. Add a meaningful button label and a reset control, then test keyboard activation. Compare a client-only build with a server-rendered framework using real requirements, not an assumption that the virtual DOM always guarantees faster performance.

**References:** [React: sunsetting Create React App](https://react.dev/blog/2025/02/14/sunsetting-create-react-app), [React: createRoot](https://react.dev/reference/react-dom/client/createRoot), [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide), [React: start a new project](https://react.dev/learn/start-a-new-react-project).
