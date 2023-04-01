## Introduction

* Cascading Style Sheets (CSS)
* The "adjectives" of the web
* Takes the basic HTML structure and styles it according to our preferences

CSS allows us to create predefined styles and reuse them across HTML documents. These styles may be included from predefined libraries (e.g., Bootstrap) or created manually.

CSS can be used to define colors, positions, sizes, and animations.

## What should a CSS developer know?

* How to change colors, borders, font types, and create animations
* How to position elements on the page and make them responsive
* When to use different selectors
* How to use Mozilla Developer Network (MDN) as a reference
* How to recreate a given component using CSS

## Three ways to add CSS to HTML

1. Directly in the element tag, using inline styles:

	```html
	<element style="property: value;">
	```

2. In the `<style>` element:

	```html
	<head>
	    <style>
		selector { property: value; }
	    </style>
	</head>
	```

3. In a dedicated file, such as style.css, and then refer to that file using the `<link>` element:

	```html	
	<head>
	     <link rel="stylesheet" href="style.css" />
	</head>
	```
	
## Selectors

Selectors are a fundamental aspect of CSS. They determine which HTML elements should be styled.

### Selectors and Properties

```css
selector {
     property_a: some_value;
     property_b: other_value;
}
```

* Selectors identify the elements on which the style should be applied
* Properties are the actual styles and values that should be applied to the elements that have been selected

### Selector Types

Selectors are used to determine which HTML elements should be styled.

1. Universal: Applies the style to all the elements.

	```css
	* {
	     font: 10px Arial;
	}
	```

1. Element: The style is applied to all elements of the provided type.

	```css
	 h1 {
	     color: green;
	}
	```

1. ID: The style is applied to all elements with the supplied id.
	
	```css
	#header_1 {
	     color: red;
	}
	 #header_2 {
	     color: blue;
	}
	```

1. Class: The style is applied to all elements belonging to the given class.
	
	```css
	 .some_class {
	     color: green;
	}
	```

1. Child: The style is applied to all children of the given element.
	
	```css
	 #gallery>p {
	     font-weight: bold;
	}
	```	
	
1. Descendant: The style is applied to all descendants of the given element.

	```css
	 #gallery p {
	     color: white;
	}
	```
 
### Inheritance and Specificity

When an element is matched by multiple selectors, it's important to know which style takes precedence. Specificity rules help determine this:

    ids > classes, attributes, pseudo-classes > elements, pseudo-elements

Links:

