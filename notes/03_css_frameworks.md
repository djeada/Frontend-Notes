## Table of Contents
<!--ts-->

  - [CSS-Preprocessors](#CSS-Preprocessors)
    - [An-outline-of-common-features](#An-outline-of-common-features)
      - [Variables](#Variables)
      - [Inheritance](#Inheritance)
      - [Nesting](#Nesting)
      - [Mathematical-operations](#Mathematical-operations)
      - [Functions](#Functions)
  - [CSS-Frameworks](#CSS-Frameworks)
    - [What-are-frameworks?](#What-are-frameworks?)
    - [Why-are-so-many-frameworks-developed?](#Why-are-so-many-frameworks-developed?)
    - [Examples](#Examples)
    - [Bootstrap](#Bootstrap)
      - [Including-Bootstrap-in-the-project](#Including-Bootstrap-in-the-project)
      - [Container](#Container)
    - [Column-layout](#Column-layout)
      - [Forms](#Forms)

<!--te-->

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

### Bootstrap

CSS framework for creating websites - we don't have to write (much) CSS

#### Including Bootstrap in the project

In the <code>head</code> section of the HTML file, add the following code:

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
```

Now Boostrap is already working in your project.

* Some elements will have Boostrap style applied on them without any additional work. Those include <code>body</code>, <code>h1</code> and <code>button</code>.
* To apply other styles, you will ne to set the appropriate <code>class</code> attribute in the HTML code.

#### Container

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

#### Forms

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
