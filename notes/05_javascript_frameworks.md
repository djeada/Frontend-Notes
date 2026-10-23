## JavaScript Frameworks

* Many web applications use frameworks or libraries, but static sites and smaller interactive pages may not need one. The right choice depends on the requirements.
* Learning a framework can help you work on existing applications, but HTML, CSS, JavaScript and browser fundamentals remain essential.
* Some take it to the extreme and start learning the frontend development with one of JavaScript frameworks. 
* I still believe that before diving into the world of JavaScript frameworks, you should first understand the fundamentals of frontend development. So if you haven't done that by now, I suggest you take a step back and learn the basics.

## What are frameworks?

### Decide whether a framework earns its complexity

A static portfolio, a content website with minimal interactivity, and a client-heavy dashboard have different requirements. Begin with an explicit feature inventory: navigation/routing, persistence, data fetching, authentication boundaries, search requirements, accessibility, localization, bundle constraints, deployment environment, and team experience. Libraries and frameworks solve some of these, but none automatically supplies good information architecture or security.

| Example | Possible starting point | What to investigate before choosing |
|---|---|---|
| Static documentation | HTML, CSS, optional build-time generator | Editing workflow, accessibility, search and hosting. |
| Small interactive widget | Native JavaScript or a small component library | DOM ownership, reusability, testing and bundle cost. |
| Multi-route application | An appropriate app framework | Routing, server/client data, error pages and deployment. |
| Embedded widget in a legacy site | An isolated component | CSS isolation, integration, versioning and cleanup. |

**Comparison experiment:** implement the [same button and form behavior](../projects/visual-examples/index.html) in vanilla JavaScript first. Add a framework only after identifying which duplication or state complexity it actually removes. Measure page size and runtime behavior in your own application; framework marketing and survey popularity are not performance tests. A framework may provide conventions for routes and data loading, whereas React by itself is a UI library: distinguish its API from the surrounding toolchain.