* [https://specificity.keegan.st/](https://specificity.keegan.st/)

### Pseudo-selectors

Pseudo-selectors are used to select elements based on their state, rather than their type.

#### Example

Consider the following example:

```html
<div id="gallery">
    <p>
        <a href="https://www.google.com">Google</a>
    </p>
    <p>
        <a href="https://www.yahoo.com">Yahoo</a>
    </p>
</div>
```

```css
#gallery {
    color: red;
}

#gallery p {
    color: blue;
}

#gallery a:hover {
    color: green;
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185158939-c73c000c-a6b9-4514-b9bd-65bbdad56218.gif" width=400 />
</p>

In the example above, the `#gallery` element is matched by the universal selector, and the `p` element is matched by the `child` selector. The `:hover pseudo-selector` changes the color of the `a` element when it's hovered over.

#### Short summary

The following pseudo-selectors are available for use in CSS:

* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:active">:active</a></code> an active element
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:focus">:focus</a></code> currently focused element
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:hover">:hover</a></code> an element being hovered over
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:link">:link</a></code> an unvisited hypertext link
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:disabled">:disabled</a></code> a disabled element
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:enabled">:enabled</a></code> an enabled element
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:checked">:checked</a></code> a checked element
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:selection">:selection</a></code> the current selection
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:lang">:lang</a></code> allows the author to specify a 
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child">:nth-child</a></code> an element that is the nth child of its parent
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-last-child">:nth-last-child</a></code> an element that is the nth-last child of its parent
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:first-child">:first-child</a></code> an element that is the first child of its parent
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:last-child">:last-child</a></code> an element that is the last child of its parent
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:only-child">:only-child</a></code> an element that is the only child of its parent
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-sibling">:nth-sibling</a></code> an element that is the n-th sibling of its type
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-last-sibling">:nth-last-sibling</a></code> an element that is the n-th last sibling of its type
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:first-of-type">:first-of-type</a></code> an element that is the first of its type in the list of children of its parent
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:last-of-type">:last-of-type</a></code> an element that is the last of its type in the list of children of its parent
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:only-of-type">:only-of-type</a></code> an element that is the only of its type in the list of children of its parent
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:root">:root</a></code> an element that is the root element of an document
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:empty">:empty</a></code> an element that has no children (including text nodes)
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/:target">:target</a></code> an element that is the target of a hyperlink

### Pseudo-element
 
Pseudo-elements are used to select elements based on their position in the document.

#### Example

Consider the following example:

```html
<div id="gallery">
    <p>
        <a href="https://www.google.com">Google</a>
    </p>
    <p>
        <a href="https://www.yahoo.com">Yahoo</a>
    </p>
</div>
```

```css
#gallery {
    color: black;
}

#gallery p::first-letter {
    color: red;
}

#gallery a:hover::before {
    content: "Example of a pseudo-element";
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185158984-96a39866-0d08-4730-8bf4-a6ddd40e9b58.gif" width=400 />
</p>

In the example above, the `#gallery` element is matched by the universal selector, and the `p` element is matched by the child selector. The `::first-letter` pseudo-element changes the color of the first letter of the `p` element. When the `a` element is hovered over, the text "Example of a pseudo-element" is displayed.

#### Short summary

* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/::before">::before</a></code> an element that is before another in the document
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/::after">::after</a></code> an element that is after another in the document
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/::first-letter">::first-letter</a></code> an element that is the first letter of a text node
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/::first-line">::first-line</a></code> an element that is the first line (of text) of a text node

#### Aditional explanations

The `::before` and `::after` pseudo-elements in CSS allow you to insert content onto a page without it needing to be in the HTML. While the end result is not actually in the DOM, it appears on the page as if it is.

## Box Model

The box model is one of the layout models used in CSS. It describes the size and position of an element.

```
Box
.......................
.  Margin             . 
.  -----------------  .
.  | Padding       |  .
.  |  ###########  |  .
.  |  # Element #  |  .
.  |  ###########  |  .
.  |               |  .
.  -----------------  .
.                     .
.......................
```

### Example

Let's take a look at a complete example:

```html
<div id="box">
	<p>Content</p>
</div>
```

```css
#box {
	width: 100px;
	height: 100px;
	padding: 10px;
	margin: 10px;
	border: 1px solid black;
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185159594-c037c582-8262-4723-80bd-b32a2776a622.PNG" width=400 />
</p>

The above example defines a box with a content area of 100x100px, a padding of 10px, a margin of 10px, and a black border with a width of 1px.

### Short summary

#### Margin

Margin is the space outside the border of an element, separating it from other elements.

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top">margin-top</a></code>: the space between the top border of an element and its adjacent element
   - auto | length | percentage
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right">margin-right</a></code>: the space between the right border of an element and its adjacent element
   - auto | length | percentage
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom">margin-bottom</a></code>: the space between the bottom border of an element and its adjacent element
   - auto | length | percentage
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left">margin-left</a></code>: the space between the left border of an element and its adjacent element
   - auto | length | percentage

#### Padding

Padding is the space between the content of an element and its border.

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top">padding-top</a></code>: the space between the content and the top border of an element
   - length | percentage
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-right">padding-right</a></code>: the space between the content and the right border of an element
   - length | percentage
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-bottom">padding-bottom</a></code>: the space between the content and the bottom border of an element
   - length | percentage
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-left">padding-left</a></code>: the space between the content and the left border of an element
   - length | percentage

#### Dimension

Dimension properties define the size of an element.

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/width">width</a></code>: the width of an element
   - auto | length | max-content | min-content | fit-content | fill-available
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/height">height</a></code>: the height of an element
   - auto | length | max-content | min-content | fit-content | fill-available
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/min-width">min-width</a></code>: the minimum width of an element
   - auto | length | max-content | min-content | fit-content | fill-available
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/min-height">min-height</a></code>: the minimum height of an element
   - auto | length | max-content | min-content | fit-content | fill-available
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/max-width">max-width</a></code>: the maximum width of an element
   - auto | length | max-content | min-content | fit-content | fill-available
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/max-height">max-height</a></code>: the maximum height of an element
   - auto | length | max-content | min-content | fit-content | fill-available

#### Border and Outline

Each element can have a border and an outline around it.

Border properties:

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-width">border-width</a></code>: the width of the border
   - auto | length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-style">border-style</a></code>: the style of the border
   - none | hidden | dotted | dashed | solid | double | groove | ridge | inset | outset
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-color">border-color</a></code>: the color of the border
   - color
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius">border-radius</a></code>: the radius of the border
   - length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-image">border-image</a></code>: the image of the border
   - none | image

Outline properties:

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/outline-width">outline-width</a></code>: the width of the outline
   - auto | length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/outline-style">outline-style</a></code>: the style of the outline
   - none | hidden | dotted | dashed | solid | double | groove | ridge | inset | outset
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/outline-color">outline-color</a></code>: the color of the outline
   - color

### Aditional explanations

* Setting the dimensions of an element might be challenging, as it could look odd if it is too big or too small. Values like `max-content`, `min-content`, and `fit-content` might come in handy. `min-content` makes the element as small as possible, whereas `max-content` makes the element as large as possible. The important point to remember is that once an element has been initialized with one of these values, its dimensions will not change.

## Flexbox

Flexbox is a module that involves a set of properties for managing layout in a flexible and efficient manner. Some properties are meant to be set on the container (parent element, known as "flex container"), while others are meant to be set on the children ("flex items").

By default, flexbox will shrink items down to make them fit on the screen.

When `flex-direction` is set to `row`, the flex items will be laid out horizontally:

```
<---------------------- axis ---------------------->
##########    ##########    ##########    ##########
# Elem 1 #    # Elem 2 #    # Elem 3 #    # Elem 4 #
##########    ##########    ##########    ##########
```

When `flex-direction` is set to `column`, the flex items will be laid out vertically:

```
˄     ##########
|     # Elem 1 #
|     ##########
|
|     ##########
a     # Elem 2 #
x     ##########
i
s     ##########
|     # Elem 3 #
|     ##########
|
|     ##########
|     # Elem 4 #
|     ##########
˅
```

The cross axis runs perpendicular to the main axis. If your `flex-direction` (main axis) is set to `row` or `row-reverse`, the cross axis runs down the columns.

### Example

Let's take a look at a complete example:

```html
<div class="container">
	<div class="row">
		<div class="col-md-4">
			<div class="box">
				<h1>Box 1</h1>
			</div>
		</div>
		<div class="col-md-4">
			<div class="box">
				<h1>Box 2</h1>
			</div>
		</div>
		<div class="col-md-4">
			<div class="box">
				<h1>Box 3</h1>
			</div>
		</div>
	</div>
</div>
```

 ```css
.container {
   display: flex;
   justify-content: center;
   align-items: center;
}

.row {
   display: flex;
   flex-direction: row;
   justify-content: center;
   align-items: center;
}

.col-md-4 {
   margin: 10px;
}

.box {
   background-color: #f5f5f5;
   padding: 20px;
   border-radius: 5px;
   box-shadow: 0px 0px 5px #ccc;
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185159826-14526321-a3c0-4726-bd15-711cd7221cf6.PNG" width=400 />
</p>

In the above example, we have a container with a row of three boxes. The boxes are all the same size, but the container is set to `flex-direction: row`. This means that the boxes will be laid out horizontally. The boxes are also centered in the container.

Links:

 * https://css-tricks.com/snippets/css/a-guide-to-flexbox/
 * https://yoksel.github.io/flex-cheatsheet/#section-display

### Short summary

#### Flex containers

The `display` property specifies the inner and outer display formats of an element. When the `display` property is set to `flex`, the element turns into a flex container. 

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display">display</a></code>: display type of the element
   - flex | inline-flex

#### Ordering and orientation

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/order">order</a></code>: order of the element
   - number
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction">flex-direction</a></code>: direction of the element
   - row | row-reverse | column | column-reverse
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap">flex-wrap</a></code>: wrap the element
   - nowrap | wrap | wrap-reverse
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow">flex-flow</a></code>: flow of the element
   - row | row-reverse | column | column-reverse

#### Alignment

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/align-items">align-items</a></code>: align the items
   - flex-start | flex-end | center | baseline | stretch
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/align-content">align-content</a></code>: align the content
   - flex-start | flex-end | center | space-between | space-around
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content">justify-content</a></code>: justify the content
   - flex-start | flex-end | center | space-between | space-around

#### Flexibility

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex">flex</a></code>: flex of the element
   - number
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow">flex-grow</a></code>: grow of the element
   - number
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink">flex-shrink</a></code>: shrink of the element
   - number
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis">flex-basis</a></code>: basis of the element
   - auto | number

### Aditional explanations

* Justifying and aligning flex items is a crucial flexbox feature that you will use frequently. To align flex items along the main axis, use `justify-content`, and to align flex items along the cross axis, use `align-items`.

For `justify-content`, we can choose one of the following values:
  
  - <code>flex-start</code> will put the flex-item to the beginning of the flex-container
  - <code>flex-end</code> moves the flex-item to the end of a flex-container 
  - <code>center</code> to center flex-items
  - <code>space-around</code> space-up space-around space-around space-around space-around space-around space
  - <code>space-between</code> makes use of the entire frame and space item between.
  - <code>space-evenly</code> equally distribute all items 

For `align-items`, we can choose one of the following values:

  - <code>flex-start</code> will put the flex-item to the beginning of the flex-container (refer the first image above)
  - <code>flex-end</code> moves the flex-item to the end of the flex-container.
  - <code>center</code> to center flex-items.
  - <code>baseline</code> moves flex-item to base item.

* Flexbox allows you to control the size of the flex items by using the `flex-grow`, `flex-shrink`, and `flex-basis` properties.

  - `flex-grow`: Determines the ability of a flex item to grow when there is extra space in the container. It accepts a unitless value that serves as a proportion. For example, if all flex items have a `flex-grow` value of 1, they will grow equally and fill the available space. If one item has a `flex-grow` value of 2, it will take up twice as much space as the other items.

  - `flex-shrink`: Defines the ability of a flex item to shrink when there isn't enough space in the container. Like `flex-grow`, it takes a unitless value that serves as a proportion. If all flex items have a `flex-shrink` value of 1, they will shrink equally when the container is too small. If one item has a `flex-shrink` value of 2, it will shrink twice as much as the other items.

  - `flex-basis`: Specifies the initial size of a flex item before any extra space is distributed according to the `flex-grow` and `flex-shrink` values. It accepts `auto`, which sizes the item based on its content, or a length value (e.g., `50%`, `100px`, etc.).

  The `flex` property is a shorthand for setting the `flex-grow`, `flex-shrink`, and `flex-basis` properties. Its syntax is `flex: <flex-grow> <flex-shrink> <flex-basis>`. For example, `flex: 1 1 auto` would set `flex-grow` to 1, `flex-shrink` to 1, and `flex-basis` to auto.

* When working with flex items, you can also control their alignment along the cross axis individually using the `align-self` property. The `align-self` property accepts the same values as `align-items` (`flex-start`, `flex-end`, `center`, `baseline`, and `stretch`) and allows you to override the `align-items` value for a specific flex item.

  For example, if you have a flex container with `align-items: center`, but you want one specific flex item to be aligned to the start of the cross axis, you can apply `align-self: flex-start` to that item.

* When you need to control the order of flex items within a flex container, you can use the `order` property. By default, all flex items have an `order` value of 0, and they are laid out in the order they appear in the source code. You can set the `order` property to a positive or negative integer value to change the order in which the items are displayed. Items with a lower `order` value will be displayed before items with a higher value.

  For example, if you have a flex container with three items and you want the third item to appear first, you can apply `order: -1` to that item. The other two items will maintain their default `order` value of 0 and will be displayed after the third item.

## Elements

There are a number of elements that have special options for styling in CSS.

### Lists and markers

Lists and markers are one type of elements with special options for styling in CSS.

#### Example

```html
<ul>
	<li>Item 1</li>
	<li>Item 2</li>
	<li>Item 3</li>
</ul>
```

```css
ul {
   list-style-type: none;
}


li {
   display: inline-block;
   margin: 10px;
   padding: 10px;
   border: 1px solid #ccc;
   border-radius: 5px;
   box-shadow: 0px 0px 5px #ccc;
}
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185166139-e4cd392e-dbaa-4d9e-b5ab-f24971dbf2e5.PNG" width=400 />
</p>

In the above example, we have a list with three items. The list is set to display: inline-block. This means that the items will be displayed horizontally as opposed to the default vertical. The items are distinguished by a border and a box-shadow.

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style">list-style</a></code>: list style of the element
   - none | \[ list-style-type, list-style-position, list-style-image ]

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type">list-style-type</a></code>: type of the list
   - disc | circle | square | decimal | decimal-leading-zero | lower-roman | upper-roman | lower-greek | lower-latin | upper-latin | armenian | georgian | none
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-position">list-style-position</a></code>: position of the list
   - inside | outside
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-image">list-style-image</a></code>: image of the list
   - url
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/marker-offset">marker-offset</a></code>: offset of the marker
   - auto | length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/marker-start">marker-start</a></code>: start marker of the element
   - url

### Table

Another type of elements with special options for styling in CSS is the table.

#### Example

```html
<table>
	<tr>
		<th>Header 1</th>
		<th>Header 2</th>
		<th>Header 3</th>
	</tr>
	<tr>
		<td>Cell 1</td>
		<td>Cell 2</td>
		<td>Cell 3</td>
	</tr>
	<tr>
		<td>Cell 1</td>
		<td>Cell 2</td>
		<td>Cell 3</td>
	</tr>
</table>
```

```css
table {
   border-collapse: collapse;
   border-spacing: 0;
}

th, td {
   padding: 10px;
   border: 1px solid #ccc;
   border-radius: 5px;
   box-shadow: 0px 0px 5px #ccc;
}
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185166325-58e220dc-4d57-4292-bb30-141baa3abb7f.PNG" width=400 />
</p>

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/table-layout">table-layout</a></code>: layout of the table
   - auto | fixed

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-collapse">border-collapse</a></code>: collapse of the borders
   - collapse | separate

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-spacing">border-spacing</a></code>: spacing of the borders
   - length

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/caption-side">caption-side</a></code>: side of the caption
   - top | bottom

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/empty-cells">empty-cells</a></code>: empty cells of the table
   - show | hide

### Text

There are numerous specific style options for text.

#### Example

```html
<p>This is a paragraph.</p>
```

```css
p {
   font-family: sans-serif;
   font-size: 1.5em;
   font-weight: bold;
   color: #333;
   text-align: center;
   text-shadow: 0px 0px 5px #ccc;
}
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185166408-c90261cb-ee50-4c94-ad5c-6f5c0c59336a.PNG" width=400 />
</p>

In the above example, we have a paragraph. The text in the paragraph is set to be bold, centered and surrounded by a shadow. The font-family is selected to be sans-serif and the font-size is set to 1.5em.

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/color">color</a></code>: color of the text
   - color
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/direction">direction</a></code>: direction of the text
   - ltr | rtl
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing">letter-spacing</a></code>: spacing of the letters
   - length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/line-height">line-height</a></code>: height of the line
   - normal | number | length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-align">text-align</a></code>: alignment of the text
   - start | end | left | right | center | justify
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration">text-decoration</a></code>: decoration of the text
   - none | underline | overline | line-through | blink
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-indent">text-indent</a></code>: indent of the text
   - length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform">text-transform</a></code>: transform of the text
   - capitalize | uppercase | lowercase | none
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/vertical-align">vertical-align</a></code>: vertical alignment of the text
   - baseline | sub | super | top | text-top | middle | bottom | text-bottom | length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/white-space">white-space</a></code>: white space of the text
   - normal | pre | nowrap | pre-wrap | pre-line
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/word-spacing">word-spacing</a></code>: spacing of the words
   - length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-outline">text-outline</a></code>: outline of the text
   - none | color | width | style | [ color, width, style ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow">text-overflow</a></code>: overflow of the text
   - clip | ellipsis
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow">text-shadow</a></code>: shadow of the text
   - none | \[ color, offset-x, offset-y, blur-radius ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap">text-wrap</a></code>: wrap of the text
   - normal | none | break-word
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/word-break">word-break</a></code>: break of the words
   - normal | break-all | keep-all
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/word-wrap">word-wrap</a></code>: wrap of the words
   - normal | break-word

## Style

There are also generic style options that may be applied to any element, such as font, which specifies how the text should be displayed, color, which specifies the text color or more broadly the foreground color.

### Font

You can use any font family on your website, as long as its specification meets the requirements of the CSS standard.
The following websites provide a list of many common font families and resources to include them in your projects:

* https://www.cssfontstack.com/
* https://fonts.google.com/

To include your own fonts, use:

1. Find a font and copy the link.
2. Paste the link into the head of your HTML file.
3. Use the font name in your CSS.
 
#### Example

 ```css
p { 
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 20px;
  font-weight: bold;
  font-style: italic;
  text-decoration: underline;
  text-decoration-style: wavy;
  text-decoration-color: red;
}
```

In the example above, the font-family is set to "Helvetica Neue", which is a font that is available on most web browsers. The font-size is set to 20px, the font-weight is bold, and the font-style is italic. The text is underlined with a wavy style, and the underline color is red.

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-style">font-style</a></code>: style of the font
   - normal | italic | oblique
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight">font-weight</a></code>: weight of the font
   - normal | bold | bolder | lighter | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-size">font-size</a></code>: size of the font
   - length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-family">font-family</a></code>: family of the font
   - string
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant">font-variant</a></code>: variant of the font
   - normal | small-caps

#### Aditional explanations

Using web fonts provides more flexibility in styling your text content. Some popular web fonts providers are Google Fonts and Adobe Fonts. To use custom fonts, you'll need to include a reference to the font file (usually hosted on a CDN) and then use the font name in your CSS.

### Colors

The color of a specific element can be specified or set to inherit from the parent element. The same is true for opacity, which is the degree of transparency.

#### Example

 ```html
<div id="container">
  <p>This is a paragraph.</p>
  <p>This is another paragraph.</p>
</div>
```

```css
#container {
  background-color: rgb(0, 25, 21);
  opacity: 0.5;
}

#container p {
  color: rgb(233, 218, 218);
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185167161-7838ed90-f2fb-4f0b-8d89-91cf81ee417a.PNG" width=400 />
</p>

The background color of the container is set to a dark greenish color in the example above, but it will appear lighter since the opacity is set to 50%. The font color is set to a light grayish color to provide contrast against the background.

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/color">color</a></code>: color of the element
   - color
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/opacity">opacity</a></code>: opacity of the element
   - number

The color value can be specified in any of the following ways:

* <code>color_name</code> e.g. *red*, *green*, *blue*
* <code>rgb(x, y, z)</code> e.g. *rgb(255, 0, 0)*
* <code>rgb(x%, y%, z%)</code> e.g. *rgb(100%, 0%, 0%)* 
* <code>rgb(x, y, z, alpha)</code> e.g. *rgb(255, 0, 0, 0.5)* 
* <code>#rrggbb</code> e.g. *#ff0000*	

#### Aditional explanations

Colors in CSS can be specified using different methods, such as color names, HEX values, RGB, RGBA, HSL, and HSLA. Each method has its own advantages and use cases. For example, using RGBA or HSLA allows you to specify an alpha channel (transparency) along with the color, while HEX values and color names don't support transparency.

### Background

The background of an element can be a solid color, gradient, image, or transparent.

#### Example

Let's take a look at the following example:

```html
<div>
  <p>This is a paragraph.</p>
  <p>This is another paragraph.</p>
</div>
```

```css
div {
  background-color: #006400;
}

p {
  background-color: #f0f0f0;
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185167742-73bbbf0f-cfb9-4685-846a-ffc9e6e96dbc.PNG" width=400 />
</p>

In the example above, the background color of the div is set to dark green, and the background color of the paragraphs is set to light gray.

#### Short summary

1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-color">background-color</a>: background color of the element
   - color
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-image">background-image</a>: background image of the element
   - none | url 
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-position">background-position</a>: background position of the element
   - length, length | length, length, length, length 
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-repeat">background-repeat</a>: background repeat of the element
   - repeat | repeat-x | repeat-y | no-repeat
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-attachment">background-attachment</a>: background attachment of the element
   - scroll | fixed | local
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-size">background-size</a>: background size of the element
   - length, length | auto

#### Aditional explanations

In addition to solid colors and images, you can also use gradients to create smooth transitions between multiple colors as the background of an element. CSS supports linear and radial gradients, and you can control the direction, color stops, and other properties to create visually appealing backgrounds. Using background images, you can create patterns, textures, or full-screen images as the background of an element. Controlling the size, position, and repeat properties allows you to customize the appearance of background images according to your design.

### Positioning

There are many different ways to position an element on the page. 

#### Example

Let's take a look at the following example:

```html
<div class="parent">
  <p>I'm the parent.</p>
  <div id="first" class="child"><p>A</p></div>
      <div id="second" class="child"><p>B</p></div>
      <div id="third" class="child"><p>C</p></div>
      <div id="fourth" class="child"><p>D</p></div>
    </div>
</div>
```

```css
.parent {
  width: 50%;
  margin: 10%;
  border: 1px solid black;
}

.child {
  width: 20%;
  height: 0;
  margin: 5%;
  padding-bottom: 20%;
  border-radius: 20%;
  text-align: center;
}

#first {
  position: absolute;
  top: 10%;
  right: 0;
  background-color: #3D9970;
}

