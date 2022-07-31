## Table of Contents
<!--ts-->

  - [Intro](#Intro)
  - [What-should-a-CSS-developer-know?](#What-should-a-CSS-developer-know?)
  - [Three-ways-to-add-CSS-to-HTML](#Three-ways-to-add-CSS-to-HTML)
  - [Selectors](#Selectors)
    - [Selectors-and-properites](#Selectors-and-properites)
    - [Selector-Types](#Selector-Types)
    - [Inheritance-and-specificity](#Inheritance-and-specificity)
    - [Pseudo-selectors](#Pseudo-selectors)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
    - [Pseudo-element](#Pseudo-element)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
  - [Box-Model](#Box-Model)
    - [Example](#Example)
    - [Short-summary](#Short-summary)
      - [Margin](#Margin)
      - [Padding](#Padding)
      - [Dimension](#Dimension)
      - [Border-and-Outline](#Border-and-Outline)
    - [Aditional-explanations](#Aditional-explanations)
  - [Flexbox](#Flexbox)
    - [Example](#Example)
    - [Short-summary](#Short-summary)
      - [Flex-containers](#Flex-containers)
      - [Ordering-and-orientation](#Ordering-and-orientation)
      - [Alignment](#Alignment)
      - [Flexibility](#Flexibility)
    - [Aditional-explanations](#Aditional-explanations)
  - [Elements](#Elements)
    - [Lists-and-markers](#Lists-and-markers)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
    - [Table](#Table)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
    - [Text](#Text)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
  - [Style](#Style)
    - [Font](#Font)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
    - [Colors](#Colors)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
    - [Background](#Background)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
    - [Positioning](#Positioning)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
  - [Animations-and-other-dynamic-effects](#Animations-and-other-dynamic-effects)
    - [Animation](#Animation)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
    - [2D/3D-Transform](#2D/3D-Transform)
      - [Short-summary](#Short-summary)
    - [Transition](#Transition)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
  - [Responsive-design](#Responsive-design)
    - [Media-queries](#Media-queries)
      - [Example](#Example)
      - [Short-summary](#Short-summary)
      - [Aditional-explanations](#Aditional-explanations)
  - [Units](#Units)
    - [Absolute-Measurement](#Absolute-Measurement)
    - [Relative-Measurement](#Relative-Measurement)
  - [Best-practices](#Best-practices)
  - [Links](#Links)

<!--te-->

## Intro

* Cascading Style Stylesheet
* The "adjectives" of the web
* Takes the boring, ugly HTML and makes it looks like we want.

Stylesheets allow us to include predefined styles and reuse them across HTML documents
they may be included from predefined libraries (e.g. _Bootstrap_) or created manually

Colors, positions, sizes and animations.

## What should a CSS developer know?

* How to change colors, borders, font types and create animations
* How to position elements on the page and make them repsonsive
* In what scenerio different selectors should be used
* How to use MDN as a refrence
* Recreate a given component using CSS

## Three ways to add CSS to HTML


1. Directly in the element tag, inline styles:

	```html
	<element style="property: value;">
	```

1. In the <code>&lt;style&gt;</code> element:

	```html
	<head>
	    <style>
		selectors { property: value; }
	    </style>
	</head>
	```

1. In a dedicated file, such as style.css, and then refer to that file using the <code>&lt;link&gt;</code> element: 

	```html	
	<head>
	     <link rel="stylesheet" href="style.css" />
	</head>
	```
	
## Selectors

Probably the most crucial aspect of CSS to comprehend. Everything else is built around that concept.

### Selectors and properites

```css
selector {
     property_a: some_value;
     property_b: other_value;
}
```

* Selectors are the elements on which the style should be applied.
* The properties are the actual styles and values that should be applied to the elements that have been selected.

### Selector Types

Selectors are used to determine which HTML elements should be styled.

1. Universal
	Applies the style to all the elements.

	```css
	* {
	     font: 10px Arial;
	}
	```

1. Element
	The style is applied to all elements of the provided type. 

	```css
	 h1 {
	     color: green;
	}
	```

1. ID
	The style is applied to all elements with the supplied id.
	
	```css
	#header_1 {
	     color: red;
	}
	 #header_2 {
	     color: blue;
	}
	```

1. Class
	The style is applied to all elements belonging to the given class.
	
	```css
	 .some_class {
	     color: green;
	}
	```

1. Child
	The style is applied to all children of the given element. 
	
	```css
	 #gallery>p {
	     font-weight: bold;
	}
	```	
	
1. Descendant
	The style is applied to all descendants of the given element. 

	```css
	 #gallery p {
	     color: white;
	}
	```
 
### Inheritance and specificity

A given element might be matched several times by distinct selectors. The question therefore is, which style should take precedence? The specificity rules rigorously specify this: 

	ids > classes, attributes, pseudo-classes > elements, pseudo-elements

Links:

* https://specificity.keegan.st/

### Pseudo-selectors

Pseudo-selectors are used to select elements based on their state as opposed to their type.

#### Example

Let's take a look at a general example:

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

In the above example, the <code>#gallery</code> element is matched by the universal selector, and the <code>p</code> element is matched by the <code>child</code> selector. The pseudo-selector <code>:hover</code> changes the color of the <code>a</code> element when it is hovered over.

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

Let's take a look at a general example:

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

In the above example, the <code>#gallery</code> element is matched by the universal selector, and the <code>p</code> element is matched by the <code>child</code> selector. The pseudo-element <code>:first-letter</code> changes the color of the first letter of the <code>p</code> element. The following text is displayed when the <code>a</code> element is hovered over: <code>Example of a pseudo-element</code>.

#### Short summary

* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/::before">::before</a></code> an element that is before another in the document
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/::after">::after</a></code> an element that is after another in the document
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/::first-letter">::first-letter</a></code> an element that is the first letter of a text node
* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/::first-line">::first-line</a></code> an element that is the first line (of text) of a text node

#### Aditional explanations

* The ::before and ::after pseudo-elements in CSS allows you to insert content onto a page without it needing to be in the HTML. While the end result is not actually in the DOM, it appears on the page as if it is, and would essentially be like this:

## Box Model

Box model is one of a couple layout models used in CSS. It is a way to describe the size and position of an element.

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

The above example defines a box with a content area of 100x100px, a padding of 10px, a margin of 10px, and a black border with a width of 1px.

### Short summary

#### Margin

Margin is the space between the border and the content.

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top">margin-top</a></code>: the space between the top border and the content
	- auto | length 
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right">margin-right</a></code>: the space between the right border and the content
	- auto | length 
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom">margin-bottom</a></code>: the space between the bottom border and the content
	- auto | length 
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left">margin-left</a></code>: the space between the left border and the content
	- auto | length 

#### Padding

Padding is the space between the content and the border.

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top">padding-top</a></code>: the space between the content and the top border
	- auto | length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-right">padding-right</a></code>: the space between the content and the right border
	- auto | length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-bottom">padding-bottom</a></code>: the space between the content and the bottom border
	- auto | length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-left">padding-left</a></code>: the space between the content and the left border
	- auto | length

#### Dimension

Dimension is used to precisely define the size of an element.

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

Each element has a border around it. 

There are number of properties that can be used to define the border:

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
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/outline-width">outline-width</a></code>: the width of the outline
	- auto | length
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/outline-style">outline-style</a></code>: the style of the outline
	- none | hidden | dotted | dashed | solid | double | groove | ridge | inset | outset
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/outline-color">outline-color</a></code>: the color of the outline
	- color

### Aditional explanations

* Setting the dimensions of an element might be difficult since it will look odd if it is too big or too small. Values like <code>max-content</code>, <code>min-content</code>, and <code>fit-content</code> might come in handy. The value <code>min-content</code> makes the element as small as possible, whereas the value <code>max-content</code> makes the element as large as possible. The crucial point to remember is that once an element has been initialized with one of these values, its dimensions will not change even if the window is resized. The <code>fit-content</code> will adapt to window resizing and use the available space, but never less than <code>min-content</code> and never more than <code>max-content</code>. 

## Flexbox

Since flexbox is a whole module and not a single property, it involves a lot of things including its whole set of properties. Some of them are meant to be set on the container (parent element, known as “flex container”) whereas the others are meant to be set on the children (said “flex items”).

Flexbox by defualt will shrink thigns down to make them fit on the screen.

When flex-direction is set to <code>row</code>, the flex items will be laid out horizontally:

		<---------------------- axis ---------------------->
		##########    ##########    ##########    ##########
		# Elem 1 #    # Elem 2 #    # Elem 3 #    # Elem 4 #
		##########    ##########    ##########    ##########


When flex-direction is set to <code>column</code>, the flex items will be laid out vertically:

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

The cross axis runs perpendicular to the main axis, therefore if your flex-direction (main axis) is set to row or row-reverse the cross axis runs down the columns

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

In the above example, we have a container with a row of three boxes. The boxes are all the same size, but the container is set to flex-direction: column. This means that the boxes will be stacked vertically. The boxes are also centered in the container.

Links:

 * https://css-tricks.com/snippets/css/a-guide-to-flexbox/
 * https://yoksel.github.io/flex-cheatsheet/#section-display

### Short summary

#### Flex containers

Formally, the display property specifies the inner and outer display formats of an element. The outer type determines an element's participation in flow layout; the inner type determines child layout. When the display property is set to flex, the element turns into a flex container. 

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

* Justifying and aligning flex-items is a crucial flexbox feature that you will use frequently. To align flex-items to the main axis, use <code>justify-content</code>, and to align flex-items to the cross axis, use <code>align-items</code>.

  For justify-content we can choose one of the following values:
  
  - <code>flex-start</code> will put the flex-item to the beginning of the flex-container
  - <code>flex-end</code> moves the flex-item to the end of a flex-container 
  - <code>center</code> to center flex-items
  - <code>space-around</code> space-up space-around space-around space-around space-around space-around space
  - <code>space-between</code> makes use of the entire frame and space item between.
  - <code>space-evenly</code> equally distribute all items 

  For align-items we can choose one of the following values:

  - <code>flex-start</code> will put the flex-item to the beginning of the flex-container (refer the first image above)
  - <code>flex-end</code> moves the flex-item to the end of the flex-container.
  - <code>center</code> to center flex-items.
  - <code>baseline</code> moves flex-item to base item.

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

#### Aditional explanations

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

#### Aditional explanations

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

#### Aditional explanations

## Style

There are also generic style options that may be applied to any element, such as font, which specifies how the text should be shown, color, which specifies the text color or more broadly the foreground color, what is shown in the background, and how the element is positioned.

### Font

You can use any font family on your website, as long as its specication meets the requirements of the CSS standard.
The following website provides a list of many of the most common font families:

* https://www.cssfontstack.com/
* https://fonts.google.com/ 

To include your own fonts, use:

1. Look for a font and copy the link.
2. Paste the link into the head of your html file.
3. Use the font name in CSS. 
 
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

In the example above, the font-family is set to "Helvetica Neue", which is a font that is available on most web browsers. The font-size is set to 20px, the font is bold, and the text is italicized. The text is also underlined and the color is set to red.

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

The background color of the container is set to strong red in the example above, but it will be shown as pink since the opacity is set to 50%. The font color is set to white so that it stands out against the backgroun.

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

### Background

There could be solid color, gradient, image, or transparent background.

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

In the example above, the background color of the div is set to dark green, and the background color of the p is set to light gray.

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-color">background-color</a></code>: background color of the element
	- color
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-image">background-image</a></code>: background image of the element
	- none | [ <code>url</code> ] 
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-position">background-position</a></code>: background position of the element
	- [ <code>length</code>, <code>length</code> ] | [ <code>length</code>, <code>length</code>, <code>length</code> ] | [ <code>length</code>, <code>length</code>, <code>length</code>, <code>length</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-repeat">background-repeat</a></code>: background repeat of the element
	- repeat | repeat-x | repeat-y | no-repeat
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-attachment">background-attachment</a></code>: background attachment of the element
	- scroll | fixed | local
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-size">background-size</a></code>: background size of the element
	- [ <code>length</code>, <code>length</code> ] | auto

#### Aditional explanations

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

The parent element in the example above stands out due to its narrow rectangular border. The first child element is positioned absolutely, whereas the second is positioned relatively. The other elements have default positioning.

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

The animation changes the background color of the box from <code>#3D9970</code> to <code>#85144b</code> and back again. It repeats every 3 seconds and runs forever.

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation">animation</a></code>: animation of the element
	- none | <code>animation-name</code> [ <code>animation-duration</code> ] [ <code>animation-timing-function</code> ] [ <code>animation-delay</code> ] [ <code>animation-iteration-count</code> ] [ <code>animation-direction</code> ] [ <code>animation-fill-mode</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-name">animation-name</a></code>: animation name of the element
	- [ <code>string</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-duration">animation-duration</a></code>: animation duration of the element
	- [ <code>time</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function">animation-timing-function</a></code>: animation timing function of the element
	- [ <code>timing-function</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-delay">animation-delay</a></code>: animation delay of the element
	- [ <code>time</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-iteration-count">animation-iteration-count</a></code>: animation iteration count of the element
	- [ <code>number</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-direction">animation-direction</a></code>: animation direction of the element
	- normal | alternate
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-fill-mode">animation-fill-mode</a></code>: animation fill mode of the element
	- none | forwards | backwards | both
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-play-state">animation-play-state</a></code>: animation play state of the element
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

The box element is rotated by 45 degrees first, then translated to the right by 100 pixels. 

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transform">transform</a></code>: transform of the element
	- none | <code>matrix</code> | <code>translate</code> | <code>translateX</code> | <code>translateY</code> | <code>translateZ</code> | <code>scale</code> | <code>scaleX</code> | <code>scaleY</code> | <code>scaleZ</code> | <code>rotate</code> | <code>rotateX</code> | <code>rotateY</code> | <code>rotateZ</code> | <code>skew</code> | <code>skewX</code> | <code>skewY</code> | <code>matrix3d</code> | <code>translate3d</code> | <code>translateX3d</code> | <code>translateY3d</code> | <code>translateZ3d</code> | <code>scale3d</code> | <code>scaleX3d</code> | <code>scaleY3d</code> | <code>scaleZ3d</code> | <code>rotate3d</code> | <code>rotateX3d</code> | <code>rotateY3d</code> | <code>rotateZ3d</code> | <code>perspective</code>
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin">transform-origin</a></code>: transform origin of the element
	- none | <code>origin-x</code> <code>origin-y</code> <code>origin-z</code>
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style">transform-style</a></code>: transform style of the element
	- flat | preserve-3d
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/perspective">perspective</a></code>: perspective of the element
	- [ <code>length</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/perspective-origin">perspective-origin</a></code>: perspective origin of the element
	- [ <code>length</code> ] <code>length</code>
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility">backface-visibility</a></code>: backface visibility of the element
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

#### Short summary

1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition">transition</a></code>: transition of the element
	- none | <code>transition-property</code> [ <code>transition-duration</code> ] [ <code>transition-timing-function</code> ] [ <code>transition-delay</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property">transition-property</a></code>: transition property of the element
	- [ <code>string</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration">transition-duration</a></code>: transition duration of the element
	- [ <code>time</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function">transition-timing-function</a></code>: transition timing function of the element
	- [ <code>timing-function</code> ]
1. <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay">transition-delay</a></code>: transition delay of the element
	- [ <code>time</code> ]

## Responsive design

Responsive design is a technique that allows web pages to be designed to behave differently depending on the size of the display. It is a way to make web pages more usable on different devices such as mobile phones, tablets, and desktop computers. 

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

#### Short summary

* <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/@media">@media</a></code>: media query
	- <code>screen</code> | <code>print</code> | <code>all</code> | <code>not</code> <code>screen</code> | <code>orientation</code> <code>portrait</code> | <code>orientation</code> <code>landscape</code> | <code>min-width</code> <code>length</code> | <code>max-width</code> <code>length</code> | <code>min-height</code> <code>length</code> | <code>max-height</code> <code>length</code> | <code>min-device-pixel-ratio</code> <code>number</code> | <code>max-device-pixel-ratio</code> <code>number</code> | <code>min-resolution</code> <code>resolution</code> | <code>max-resolution</code> <code>resolution</code> | <code>scan</code> <code>progressive</code> | <code>scan</code> <code>interlace</code>

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
