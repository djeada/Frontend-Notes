# CSS Frameworks and Preprocessors

CSS preprocessors and frameworks are two important tools in a web developer's toolbox that can help streamline the process of building websites. CSS preprocessors allow developers to use new functionality that is typically borrowed from another programming language, while frameworks provide pre-written app skeletons and collections of built-in functionality that allow developers to avoid having to write all of the code from scratch.

## CSS Preprocessors

CSS preprocessors are scripting languages that extend standard CSS features with new functionality borrowed from other programming languages. Variables, nesting, inheritance, mixins, functions, and mathematical operations are common examples. While preprocessors don't introduce anything that can't be accomplished with plain CSS, they offer a more efficient way of doing things.

The two most common preprocessors are:

* [SASS / SCSS](https://sass-lang.com/)
* [LESS](https://lesscss.org/)

### An outline of common features

Let's delve into some of the most prevalent CSS preprocessor features and see how they stack up against CSS4, the latest iteration of CSS.

#### Variables

Variables facilitate the use of named values in different sections of the code. For instance, if you've utilized 'red' in various properties and later opt for 'blue', with a variable, you can alter the value in a singular location, as opposed to tracking down each instance individually.

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

Inheritance copies all definitions from one selector to another.

CSS (Using @apply):

```css
.parent {
  color: red;
}

.child {
  @apply .parent;
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

Nesting provides a more structured and readable way to write styles for nested elements. While CSS lacks a direct equivalent, the same effect can be achieved using multiple nested selectors.

SASS / LESS:

```css
.parent {
  .child {
    color: red;
  }
}
```

#### Mathematical operations

Mathematical operations enable dynamic value assignment based on another value, computed in real-time.

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

Functions are named sets of instructions that take arguments and return a computed value. They provide a way to perform complex calculations or transformations on CSS properties.

CSS:

Available functions include:

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

Available functions include:

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

#### Mixins

Mixins are reusable blocks of code that can be included in multiple CSS rules. They allow for writing DRY (Don't Repeat Yourself) code, avoiding repetition.

CSS (Using @apply, somewhat limited):

```css
@custom-media --small-viewport (max-width: 30em);

@media (--small-viewport) {
  /* Rules here */
}
```

SCSS:

```scss
@mixin small-viewport {
  @media (max-width: 30em) {
    @content;
  }
}

@include small-viewport {
  /* Rules here */
}
```

LESS:

```less
.small-viewport(@rules) {
  @media (max-width: 30em) {
    @rules();
  }
}

.small-viewport({
  /* Rules here */
});
```

#### Conditionals and Loops

Conditionals and loops are not available in standard CSS. They allow for more dynamic and programmable stylesheets in preprocessors.

SCSS (Using conditionals and loops):

```scss
@for $i from 1 through 3 {
  .item-#{$i} { width: 100px * $i; }
}

@if $theme == 'dark' {
  body { background: black; }
} @else {
  body { background: white; }
}
```

LESS (Similar capabilities):

```less
.loop(@counter) when (@counter > 0) {
  .item-@{counter} { width: 100px * @counter; }
  .loop(@counter - 1);
}
.loop(3);

@theme: dark;
.body(@theme) when (@theme = dark) {
  background: black;
},
.body(@theme) when (@theme = light) {
  background: white;
}
.body(@theme);
```

### Step-by-step guide to creating LESS projects

Creating a "Hello World" project in Less (a CSS pre-processor) and compiling it to normal CSS involves a few steps. Here's a step-by-step guide in notes form:

1. **Install Node.js and npm**
   - Ensure Node.js is installed on your computer. You can download it from [https://nodejs.org/](https://nodejs.org/).
   - npm (Node Package Manager) will be installed along with Node.js.

2. **Install Less**
   - Open a terminal or command prompt.
   - Install Less globally using npm: `npm install -g less`.

3. **Create Your Project Directory**
   - Create a new directory for your project: `mkdir hello-world-less`.
   - Navigate into the directory: `cd hello-world-less`.

4. **Create a Less File**
   - Create a new file named `style.less`.
   - Open `style.less` in a text editor.
   - Write some Less code, for example:
     ```less
     @color: green;

     body {
       color: @color;
     }
     ```

5. **Compile Less to CSS**
   - In the terminal, run the following command to compile your Less file to CSS: `lessc style.less style.css`.
   - This will create a `style.css` file with the compiled CSS.

6. **Create an HTML File**
   - Create an HTML file named `index.html`.
   - Link your compiled CSS file in the HTML:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
       <link rel="stylesheet" type="text/css" href="style.css">
     </head>
     <body>
       <h1>Hello World</h1>
     </body>
     </html>
     ```

7. **View Your Project**
   - Open `index.html` in a web browser to view your project.

8. **Deploy Your Project**
   - For deployment, upload the `index.html` and `style.css` files to your web server or hosting provider.

### Step-by-step guide to creating SCSS projects

Creating a "Hello World" project in SCSS (a CSS pre-processor) and compiling it to normal CSS involves a few steps. Here's a step-by-step guide in notes form:

1. **Install Node.js and npm**
   - Ensure Node.js is installed on your computer. You can download it from [https://nodejs.org/](https://nodejs.org/).
   - npm (Node Package Manager) will be installed along with Node.js.

2. **Install Sass**
   - Open a terminal or command prompt.
   - Install Sass globally using npm: `npm install -g sass`.

3. **Create Your Project Directory**
   - Create a new directory for your project: `mkdir hello-world-scss`.
   - Navigate into the directory: `cd hello-world-scss`.

4. **Create a SCSS File**
   - Create a new file named `style.scss`.
   - Open `style.scss` in a text editor.
   - Write some SCSS code, for example:
     ```scss
     $color: green;

     body {
       color: $color;
     }
     ```

5. **Compile SCSS to CSS**
   - In the terminal, run the following command to compile your SCSS file to CSS: `sass style.scss style.css`.
   - This will create a `style.css` file with the compiled CSS.

6. **Create an HTML File**
   - Create an HTML file named `index.html`.
   - Link your compiled CSS file in the HTML:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
       <link rel="stylesheet" type="text/css" href="style.css">
     </head>
     <body>
       <h1>Hello World</h1>
     </body>
     </html>
     ```

7. **View Your Project**
   - Open `index.html` in a web browser to view your project.

8. **Deploy Your Project**
   - For deployment, upload the `index.html` and `style.css` files to your web server or hosting provider.


## CSS Frameworks

CSS frameworks are essential tools in modern web development. They offer pre-written CSS code, helping developers to quickly build attractive and responsive websites without starting from scratch.

### What are CSS Frameworks?

A CSS framework is a library meant to simplify and standardize the process of styling web pages. It typically includes:

- **Pre-defined Stylesheets**: These stylesheets contain basic styles for common HTML elements.
- **Grid System**: Most frameworks include a grid system for creating layouts.
- **Responsive Design**: Frameworks come with built-in media queries for different device sizes, ensuring that your website looks good on any device.
- **Component Library**: Many frameworks provide pre-styled components like buttons, forms, modals, etc.

### Benefits of Using CSS Frameworks

1. **Speed of Development**: Dramatically reduces the time needed to get a project off the ground.
2. **Consistency**: Ensures a uniform look and feel across your website.
3. **Cross-browser Compatibility**: Frameworks handle most of the quirks between different browsers.
4. **Community and Support**: Popular frameworks have large communities, offering support and additional resources.

### Why the Variety of Frameworks?

Different frameworks cater to different needs:

- **Design Aesthetic**: Each framework has its unique style. Some developers prefer the minimalism of Tailwind, while others like the opinionated design of Bootstrap.
- **Flexibility vs. Structure**: Frameworks like Tailwind offer more flexibility but less built-in UI components, while others like Bootstrap provide more UI components but less customization flexibility.
- **Project Requirements**: Some projects may require specific features provided by a certain framework.

### Popular CSS Frameworks

1. **[Bootstrap](https://getbootstrap.com/)**: Known for its comprehensive component library and robust grid system.
2. **[Tailwind CSS](https://tailwindcss.com/)**: A utility-first framework that allows for more design customization.
3. **[Picnic CSS](https://picnicss.com/)**: A lightweight framework, ideal for quick, simple projects.
4. **[Semantic UI](https://semantic-ui.com)**: Offers human-friendly HTML and integrates well with React.
5. **[Foundation](https://get.foundation/sites/docs/)**: Focused on professional-grade responsiveness and accessibility.

## Common Elements of All Frameworks

When building a web project, it's important to consider certain foundational elements that are commonly addressed by popular frameworks. If you decide to forego a framework, you should have a strategy for these key aspects.

### Viewport

The viewport meta tag ensures that your site is properly scaled on different devices, especially on mobile where users should not have to zoom to view content. Include this in the `<head>` section of your HTML document:

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

### Resets

Different browsers have their own default styling, which can lead to inconsistencies in how your site is rendered. To address this, there are two common strategies:

    CSS Reset: This approach strips away all built-in browser styling, giving you a clean slate. You can use Eric Meyer's Reset CSS for this purpose. Include it in your HTML:

```html
<link rel="stylesheet" href="http://meyerweb.com/eric/tools/css/reset/reset.css">
```

Normalize.css: Rather than stripping styles, Normalize.css makes built-in browser styling consistent across different browsers. Include it in your HTML:

```html
<link rel="stylesheet" href="https://necolas.github.io/normalize.css/7.0.0/normalize.css">
```

### Box-Sizing

To ensure consistent rendering of elements' sizes, it's common to reset the box-sizing property. This makes working with padding and borders more intuitive:

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

Creating an effective layout is a critical aspect of web design. The layout should be responsive, adapting to various screen sizes and devices.

#### Column-Based Layout
A common method is to divide content into columns, typically two or three. These columns can be flexible, adjusting their size based on the screen width, and can stack vertically on smaller screens.

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

#### Content Width and Readability

While background styles may extend across the full viewport, it's often advisable to limit the width of the main content to enhance readability and focus.

```css
.container {
	margin: 0 auto;
	padding: 0 8px;
	max-width: 800px;
}
```

#### Breakpoints

Breakpoints are critical in responsive design, allowing layouts to adapt at certain screen widths. They are defined using media queries.

```css
/* Base styles (applied to all screen sizes) */
body {
    font-family: 'Arial', sans-serif;
    color: #333;
    margin: 0;
    padding: 0;
}

.container {
    width: 90%;
    margin: auto;
    overflow: hidden;
}

/* Styles for small devices (mobile phones) */
@media screen and (max-width: 600px) {
    .container {
        width: 100%;
    }
    .column {
        width: 100%;
        padding: 0;
    }
}

/* Styles for medium-sized devices (tablets) */
@media screen and (min-width: 601px) and (max-width: 1024px) {
    .column {
        width: 50%;
    }
}

/* Styles for large devices (desktops) */
@media screen and (min-width: 1025px) {
    .container {
        width: 80%;
    }
    .column {
        width: 33.33%;
    }
}
```

#### Mobile-First Approach

The mobile-first technique starts by styling for smaller screens, then scaling up for larger devices. This approach ensures that your design is fundamentally responsive.

```css
/* Styles for mobile devices */

@media screen and (min-width: 800px) {
	/* Styles for laptops and PCs */
}
```

### Navigation

Effective navigation is key to a user-friendly website. Considerations for navigation design include:

- Orientation: Determine whether horizontal or vertical navigation is more appropriate for your site layout.
- Hamburger Menu: On smaller screens, a hamburger menu can save space while still offering easy access to the full menu.
- Submenu Display: Plan how to present submenu items, especially in responsive designs. This could include dropdown menus, side menus, or accordions.

#### Accessibility and UX

When designing navigation, prioritize both accessibility and user experience. Ensure that navigation is intuitive and accessible, with clear labels and logical structure.

#### Responsive Navigation

For responsive navigation, consider how the menu will adapt across different devices. For example, a horizontal menu on desktop might become a vertical sidebar or a dropdown menu on mobile.

### Typography

Typography is a fundamental element in web design, significantly impacting usability and aesthetics. CSS frameworks typically provide a set of typography rules for consistency and readability.

#### Font Styles and Sizes
Frameworks often define a set of font styles and sizes for various elements (like headings, paragraphs, and links), ensuring a harmonious and legible text hierarchy.

#### Responsive Typography
Consideration for different screen sizes is essential. Responsive typography adjusts font sizes and line heights to improve readability on various devices.

### Colors and Theming

The choice of colors and the ability to theme are crucial in defining the look and feel of a website.

#### Color Palette
Frameworks usually offer a predefined color palette that can be used throughout the project, ensuring consistency.

#### Custom Theming
Many frameworks allow for custom theming, enabling you to define your color schemes and apply them globally.

### Utility Classes

Utility classes are a set of helper classes to quickly style elements without writing custom CSS. They cover common use cases like margins, padding, text alignment, and visibility.

#### Consistency and Speed
Utility classes provide a consistent way to apply spacing, align text, and more, significantly speeding up the development process.

#### Balancing Use
While utility classes are convenient, it's important to balance their use to avoid overly verbose HTML and maintain readability.

### Forms and Inputs

Forms are an integral part of user interaction on websites. Frameworks provide styles for form elements to ensure consistency and usability.

#### Styling Controls
Consistent styling for text inputs, buttons, checkboxes, and other form controls is provided.

#### Validation and Accessibility
Frameworks often include styles for form validation states (like error messages) and focus on accessibility features.

### Grid Systems

Grid systems are the backbone of layout design, allowing for complex, responsive layouts.

#### Flexible Layouts
Grids provide a flexible way to create layouts that adapt to screen size and orientation.

#### Consistency Across Devices
By using a grid system, you ensure that your layout is consistent across different devices and screen sizes.

## Bootstrap

* A popular, open-source front-end framework for designing websites and web applications
* Developed by Twitter in 2011 by Mark Otto and Jacob Thornton
* Utilizes HTML, CSS, and JavaScript to create responsive and mobile-first designs

### Including Bootstrap in the project

* Add the following code in the `<head>` section of the HTML file:

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
```

* Now Boostrap is already working in your project.
* Bootstrap will apply styles to some elements automatically, such as `<body>`, `<h1>`, and `<button>`
* To apply other styles, set the appropriate `class` attribute in the HTML code
	
### Containers

* Containers are the basic building blocks for Bootstrap.
* Use the `container` class in `<div>` tags:
  
```html
<div class="container">
    <h1>Hello World</h1>
</div>
```

### Column layout 

* Use the 12-column layout system for designing responsive layouts:

```html
<div class="container">
    <div class="row">
        <div class="col-md-4">
            <h1>Hello World</h1>
        </div>
        <!-- Add more columns as needed -->
    </div>
</div>
```

### Typography

* Use Bootstrap's typography classes for headings, paragraphs, lists, and more:

```html
<h1 class="display-1">Display Heading 1</h1>
<p class="lead">This is a leading paragraph.</p>
<small class="text-muted">This is a small, muted text.</small>
```

### Forms

* Create responsive and styled forms using Bootstrap's form classes:

```html
<div class="container">
    <form>
        <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
        </div>
        <!-- Add more form elements as needed -->
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
```

### Typography

* Bootstrap offers various components, such as navigation bars, cards, modals, and alerts:

```html
<!-- Example: Navigation bar -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <!-- Add more navigation elements as needed -->
</nav>
```

### Customization

*  Customize Bootstrap's built-in styles using SASS/SCSS, modify color schemes, fonts, and component styles
*  Use build tools like Webpack, Grunt, or Gulp to streamline the customization process

```html
// Example: Customizing the primary color
$theme-colors: (
  "primary": #ff6347
);

@import "bootstrap";
```

### Step-by-step guide to creating Bootstrap projects

Creating a basic "Hello World" project with Bootstrap involves the following steps. This guide assumes you are familiar with basic HTML and CSS:

1. **Set Up Your HTML File**
   - Create a new HTML file named `index.html`.
   - Open `index.html` in a text editor.

2. **Include Bootstrap**
   - Add Bootstrap's CSS and JS to your HTML file. You can use Bootstrap's CDN (Content Delivery Network) for quick setup.
   - Inside the `<head>` tag, include Bootstrap’s CSS:
     ```html
     <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ775iR6n9rC6jxo2E5h7X/0pZ72n/VAapMo" crossorigin="anonymous">
     ```
   - Before the closing `</body>` tag, include Bootstrap’s JS and its dependencies:
     ```html
     <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
     <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
     <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
     ```

3. **Create a Basic Layout**
   - Use Bootstrap’s grid system or components to create your page layout.
   - For a simple "Hello World" message, you can use a Bootstrap container:
     ```html
     <div class="container">
       <h1>Hello World</h1>
     </div>
     ```

4. **Customize with Bootstrap Classes**
   - Utilize Bootstrap's classes for typography, buttons, or other components to enhance your page.

5. **View Your Project**
   - Open `index.html` in a web browser to view your Bootstrap-styled "Hello World" project.

## Links

* https://bootstrap-cheatsheet.themeselection.com/
* https://stackoverflow.com/questions/6887336/what-is-the-difference-between-normalize-css-and-reset-css
