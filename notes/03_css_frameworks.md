## CSS Frameworks and Preprocessors

CSS preprocessors and frameworks are two important tools in a web developer's toolbox that can help streamline the process of building websites. CSS preprocessors allow developers to use new functionality that is typically borrowed from another programming language, while frameworks provide pre-written app skeletons and collections of built-in functionality that allow developers to avoid having to write all of the code from scratch.

## CSS Preprocessors

CSS preprocessors are scripting languages that are used to expand standard CSS features with new functionality that is typically borrowed from another programming language. Variables, nesting, inheritance, mixins, functions, and mathematical operations are common examples. Important: they don't give anything you can't accomplish with plain old CSS, only a different way of doing things that someone thought was more efficient.

The two most common ones are:

* [SASS / SCSS](https://sass-lang.com/)
* [LESS](https://lesscss.org/)

### An outline of common features

Let's look at some of the most common CSS preprocessor features and how they compare to CSS4.

#### Variables

Variables are used to provide values names that will be used in various parts of the code. For example, if you used red as value in several properties and then decided to change it to blue, you may update the value in one place if you used a variable or try to track down all those places separately otherwise.

CSS:

```css
:root {
  --important-color: red;
}

body {
  color: var(--important-color);
}
```

SCSS:

```scss
$important-color: red;

body {
  color: $important-color;
}
```

LESS:

```less
@important-color: red;

body {
  color: @important-color;
}
```

#### Inheritance

Copies all definitions from one selector to another.

CSS:

you have to use @apply
  
  ```css
  .parent {
    color: red;
  }

  .child {
    @apply parent;
  }
  ```

SCSS:

```scss
%parent {
  color: red;
}

child {
  @extend %parent;
}
```

LESS:

```less
.parent {
  color: red;
}

child {
  .parent();
}
```

#### Nesting

This feature is not yet available in CSS. 

SASS / LESS:

```css
.parent {
  .child {
    color: red;
  }
}
```

#### Mathematical operations

Instead of providing a single constant value, you may condition it on another value and compute it in real time.

CSS:

```css
body {
  font-size: calc(100% - 10px);
}
```

SCSS / LESS:

```scss
body {
  font-size: calc(100% - 10px);
}
```

#### Functions

Functions are collections of instructions that are labeled with a name. You provide it some arguments and it will return a value that is the result of its computations.

CSS:

Among available functions are:

* `rgb()`
* `min()`
* `max()`

```css
body {
  background-color: rgb(255, 255, 255);
  background-color: min(rgb(255, 255, 255), rgb(0, 0, 0));
  background-color: max(rgb(255, 255, 255), rgb(0, 0, 0));
}
```

SCSS / LESS: 

Among available functions are:

* `lighten()`
* `darken()`
* `saturate()`

```scss
body {
  background-color: lighten(rgb(255, 255, 255), 10%);
  background-color: darken(rgb(255, 255, 255), 10%);
  background-color: saturate(rgb(255, 255, 255), 10%);
}
```

## CSS Frameworks

There are a variety of CSS frameworks available. They provide the developer with a collection of built-in functionality, allowing them to avoid having to write all of the code from scratch. 

### What are frameworks?

A software framework is a pre-written app skeleton on which you may further develop. It is a collection of files and folders to which you may modify as well as add your files and folders. A framework addresses following development issues:

* We don't want to start projects from scratch every time. A framework offers boilerplate code. 
* We want a consistent method of spreading functions across files and directories. A framework provides a structure for your project.
* We want consistency in the way our UI elements are styled. A framework provides a consistent style guide.
* When writing functions, we need rules to follow. A framework offers us with numerous examples that we may strive to emulate. 

### Why are so many frameworks developed?

There are an infinite number of methods to mix multiple styles to build UI components. Aside from obvious aspects like margin widths and colors, here are also considerations such as how many fonts to use, what different button states there are, and how intuitive forms look. The comunity behind the CSS is also huge. For these two reasons alone, there will undoubtedly be numerous attempts to develop CSS frameworks. Different people find different things useful, and different styles appeal to different people.

### Examples

Among commonly used CSS frameworks are:

- [Bootstrap](https://getbootstrap.com/)
- [Tailwind](https://tailwindcss.com/)
- [Picnic CSS](https://picnicss.com/)
- [Semantic UI](https://semantic-ui.com)
- [Foundation](https://get.foundation/sites/docs/)

## Common elements of all frameworks

Most popular frameworks adress some common issues. If you decide to not use any framework in your project you may want to think about how you want to approach those issues. 

### Viewport and resets

Viewport ensures that your site has no horizontal scroll - the full site will be visible, and users will not have to zoom on mobile to see the content. Put the following line in the head section of your HTML documment:

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

Every browser renders content a little differently (this also changes between different versions of the same browser). To unify the rendering there are two common strategies:

* <a href="https://meyerweb.com/eric/tools/css/reset/">Reset</a> which removes all built-in browser styling.
* <a href="https://necolas.github.io/normalize.css/">Normalize</a> which tries to unify the built-in browser styling.

To use Reset in your project, add the following line to the head section of your HTML document: 
```html
<link rel="stylesheet" href="http://meyerweb.com/eric/tools/css/reset/reset.css">
```

To use Normalize in your project, add the following line to the head section of your HTML document: 

```html
<link rel="stylesheet" href="https://necolas.github.io/normalize.css/7.0.0/normalize.css">
```

Additionally you may want to reset the border box:

```css
html {
	box-sizing: border-box;
}

*,
*:before,
*:after {
	box-sizing: inherit;
}
```

### Layout

The most common method to layout a website is to split the content into columns (usually two or three).
Then we have a lot of options.
Depending on the screen size, all or some columns may shrink.
Columns can be transformed into rows if they reach a certain minimum width.

```css
.column {
	float: left;
	width: 33.33%;
}

.row:after {
	content: "";
	display: table;
	clear: both;
}

@media screen and (max-width: 600px) {
	.column {
		width: 100%;
	}
}
```

Background colors and styles, should extend the width of the full viewport.
To improve readability, content should normally be limited to a specific width. 

```css
.container {
	margin: 0 auto;
	padding: 0 8px;
	max-width: 800px;
}
```

### Breakpoints

Breakpoints are defined using media queries.
A breakpoint specifies the pixel width at which the content will collapse, for as when a navigation bar transitions from horizontal to vertical display or a grid breaks into specified parts.


The mobile first technique is one of the most common ways to define breakpoints.
In that approach, we first specify how our website will look on small mobile screens, then we specify breakpoints and their behavior on larger screens.
The general CSS template looks like this: 

```css
/* Styles for mobile devices */

@media screen and (min-width: 800px) {
	/* Styles for laptops and PCs */
}
```

### Navigation

One of the most crucial aspects of the website is navigation. Users will not explore your site if it is not intuitive to them. Consider the following:

* Is it better to show navigation horizontally or vertically?
* Should you go with the hamburger menu?
* How do I show submenu items? 

## Bootstrap

CSS framework for creating websites - we don't have to write (much) CSS

### Including Bootstrap in the project

In the <code>head</code> section of the HTML file, add the following code:

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
```

Now Boostrap is already working in your project.

* Some elements will have Boostrap style applied on them without any additional work. Those include <code>body</code>, <code>h1</code> and <code>button</code>.
* To apply other styles, you will ne to set the appropriate <code>class</code> attribute in the HTML code.

### Container

Container is the basic building block for bootstrap. It is top-level division of a document, you will usually set container classes in <code>div</code> tags.
  
```html
<div class="container">
    <h1>Hello World</h1>
</div>
```

### Column layout 

Columns are the most common way to layout content in Bootstrap.

```html
<div class="container">
    <div class="row">
        <div class="col-md-4">
            <h1>Hello World</h1>
        </div>
        <div class="col-md-4">
            <h1>Hello World</h1>
        </div>
        <div class="col-md-4">
            <h1>Hello World</h1>
        </div>
    </div>
</div>
```

### Forms

Forms are the most common way to interact with a user.

```html
<div class="container">
    <form>
        <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
        </div>
        <div class="form-group">
            <label for="exampleInputPassword1">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
```

## Links

* https://bootstrap-cheatsheet.themeselection.com/
* https://stackoverflow.com/questions/6887336/what-is-the-difference-between-normalize-css-and-reset-css
