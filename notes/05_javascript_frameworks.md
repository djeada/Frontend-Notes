## Table of Contents
<!--ts-->

- [JavaScript-frameworks](#JavaScript-frameworks)
- [What-are-frameworks?](#What-are-frameworks?)
  - [Problems-addressed-by-the-frameworks](#Problems-addressed-by-the-frameworks)
  - [Disadvantages](#Disadvantages)
  - [What-kinds-of-frameworks-are-there?](#What-kinds-of-frameworks-are-there?)
  - [How-to-learn-a-framework?](#How-to-learn-a-framework?)
- [React](#React)
  - [Core-elements](#Core-elements)
    - [Component](#Component)
    - [Props](#Props)
    - [Mounting](#Mounting)
    - [State](#State)
    - [DOM-events](#DOM-events)
    - [Conditional-rendering](#Conditional-rendering)
    - [Hooks](#Hooks)
      - [useState](#useState)
      - [useEffect](#useEffect)
      - [useRef](#useRef)
      - [useReducer](#useReducer)
      - [useContext](#useContext)
      - [useMemo](#useMemo)
  - [Minimal-app](#Minimal-app)
    - [Prerequisites](#Prerequisites)
    - [Project-sructure](#Project-sructure)
    - [Transcompiler](#Transcompiler)
    - [Module-bundler](#Module-bundler)
    - [Installing-React](#Installing-React)
    - [The-actual-React-code](#The-actual-React-code)
    - [Usage](#Usage)
- [Vue](#Vue)
  - [Core-elements](#Core-elements)
  - [Minimal-app](#Minimal-app)
    - [Prerequisites](#Prerequisites)
    - [Project-sructure](#Project-sructure)
    - [Installing-Vue](#Installing-Vue)
  - [Generating-Vue-app-structure](#Generating-Vue-app-structure)
    - [Usage](#Usage)
- [Angular](#Angular)
  - [Core-elements](#Core-elements)
  - [Minimal-app](#Minimal-app)
    - [Prerequisites](#Prerequisites)
    - [Project-sructure](#Project-sructure)
    - [Installing-Angular](#Installing-Angular)
    - [The-actual-Angular-code](#The-actual-Angular-code)
    - [Usage](#Usage)
- [Sate-managment-tools](#Sate-managment-tools)
- [Links](#Links)

<!--te-->

## JavaScript frameworks

* Most Web Apps today are built using a JavaScript framework rather than written in Vanilla JavaScript.
* Almost everyone agrees that every frontend developer should be familiar with at least one JavaScript framework.
* Some take it to the extreme and start learning the frontend development with one of JavaScript frameworks. 
* I still believe that before diving into the world of JavaScript frameworks, you should first understand the fundamentals of frontend development. So if you haven't done that by now, I suggest you take a step back and learn the basics.

## What are frameworks?

A software framework is a pre-written app skeleton on which you may further develop. It is a collection of files and folders to which you may modify as well as add your files and folders. A framework addresses following development issues:

* We don't want to start projects from scratch every time. A framework offers boilerplate code. 
* We want a consistent method of spreading functions across files and directories. A framework provides a structure for your project.
* We want consistency in the way our UI elements are styled. A framework provides a consistent style guide.
* When writing functions, we need rules to follow. A framework offers us with numerous examples that we may strive to emulate. 

### Problems addressed by the frameworks

We already learned how to create a simple website using just three files: index.html, style.css and script.js. This setup works well for a simple website, but quickly becomes cumbersome when you want to add more functionality.

* Fast setup: Frameworks usually come with a set of files and folders that you can modify as needed. That boilerplate code allows you to setup a working project in a matter of minutes.
* Maintainability: Frameworks are designed to be easily maintainable. You can easily add new functionality to your project without having to rewrite the code.
* Separation of concerns: Most frameworks separate the logic and the presentation. It's easier to write the code that does a single thing well, instead of trying to do everything at once.
* Community: There hundreds of articles, blog posts, YouTube videos and tutorials on the subject. You can find everything you need to know about frameworks, ask questions and get help from the community.
* Trained workforce: Because most frameworks are open source, they are available to anyone who wants to learn how to use them. Many developers are familiar with them and can easily contribute to the project based on their experience.

### Disadvantages

As with everything in life, there are benefits and costs to using frameworks.

* Black box: When starting to learn a framework, you are presented with a black box. You have no idea what the framework is doing behind the scenes. Understanding the underlying workings of any framework takes time and effort.
* Learning curve: Frameworks are often quite complicated. It may take some time for you to feel completely comfortable with them.
* Constraints: Frameworks frequently contain restrictions on how they may be used. In contrast to using a library, you do not have complete control over the structure of your project. Depending on how you look at it, this might be good or bad. 
* Overkill: Unless your project is quite large, utilizing a framework provides little advantage. This includes some comercial products as well. Frameworks are not always the best answer.
* Ecosystem volatility: The JavaScript framework ecosystem is notorious for its volatility. There are several new frameworks and libraries being introduced to the ecosystem all the time. 

### What kinds of frameworks are there? 

There are, in reality, hundreds, if not thousands, different frameworks. Anyone, including you and me, may create their own framework. Fortunately, there are just a few that are widely popular, so it's not too bad. <a href="https://en.wikipedia.org/wiki/Comparison_of_JavaScript-based_web_frameworks
">Wikipedia</a> mentions over 20 frameworks and their comparisons, although the vast majority of those mentioned are either dead or outdated. 

Links:

* https://www.statista.com/statistics/1124699/worldwide-developer-survey-most-used-frameworks-web/

### How to learn a framework?

1. I recommend first learning the basics of Vanilla JavaScript and working on a few projects in it.
1. Then, you may try to take a crash course on the framework of your choice to obtain a rough sense of what it is and what it can be used for.
1. Then, immediately begin converting one of your previous projects to your preferred framework. 

## React

React is technically a library, not a framework. A library, as opposed to a framework, allows for more flexibility in how things are done. 

Pros:
- Currently the most popular framework in the world.
- Backed by Meta (formerly Facebook).
- The core library is relatively small.
- Huge community.

Cons:
- Small library means that there is often need to incorporate many other plugins and libraries.


### Core elements

#### Component

React elements are written using plain HTML syntax with minor changes. It is possible thanks to React's extension to JavaScript called JSX. 

Component is a JavaScript function that returns a React element and meets two requirements:

1. It must start with a capital letter.
2. It must return JSX.

An example of a component is:

```JSX
import React from 'react'
import ReactDOM from 'react-dom'

class HelloWorld extends React.Component {
  render () {
    return <div>
               <h1>Hello World</h1>
               <p>This is a paragraph</p>
          </div>
  }
}

ReactDOM.render(<HelloWorld/>, document.body)
```

#### Props

Props are the properties of a React element. They are passed to the component as an argument. Props are objects and you can access them using dot notation.

```JSX
function App() {
     return (
          <Paragraph text="This is a paragraph" />
     );
}

function Paragraph(props) {
     return <p>{props.text}</p>;
}
```

Props can also be passed by placing data between the opening and closing tags of a component. 

```JSX
function App() {
     return <Container>
          <div>
               <h1>Hello World</h1>
               <p>This is a paragraph</p>
          </div>
     </Container>;
}

function Container(props) {
     return <div>{props.children}</div>;
}
```

#### Mounting

Mounting is the process of taking a React element and putting it on the page.

1. <code>constructor(props)</code> is called before rendering.
1. <code>render()</code> when first rendered.
1. <code>componentDidMount()</code> after the first render (DOM is ready).
1. <code>componentWillUnmount()</code> when the component is removed from the DOM.
1. <code>componentDidCatch()</code> when an error is thrown.

#### State

State is the data that a component keeps track of. It is an object that is passed to the component as an argument.

```JSX
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
#### DOM events
We have access to all DOM events. Let's create an alert when the user clicks on the button.

```JSX
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

#### Conditional rendering

In React, conditional rendering is done using the <code>if</code> statement. In the example below we change the text display on the button depending on whether the button is clicked or not.

```JSX
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

#### Hooks
Props and state are passed as arguments to the component. React provides a collection of hooks for using state and props in a functional component. Hooks do not work within classes; they allow you to use React without them. React has a few built-in Hooks, such as useState. You may also define your own Hooks. 

##### useState

The <code>useState</code> hook is used to create a state variable. Let's create a state variable that increments every time the button is clicked.

```JSX
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

##### useEffect

The <code>useEffect</code> runs a function every time the component is rendered.


```JSX
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

##### useRef

The <code>useRef</code> hook is used to create a reference to a DOM element.

```JSX
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

##### useReducer

The <code>useReducer</code> hook is used to create a state variable.

```JSX
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

##### useContext
The <code>useContext</code> hook is used to access the context object.

```JSX
function App() {
     const theme = useContext(ThemeContext);
     return (
          <div>
               <h1>Hello World</h1>
               <p>This is a paragraph</p>
               <p>{theme.primary}</p>
          </div>
     );
}
```

##### useMemo
The <code>useMemo</code> hook is used to memoize expensive computations.

```JSX
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
     
### Minimal app

Let's take a look at a minimal web app that uses React.

#### Prerequisites

In order to install any dependency a package manager is needed. The most common one is NPM.

1. Download <a href="https://nodejs.org/en/download/">NodeJS</a> by selecting the right isntaller for your platform. It will include <a href="">NPM</a> package manager.
2. Verify that <code>NPM</code> was installed: <code>npm --version</code>
3. Create an empty NPM package:

          npm init
4. The last step creates a package.json file which is a build configuration file. It defines all dependencies and scripts for creating and testing the project. 

#### Project sructure

At the end of this setup, the project will have the following structure:

     |
     |-- src
          |-- App.js
     |-- dist
          |-- index.html
     |-- package.json
     |-- webpack.config.js
     |-- .babelrc

#### Transcompiler

Transcompilers are used to convert code between various programming languages or versions of the same programming language. We can use a transcompiler to transform our code to an earlier version of JavaScript that is definitely supported by all web browsers if we utilize any modern JavaScript feature or framework. 

The transcompiler used in this example is called Babel. To install it use the following commands:

     npm install --save-dev babel-loader
     npm install --save-dev @babel/preset-react
     npm install --save-dev @babel/preset-env

Create a .babelrc file to configure Babel. This file, in JSON format, describes how to transcompile JavaScript code: 

```JSON
{
     "presets": ["@babel/preset-env", "@babel/preset-react"]
}
```

#### Module bundler
Webpack combines all NPM dependencies into a single bundle.js that can run in a browser. Use the following command to install it:

     npm install --save-dev webpack

A special file named webpack.config.js is needed to configure Webpack. The following is an example of this file:

```JavaScript
const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: path.resolve(__dirname, './src/app.js'),
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

Two libraries are needed to use React: react and react-dom. Use the following command to install them:

     npm install --save react react-dom

#### The actual React code

In the src/app.js file, we will include the following React script: 

```javascript
import React from 'react';
import ReactDOM from 'react-dom';

const App = () => {
     return <h1>Hello World</h1>;
};

ReactDOM.render(<App />, document.getElementById('root'));
```

A man can't live by JavaScript alone.An HTML file is also required to render the React code. Put the index.html file in the dist folder.

```html
<!DOCTYPE html>
<html lang="en">
<head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>Document</title>
</head>
<body>
     <div id="root"></div>
     <script src="bundle.js"></script>
</body>
</html>
```

#### Usage

1. To use the app, first the server must be started. The script to perform this task is already defined in the package.json file. You only need to invoke it from the command line:

          npm start     
2. Now open amu browser and navigate to http://localhost:8000/ to see the React app in action.

## Vue

Pros:
- Easy to integrate to existing projects (can mix with plain JavaScript).
- Close to vanilla JavaScript.
- Easy to learn.

Cons:
- Not backed by any big company.

### Core elements

TODO...

### Minimal app

Let's take a look at a minimal web app that uses Vue.

#### Prerequisites

In order to install any dependency a package manager is needed. The most common one is NPM.

1. Download <a href="https://nodejs.org/en/download/">NodeJS</a> by selecting the right isntaller for your platform. It will include <a href="">NPM</a> package manager.
2. Verify that <code>NPM</code> was installed: <code>npm --version</code>
3. Create an empty NPM package:

          npm init
4. The last step creates a package.json file which is a build configuration file. It defines all dependencies and scripts for creating and testing the project. 

#### Project sructure

At the end of this setup, the project will have the following structure:

     |
     |-- public
          |-- favicon.ico
          |-- index.html
     |-- src
          |-- assets
          |-- components
          |-- App.vue
          |-- main.js
     |-- babel.config.js
     |-- jsconfig.json
     |-- package.json
     |-- vue.config.js

#### Installing Vue

In order to install Vue locally, you need to install the vue-cli tool. To do this, use the following command:

     npm install @vue/cli

Verify that the tool was installed:

     npx -p @vue/cli vue --version

### Generating Vue app structure

Vue comes with a command allowing for automatic generation of the project structure. Use the following command to generate the project structure:

     npx @vue/cli create .     

#### Usage

1. Run the following command:

          npm start     
2. visit http://localhost:8080/


## Angular

Pros:
- Backed by Google.
- Full-fledged solution that does not necessitate additional components, as React frequently does.

Cons:
- Relatively hard to learn.

### Core elements

TODO...

### Minimal app

Let's take a look at a minimal web app that uses Angular.

#### Prerequisites

In order to install any dependency we need a package manager. The most common one is NPM.

1. Download <a href="https://nodejs.org/en/download/">NodeJS</a> by selecting the right isntaller for your platform. It will include <a href="">NPM</a> package manager.
2. Verify that <code>NPM</code> was installed: <code>npm --version</code>
3. Create create an empty NPM package:

          npm init
          
4. this creates a package.json file. this will be our ONLY build configuration file. it specifies all of our dependencies, how to build, and how to test.

#### Project sructure

At the end of this setup, the project will have the following structure:

     |
     |-- dist
          |-- 3rdpartylicenses.txt
          |-- favicon.ico
          |-- index.html
          |-- main.js
          |-- polyfills.js
          |-- runtime.js
          |-- styles.css
     |-- src
          |-- app
               |-- app-routing.module.ts
               |-- app.component.html
               |-- app.component.css
               |-- app.component.spec.ts
               |-- app.component.ts
               |-- app.module.ts
          |-- assets
               |-- .gitkeep
          |-- environment
               |-- environment.prod.ts
               |-- environment.ts
          |-- favicon.ico
          |-- index.html
          |-- main.ts
          |-- polyfills.ts
          |-- styles.css
          |-- test.ts
     |-- angular.json
     |-- karma.conf.js
     |-- tsconfig.app.json
     |-- tsconfig.json
     |-- tsconfig.spec.json
     |-- package.json

#### Installing Angular

In order to install Angular locally, you need to install the angular-cli tool. To do this, use the following command:

     npm install @angular/cli

Verify that the tool was installed:

     npx -p @angular/cli ng --version

#### The actual Angular code

To generate the project structure, use the following command:

     npx -p @angular/cli ng new angular-app
     cd angular-app

#### Usage

1. Run the following command:

     npx -p @angular/cli ng serve --open
 2. visit http://localhost:4200/


## Sate managment tools

A state management tool is something that goes hand in hand with frameworks. Instead of delivering messages from the root component to all of its descendant components, it regulates who can communicate with whom. It regulates moving from a higher level to a lower level component. 

## Links

* https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks
* https://en.wikipedia.org/wiki/Comparison_of_JavaScript-based_web_frameworks
* https://www.statista.com/statistics/1124699/worldwide-developer-survey-most-used-frameworks-web/
* https://reactjs.org/docs/getting-started.html
* https://vuejs.org/v2/guide/
* https://angular.io/docs/ts/latest/quickstart