**Accessibility contract:** whichever stack is chosen, a button should remain a button, a label should still name its input, keyboard focus must be visible, and API authorization still belongs on the server. Reference: [React project options](https://react.dev/learn/start-a-new-react-project).


A software framework is a pre-written app skeleton on which you may further develop. It is a collection of files and folders to which you may modify as well as add your files and folders. A framework addresses following development issues:

* We don't want to start projects from scratch every time. A framework offers boilerplate code. 
* We want a consistent method of spreading functions across files and directories. A framework provides a structure for your project.
* We want consistency in the way our UI elements are styled. A framework provides a consistent style guide.
* When writing functions, we need rules to follow. A framework offers us with numerous examples that we may strive to emulate. 

### Problems addressed by the frameworks

We already learned how to create a simple website using just three files: index.html, style.css and script.js. This setup works well for a simple website, but quickly becomes cumbersome when you want to add more functionality.

* Frameworks usually come with a set of files and folders that you can modify as needed. That boilerplate code allows you to setup a working project in a matter of minutes.
* Frameworks are designed to be easily maintainable. You can easily add new functionality to your project without having to rewrite the code.
* Most frameworks separate the logic and the presentation. It's easier to write the code that does a single thing well, instead of trying to do everything at once.
* There hundreds of articles, blog posts, YouTube videos and tutorials on the subject. You can find everything you need to know about frameworks, ask questions and get help from the community.
* Because most frameworks are open source, they are available to anyone who wants to learn how to use them. Many developers are familiar with them and can easily contribute to the project based on their experience.

### Disadvantages

As with everything in life, there are benefits and costs to using frameworks.

* When starting to learn a framework, you are presented with a black box. You have no idea what the framework is doing behind the scenes. Understanding the underlying workings of any framework takes time and effort.
* Frameworks are often quite complicated. It may take some time for you to feel completely comfortable with them.
* Frameworks frequently contain restrictions on how they may be used. In contrast to using a library, you do not have complete control over the structure of your project. Depending on how you look at it, this might be good or bad. 
* A small project may gain little from a framework, or may benefit from familiar shared components and team conventions. Compare its concrete coordination needs with the dependency and learning cost.
* The JavaScript framework ecosystem is notorious for its volatility. There are several new frameworks and libraries being introduced to the ecosystem all the time. 

### What kinds of frameworks are there? 

There are, in reality, hundreds, if not thousands, different frameworks. Anyone, including you and me, may create their own framework. Fortunately, there are just a few that are widely popular, so it's not too bad. <a href="https://en.wikipedia.org/wiki/Comparison_of_JavaScript-based_web_frameworks
">Wikipedia</a> mentions over 20 frameworks and their comparisons, although the vast majority of those mentioned are either dead or outdated. 

Links:

* https://www.statista.com/statistics/1124699/worldwide-developer-survey-most-used-frameworks-web/

### How to learn a framework?

1. I recommend first learning the basics of Vanilla JavaScript and working on a few projects in it.
2. Then, you may try to take a crash course on the framework of your choice to obtain a rough sense of what it is and what it can be used for.
3. Then, immediately begin converting one of your previous projects to your preferred framework. 

## Different framework philosophies

Component tools address the problem of coordinating interface changes, but place the complexity in different places:

| Approach | Mental model | Cost to understand |
|---|---|---|
| React | Describe output from a render's props/state; compose behavior with hooks. | Render snapshots, identity, and synchronization with external systems. |
| Vue | Templates and reactive dependencies connect state to output. | What is reactive, when dependencies are tracked, and where reusable logic belongs. |
| Angular | Components within an integrated system for templates, DI, routing, and forms. | Framework conventions and the boundaries between signals, services, and asynchronous streams. |

These models are useful lenses, not performance rankings. React's small UI core leaves application-level decisions to additional tooling; Angular supplies more conventions; Vue supports incremental use and multiple authoring styles. Read each tool's own explanation: [React's UI model](https://react.dev/learn/describing-the-ui), [Vue's reactivity](https://vuejs.org/guide/extras/reactivity-in-depth.html), and [Angular's essentials](https://angular.dev/essentials).

### Why server rendering returned to the conversation

Moving navigation and rendering into a single-page application can preserve client state across interactions, but also puts more work on initial JavaScript loading and execution. Server rendering, static generation, and selective hydration offer other distributions of that work. They are not evidence that client applications have become obsolete. A content-heavy article and a spreadsheet-like editor need different balances.

For example, [Astro's islands](https://docs.astro.build/en/concepts/islands/) keep most content as HTML and hydrate selected interactive components; [Angular hybrid rendering](https://angular.dev/guide/ssr) lets routes use different rendering modes. The practical question is which content must be fresh, personalized, or interactive, and when. Include caching, hydration, navigation, and deployment costs in the answer. Rendering HTML on a server does not remove all client JavaScript or guarantee faster results.

## React

**Current entry-point API:** React 19 removed legacy `ReactDOM.render`. Import `createRoot` from `react-dom/client`, then call `createRoot(container).render(<App />)`. The React examples below now use `createRoot`; ensure the same code block imports it rather than importing `ReactDOM` from `react-dom`.

```jsx
import { createRoot } from 'react-dom/client';
function App() { return <button type="button">Hello</button>; }
createRoot(document.getElementById('root')).render(<App />);
```

For a new project, follow the current [React project guide](https://react.dev/learn/start-a-new-react-project), not deprecated Create React App instructions. Choose a framework or build tool based on routing, deployment, server rendering and learning goals; a library alone does not decide these requirements. The [button states illustration](https://github.com/djeada/Frontend-Notes/raw/refs/heads/main/assets/visual-examples/button-states.svg) shows UI states that are necessary regardless of framework, and the [vanilla JavaScript demo](../projects/visual-examples/index.html) provides a baseline before adding dependencies.


React is a JavaScript library for building user interfaces, often referred to as a framework due to its extensive ecosystem. Unlike a framework, which provides a structured approach to building applications, a library like React allows for more flexibility in implementation.

Pros:

- React is widely used for building user interfaces; usage surveys and hiring demand differ by population and date, so do not infer current market rankings from an undated claim. This popularity also indicates a robust job market and numerous opportunities for React developers.
- React is maintained by a community and Meta contributors, but organizational backing does not guarantee an indefinite support timeline. This backing provides confidence in React’s longevity and relevance in the industry.
- React focuses on composing UI, but a small core does not make the full application small or automatically easy to learn. Account for routing, data, rendering, and build choices as well.
- There is a huge and active community around React. This extensive community provides a wealth of resources, including tutorials, documentation, forums, and third-party libraries. Developers can easily find solutions to common problems, share knowledge, and collaborate on projects.
- React’s component-based architecture allows for reusable and maintainable code. Developers can create modular components that can be reused across different parts of an application, reducing redundancy and improving code quality.
- React reconciles component output to update interfaces. Actual performance depends on application architecture, rendering patterns, bundle size and measurement; a virtual DOM is not an automatic performance guarantee.
- React has a rich ecosystem with numerous tools and libraries that enhance development productivity. Tools such as React DevTools and appropriate state management can support development. Create React App is deprecated for new projects; consult the current React project setup guide.

Cons:

- The small core library of React means that developers often need to incorporate many other plugins and libraries to achieve desired functionality. This can lead to increased complexity in managing dependencies, potential version conflicts, and a steeper learning curve to understand how different libraries work together.
- React and its ecosystem evolve rapidly, which can be challenging for developers to keep up with. Frequent updates and changes in best practices require continuous learning and adaptation.
- Setting up a React project can involve a significant amount of boilerplate code, especially when integrating additional libraries for state management, routing, and other functionalities.
- While the basics of React are easy to grasp, advanced concepts such as state management, context API, hooks, and server-side rendering can have a steep learning curve.
- React includes component state and form-related APIs, while application routing and broader data/deployment conventions depend on the surrounding stack. Choosing those integrations adds decisions that a more integrated framework may make for you.

### Core Elements

**Reading older React:** class lifecycles, higher-order components, and render props explain patterns you will encounter in maintained applications. Hooks provide another way to compose stateful logic without changing the component hierarchy. [Classes remain supported](https://react.dev/reference/react/Component), though React recommends functions for new components. Avoid rewriting a stable component solely to make its syntax newer; migrate when a change simplifies behavior or removes a concrete maintenance problem. An Effect is not a line-for-line replacement for every lifecycle method.

#### Component

##### Modern functional component: props, state, and an observable outcome

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

**Test cases:** initial value 1; clicking Increase twice displays 3; Decrease returns to 2; the maximum cannot be exceeded. Check the disabled state's explanation and color contrast against the [button-states browser screenshot](https://github.com/djeada/Frontend-Notes/raw/refs/heads/main/assets/visual-examples/button-states-browser.png). Reference: [React state as a snapshot](https://react.dev/learn/state-as-a-snapshot).


React components are the building blocks of a React application. They can be thought of as custom, reusable HTML elements, and they encapsulate their own structure, style, and behavior.

Components in React are written using JSX, an extension to JavaScript that allows writing HTML-like syntax within JavaScript. A component is a JavaScript function or class that returns a React element.

**Example of a Class Component:**

```jsx
import React from 'react';
import { createRoot } from 'react-dom/client';

class HelloWorld extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello World</h1>
        <p>This is a paragraph</p>
      </div>
    );
  }
}

createRoot(document.getElementById("root")).render(<HelloWorld />);
```

#### Props

Props (short for properties) are read-only attributes used to pass data from parent components to child components. They are passed to the component as an argument.

**Example of Passing Props:**

```jsx
function App() {
  return <Paragraph text="This is a paragraph" />;
}

function Paragraph(props) {
  return <p>{props.text}</p>;
}
```

Props can also be passed between opening and closing tags of a component, accessible via `props.children`.

```jsx
function App() {
  return (
    <Container>
      <div>
        <h1>Hello World</h1>
        <p>This is a paragraph</p>
      </div>
    </Container>
  );
}

function Container(props) {
  return <div>{props.children}</div>;
}
```

#### Mounting

Mounting adds a component to the rendered tree. The following are **class-component lifecycle methods across mounting, updating, unmounting and error handling**, not a list of methods all invoked during mounting:

1. `constructor(props)` - Called before the component is mounted.
2. `render()` - Defines what the component UI looks like.
3. `componentDidMount()` - Called after the component is mounted.
4. `componentWillUnmount()` - Called before the component is unmounted and destroyed.
5. `componentDidCatch()` - Called when an error is thrown during rendering.

#### State

State is a way to manage dynamic data in a React component. It is an object that determines how that component renders and behaves.

**Example of Using State:**

```jsx
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  render() {
    return (
      <div>
        <h1>Hello World</h1>
        <p>This is a paragraph</p>
        <p>{this.state.count}</p>
      </div>
    );
  }
}
```

#### DOM Events

React supports all standard DOM events. Below is an example of handling a click event:

```jsx
class App extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello World</h1>
        <p>This is a paragraph</p>
        <button onClick={() => alert('Hello World')}>Click me</button>
      </div>
    );
  }
}
```

#### Virtual DOM

React uses a virtual DOM to improve performance. When a component’s state or props change, React creates a new virtual DOM tree and compares it to the previous one. Only the changed elements are updated in the real DOM.

Steps:

1. The entire virtual DOM is updated.
2. The virtual DOM is compared to its previous state.
3. Only the changed elements are updated in the real DOM.
4. The changes in the real DOM trigger the actual rendering on the screen.

This process can lead to performance improvements, especially for applications with frequent updates.

#### Conditional Rendering

Conditional rendering in React can be done using JavaScript conditional statements like `if` or ternary operators.

**Example of Conditional Rendering:**

```jsx
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false
    };
  }

  render() {
    return (
      <div>
        <h1>Hello World</h1>
        <p>This is a paragraph</p>
        <button onClick={() => this.setState({ clicked: !this.state.clicked })}>
          {this.state.clicked ? 'Clicked' : 'Not clicked'}
        </button>
      </div>
    );
  }
}
```

### Hooks

#### Effects synchronize with external systems; derived values usually do not need one

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

**Compare:** computing `const doubled = count * 2` in render needs no effect. Starting a timer inside rendering, by contrast, creates a new timer on each render and is incorrect. For network requests, cancel or ignore stale results when a dependency changes, handle loading/error/empty states, and do not put authentication secrets in browser bundles. Reference: [React synchronizing with effects](https://react.dev/learn/synchronizing-with-effects) and [you might not need an effect](https://react.dev/learn/you-might-not-need-an-effect).


Hooks are functions that let you use state and other React features without writing a class. They work inside functional components and provide a way to reuse stateful logic.

#### useState

The `useState` hook allows you to add state to functional components.

**Example of useState:**

```jsx
function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>Hello World</h1>
      <p>This is a paragraph</p>
      <button onClick={() => setCount(count + 1)}>
        {count}
      </button>
    </div>
  );
}
```

#### useEffect

The `useEffect` hook lets you perform side effects in functional components. It runs after the component renders.

**Example of useEffect:**

```jsx
function App() {
  useEffect(() => {
    console.log('Component rendered');
  });

  return (
    <div>
      <h1>Hello World</h1>
      <p>This is a paragraph</p>
    </div>
  );
}
```

#### useRef

The `useRef` hook is used to access DOM elements directly.

**Example of useRef:**

```jsx
function App() {
  const inputRef = useRef();
  const onButtonClick = () => {
    inputRef.current.focus();
  };

  return (
    <div>
      <h1>Hello World</h1>
      <p>This is a paragraph</p>
      <input ref={inputRef} type="text" />
      <button onClick={onButtonClick}>Focus the input</button>
    </div>
  );
}
```

#### useReducer

The `useReducer` hook is an alternative to `useState` for managing complex state logic.

**Example of useReducer:**

```jsx
function App() {
  const [count, dispatch] = useReducer((state, action) => {
    switch (action.type) {
      case 'increment':
        return state + 1;
      case 'decrement':
        return state - 1;
      default:
        throw new Error();
    }
  }, 0);

  return (
    <div>
      <h1>Hello World</h1>
      <p>This is a paragraph</p>
      <button onClick={() => dispatch({ type: 'increment' })}>
        {count}
      </button>
      <button onClick={() => dispatch({ type: 'decrement' })}>
        {count}
      </button>
    </div>
  );
}
```

#### useContext

The `useContext` hook allows you to access the context object and subscribe to its changes.

**Example of useContext:**

```jsx
function App() {
  const theme = useContext(ThemeContext);

  return (
    <div style={{ background: theme.background, color: theme.foreground }}>
      <h1>Hello World</h1>
      <p>This is a paragraph</p>
    </div>
  );
}
```

#### useMemo

The `useMemo` hook memoizes expensive computations to avoid re-executing them on every render.

**Example of useMemo:**

```jsx
function App() {
  const expensiveComputation = () => {
    let sum = 0;
    for (let i = 0; i < 10000000; i++) {
      sum += i;
    }
    return sum;
  };

  const memoizedComputation = useMemo(expensiveComputation, []);

  return (
    <div>
      <h1>Hello World</h1>
      <p>This is a paragraph</p>
      <p>{memoizedComputation}</p>
    </div>
  );
}
```

#### Context API

The Context API is used for managing global state across a React application, especially for passing data through the component tree without having to pass props down manually at every level.

**Creating a Context:**

```jsx
const ThemeContext = React.createContext('light');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Toolbar />
    </ThemeContext.Provider>
  );
}

function Toolbar() {
  return (
    <div>
      <ThemedButton />
    </div>
  );
}

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <button style={{ background: theme === 'dark' ? '#333' : '#FFF' }}>Themed Button</button>;
}
```

#### Error Boundaries

Error boundaries are React components that catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI instead of the component tree that crashed.

**Example of an Error Boundary:**

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.log(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}

function App() {
  return (
    <ErrorBoundary>
      <ComponentThatMayError />
    </ErrorBoundary>
  );
}
```

#### Higher-Order Components (HOCs)

HOCs are functions that take a component and return a new component. They are used to reuse component logic.

**Example of a Higher-Order Component:**

```jsx
function withLoading(Component) {
  return function WithLoadingComponent({ isLoading, ...props }) {
    if (!isLoading) return <Component {...props} />;
    return <p>Loading...</p>;
  };
}

function MyComponent(props) {
  return <div>Data: {props.data}</div>;
}

const MyComponentWithLoading = withLoading(MyComponent);

function App() {
  return <MyComponentWithLoading isLoading={true} data="Some data" />;
}
```

#### Render Props

Render props is a technique for sharing code between React components using a prop whose value is a function.

**Example of Render Props:**

```jsx
class Mouse extends React.Component {
  constructor(props) {
    super(props);
    this.state = { x: 0, y: 0 };
  }

  handleMouseMove = (event) => {
    this.setState({
      x: event.clientX,
      y: event.clientY,
    });
  };

  render() {
    return (
      <div style={{ height: '100vh' }} onMouseMove={this.handleMouseMove}>
        {this.props.render(this.state)}
      </div>
    );
  }
}

function App() {
  return (
    <Mouse render={({ x, y }) => (
      <h1>The mouse position is ({x}, {y})</h1>
    )} />
  );
}
```

#### Portals

Portals provide a way to render children into a DOM node that exists outside the DOM hierarchy of the parent component.

**Example of Using Portals:**

```jsx
import ReactDOM from 'react-dom';

function Modal({ children }) {
  return ReactDOM.createPortal(
    <div className="modal">
      {children}
    </div>,
    document.getElementById('modal-root')
  );
}

function App() {
  return (
    <div>
      <h1>Hello World</h1>
      <Modal>
        <h2>This is a modal</h2>
      </Modal>
    </div>
  );
}
```

#### Fragments

Fragments let you group a list of children without adding extra nodes to the DOM.

**Example of Using Fragments:**

```jsx
function App() {
  return (
    <>
      <h1>Hello World</h1>
      <p>This is a paragraph</p>
    </>
  );
}
```

#### React.memo

`React.memo` is a higher-order component that memoizes the result of a component rendering, preventing unnecessary re-renders.

**Example of Using React.memo:**

```jsx
const MyComponent = React.memo(function MyComponent({ count }) {
  console.log('Rendered MyComponent');
  return <div>{count}</div>;
});

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <MyComponent count={count} />
    </div>
  );
}
```

#### Concurrent rendering and transitions

Older articles use “Concurrent Mode” as if it were one switch. React 18 introduced concurrent rendering through features such as transitions. The root API below establishes an application root; it does not mark every update as non-urgent or move expensive JavaScript onto a worker. See the [React 18 explanation](https://react.dev/blog/2022/03/29/react-v18) and [`useTransition`](https://react.dev/reference/react/useTransition).

**Current root setup:**

```jsx
import { createRoot } from 'react-dom/client';

const root = createRoot(document.getElementById('root'));
root.render(<App />);
```

**Practical distinction:** typing into an input should stay urgent; updating an expensive results view may be a transition. Measure interaction delays and choose the boundary deliberately. Concurrency does not make a slow synchronous loop free.

#### Suspense

Suspense lets you wait for some code to load and declaratively specify a loading state.

**Example of Using Suspense:**

```jsx
const OtherComponent = React.lazy(() => import('./OtherComponent'));

function App() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <OtherComponent />
      </Suspense>
    </div>
  );
}
```

#### Refs and the useImperativeHandle Hook

Refs provide a way to access the DOM nodes or React elements created in the render method. The `useImperativeHandle` hook customizes the instance value that is exposed when using refs.

**Example of Using Refs and useImperativeHandle:**

```jsx
function CustomInput(props, ref) {
  const inputRef = useRef();
  useImperativeHandle(ref, () => ({
    focus: () => {
      inputRef.current.focus();
    },
  }));
  return <input ref={inputRef} />;
}

CustomInput = forwardRef(CustomInput);

function App() {
  const inputRef = useRef();

  return (
    <div>
      <CustomInput ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus Input</button>
    </div>
  );
}
```

### Minimal Web App Using React

Let's take a look at a minimal web app that uses React. This guide will walk you through setting up the app from scratch, including installing necessary dependencies, setting up project structure, configuring Babel and Webpack, and writing the actual React code.

#### Prerequisites

To install any dependency, a package manager is needed. The most common one is NPM, which comes with Node.js.

1. Download and install [Node.js](https://nodejs.org/en/download/) by selecting the right installer for your platform. It includes the NPM package manager.
2. Verify that NPM was installed correctly by running the following command in your terminal:

```sh
npm --version
```

3. Create an empty NPM package by initializing a new project:

```sh
npm init
```

4. This will create a `package.json` file, which is a build configuration file that defines all dependencies and scripts for creating and testing the project.

#### Project Structure

At the end of this setup, your project will have the following structure:

```
Project Root
│
├── src
│   └── App.js
│
├── dist
│   └── index.html
│
├── package.json
├── webpack.config.js
└── .babelrc
```

#### Transpiler

Transpilers are used to convert code between various programming languages or versions of the same programming language. If we use any modern JavaScript features or frameworks, we can use a transpiler to transform our code to an earlier version of JavaScript that is supported by all web browsers.

The transpiler used in this example is Babel. To install it, use the following commands:

```sh
npm install --save-dev babel-loader
npm install --save-dev @babel/preset-react
npm install --save-dev @babel/preset-env
```

Create a `.babelrc` file to configure Babel. This file, in JSON format, describes how to transpile JavaScript code:

```json
{
    "presets": ["@babel/preset-env", "@babel/preset-react"]
}
```

#### Module Bundler

Webpack combines all NPM dependencies into a single `bundle.js` that can run in a browser. Use the following command to install it:

```sh
npm install --save-dev webpack webpack-cli webpack-dev-server
```

A special file named `webpack.config.js` is needed to configure Webpack. The following is an example of this file:

```javascript
const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: path.resolve(__dirname, './src/App.js'),
    module: {
        rules: [{
            test: /\.jsx?$/,
            exclude: /node_modules/,
            use: {
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/preset-env', '@babel/preset-react']
                }
            }
        }]
    },
    output: {
        path: path.resolve(__dirname, './dist'),
        filename: 'bundle.js'
    },
    devServer: {
        static: path.resolve(__dirname, './dist'),
        port: 8000,
        hot: true
    },
};
```

#### Installing React

Two libraries are needed to use React: `react` and `react-dom`. Use the following command to install them:

```sh
npm install --save react react-dom
```

#### The Actual React Code

In the `src/App.js` file, include the following React script:

```javascript
import React from 'react';
import { createRoot } from 'react-dom/client';