#second {
  position: relative;
  left: 10%;
  background-color: #001f3f;
}

#third {
  background-color: #85144b;
}

#fourth {
  background-color: #DDDDDD;
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185168266-2bc43ea1-4112-43bc-806f-edfd1e6bf2c2.PNG" width=600 />
</p>

In the example above, the parent element has a narrow rectangular border. The first child element is positioned absolutely, whereas the second is positioned relatively. The other elements have default (static) positioning.

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">position</a></code>: position of the element
   - static | relative | absolute | fixed | sticky
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/float">float</a></code>: float of the element
   - none | left | right
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/clear">clear</a></code>: clear of the element
   - none | left | right | both
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display">display</a></code>: display of the element
   - inline | block | inline-block | table | table-row | table-cell | none
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/visibility">visibility</a></code>: visibility of the element
   - visible | hidden | collapse
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow">overflow</a></code>: overflow of the element
   - visible | hidden | scroll | auto

#### Aditional explanations

Let's discuss different values of <code>position</code> property:

* The position property in CSS is set to static by default for all elements. Visually, all elements follow the order of the HTML code, resulting in the normal page flow. In this mode, you cannot adjust the top, bottom, right, or left properties.
* Relative position operates similarly to static position, except that you may now change the position of an element. Modifiable properties include top, bottom, right, and left. All the changes are relative to the position of the parent element. What matters is that the parent element's other children be unaffected and act as if the moved element were still in its original place.
* Absolute-positioned elements are fully removed from the web page's normal flow. They are positioned depending on the location of their ancestor rather than their regular position in the document flow. Other children of the parent element fill the gap left by the moved element.