const App = () => {
    return <h1>Hello World</h1>;
};

createRoot(document.getElementById("root")).render(<App />);
```

In addition to JavaScript, an HTML file is required to render the React code. Place the `index.html` file in the `dist` folder:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Minimal React App</title>
</head>
<body>
    <div id="root"></div>
    <script src="bundle.js"></script>
</body>
</html>
```

#### Usage

1. To use the app, first, start the development server. Add the following script to the `scripts` section of your `package.json` file:

```json
"scripts": {
    "start": "webpack serve --mode development"
}
```

2. Now, start the server by invoking the following command in your terminal:

```sh
npm start
```

3. Open a web browser and navigate to `http://localhost:8000/` to see the React app in action.

By following these steps, you will have set up a minimal React web application with Babel and Webpack.

## Vue

### Vue 2, Vue 3, and two supported authoring styles

Vue's incremental adoption model lets a team enhance a page before committing to a full application. But Vue's major versions are not interchangeable: [Vue 2 reached end of life on 31 December 2023](https://v2.vuejs.org/eol/). `new Vue(...)` and global `Vue.use(...)` belong to that older setup; Vue 3 uses `createApp(...)` and installs plugins on the app instance.

Do not confuse this version change with **Options API versus Composition API**. Options groups code by categories such as `data`, `computed`, and `methods`; Composition groups related behavior using functions and composables. Composition can keep a complex feature's state and effects together, while Options can offer a clear structure for a smaller component. [Options API is not deprecated](https://vuejs.org/guide/extras/composition-api-faq.html#will-options-api-be-deprecated). The Options-style components below can be valid Vue 3 code.

**Migration lesson:** check router, store, component-library, and build-plugin compatibility together. Changing the entry point while leaving a Vue 2 compiler or plugin in the dependency tree produces a mixed setup, not a migration.

Vue.js is a progressive JavaScript framework used for building user interfaces and single-page applications. It is designed to be incrementally adoptable, meaning you can use as much or as little of Vue as you need.

### Pros and Cons

Pros:

- Vue is easy to learn and integrate with projects, even if they are using other JavaScript libraries.
- It can be used for small parts of a webpage or for large-scale single-page applications.
- Vue provides a reactive data-binding system.
- Similar to React, Vue uses a component-based structure.

Cons:

- Although growing, Vue's ecosystem is not as extensive as React's.
- The community and corporate backing are smaller compared to React.

### Core Elements

#### Component

Vue components are reusable instances with their own structure, style, and behavior. They are defined using a single file component (SFC) format with the `.vue` extension.

**Example of a Vue Component:**

```html
<template>
  <div>
    <h1>Hello World</h1>
    <p>This is a paragraph</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld'
}
</script>

<style scoped>
h1 {
  color: blue;
}
</style>
```

#### Props

Props are custom attributes you can register on a component. When a value is passed to a prop attribute, it becomes a property on that component instance.

**Example of Passing Props:**

```html
<template>
  <div>
    <Paragraph text="This is a paragraph" />
  </div>
</template>

<script>
import Paragraph from './Paragraph.vue';

export default {
  components: {
    Paragraph
  }
}
</script>
```

```html
<template>
  <p>{{ text }}</p>
</template>

<script>
export default {
  props: ['text']
}
</script>
```

#### Directives

Directives are special tokens in the markup that tell the library to do something to a DOM element. Vue has built-in directives such as `v-bind`, `v-model`, and `v-if`.

**Example of Using Directives:**

```html
<template>
  <div>
    <input v-model="message" />
    <p>{{ message }}</p>
    <p v-if="seen">Now you see me</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
      seen: true
    }
  }
}
</script>
```

#### Computed Properties

Computed properties are cached based on their dependencies and only re-evaluate when necessary. They are useful for complex data manipulations.

**Example of Computed Properties:**

```html
<template>
  <div>
    <p>Original message: {{ message }}</p>
    <p>Reversed message: {{ reversedMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello World'
    }
  },
  computed: {
    reversedMessage() {
      return this.message.split('').reverse().join('');
    }
  }
}
</script>
```

#### Methods

Methods are functions that are executed when events occur. They are useful for handling user inputs or other interactions.

**Example of Methods:**

```html
<template>
  <div>
    <button @click="greet">Greet</button>
  </div>
</template>

<script>
export default {
  methods: {
    greet() {
      alert('Hello World');
    }
  }
}
</script>
```

#### Lifecycle Hooks

Vue components have a series of lifecycle hooks that allow you to add code at specific stages.

1. `beforeCreate`
2. `created`
3. `beforeMount`
4. `mounted`
5. `beforeUpdate`
6. `updated`
7. `beforeDestroy`
8. `destroyed`

**Example of Lifecycle Hooks:**

```html
<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello World'
    }
  },
  created() {
    console.log('Component created');
  },
  mounted() {
    console.log('Component mounted');
  }
}
</script>
```

#### Watchers

Watchers are used to perform actions in response to data changes. They are particularly useful for asynchronous operations.

**Example of Watchers:**

```html
<template>
  <div>
    <input v-model="question" />
    <p>{{ answer }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      question: '',
      answer: 'I cannot give you an answer until you ask a question!'
    }
  },
  watch: {
    question(newQuestion, oldQuestion) {
      this.answer = 'Waiting for you to stop typing...';
      this.getAnswer();
    }
  },
  methods: {
    getAnswer() {
      setTimeout(() => {
        this.answer = 'The answer to your question is 42!';
      }, 1000);
    }
  }
}
</script>
```

### Vue Router

Vue Router is the official router for Vue.js, making it easy to map components to routes and manage navigation.

**Example of Vue Router:**

```javascript
import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import Home from './components/Home.vue';
import About from './components/About.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About }
  ]
});

createApp(App).use(router).mount('#app');
```

This uses Vue 3's router API; `App.vue` needs a `<RouterView />` for matched content. History mode also needs host routing that can serve the app on a direct visit to `/about`. See [Vue Router's guide](https://router.vuejs.org/guide/).

### Vuex

**Status:** Vuex helps explain existing centralized stores, but [its maintainers recommend Pinia for new projects](https://vuex.vuejs.org/). Vuex 4 works with Vue 3; the example below uses that pairing. See the Pinia example in [state management](#state-management-tools) before choosing a new store.

Vuex is a state management pattern + library for Vue.js applications. It serves as a centralized store for all the components in an application, with rules ensuring that the state can only be mutated in a predictable fashion.

**Example of Vuex:**

```javascript
import { createApp } from 'vue';
import { createStore } from 'vuex';
import App from './App.vue';

const store = createStore({
  state() {
    return { count: 0 };
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  }
});

createApp(App).use(store).mount('#app');
```

### Minimal Web App Using Vue

**Choose the learning goal:** for a new Vue 3 application, the [official quick start](https://vuejs.org/guide/quick-start.html) uses `npm create vue@latest` and a Vite-based setup. The manual Webpack walkthrough below exposes the moving parts for learning or maintenance; it is not required ceremony for every Vue project. Use a Node version supported by your selected tools and keep the lockfile.

Let's take a look at a minimal web app that uses Vue. This guide will walk you through setting up the app from scratch, including installing necessary dependencies, setting up project structure, configuring Babel and Webpack, and writing the actual Vue code.

#### Prerequisites

To install any dependency, a package manager is needed. The most common one is NPM, which comes with Node.js.

1. Download and install [Node.js](https://nodejs.org/en/download/) by selecting the right installer for your platform. It includes the NPM package manager.
2. Verify that NPM was installed correctly by running the following command in your terminal:

```sh
npm --version
```

3. Create an empty NPM package by initializing a new project:

```sh
npm init
```

4. This will create a `package.json` file, which is a build configuration file that defines all dependencies and scripts for creating and testing the project.

#### Project Structure

At the end of this setup, your project will have the following structure:

```
│
├── src
│   ├── main.js
│   └── App.vue
│
├── dist
│   └── index.html
│
├── package.json
├── webpack.config.js
└── .babelrc
```

#### Transpiler

Transpilers are used to convert code between various programming languages or versions of the same programming language. If we use any modern JavaScript features or frameworks, we can use a transpiler to transform our code to an earlier version of JavaScript that is supported by all web browsers.

The transpiler used in this example is Babel. To install it, use the following commands:

```sh
npm install --save-dev babel-loader @babel/core @babel/preset-env
npm install --save-dev vue-loader@17 @vue/compiler-sfc@3 style-loader css-loader
```

Create a `.babelrc` file to configure Babel. This file, in JSON format, describes how to transpile JavaScript code:

```json
{
    "presets": ["@babel/preset-env"]
}
```

#### Module Bundler

Webpack combines all NPM dependencies into a single `bundle.js` that can run in a browser. Use the following command to install it:

```sh
npm install --save-dev webpack webpack-cli webpack-dev-server
```

A special file named `webpack.config.js` is needed to configure Webpack. The following is an example of this file:

```javascript
const path = require('path');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
    entry: path.resolve(__dirname, './src/main.js'),
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin()
    ],
    output: {
        path: path.resolve(__dirname, './dist'),
        filename: 'bundle.js'
    },
    devServer: {
        static: path.resolve(__dirname, './dist'),
        port: 8000,
        hot: true
    },
};
```

#### Installing Vue

To use Vue, you need to install the `vue` library. Use the following command to install it:

```sh
npm install --save vue@3
```

Keep `vue` and `@vue/compiler-sfc` on matching versions in the lockfile. Vue 2's `vue-template-compiler` is not the compiler for this setup. See the [Vue Loader repository's v16/v17 notes and compiler explanation](https://github.com/vuejs/vue-loader). Its older published installation page describes the Vue 2 compiler workflow, so check the version before copying commands.

#### The Actual Vue Code

In the `src/App.vue` file, include the following Vue template:

```vue
<template>
  <div class="app">
    <h1>Hello World</h1>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
.app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

In the `src/main.js` file, include the following Vue script:

```javascript
import { createApp } from 'vue';
import App from './App.vue';

createApp(App).mount('#app');
```

In addition to JavaScript, an HTML file is required to render the Vue code. Place the `index.html` file in the `dist` folder:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Minimal Vue App</title>
</head>
<body>
  <div id="app"></div>
  <script src="bundle.js"></script>
</body>
</html>
```

#### Usage

1. To use the app, first, start the development server. Add the following script to the `scripts` section of your `package.json` file:

```json
"scripts": {
    "start": "webpack serve --mode development"
}
```

2. Now, start the server by invoking the following command in your terminal:

```sh
npm start
```

3. Open a web browser and navigate to `http://localhost:8000/` to see the Vue app in action.

By following these steps, you will have set up a minimal Vue web application with Babel and Webpack.

## Angular

### From NgModules to standalone components and signals

NgModules organized declarations and dependency scopes in earlier Angular applications. They remain relevant when maintaining those applications, but [Angular recommends standalone components for new code](https://angular.dev/guide/ngmodules/overview). Standalone components make their dependencies explicit without requiring an app module. This is an evolution within Angular, not a replacement of Angular by a different framework.

For a current CLI project, a small standalone counter can be written as follows. Its HTML needs `<app-root></app-root>`; the CLI supplies the build pipeline:

```typescript
import { Component, signal } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  standalone: true,
  template: `<button type="button" (click)="count.update(increment)">
    Count: {{ count() }}
  </button>`
})
class CounterComponent {
  readonly count = signal(0);
  readonly increment = (value: number) => value + 1;
}

bootstrapApplication(CounterComponent).catch(console.error);
```

[Signals](https://angular.dev/guide/signals) model reactive values and derivations; asynchronous streams still have different concerns, such as cancellation and combining events. Do not mechanically replace every RxJS pipeline with a signal. The module-based examples below document older application structure; follow the [standalone migration](https://angular.dev/reference/migrations/standalone) when changing an existing app, and use version-matched CLI instructions for a new one.

Angular is a platform and framework for building single-page client applications using HTML and TypeScript. Angular is developed and maintained by Google, providing a robust and complete solution for web application development.

### Pros and Cons

Pros:

- Angular provides a complete solution for front-end development, including a powerful CLI, routing, form handling, HTTP client, and more.
- Built with TypeScript, which offers static typing, better tooling, and helps catch errors early.
- Provides a powerful dependency injection mechanism.
- Promotes a modular approach to building applications.

Cons:

- Can be complex and have a steep learning curve compared to other frameworks.
- Angular applications can be verbose, requiring more boilerplate code.

### Core Elements

#### Component

Components are the fundamental building blocks of an Angular application. Each component consists of an HTML template, a CSS stylesheet, and a TypeScript class.

**Example of an Angular Component:**

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Hello World';
}
```

```html
<!-- app.component.html -->
<div>
  <h1>{{ title }}</h1>
  <p>This is a paragraph</p>
</div>
```

#### Modules

NgModules group declarations, imports, and providers in module-based applications. Standalone applications do not require a root NgModule. If you place a component in an NgModule's `declarations`, declare it with `standalone: false` on current Angular; the standalone counter above is bootstrapped directly instead.

**Example of an Angular Module:**

```typescript
// app.module.ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

#### Directives

Directives are classes that add additional behavior to elements in your Angular applications. There are three kinds of directives in Angular: components, structural directives, and attribute directives.

**Older structural-directive syntax (`ngIf`):**

```html
<div *ngIf="isVisible">
  This is visible.
</div>
```

For new templates, use Angular's [built-in control flow](https://angular.dev/guide/templates/control-flow), such as `@if (isVisible) { <div>This is visible.</div> }`. Read old `*ngIf` examples as version-specific syntax; use the official migration for an existing application.

**Example of an Attribute Directive:**

```typescript
import { Directive, ElementRef, Renderer2 } from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  constructor(el: ElementRef, renderer: Renderer2) {
    renderer.setStyle(el.nativeElement, 'backgroundColor', 'yellow');
  }
}
```

#### Services and Dependency Injection

Services in Angular are used to share data or logic across multiple components. Dependency Injection (DI) is a design pattern used to implement IoC, allowing a class to receive its dependencies from an external source.

**Example of a Service:**

```typescript
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  private data: string[] = ['Data 1', 'Data 2', 'Data 3'];

  getData() {
    return this.data;
  }
}
```

**Injecting a Service into a Component:**

```typescript
import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-data',
  template: `
    <ul>
      <li *ngFor="let item of data">{{ item }}</li>
    </ul>
  `
})
export class DataComponent implements OnInit {
  data: string[];

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.data = this.dataService.getData();
  }
}
```

#### Routing

Angular Router enables navigation from one view to the next as users perform application tasks. It is a separate module in Angular that needs to be imported.

**Example of Configuring Routes:**

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

**Using Router Outlet:**

```html
<!-- app.component.html -->
<nav>
  <a routerLink="/">Home</a>
  <a routerLink="/about">About</a>
</nav>
<router-outlet></router-outlet>
```

#### Forms

Angular provides two approaches to handling user input through forms: reactive forms and template-driven forms.

**Example of Template-Driven Form:**

```html
<!-- app.component.html -->
<form #form="ngForm" (ngSubmit)="onSubmit(form)">
  <input name="name" ngModel required />
  <button type="submit">Submit</button>
</form>
```

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})
export class AppComponent {
  onSubmit(form) {
    console.log(form.value);
  }
}
```

**Example of Reactive Form:**

```typescript
// app.module.ts
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  imports: [
    // other imports
    ReactiveFormsModule
  ],
  // other properties
})
export class AppModule { }
```

```typescript
// app.component.ts
import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})
export class AppComponent {
  form = new FormGroup({
    name: new FormControl('')
  });

  onSubmit() {
    console.log(this.form.value);
  }
}
```

```html
<!-- app.component.html -->
<form [formGroup]="form" (ngSubmit)="onSubmit()">
  <input formControlName="name" />
  <button type="submit">Submit</button>
</form>
```

### Angular CLI

The Angular CLI is a powerful tool that provides commands to scaffold, build, and manage Angular applications.

**Creating a New Angular Application:**

```bash
ng new my-angular-app
```

**Serving the Application:**

```bash
cd my-angular-app
ng serve
```

**Generating Components, Services, etc.:**

```bash
ng generate component my-component
ng generate service my-service
```

### HttpClient

Angular's `HttpClient` service allows you to communicate with backend services over the HTTP protocol.

**Example of Using HttpClient:**

```typescript
// app.module.ts
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [
    // other imports
    HttpClientModule
  ],
  // other properties
})
export class AppModule { }
```

```typescript
// data.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  constructor(private http: HttpClient) {}

  getData() {
    return this.http.get('https://api.example.com/data');
  }
}
```

```typescript
// data.component.ts
import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-data',
  template: `
    <ul>
      <li *ngFor="let item of data">{{ item }}</li>
    </ul>
  `
})
export class DataComponent implements OnInit {
  data: any;

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.dataService.getData().subscribe(data => {
      this.data = data;
    });
  }
}
```

#### Angular Material

Angular Material is a UI component library for Angular developers. It follows Google's Material Design guidelines and provides a rich set of UI components.

**Example of Using Angular Material:**

```bash
ng add @angular/material
```

```typescript
// app.module.ts
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';