Now let's take a look at <code>display</code> property:

Inline elements:
* respects left and right margins and padding but not top and bottom margins and padding
* there is no way to specify width and height.
* elements can be placed on the sides (left and right). 

Block elements:
* respects all the margins and paddings.
* puts a line break after the block element.
* by default take the full available width.

Inline-block elements:
* respects top and bottom margins and padding.
* height and width can be specified.
* Elements can be placed on the sides (left and right). 

![Screenshot from 2022-10-11 20-46-35](https://user-images.githubusercontent.com/37275728/195174303-2330e847-fcb9-4c86-9b38-13130dd010e6.png)

## Animations and other dynamic effects

Besides static colors CSS3 provides a number of ways to animate colors, backgrounds, and other properties. 

### Animation

An animation lets an element gradually change from one style to another. You can change as many CSS properties you want, as many times as you want. To use CSS animation, you must first specify some keyframes for the animation. Keyframes hold what styles the element will have at certain times.

#### Example

Let's take a look at the following example:

```html
<div id="box">
  <p>I'm the box.</p>
</div>
```

```css
@keyframes change_background {
  0% {
	background-color: #3D9970;
  }
  50% {
	background-color: #85144b;
  }
  100% {
	background-color: #3D9970;
  }
}

#box {
  background-color: #3D9970;
  width: 100px;
  height: 100px;
  text-align: center;
  animation: change_background 3s infinite;
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185173016-a44f199e-1595-40f5-9f27-3a12c9302bec.gif" width=400 />
</p>

The animation changes the background color of the box from <code>#3D9970</code> to <code>#85144b</code> and back again. It repeats every 3 seconds and runs forever.

#### Short summary

1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation">animation</a>: animation of the element
   - none | animation-name | animation-duration | animation-timing-function | animation-delay | animation-iteration-count | animation-direction | animation-fill-mode 
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-name">animation-name</a>: animation name of the element
   - string
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-duration">animation-duration</a>: animation duration of the element
   - time
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function">animation-timing-function</a>: animation timing function of the element
   - timing-function
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-delay">animation-delay</a>: animation delay of the element
   -  time 
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-iteration-count">animation-iteration-count</a>: animation iteration count of the element
   -  number 
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-direction">animation-direction</a>: animation direction of the element
   - normal | alternate
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-fill-mode">animation-fill-mode</a>: animation fill mode of the element
   - none | forwards | backwards | both
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-play-state">animation-play-state</a>: animation play state of the element
   - running | paused

#### Aditional explanations

### 2D/3D Transform

Transformations are used to change the position, size, and orientation of an element. CSS provides a number of ways to use transformations.

#### Example

```html
<div id="box">
  <p>I'm the box.</p>
</div>
```

```css
#box {
  background-color: #3D9970;
  width: 100px;
  height: 100px;
  text-align: center;
  transform: rotate(45deg) translate(100px, 0);
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185172969-8d99490a-e757-416d-8f3e-254594462cdd.PNG" width=400 />
</p>

The box element is rotated by 45 degrees first, then translated to the right by 100 pixels. 

#### Short summary

1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transform">transform</a>: transform of the element
   - none | matrix | translate | translateX | translateY | translateZ | scale | scaleX | scaleY | scaleZ | rotate | rotateX | rotateY | rotateZ | skew | skewX | skewY | matrix3d | translate3d | translateX3d | translateY3d | translateZ3d | scale3d | scaleX3d | scaleY3d | scaleZ3d | rotate3d | rotateX3d | rotateY3d | rotateZ3d | perspective
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin">transform-origin</a>: transform origin of the element
   - none | origin-x origin-y origin-z
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style">transform-style</a>: transform style of the element
   - flat | preserve-3d
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/perspective">perspective</a>: perspective of the element
   - length
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/perspective-origin">perspective-origin</a>: perspective origin of the element
   - length
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility">backface-visibility</a>: backface visibility of the element
   - visible | hidden

### Transition

Transitions are used to change the style of an element over a period of time.

#### Example

```html
<div id="box">
  <p>I'm the box.</p>
</div>
```

```css
#box {
  background-color: #3D9970;
  width: 100px;
  height: 100px;
  text-align: center;
  transition: width 5s, height 5s, background-color 10s;
}

#box:hover {
  width: 200px;
  height: 200px;
  background-color: #FF4136;
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185173067-7bbce7ec-c113-4649-bd22-cd6d5d5e37b2.gif" width=400 />
</p>

#### Short summary

1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition">transition</a>: transition of the element
   - none | transition-property | transition-duration |  transition-timing-function | transition-delay 
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property">transition-property</a>: transition property of the element
   -  string 
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration">transition-duration</a>: transition duration of the element
   -  time 
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function">transition-timing-function</a>: transition timing function of the element
   -  timing-function 
1. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay">transition-delay</a>: transition delay of the element
   -  time 

## Responsive design

Responsive design is a technique that allows websites to be designed to behave differently depending on the size of the display. It is a way to make websites more usable on different devices such as mobile phones, tablets, and desktop computers. The goal is to provide a solid user experience no matter the device.

### Responsive grid vs fluid grid

* A conventional 12-column grid system with pixels for scaling is used in responsive grid.
* Fluig grid leverages percentages, allowing components to resize to fit the available space. 

Rules of thumb for number of columns:

* 12 for desktop
* 8 for tablet
* 4 for mobile

### Mobile first

Mobile first is a design method that begins with the smallest screen (mobile devices) and then scales up to tablets, laptops, and desktop computers.
It is based on the premise that converting a design from a smaller screen to a larger screen is easier. 

### Media queries

Meda queries give the developer the possibility to query the screen size and orientation. It allows us to create different styles for different devices.

#### Example

Let's say we want to create a button that changes its color depending on the screen size.

```html
<button id="button">Click me!</button>
```

```css
#button {
  background-color: #3D9970;
  width: 100px;
  height: 100px;
  text-align: center;
}