@NgModule({
  imports: [
    // other imports
    MatButtonModule,
    MatInputModule
  ],
  // other properties
})
export class AppModule { }
```

```html
<!-- app.component.html -->
<button mat-raised-button>Click me</button>
<input matInput placeholder="Enter text">
```

#### Custom Directives

Custom directives in Angular allow you to extend the functionality of HTML elements.

**Example of a Custom Directive:**

```typescript
import { Directive, ElementRef, Renderer2, HostListener } from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  constructor(private el: ElementRef, private renderer: Renderer2) {}

  @HostListener('mouseenter') onMouseEnter() {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', 'yellow');
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', 'white');
  }
}
```

```html
<!-- app.component.html -->
<p appHighlight>Hover over me!</p>
```

#### Pipes

Pipes are a way to transform data in templates. Angular provides several built-in pipes, and you can also create your own custom pipes.

**Example of a Custom Pipe:**

```typescript
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({name: 'exponentialStrength'})
export class ExponentialStrengthPipe implements PipeTransform {
  transform(value: number, exponent: string): number {
    let exp = parseFloat(exponent);
    return Math.pow(value, isNaN(exp) ? 1 : exp);
  }
}
```

```html
<!-- app.component.html -->
<p>{{ 2 | exponentialStrength: '10' }}</p>
```

#### Lazy Loading

Lazy loading is a technique in Angular to load modules only when they are needed. This can significantly improve the performance of your application.

**Example of Lazy Loading:**

```typescript
// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'feature',
    loadChildren: () => import('./feature/feature.module').then(m => m.FeatureModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

```typescript
// feature-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FeatureComponent } from './feature.component';

const routes: Routes = [
  { path: '', component: FeatureComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FeatureRoutingModule { }
```

#### Testing

Angular provides robust tools for testing your applications, including unit tests and end-to-end tests.

**Example of Unit Testing with Jasmine and Karma:**

```typescript
import { TestBed } from '@angular/core/testing';
import { AppComponent } from './app.component';

describe('AppComponent', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AppComponent],
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app).toBeTruthy();
  });
});
```

**Example of End-to-End Testing with Protractor:**

```typescript
// e2e/src/app.e2e-spec.ts
import { browser, by, element } from 'protractor';

describe('workspace-project App', () => {
  it('should display welcome message', () => {
    browser.get('/');
    expect(element(by.css('app-root h1')).getText()).toEqual('Welcome to app!');
  });
});
```

#### Angular Animations

Angular provides a module for adding animations to your applications. The `@angular/animations` package offers a DSL (Domain Specific Language) to define and run animations.

**Example of Angular Animations:**

```typescript
// app.module.ts
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  imports: [
    // other imports
    BrowserAnimationsModule
  ],
  // other properties
})
export class AppModule { }
```

```typescript
// app.component.ts
import { trigger, state, style, transition, animate } from '@angular/animations';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  animations: [
    trigger('openClose', [
      state('open', style({
        height: '200px',
        opacity: 1,
        backgroundColor: 'yellow'
      })),
      state('closed', style({
        height: '100px',
        opacity: 0.5,
        backgroundColor: 'green'
      })),
      transition('open => closed', [
        animate('0.5s')
      ]),
      transition('closed => open', [
        animate('0.5s')
      ]),
    ]),
  ],
})
export class AppComponent {
  isOpen = true;

  toggle() {
    this.isOpen = !this.isOpen;
  }
}
```

```html
<!-- app.component.html -->
<div [@openClose]="isOpen ? 'open' : 'closed'" class="box">
  <button (click)="toggle()">Toggle</button>
</div>
```

#### Server-side rendering: from Angular Universal to Angular SSR

Older tutorials use Angular Universal and `@nguniversal/express-engine`. Current Angular integrates server and hybrid rendering through `@angular/ssr`. In an existing compatible CLI project, add it with:

```bash
ng add @angular/ssr
```

Choose prerendering or request-time rendering by route, then inspect the generated scripts and deployment output. Script names from older Universal tutorials are not a stable interface. SSR adds server execution and caching concerns; it does not automatically improve every route. Follow the [current SSR guide](https://angular.dev/guide/ssr).

### Minimal Web App Using Angular

**Historical build anatomy:** the walkthrough below demonstrates an NgModule-based, manually configured Webpack application. It is not the current Angular CLI setup recipe. Use the [Angular installation guide](https://angular.dev/installation) for new work; match Angular, TypeScript, Node, compiler tooling, and bootstrapping style when reproducing an older project. The standalone example above shows the newer component model.

Let's take a look at a minimal web app that uses Angular. This guide will walk you through setting up the app from scratch, including installing necessary dependencies, setting up project structure, configuring TypeScript and Webpack, and writing the actual Angular code.

#### Prerequisites

To install any dependency, a package manager is needed. The most common one is NPM, which comes with Node.js.

1. Download and install [Node.js](https://nodejs.org/en/download/) by selecting the right installer for your platform. It includes the NPM package manager.
2. Verify that NPM was installed correctly by running the following command in your terminal:

```sh
npm --version
```

3. Create an empty NPM package by initializing a new project:

```sh
npm init
```

4. This will create a `package.json` file, which is a build configuration file that defines all dependencies and scripts for creating and testing the project.

#### Project Structure

At the end of this setup, your project will have the following structure:

```
│
├── src
│   ├── app
│   │   ├── app.component.ts
│   │   ├── app.component.html
│   │   ├── app.component.css
│   │   └── app.module.ts
│   └── main.ts
│
├── dist
│   └── index.html
│
├── package.json
├── tsconfig.json
└── webpack.config.js
```

#### Installing Angular

To use Angular, you need to install the Angular core library and its dependencies. Use the following command to install them:

```sh
npm install --save @angular/core @angular/common @angular/compiler @angular/platform-browser @angular/platform-browser-dynamic @angular/router rxjs zone.js
```

#### Setting Up TypeScript

Angular is built using TypeScript, a statically typed superset of JavaScript. To install TypeScript and configure it, use the following command:

```sh
npm install --save-dev typescript ts-loader
```

Create a `tsconfig.json` file to configure TypeScript. This file, in JSON format, describes how to compile TypeScript code:

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "es2015",
    "moduleResolution": "node",
    "sourceMap": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "lib": ["es2017", "dom"],
    "outDir": "./dist",
    "baseUrl": "./",
    "paths": {
      "@app/*": ["src/app/*"]
    }
  },
  "exclude": ["node_modules"]
}
```

#### Module Bundler

Webpack combines all NPM dependencies into a single `bundle.js` that can run in a browser. Use the following command to install it:

```sh
npm install --save-dev webpack webpack-cli webpack-dev-server html-webpack-plugin
```

A special file named `webpack.config.js` is needed to configure Webpack. The following is an example of this file:

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: path.resolve(__dirname, './src/main.ts'),
  resolve: {
    extensions: ['.ts', '.js']
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/
      },
      {
        test: /\.html$/,
        use: 'html-loader'
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, './src/index.html')
    })
  ],
  output: {
    path: path.resolve(__dirname, './dist'),
    filename: 'bundle.js'
  },
  devServer: {
    static: path.resolve(__dirname, './dist'),
    port: 8000,
    hot: true
  },
};
```

#### The Actual Angular Code

Create an Angular component in the `src/app/app.component.ts` file:

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Hello World';
}
```

Create the HTML template for the component in `src/app/app.component.html`:

```html
<h1>{{ title }}</h1>
```

Create the CSS for the component in `src/app/app.component.css`:

```css
h1 {
  color: #2c3e50;
  font-family: Arial, sans-serif;
  text-align: center;
  margin-top: 50px;
}
```

Create the main module for the application in `src/app/app.module.ts`:

```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

Create the main entry file for the application in `src/main.ts`:

```typescript
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
```

Create the HTML file for the application in `src/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Minimal Angular App</title>
</head>
<body>
  <app-root></app-root>
  <script src="bundle.js"></script>
</body>
</html>
```

#### Usage

1. To use the app, first, start the development server. Add the following script to the `scripts` section of your `package.json` file:

```json
"scripts": {
    "start": "webpack serve --mode development"
}
```

2. Now, start the server by invoking the following command in your terminal:

```sh
npm start
```

3. Open a web browser and navigate to `http://localhost:8000/` to see the Angular app in action.

By following these steps, you will have set up a minimal Angular web application with TypeScript and Webpack.

## State Management Tools

State tools make different tradeoffs about ownership, updates, and observation. The examples below include both current approaches and historical APIs worth recognizing in existing code.

### Choose the owner before the library

A dialog's open state may belong to one component; a shareable search filter may belong in the URL; cached server data needs freshness and invalidation rules. Putting all three in one global object does not solve their different lifecycles. Copying fetched data into a store also creates responsibility for keeping that copy current.

Redux emphasizes explicit actions and reducers; reactive stores emphasize observable dependencies; local state keeps ownership close to a component. Choose the smallest scope that gives all consumers a consistent view. A team debugging cross-screen updates may value explicit event history more than a tiny counter example suggests.

### Pinia for new Vue stores

Vuex established centralized state with mutations and actions. Pinia is the Vue team's recommended successor for new projects; existing Vuex stores can migrate incrementally. Install `pinia`; a minimal Vue 3 setup uses two modules:

```javascript
// stores/counter.js
import { defineStore } from 'pinia';
export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  actions: {
    increment() { this.count += 1; }
  }
});
```

```javascript
// main.js
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
createApp(App).use(createPinia()).mount('#app');
```

Inside a component's `setup`, assign `const counter = useCounterStore()` and use `counter.count` and `counter.increment()`. Directly destructuring reactive state can lose its reactive connection; use the documented helpers when needed. See [Pinia's core concepts](https://pinia.vuejs.org/core-concepts/).

### Redux

**Evolution:** the hand-written action types and `createStore` below explain Redux's original mechanics. For new code, [Redux recommends Redux Toolkit](https://redux.js.org/usage/migrating-to-modern-redux). `createStore` is deprecated as guidance, but [remains functional](https://redux.js.org/api/createstore); Redux itself has not been replaced by Toolkit.

The same counter can use `createSlice` and `configureStore`. Install `@reduxjs/toolkit`; React bindings additionally use `react-redux` and a `<Provider store={store}>` around the app:

```javascript
import { configureStore, createSlice } from '@reduxjs/toolkit';
const counter = createSlice({
  name: 'counter',
  initialState: { count: 0 },
  reducers: {
    increment(state) { state.count += 1; },
    decrement(state) { state.count -= 1; }
  }
});
export const { increment, decrement } = counter.actions;
export const store = configureStore({ reducer: counter.reducer });
```

The apparent mutation is safe **inside these Toolkit reducers** because Immer produces immutable updates; it is not permission to mutate arbitrary Redux state. Toolkit reduces ceremony while retaining actions, reducers, and predictable updates. Reference: [`createSlice`](https://redux-toolkit.js.org/api/createSlice).

Redux is a predictable state container for JavaScript apps. It is commonly used with React but can be used with any other JavaScript framework or library.

Pros:

- Predictable state updates with strict rules.
- Centralized state makes debugging and testing easier.
- Large ecosystem and community support.

Cons:

- Can be verbose and require boilerplate code.
- Learning curve for newcomers.

Core Concepts:

- **Store:** Holds the application state.
- **Actions:** Plain objects representing events that describe something that happened in the application.
- **Reducers:** Pure functions that take the current state and an action, and return a new state.

**Example:**

```javascript
// actions.js
export const increment = () => ({ type: 'INCREMENT' });
export const decrement = () => ({ type: 'DECREMENT' });

// reducer.js
const initialState = { count: 0 };

export const counter = (state = initialState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state;
  }
};

// store.js
import { createStore } from 'redux';
import { counter } from './reducer';

const store = createStore(counter);

// App.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement } from './actions';

const App = () => {
  const count = useSelector(state => state.count);
  const dispatch = useDispatch();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch(increment())}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
    </div>
  );
};

export default App;
```

### Vuex

**Legacy API example:** the code in this section uses Vue 2/Vuex 3 conventions. Read it to understand a store you are maintaining; do not combine it with the Vue 3 setup above. Pinia is the recommended starting point for a new Vue store.

Vuex is the state management pattern and library for Vue.js applications, designed to manage the state of the entire application.

Pros:

- Deep integration with Vue.
- Provides a single source of truth for the application state.
- Strong developer tooling support.

Cons:

- Can be complex for simple applications.
- Requires boilerplate code.

Core Concepts:

- **State:** The single source of truth.
- **Getters:** Computed properties for the store's state.
- **Mutations:** Synchronous functions that directly change the state.
- **Actions:** Asynchronous functions that commit mutations.
- **Modules:** Allowing state, mutations, actions, and getters to be divided into smaller, manageable pieces.

**Example:**

```javascript
// store.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++;
    },
    decrement(state) {
      state.count--;
    }
  },
  actions: {
    increment({ commit }) {
      commit('increment');
    },
    decrement({ commit }) {
      commit('decrement');
    }
  },
  getters: {
    count: state => state.count
  }
});
```

```html
<!-- App.vue -->
<template>
  <div>
    <p>Count: {{ count }}</p>
    <button @click="increment">+</button>
    <button @click="decrement">-</button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  computed: {
    ...mapGetters(['count'])
  },
  methods: {
    ...mapActions(['increment', 'decrement'])
  }
}
</script>
```

### MobX

MobX is a library for managing state that makes state management simple and scalable by transparently applying functional reactive programming (TFRP).

Pros:

- Simplicity and minimal boilerplate.
- Automatic state management with observables.
- Good performance.

Cons:

- Less predictable compared to Redux.
- Smaller community compared to Redux.

Core Concepts:

- **Observable State:** The state that MobX tracks.
- **Computed Values:** Values derived from the state.
- **Reactions:** Side effects that react to state changes.
- **Actions:** Functions that modify the state.

**Example:**

```javascript
// store.js
import { makeAutoObservable } from 'mobx';

class CounterStore {
  count = 0;

  constructor() {
    makeAutoObservable(this);
  }

  increment() {
    this.count++;
  }

  decrement() {
    this.count--;
  }
}

export const counterStore = new CounterStore();
```

```javascript
// App.js
import React from 'react';
import { observer } from 'mobx-react-lite';
import { counterStore } from './store';

const App = observer(() => {
  return (
    <div>
      <p>Count: {counterStore.count}</p>
      <button onClick={() => counterStore.increment()}>+</button>
      <button onClick={() => counterStore.decrement()}>-</button>
    </div>
  );
});

export default App;
```

### NgRx

NgRx is a reactive state management library for Angular applications, inspired by Redux.

Pros:

- Predictable state management with unidirectional data flow.
- Integrates well with Angular's ecosystem.
- Strong community support.

Cons:

- Steeper learning curve and more boilerplate.
- Verbose compared to simpler state management solutions.

Core Concepts:

- **Store:** The single source of truth for the application state.
- **Actions:** Events that describe state changes.
- **Reducers:** Pure functions that handle state transitions.
- **Selectors:** Functions to select slices of the state.
- **Effects:** Side effects that handle complex logic.

**Example:**

```typescript
// actions.ts
import { createAction } from '@ngrx/store';

export const increment = createAction('[Counter] Increment');
export const decrement = createAction('[Counter] Decrement');
```

```typescript
// reducer.ts
import { createReducer, on } from '@ngrx/store';
import { increment, decrement } from './actions';

export const initialState = 0;

const _counterReducer = createReducer(
  initialState,
  on(increment, state => state + 1),
  on(decrement, state => state - 1)
);

export function counterReducer(state, action) {
  return _counterReducer(state, action);
}
```

```typescript
// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { StoreModule } from '@ngrx/store';
import { counterReducer } from './reducer';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    StoreModule.forRoot({ count: counterReducer })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

```typescript
// app.component.ts
import { Component } from '@angular/core';
import { Store } from '@ngrx/store';
import { Observable } from 'rxjs';
import { increment, decrement } from './actions';

@Component({
  selector: 'app-root',
  template: `
    <div>
      <p>Count: {{ count$ | async }}</p>
      <button (click)="increment()">+</button>
      <button (click)="decrement()">-</button>
    </div>
  `
})
export class AppComponent {
  count$: Observable<number>;

  constructor(private store: Store<{ count: number }>) {
    this.count$ = store.select('count');
  }

  increment() {
    this.store.dispatch(increment());
  }

  decrement() {
    this.store.dispatch(decrement());
  }
}
```

### Recoil: historical example

Recoil explored atom-based state and derived selectors for React. Its [repository was archived on 1 January 2025](https://github.com/facebookexperimental/Recoil); treat the code below as historical context, not a recommendation for a new dependency. Before changing React versions in an existing Recoil application, verify compatibility and plan how its atoms, selectors, and consumers will migrate. There is no single automatic successor for every application.

Design ideas illustrated:

- Minimal boilerplate and easy to use.
- Fine-grained dependencies between atoms and selectors.
- Sharing state without threading it through each intermediate component.

Maintenance constraints:

- The upstream repository is archived and read-only.
- Limited to React.

Core Concepts:

- **Atoms:** Units of state.
- **Selectors:** Functions that compute derived state.
- **RecoilRoot:** The context provider for Recoil state.

**Example:**

```javascript
// atoms.js
import { atom } from 'recoil';

export const countState = atom({
  key: 'countState',
  default: 0
});
```

```javascript
// App.js
import React from 'react';
import { RecoilRoot, useRecoilState } from 'recoil';
import { countState } from './atoms';

const Counter = () => {
  const [count, setCount] = useRecoilState(countState);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
    </div>
  );
};

const App = () => (
  <RecoilRoot>
    <Counter />
  </RecoilRoot>
);

export default App;
```

### Best Practices

#### General Guidelines

- Use **TypeScript** with JavaScript frameworks to take advantage of strong typing, improved tooling, and better error detection, especially for large-scale applications.
- Follow the **framework’s official style guide** (like React’s or Vue’s) for consistent code practices, readability, and alignment with best practices recommended by the framework’s community.
- Be mindful of **dependency management** to avoid unnecessary packages, minimizing potential security vulnerabilities and reducing bundle sizes.
- Organize **project structure** logically by grouping components, services, and utilities in a way that reflects the framework’s conventions and makes it easy to navigate the codebase.
- Regularly refer to **framework documentation** to stay updated on features, best practices, and performance optimizations.

#### State Management

- Use **state management libraries** (like Redux for React or Pinia for Vue) for complex applications to centralize and manage state effectively, improving scalability.
- Avoid **excessive global state**; limit state management to where it is necessary, and consider using local state for component-specific data to reduce complexity.
- When possible, utilize **built-in state solutions** like React’s Context API or Vue’s reactive properties for simpler state needs, enhancing clarity and reducing dependency overhead.
- Organize **state in a modular way**, segmenting related states into slices or modules for better maintainability and separation of concerns.

#### Components and Reusability

- Create **reusable components** by following a modular design approach, making them flexible with props and events for adaptability across different parts of the application.
- Use **functional components** when possible, especially in React, as they are easier to read, test, and typically perform better with modern JavaScript frameworks.
- Break down **complex components** into smaller, single-purpose components to promote reusability, testability, and easier maintenance.
- Embrace **component lifecycle hooks** (such as `useEffect` in React or `onMounted` in Vue) to manage side effects efficiently, like API calls or subscriptions.
- Use **slots** in frameworks like Vue or **children props** in React to enhance component flexibility, allowing developers to insert content into components dynamically.

#### Performance Optimization

- Implement **code splitting** using lazy loading techniques (like React’s `React.lazy` or Vue’s `defineAsyncComponent`) to load only what’s needed, improving initial load times.
- Utilize **memoization** techniques, such as React’s `useMemo` and `useCallback`, to optimize performance by caching the results of expensive computations.
- Employ **shallow comparisons** for props in components where frequent re-renders could impact performance, using tools like `React.memo` or Vue’s `v-once` directive.
- For **large lists**, consider virtualized rendering libraries like `react-window` or Vue’s `vue-virtual-scroller`, which render only visible items for better performance.
- Reduce **unnecessary renders** by carefully managing dependencies in hooks or lifecycle methods, ensuring components re-render only when required.

#### Routing and Navigation

- Use **lazy-loaded routes** to split code by page, reducing the initial bundle size and improving load times for single-page applications.
- Organize **route files logically**, grouping routes by feature or section for better maintainability and readability.
- Implement **route guards** (like `beforeEnter` in Vue Router or checking conditions in React Router) for authentication and authorization, enhancing security and user experience.
- Leverage **dynamic routing** for applications with user-generated or variable content, making routes adaptable based on user actions or inputs.
- Handle **404 and error pages** gracefully by configuring fallback routes, ensuring users are directed to informative error pages for better UX.

#### Asynchronous Data Handling

- Manage **asynchronous code** with hooks or framework utilities, such as React’s `useEffect` or Vue’s `watch`, to handle data fetching and side effects efficiently.
- Use **data-fetching libraries** like Axios or framework-specific solutions like React Query for efficient server interactions and built-in caching, optimizing API request management.
- For more complex applications, consider **centralized data fetching** with a state management library to keep track of data loading, caching, and error states.
- Implement **caching and deduplication** for repeated requests, especially for data that changes infrequently, to reduce network overhead and enhance performance.
- Provide **loading indicators** and clear error messages for asynchronous operations, improving the user experience by keeping users informed about the application’s status.

#### Forms and Input Handling

- Use **controlled components** to manage form inputs, especially in React, allowing for real-time input validation and synchronization with component state.
- Embrace **form libraries** like Formik for React or Vuelidate for Vue to simplify form handling, validation, and error management.
- Implement **debouncing** for inputs like search bars to minimize API calls or processing on every keystroke, improving performance.
- Provide **clear and concise error messages** for form validation, ensuring users understand what’s required for successful form submission.
- Leverage **custom hooks or reusable functions** for complex forms, encapsulating repetitive form logic and enhancing code reuse across the application.

#### Security

- Use **environment variables** to manage sensitive information like API keys, keeping them out of the source code for security.
- Sanitize and validate **user inputs** to prevent common vulnerabilities like XSS (Cross-Site Scripting) and SQL injection.
- Implement **authentication and authorization** in conjunction with secure storage mechanisms (like cookies or local storage with tokens) to protect sensitive data.
- Follow **CORS (Cross-Origin Resource Sharing)** best practices, configuring the server to only allow trusted domains access to resources.
- Regularly update **dependencies** to address security patches and prevent vulnerabilities in third-party libraries.

#### Testing and Debugging

- Write **unit tests** for individual components and utilities, using testing libraries like Jest and framework-specific tools like React Testing Library or Vue Test Utils.
- Implement **integration tests** to ensure components and modules work together as expected, focusing on areas like data flow and state management.
- Use **end-to-end testing tools** like Cypress or Playwright to test complete user flows, verifying that the application behaves correctly from the user’s perspective.
- Set up **testing environments** to simulate real production conditions, allowing tests to reveal issues that may not appear in development.
- Enable **development tools** like React Developer Tools or Vue DevTools to facilitate debugging by inspecting component states, props, and lifecycle events.

#### Documentation and Code Quality

- Maintain **comprehensive documentation** for components, modules, and custom hooks or utilities, aiding future developers and simplifying onboarding.
- Use **prop types** (React PropTypes or TypeScript interfaces) to define expected data types, improving code clarity and catching potential issues early.
- Set up **code quality tools** like ESLint with framework-specific plugins to enforce coding standards and catch potential errors.
- Follow **version control best practices** with Git, using branching strategies and pull requests to facilitate code reviews and manage changes effectively.
- Document **common patterns and conventions** in a style guide for the project, ensuring consistency across components and team members.

## Links

### General Resources

* [MDN Web Docs - Client-side JavaScript frameworks](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks)
* [Wikipedia - Comparison of JavaScript-based web frameworks](https://en.wikipedia.org/wiki/Comparison_of_JavaScript-based_web_frameworks)
* [Statista - Most used frameworks among developers worldwide](https://www.statista.com/statistics/1124699/worldwide-developer-survey-most-used-frameworks-web/)

### React

* [React Documentation - Getting Started](https://reactjs.org/docs/getting-started.html)
* [React Official Tutorial](https://reactjs.org/tutorial/tutorial.html)
* [React GitHub Repository](https://github.com/facebook/react)
* [React Patterns](https://reactpatterns.com/)
* [Awesome React - Curated List of React Resources](https://github.com/enaqx/awesome-react)

### Vue.js

* [Vue.js Guide](https://vuejs.org/v2/guide/)
* [Vue.js Documentation](https://vuejs.org/v2/guide/index.html)
* [Vue.js Official Tutorial](https://vuejs.org/v2/guide/#Getting-Started)
* [Vue.js GitHub Repository](https://github.com/vuejs/vue)
* [Awesome Vue - Curated List of Vue.js Resources](https://github.com/vuejs/awesome-vue)

### Angular

* [Angular Documentation - Quickstart](https://angular.io/docs/ts/latest/quickstart)
* [Angular Official Guide](https://angular.io/guide/quickstart)
* [Angular GitHub Repository](https://github.com/angular/angular)
* [Angular Tutorial: Tour of Heroes](https://angular.io/tutorial)
* [Awesome Angular - Curated List of Angular Resources](https://github.com/gdi2290/awesome-angular)

### Redux

* [Redux Documentation - Introduction](https://redux.js.org/introduction/getting-started)
* [Redux Official Tutorial](https://redux.js.org/tutorials/index)
* [Redux GitHub Repository](https://github.com/reduxjs/redux)
* [Awesome Redux - Curated List of Redux Resources](https://github.com/xgrommx/awesome-redux)

### Vuex

* [Vuex Documentation](https://vuex.vuejs.org/)
* [Vuex Guide](https://vuex.vuejs.org/guide/)
* [Vuex GitHub Repository](https://github.com/vuejs/vuex)
* [Vuex Getting Started](https://vuex.vuejs.org/guide/)

### MobX

* [MobX Documentation](https://mobx.js.org/README.html)
* [MobX Guide](https://mobx.js.org/getting-started)
* [MobX GitHub Repository](https://github.com/mobxjs/mobx)
* [Awesome MobX - Curated List of MobX Resources](https://github.com/mobxjs/awesome-mobx)

### NgRx

* [NgRx Documentation](https://ngrx.io/docs)
* [NgRx Guide](https://ngrx.io/guide/store)
* [NgRx GitHub Repository](https://github.com/ngrx/platform)
* [NgRx Store Guide](https://ngrx.io/guide/store)

### Recoil

* [Recoil Documentation](https://recoiljs.org/docs/introduction/getting-started)
* [Recoil Guide](https://recoiljs.org/docs/introduction/installation)
* [Recoil GitHub Repository](https://github.com/facebookexperimental/Recoil)
* [Recoil Examples](https://recoiljs.org/docs/basic-tutorial/intro)