@media screen and (max-width: 600px) {
  #button {
	background-color: #FF4136;
  }
}
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/185173675-ced1fce4-8ab2-4b11-8672-e75ec79f0663.gif" width=400 />
</p>

#### Short summary

* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/@media">@media</a></code>: media query
   - screen | print | all | not screen | orientation portrait | orientation landscape | min-width length | max-width length | min-height length | max-height length | min-device-pixel-ratio number | max-device-pixel-ratio number | min-resolution resolution | max-resolution resolution | scan progressive | scan interlace


#### Aditional explanations

* Be careful if you use a selctor in a media query and then use exact same selector somewhere in the stylesheet below the media query only the last selector will be used. It is because the browser will read the stylesheet from top to bottom and it is possible to overwrite one style with another.

## Units

CSS units are used to define the size of an element.

### Absolute Measurement

* <code>%</code>: percentage 
* <code>cm</code>: centimeter 
* <code>in</code>: inch 
* <code>mm</code>: millimeter 
* <code>pc</code>: pica (lp = 12 points) 
* <code>pt</code>: point (lpt 1/72 inch) 
* <code>px</code>: pixels 

### Relative Measurement
 
* <code>ch</code>: width of the '0' glyph found in the font for the font size used to render
* <code>em</code>: 1em = current font size of current element
* <code>ex</code>: x-height of the element's font 
* <code>gd</code>: the grid defined by 'layout-grid' 
* <code>rem</code>: the font size of the root element
* <code>vh</code>: the viewport's height 
* <code>vw</code>: the viewport's width
	
## Best practices

* Place external CSS files within the `head` tag.
* Don't leave out the last semicolon of a CSS block.
* The box model should ideally be consistent throughout the document.
* Don't break from the flow by using absolute positioning.
* Only layouts you need are Flexbox and Grid.
* Prefer classes to selectors that are tightly coupled to the DOM. 
* Reduce the usage of IDs. 
* Style declarations that can be inherited should not be duplicated. 
* Minimize the use of vendor prefixes (like `-moz-transition` and so on).
* When possible, use unitless values. If you're working with relative units, go with `rem`.
* Use the hexadecimal format for colors.

## Links

* Official Website: https://www.w3.org/Style/CSS/
* http://isobar-idev.github.io/code-standards/
* https://github.com/hail2u/html-best-practices
* http://learn.shayhowe.com/html-css/writing-your-best-code/
* https://www.webaccessibility.com/best_practices.php
* Formatter: https://www.cleancss.com/css-beautify/
