## CSS

* Cascading Style Sheets (CSS)
* The "adjectives" of the web
* Takes the basic HTML structure and styles it according to our preferences

### Key Points about CSS

- CSS, which stands for **Cascading Style Sheets**, is a style sheet language used to define the visual appearance of documents, primarily written in HTML, on web pages.
- In **web development**, CSS plays a vital role by adding styling and visual appeal, complementing HTML, which provides the page structure.
- CSS enables developers to create **predefined styles**, which can ensure a consistent look and feel across a website. These styles can be custom-built or leveraged from libraries like Bootstrap, TailwindCSS, or Bulma for rapid development.
- Through CSS, developers have the power to control **visual properties** such as colors, fonts, margins, layouts, and even more advanced animations and transitions, which enhance the user experience.

### Skills Every CSS Developer Should Have

1. Proficiency in **basic styling** is fundamental, covering the adjustment of visual properties such as colors, font sizes, line spacing, and borders to enhance readability and aesthetics.
2. **Layout and positioning** expertise is essential, as developers must be skilled in tools like Flexbox and CSS Grid for building responsive and well-structured designs across various screen sizes.
3. An understanding of **CSS selectors** is necessary for efficiently targeting and styling specific HTML elements, classes, and IDs without overcomplicating the code.
4. Regular use of resources like **MDN** (Mozilla Developer Network) is valuable for staying informed on CSS standards, learning best practices, and understanding how to leverage newer features effectively.
5. Being able to **build and customize components** is crucial, as it allows developers to recreate UI elements, like buttons, cards, and modals, purely with CSS for both design precision and responsiveness.

### Integrating CSS with HTML

You can add CSS to your HTML documents in three primary ways:

1. **Inline Styles**: This method involves adding CSS directly within the HTML tags. However, it's not recommended for larger styles or for maintaining consistency across pages.
  
```html
<element style="property: value;">
```

2. **Internal (or Embedded) Styles**: You can define styles for a particular page within the `<style>` tags in the `<head>` section. This is suitable for page-specific styles.

```html
<head>
    <style>
	selector { property: value; }
    </style>
</head>
```

3. **External Styles**: This is the most commonly used method for large websites. Styles are defined in a separate `.css` file and then linked to the HTML document. This way, one stylesheet can be used across multiple pages, ensuring consistency and ease of maintenance.

```html	
<head>
     <link rel="stylesheet" href="style.css" />
</head>
```

### Understanding Selectors

CSS Selectors play a pivotal role in defining which HTML elements should receive specific styles. By combining different types of selectors and properties, web developers can create intricate designs and layouts.

#### Selectors and Properties

In CSS, a basic rule-set consists of a selector and a declaration block. The declaration block contains properties and their values.

```css
selector {
    property_1: value_1;
    property_2: value_2;
    /* ... and so on */
}
```

- CSS selectors **identify** which HTML elements are targeted by the style rules, allowing specific elements to be styled according to the defined criteria.
- Inside the declaration block, **properties** indicate what aspect of the element will be styled, while **values** specify how the styling should be applied, defining the visual characteristics of the selected elements.

#### Different Types of CSS Selectors

There's a plethora of selectors in CSS, each serving a distinct purpose. Here are some of the fundamental selectors:

1. **Universal Selector**: It targets every element on the page. Often used with caution due to its broad reach.

```css
* {
    font-family: Arial, sans-serif;
}
```

2. **Element (or Type) Selector**: Targets all instances of a specific element type.

```css
h1 {
    color: green;
}
```

3. **ID Selector**: Targets a specific element based on its id attribute. Each ID should be unique within a page.

```css
#header_1 {
    color: red;
}
#header_2 {
    color: blue;
}
```

4. **Class Selector**: Targets elements based on their class attribute. Useful for grouping elements with similar styles.

```css
.highlight {
    color: yellow;
}
```

5. **Child Selector**: Targets direct children of a specified element. It doesn't affect nested or inner elements.

```css
#gallery > p {
    font-weight: bold;
}
```

6. **Descendant Selector**: Targets all nested elements (or descendants) that match the specified selector, not just direct children.

```css
#container div {
border: 1px solid black;
}
```

Additionally, CSS offers combinations of selectors, pseudo-classes, pseudo-elements, and more, giving developers a wide array of tools for precise styling.

#### Introduction to Pseudo-selectors

Pseudo-selectors, also known as pseudo-classes, allow us to style elements based on their state or position, rather than just their type or attribute.

Consider the following HTML and CSS:

```html
<div id="gallery">
    <p><a href="https://www.google.com">Google</a></p>
    <p><a href="https://www.yahoo.com">Yahoo</a></p>
</div>

css

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

In the example above, the color of text in the #gallery is red. However, paragraphs inside it are blue. Additionally, links turn green when hovered.

#### Common Pseudo-selectors

Pseudo-selectors, often termed pseudo-classes, allow developers to target and style HTML elements based on specific conditions, states, or positions rather than solely on their tags or attributes.

Below is a list of commonly-used pseudo-selectors, each paired with a brief description and a link to its documentation on MDN for deeper insights:

| Pseudo-Class          | Description                                                                     | MDN Documentation                                                                                  |
|-----------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `:active`             | Targets elements currently being activated by the user (e.g., clicked links).   | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:active)                               |
| `:focus`              | Highlights the currently focused element, commonly used with form fields.       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus)                                |
| `:hover`              | Styles an element when a user hovers over it with their cursor.                 | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:hover)                                |
| `:link`               | Targets hyperlinks that haven't been visited by the user.                       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:link)                                 |
| `:visited`            | Selects links that have been visited by the user.                               | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:visited)                              |
| `:checked`            | Targets checked elements like radio buttons or checkboxes.                      | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:checked)                              |
| `:first-child`        | Targets the first child element inside a parent element.                        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:first-child)                          |
| `:last-child`         | Selects the last child element within a parent.                                 | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:last-child)                           |
| `:nth-child(n)`       | Styles elements based on their position within a parent element.                | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child)                            |
| `:disabled`           | Targets disabled form controls.                                                | [MDN Docs for `:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/:disabled)             |
| `:enabled`            | Targets enabled form controls.                                                 | [MDN Docs for `:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/:enabled)               |
| `:not(selector)`      | Selects elements that do not match a specified selector.                        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:not)                                  |

### Inheritance and Specificity in CSS

In the world of CSS, it's crucial to understand how rules cascade and how specificity works. Specificity determines which CSS rule is applied to an element when there are multiple conflicting rules.

#### Specificity Hierarchy

When two or more CSS rules target the same element but have conflicting styles, the specificity hierarchy determines which rule is applied:

1. **IDs**
2. **Classes, attributes, and pseudo-classes**
3. **Elements and pseudo-elements**

Visualized:

```
ids > classes, attributes, pseudo-classes > elements, pseudo-elements
```

Useful tools like [Specificity Calculator](https://specificity.keegan.st/) can help understand and calculate the specificity of your selectors.

### Pseudo-elements in CSS

Pseudo-elements are a powerful feature in CSS, allowing you to style certain parts of a document, or to virtually insert content into the document, without altering the actual HTML structure.

#### Concept

Pseudo-elements are different from pseudo-classes. While pseudo-classes select elements based on their state or position in relation to others (like `:hover` or `:nth-child`), pseudo-elements target specific parts of an element, like the first line or first letter, or they can virtually insert content before or after an element's content.

Consider this sample:

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

And the accompanying styles:

```css
#gallery {
    color: black;
}

#gallery p::first-letter {
    font-size: 20px;
    color: red;
}

#gallery a:hover::before {
    content: "→ ";
    color: green;
}
```

In this illustration, the `::first-letter` pseudo-element targets and enlarges the initial letter of each paragraph, coloring it red. The `::before` pseudo-element introduces an arrow symbol (`→`) preceding the anchor text, appearing when hovered.

#### Common Pseudo-elements

Pseudo-elements target specific parts of elements or create virtual content around them. They're instrumental in achieving certain design patterns and effects without altering the actual HTML content.

| Pseudo-Element      | Description                                                                        | MDN Documentation                                                                                   |
|---------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `::before`          | Inserts virtual content before an element's actual content. Typically used with the `content` property. | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/::before)                               |
| `::after`           | Inserts virtual content after an element's content. Often used with the `content` property. | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/::after)                                |
| `::first-letter`    | Targets the first letter of block-level elements, useful for drop cap styling.     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/::first-letter)                         |
| `::first-line`      | Applies styles to the first line of text within block-level elements.              | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/::first-line)                           |

Noteworthy Points:

- The `content` property is **crucial** for `::before` and `::after` pseudo-elements to render any visual effect. This property specifies what content, if any, these pseudo-elements should display, making it a fundamental aspect of their functionality.
- Pseudo-elements are purely **styling** tools and do not modify the DOM. They are not part of the source HTML and therefore cannot be directly accessed or manipulated through JavaScript, remaining invisible in the document's structure.
- As CSS-only constructs, pseudo-elements are **inaccessible** to JavaScript. This limitation is essential to consider when planning interactive elements, as pseudo-elements cannot directly contribute to JavaScript-driven functionality.

### Box Model

The CSS Box Model is a fundamental concept in web design that describes the rectangular boxes which are generated for elements in the document tree and laid out according to the visual formatting model. Each box has a content area and optional surrounding padding, border, and margin areas.

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

#### Margins

Margins create space around an element, separating it from other elements.

| Property         | Description                            | Values                                | MDN Documentation                                                                                  |
|------------------|----------------------------------------|---------------------------------------|----------------------------------------------------------------------------------------------------|
| `margin-top`     | Defines the space above the element.   | `auto`, `length`, `percentage`        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top)                             |
| `margin-right`   | Defines the space to the right of the element. | `auto`, `length`, `percentage`        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right)                           |
| `margin-bottom`  | Defines the space below the element.   | `auto`, `length`, `percentage`        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom)                          |
| `margin-left`    | Defines the space to the left of the element.  | `auto`, `length`, `percentage`        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left)                            |

#### Padding

Padding creates space within an element, between the content and its border.

| Property         | Description                                       | Values                     | MDN Documentation                                                                                  |
|------------------|---------------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------------|
| `padding-top`    | Defines the space between the content and the top border of the element.    | `length`, `percentage`     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top)                           |
| `padding-right`  | Defines the space between the content and the right border of the element.  | `length`, `percentage`     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-right)                         |
| `padding-bottom` | Defines the space between the content and the bottom border of the element. | `length`, `percentage`     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-bottom)                        |
| `padding-left`   | Defines the space between the content and the left border of the element.   | `length`, `percentage`     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-left)                          |


#### Border

Borders surround an element, giving it structure and sometimes helping it stand out. You can define the width, style, color, and even use images as borders.

| Property         | Description                           | Values                                                        | MDN Documentation                                                                                   |
|------------------|---------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `border-width`   | Defines the thickness of the border.  | `auto`, `length`                                              | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/border-width)                           |
| `border-style`   | Determines the pattern or design of the border. | `none`, `hidden`, `dotted`, `dashed`, `solid`, `double`, `groove`, `ridge`, `inset`, `outset` | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style)    |
| `border-color`   | Sets the color of the border.         | Color name, hex, rgba, etc.                                   | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/border-color)                           |
| `border-radius`  | Creates rounded borders.              | `length` (can set each corner individually)                   | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius)                          |
| `border-image`   | Uses an image as the border.          | `none`, image source, slice, width, outset, repeat            | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/border-image)                           |


#### Outline

Outlines are similar to borders but don't take up space. They're often used for focus styles and other UI states.

| Property          | Description                             | Values                                                        | MDN Documentation                                                                                   |
|-------------------|-----------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `outline-width`   | Defines the thickness of the outline.   | `auto`, `length`                                              | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/outline-width)                          |
| `outline-style`   | Determines the pattern or design of the outline. | `none`, `hidden`, `dotted`, `dashed`, `solid`, `double`, `groove`, `ridge`, `inset`, `outset` | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/outline-style)    |
| `outline-color`   | Sets the color of the outline.          | Color name, hex, rgba, etc.                                   | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/outline-color)                          |


#### Advanced Tips

When setting the dimensions of an element, be cautious of extremes. An element that is either too small or too large can disrupt the layout and aesthetics of a page. In these cases, special values such as `max-content`, `min-content`, and `fit-content` are valuable:

- `min-content`: Shrinks the element to its smallest size.
- `max-content`: Expands the element to its largest size based on its content.
- `fit-content`: Scales the element based on available space and its content size.

### Flexbox

Flexbox, short for "Flexible Box Layout", is a design model in CSS that allows you to design complex layout structures with a more efficient and predictable way than traditional models, especially when dealing with different screen sizes and dynamic content.

#### Flex Container vs. Flex Items

When an element is defined as a flex container (using `display: flex` or `display: inline-flex`), its children automatically become flex items. Flexbox involves two sets of properties:

1. **Container Properties**: These are set on the flex container.

| Property           | Description                                                                                              | Values                                                                            |
|--------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `display`          | Initiates the flex context, allowing use of Flexbox properties.                                          | `flex`, `inline-flex`                                                             |
| `flex-direction`   | Defines the direction of the main axis, controlling the flow of flex items.                              | `row`, `row-reverse`, `column`, `column-reverse`                                  |
| `flex-wrap`        | Determines whether flex items should wrap onto multiple lines when there isn’t enough space.             | `nowrap`, `wrap`, `wrap-reverse`                                                  |
| `justify-content`  | Aligns items along the main axis within the container.                                                   | `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly` |
| `align-items`      | Aligns items along the cross axis within the container.                                                  | `flex-start`, `flex-end`, `center`, `baseline`, `stretch`                         |
| `align-content`    | Aligns lines of flex items when there is extra space on the cross axis.                                 | `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `stretch`    |


2. **Item Properties**: These are set on the flex items.

| Property         | Description                                                                                     | Values                                                    |
|------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `flex`           | Shorthand for setting `flex-grow`, `flex-shrink`, and `flex-basis`.                             | `none`, `auto`, `<flex-grow> <flex-shrink> <flex-basis>`  |
| `align-self`     | Allows an individual flex item to override the container’s `align-items` property.              | `auto`, `flex-start`, `flex-end`, `center`, `baseline`, `stretch` |
| `order`          | Specifies the order of the flex item within the container.                                      | Integer values, e.g., `0` (default), `1`, `-1`, etc.      |
| `flex-basis`     | Sets the initial main size of a flex item before any space distribution by `flex-grow` and `flex-shrink`. | `auto`, `length`, `percentage`                            |
| `flex-grow`      | Specifies how much a flex item will grow relative to the rest of the flex items.                | Integer values, e.g., `0` (default), `1`, `2`, etc.       |
| `flex-shrink`    | Specifies how much a flex item will shrink relative to the rest of the flex items.              | Integer values, e.g., `1` (default), `0`, etc.            |

#### Understanding the Axes

Flexbox layout revolves around two axes: the main axis and the cross axis.

- The main axis in a flex container is the **primary axis** along which flex items are arranged. The direction of this axis is controlled by the `flex-direction` property, allowing items to be laid out horizontally or vertically.
- The cross axis is **perpendicular** to the main axis and defines the space across which items are aligned in the flex container. This axis adjusts based on the orientation of the main axis, facilitating flexible and responsive alignment options.

- If `flex-direction` is set to `row` or `row-reverse`, flex items are laid out **horizontally**:

```
<---------------------- axis ---------------------->
##########    ##########    ##########    ##########
# Elem 1 #    # Elem 2 #    # Elem 3 #    # Elem 4 #
##########    ##########    ##########    ##########
```

The cross axis, in this case, runs vertically.

- When `flex-direction` is `column` or `column-reverse`, flex items are arranged **vertically**:

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

The cross axis, in this setup, runs horizontally.

HTML:

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

CSS:

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

#### Flexbox Properties

Flexbox introduces a set of properties that provide a more efficient and predictable way to layout, align, and distribute space among items in a container, even when their sizes are unknown or dynamic.

##### Flex Containers

To create a flex container, use the `display` property:

| Property   | Description                                                      | Values                                   | MDN Documentation                                                                 |
|------------|------------------------------------------------------------------|------------------------------------------|------------------------------------------------------------------------------------|
| `display`  | Determines the element's inner and outer display type.           | `flex` (block-level) , `inline-flex` (inline-level) | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/display)              |


##### Ordering and Orientation

Control the order in which items appear and their directional flow:

| Property          | Description                                                                                     | Values                                                  | MDN Documentation                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `order`           | Specifies the order of the flex item relative to its siblings.                                  | `<number>` (default: `0`)                               | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/order)                                  |
| `flex-direction`  | Defines the direction of the main axis, determining the orientation of flex items.              | `row`, `row-reverse`, `column`, `column-reverse`        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction)                         |
| `flex-wrap`       | Specifies whether flex items wrap onto multiple lines or columns.                               | `nowrap`, `wrap`, `wrap-reverse`                        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap)                              |
| `flex-flow`       | Shorthand property for setting both `flex-direction` and `flex-wrap`.                           | `<flex-direction> || <flex-wrap>`                       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow)                              |

##### Alignment and Justification

Determine how items are aligned and spaced within the flex container:

| Property           | Description                                                                                          | Values                                                                          | MDN Documentation                                                                                      |
|--------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `align-items`      | Aligns flex items along the cross axis of the flex container.                                        | `flex-start`, `flex-end`, `center`, `baseline`, `stretch`                       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items)                               |
| `align-content`    | Aligns flex lines within the container when there’s extra space in the cross-axis.                   | `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `stretch`  | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/align-content)                             |
| `justify-content`  | Defines how flex items are spaced along the main axis.                                               | `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly` | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)                           |

##### Flexibility of Items

Define how flex items grow and shrink:

| Property         | Description                                                                                   | Values                                          | MDN Documentation                                                                                  |
|------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `flex`           | Shorthand to set the `flex-grow`, `flex-shrink`, and `flex-basis` properties.                 | `<flex-grow> <flex-shrink> <flex-basis>`        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex)                                  |
| `flex-grow`      | Specifies the flex item’s ability to grow relative to other items.                            | `<number>` (default: `0`)                       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow)                             |
| `flex-shrink`    | Defines the flex item’s ability to shrink relative to other items.                            | `<number>` (default: `1`)                       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink)                           |
| `flex-basis`     | Sets the default size of a flex item before space distribution among items.                   | `auto`, `<length>`, `<percentage>`          | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis)                            |

Leveraging these properties allows for sophisticated layout designs that adapt gracefully across different screen sizes and resolutions.

Noteworthy Points:

- Flexbox layouts adapt to the size of the container and the size of the content. This makes it great for creating responsive designs without depending heavily on media queries.
- Flex items will, by default, try to fit onto one line. Use the `flex-wrap` property if you want items to wrap onto multiple lines.
- Flexbox also provides tools for alignment, distribution, and spacing of items, using properties like `align-items`, `justify-content`, and `gap`.

### Special Styling Elements

Certain elements in CSS come with a unique set of styling options. One such element is the list, with its associated markers.

#### Lists & Markers

In web design, lists are ubiquitous. CSS provides granular control over the appearance and positioning of list items and their markers.

| Property             | Description                                                                   | Values                                                                                  | MDN Documentation                                                                                      |
|----------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `list-style`         | Defines an element's list style, including type, position, and image.         | `none`, `<list-style-type> <list-style-position> <list-style-image>`                    | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style)                                |
| `list-style-type`    | Specifies the type of list marker.                                            | `disc`, `circle`, `square`, `decimal`, `lower-roman`, `upper-roman`, etc.               | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type)                           |
| `list-style-position`| Determines the marker’s position relative to the list item content.           | `inside`, `outside`                                                                     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-position)                       |
| `list-style-image`   | Allows using an image as the list item marker.                                | `url("path_to_image")`                                                                  | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-image)                          |
| `marker-offset`      | *(Deprecated)* Sets the distance between the marker and the nearest border edge of the list item box. | `auto`, `<length>`                                                                      | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/marker-offset)                             |
| `marker-start`       | *(Deprecated)* Specifies a marker for the start of lines, replaced by SVG `marker` attribute. | Depends on SVG marker settings                                                          | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/marker-start)                              |

HTML:

```html
<ul>
	<li>Item 1</li>
	<li>Item 2</li>
	<li>Item 3</li>
</ul>
```

CSS: 

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

#### Table

Tables in CSS are designed to structure tabular data. They come with a rich set of properties that offer detailed styling options to enhance their appearance and usability.

| Property          | Description                                                                                   | Values                                                                                           | MDN Documentation                                                                                       |
|-------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `table-layout`    | Determines the algorithm used to layout the table cells, rows, and columns.                   | `auto`, `fixed`                                                                                  | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/table-layout)                               |
| `border-collapse` | Specifies whether cell borders are collapsed into a single border or detached.                | `collapse`, `separate`                                                                           | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/border-collapse)                            |
| `border-spacing`  | Defines spacing between the borders of adjacent cells when `border-collapse` is set to `separate`. | `<length> <length>` (e.g., `2px 4px`)                                                            | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/border-spacing)                             |
| `caption-side`    | Specifies the position of the table's caption.                                                | `top`, `bottom`                                                                                  | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/caption-side)                               |
| `empty-cells`     | Determines the visibility of borders and backgrounds of empty cells.                          | `show`, `hide`                                                                                   | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/empty-cells)                                |

HTML:

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

CSS: 

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

#### Text

Text is a fundamental aspect of web design, and CSS offers an extensive suite of properties to style text with precision. From basic color settings to intricate shadow effects, text styling can be as simple or as detailed as the design requires.

| Property           | Description                                                                  | Values                                                                                  | MDN Documentation                                                                                          |
|--------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `color`            | Specifies the color of the text.                                             | HEX, RGB, RGBA, HSL, or named colors                                                    | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/color)                                          |
| `direction`        | Sets the direction in which text is written.                                 | `ltr`, `rtl`                                                                            | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/direction)                                      |
| `letter-spacing`   | Adjusts the space between characters.                                        | Units like `px`, `em`, `rem`                                                            | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing)                                 |
| `line-height`      | Determines the height of a line box.                                         | `normal`, Number values, Units like `px`, `em`                                          | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height)                                    |
| `text-align`       | Aligns the inline content, such as text.                                     | `start`, `end`, `left`, `right`, `center`, `justify`                                    | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align)                                     |
| `text-decoration`  | Adds decorative lines to text.                                               | `none`, `underline`, `overline`, `line-through`                                         | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration)                                |
| `text-indent`      | Indents the first line of a text block.                                      | Units like `px`, `em`, `rem`                                                            | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-indent)                                    |
| `text-transform`   | Controls the capitalization of text.                                         | `capitalize`, `uppercase`, `lowercase`, `none`                                          | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)                                 |
| `vertical-align`   | Sets the vertical positioning of an element relative to its parent or line height. | `baseline`, `sub`, `super`, `top`, `text-top`, `middle`, `bottom`, `text-bottom`, Units like `px`, `em` | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/vertical-align)   |
| `white-space`      | Specifies how whitespace inside an element is handled.                       | `normal`, `pre`, `nowrap`, `pre-wrap`, `pre-line`                                       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/white-space)                                    |
| `word-spacing`     | Adjusts the space between words.                                             | Units like `px`, `em`, `rem`                                                            | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/word-spacing)                                  |
| `text-outline`     | *(Non-standard)* Defines an outline for the text.                            | `none`, `color`, `width`, `style`                                                       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-outline)                                   |
| `text-overflow`    | Specifies how overflowed content is signaled to the user.                    | `clip`, `ellipsis`                                                                      | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow)                                 |
| `text-shadow`      | Adds shadow effects to the text.                                             | `color`, `offset-x`, `offset-y`, `blur-radius`                                          | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow)                                   |
| `text-wrap`        | *(Non-standard)* Specifies line breaking rules.                              | `normal`, `none`, `break-word`                                                          | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap)                                     |
| `word-break`       | Controls how lines should break in case of long words or overflow.           | `normal`, `break-all`, `keep-all`                                                       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/word-break)                                    |
| `word-wrap`        | Specifies whether to break words when they overflow the content box.         | `normal`, `break-word`                                                                  | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/word-wrap)                                     |

HTML:

```html
<p>This is a paragraph.</p>
```

CSS:

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

### Style

CSS provides a suite of generic styling properties that can be applied universally across elements. Two commonly used properties are `font` and `color`. While `font` dictates the appearance and style of text, `color` sets the foreground color for text and other graphical elements.

#### Font

Fonts play a pivotal role in establishing the visual identity of a website. With the advent of web fonts, designers are no longer restricted to a few standard system fonts. Today, a vast collection of fonts can be easily integrated into web projects to achieve the desired typography.

There are numerous platforms that offer free and premium web fonts:

* [CSS Font Stack](https://www.cssfontstack.com/)
* [Google Fonts](https://fonts.google.com/)

Steps to Incorporate Custom Fonts:

1. Navigate to a web fonts platform and select a desired font.
2. Obtain the link or `@font-face` code snippet for the chosen font.
3. Insert the link or code snippet into the `<head>` section of your HTML file.
4. Reference the font in your CSS using the `font-family` property.
 
| Property       | Description                                | Values                                                                | MDN Documentation                                                                                          |
|----------------|--------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `font-style`   | Dictates the style of a font.              | `normal`, `italic`, `oblique`                                         | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style)                                     |
| `font-weight`  | Determines the thickness of characters.    | `normal`, `bold`, `bolder`, `lighter`, `100` - `900`                  | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)                                    |
| `font-size`    | Specifies the size of the font.            | Units like `px`, `em`, `rem`, `%`, etc.                               | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)                                      |
| `font-family`  | Defines which font should be used.         | Font names in quotes, e.g., `"Helvetica, sans-serif"`                 | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)                                    |
| `font-variant` | Controls font variants, mainly for capitalized text. | `normal`, `small-caps`                                              | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant)                                   |


Example:

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

#### Aditional explanations

Web fonts have reshaped the landscape of web typography. Platforms like Google Fonts and Adobe Fonts host a myriad of fonts, ensuring websites can have unique and tailored typography. When using custom fonts, it's vital to ensure they're web-optimized for performance and that fallback fonts are specified to cater to users with limited font access or slow internet connections.

#### Colors

In web design, colors have a profound influence on user experience and branding. CSS provides diverse methods to assign colors to HTML elements. Besides color, you can also control an element's transparency or opacity, impacting how underlying content might be visible through it.

| Property  | Description                                     | Values                                              | MDN Documentation                                                                                      |
|-----------|-------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `color`   | Specifies the foreground color of an element.   | HEX, RGB, RGBA, HSL, HSLA, color names               | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/color)                                      |
| `opacity` | Determines the transparency level of an element.| Range from `0.0` (fully transparent) to `1.0` (fully opaque) | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity)                                    |

Common Methods to Define Colors:

| Color Format | Description                                                                                      | Example                           |
|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------|
| Color Names  | Human-friendly names for colors.                                                                 | `red`, `blue`, `goldenrod`        |
| RGB          | Specifies colors using Red, Green, and Blue values.                                              | `rgb(255, 0, 0)` (red)            |
| RGBA         | Like RGB, but with an added Alpha channel to indicate transparency.                              | `rgba(255, 0, 0, 0.5)` (semi-transparent red) |
| HEX          | Uses hexadecimal values to define colors.                                                        | `#ff0000` (red)                   |
| HSL          | Represents colors using Hue, Saturation, and Lightness. Useful for creating color variations.    | `hsl(0, 100%, 50%)` (red)         |
| HSLA         | Combines HSL with an Alpha channel for transparency control.                                     | `hsla(0, 100%, 50%, 0.5)` (semi-transparent red) |

HTML:

```html
<div id="container">
  <p>This is a paragraph.</p>
  <p>This is another paragraph.</p>
</div>
```

CSS:

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

Additional explanations:

- The color you choose in design can evoke emotions, deliver messages, and even influence decision-making. Being adept at using various color definitions in CSS can empower designers to create visually striking and user-friendly interfaces.
- While HEX and RGB are ubiquitous methods for setting colors, HSL can be more intuitive when making adjustments or creating color schemes. Furthermore, the inclusion of an alpha channel in RGBA and HSLA allows designers to introduce varying levels of transparency, perfect for layered designs and overlays.

#### Background

Backgrounds serve as a foundation for web elements. Whether it's a vivid color, a subtle gradient, or an evocative image, the background can enhance or soften content, guiding users' attention and enriching the visual experience.

| Property            | Description                                                   | Values                                                   | MDN Documentation                                                                                             |
|---------------------|---------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `background-color`  | Defines the solid background color of an element.             | Any valid color value (HEX, RGB, HSL, color names)       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color)                                 |
| `background-image`  | Sets an image or gradient as the element's background.        | `none`, `url(path_to_image)`                             | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image)                                 |
| `background-position` | Specifies the starting position of the background image.    | `top left`, `center center`, `10px 20px`                 | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/background-position)                              |
| `background-repeat` | Determines if/how the background image will repeat.           | `repeat`, `repeat-x`, `repeat-y`, `no-repeat`            | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/background-repeat)                                |
| `background-attachment` | Specifies if the background image scrolls with content or remains fixed. | `scroll`, `fixed`, `local`              | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/background-attachment)                            |
| `background-size`   | Indicates the size of the background images.                  | `cover`, `contain`, `50% 50%`                            | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/background-size)                                  |


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

CSS offers impressive flexibility with backgrounds. Beyond mere solid colors:

- Gradients allow for **smooth transitions** between multiple colors, enhancing visual appeal. CSS provides options for both linear gradients, where colors shift side-by-side, and radial gradients, where colors transition in a circular pattern, enabling diverse styling possibilities.
- Images in the background can act as **decorative elements**, textures, or even full-screen backdrops. Using properties like `background-size`, `background-position`, and `background-repeat`, designers can customize images to suit various aesthetic goals and functional requirements.

### Positioning

Positioning elements on a web page is a fundamental task in web design. CSS provides multiple methods to achieve desired layouts and presentations.

Core Positioning Properties:

| Property      | Description                                                      | Values                                                                                 | MDN Documentation                                                                                     |
|---------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `position`    | Determines the positioning method used for an element.           | `static`, `relative`, `absolute`, `fixed`, `sticky`                                    | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/position)                                  |
| `float`       | Specifies how an element should float.                           | `none`, `left`, `right`                                                                | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/float)                                     |
| `clear`       | Sets which sides of an element will not be adjacent to floating elements. | `none`, `left`, `right`, `both`                                                | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/clear)                                     |
| `display`     | Dictates the display box type of an element.                     | `inline`, `block`, `inline-block`, `table`, `table-row`, `table-cell`, `none`          | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/display)                                   |
| `visibility`  | Defines if an element is visible.                                | `visible`, `hidden`, `collapse`                                                       | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility)                                |
| `overflow`    | Controls what happens to content that overflows its box.         | `visible`, `hidden`, `scroll`, `auto`                                                 | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow)                                  |

HTML:

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

CSS:

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

Position Property:

| Position Value | Description                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------|
| `Static`       | The default position. Elements are ordered as they appear in the HTML document.                                               |
| `Relative`     | Elements are positioned relative to their normal position but do not affect the position of adjacent elements.                |
| `Absolute`     | Elements are positioned relative to their closest positioned ancestor. If none exists, it is relative to the initial container. |
| `Fixed`        | Positioned relative to the viewport, so the element stays fixed even during scrolling.                                        |
| `Sticky`       | A hybrid of relative and fixed. The element behaves as relative until a given scroll point, after which it acts as fixed.     |

Display Property:

| Display Value   | Description                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Inline`        | Elements are in line with adjacent elements. Respects left/right margins and padding, but not top/bottom. Width and height cannot be set.                             |
| `Block`         | Elements form a block, breaking onto a new line. They respect all margins and padding and occupy the full width by default.                                           |
| `Inline-block`  | Elements are inline but can have properties like block elements, such as width and height. Useful for buttons or items in a horizontal navigation.                    |

Lastly, always remember that with the evolving nature of CSS and web design, utilizing developer tools in browsers and referencing platforms like MDN can help keep your understanding current and your designs sharp.

![Screenshot from 2022-10-11 20-46-35](https://user-images.githubusercontent.com/37275728/195174303-2330e847-fcb9-4c86-9b38-13130dd010e6.png)

### Animations and Dynamic Effects

In the digital era, motion design plays a pivotal role in enhancing user experience. CSS3, the third level of Cascading Style Sheets, offers a wide variety of animation capabilities to bring life to web elements and improve user interaction.

#### Animations

CSS animations allow elements to transition between styles over a set duration and through specified keyframes. This means an element can smoothly shift from one style to another over a given time period.

Core Animation Properties

| Property                  | Description                                                             | Values                                                                                               | MDN Documentation                                                                                             |
|---------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `animation`               | Shorthand to set multiple animation properties at once.                | `animation-name`, `animation-duration`, `animation-timing-function`, `animation-delay`, `animation-iteration-count`, `animation-direction`, `animation-fill-mode`, `animation-play-state` | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)                                         |
| `animation-name`          | Names the animation for reference.                                      | `string` (name of the keyframes)                                                                     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-name)                                   |
| `animation-duration`      | Specifies how long the animation takes for a single cycle.              | `time` (e.g., `2s`, `200ms`)                                                                         | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-duration)                               |
| `animation-timing-function` | Describes the pacing of the animation.                                | `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out`                                               | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function)                        |
| `animation-delay`         | Sets a delay before the animation starts.                               | `time`                                                                                               | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-delay)                                  |
| `animation-iteration-count` | Dictates how many times the animation plays.                          | `number` or `infinite`                                                                               | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-iteration-count)                        |
| `animation-direction`     | Determines the direction of the animation.                              | `normal`, `reverse`, `alternate`, `alternate-reverse`                                                | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-direction)                              |
| `animation-fill-mode`     | Defines what values are applied before/after the animation.             | `none`, `forwards`, `backwards`, `both`                                                              | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-fill-mode)                              |
| `animation-play-state`    | Determines whether the animation is running or paused.                  | `running`, `paused`                                                                                  | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-play-state)                             |

HTML:

```html
<div id="box">
  <p>I'm the box.</p>
</div>
```

CSS:

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

To create CSS animations, you'll define `@keyframes` that set the styling for different stages or "frames" of the animation. These `@keyframes` can be referenced using the `animation-name` property.

```css
@keyframes slideIn {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}
```

In the example above, an animation named slideIn moves an element from off the screen (-100%) to its natural position (0). Using the animation property, you can then apply this animation to an element:

```css
element {
  animation: slideIn 2s ease-in-out;
}
```

This CSS rule applies the slideIn animation to the element over a 2-second duration with an ease-in-out timing function. The possibilities are vast—allowing for rich, interactive, and engaging web designs.

#### 2D/3D Transform

In modern web design, the ability to animate and transform elements has become a staple. CSS offers a powerful suite of properties to apply 2D and 3D transformations to elements, granting designers and developers the capacity to change an element's position, size, and orientation in creative ways.

| Property              | Description                                                                          | Values                                                                                       | MDN Documentation                                                                                               |
|-----------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `transform`           | Applies a 2D or 3D transformation to an element.                                     | `none`, `matrix`, `translate`, `translateX`, `translateY`, `scale`, `rotate`, `skew`, `perspective`, and 3D variants such as `translate3d`, `rotate3d`, etc.  | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)                                          |
| `transform-origin`    | Defines the point around which a transformation is applied.                          | `origin-x origin-y origin-z` (e.g., `50% 50%` or `center center`)                             | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin)                                   |
| `transform-style`     | Specifies how nested elements are rendered in 3D space.                              | `flat`, `preserve-3d`                                                                        | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style)                                    |
| `perspective`         | Determines the distance between the viewer and the z=0 plane, affecting 3D transformations. | `length` (e.g., `1000px`)                                                                     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective)                                        |
| `perspective-origin`  | Establishes the origin for the perspective property.                                 | `length` or percentage (e.g., `50% 50%`)                                                     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective-origin)                                 |
| `backface-visibility` | Defines whether the back face of an element is visible when turned towards the viewer.| `visible`, `hidden`                                                                          | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility)                               |

HTML:

```html
<div id="box">
  <p>I'm the box.</p>
</div>
```

CSS:

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

Additional Insights:

- Transformations in CSS encompass various **operations** such as moving (`translate`), scaling (`scale`), rotating (`rotate`), and skewing (`skew`). These can be implemented in both 2D and 3D spaces, allowing for versatile adjustments like revolving an element around its X-axis with `rotateX` in 3D.
- By default, transformations are based around the **center** of an element. The `transform-origin` property, however, lets you change this pivot point, enabling transformations around specific points such as a corner, which can be especially useful for precise rotation effects.
- In 3D transformations, both `transform-style` and `perspective` play important roles by introducing **depth**. The `transform-style` property allows child elements to be placed in 3D space, while `perspective` adds a realistic depth effect, making the 3D transformations more visually engaging.
- The `backface-visibility` property controls the **visibility** of an element’s reverse side in 3D space. This feature is useful when, for example, you want to hide the back side of a card during a flip animation, keeping only the front view visible to the user.

#### Transition

Transitions in CSS provide a way to control animation speed when changing CSS properties. Instead of having property changes take effect instantly, you can cause the changes to take place over a period of time. This makes for a smoother visual experience and can add a touch of dynamism to web designs.

| Property                | Description                                                                        | Values                                                                                                    | MDN Documentation                                                                                             |
|-------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `transition`            | Shorthand for setting multiple transition properties at once.                      | `[ transition-property, transition-duration, transition-timing-function, transition-delay ]`              | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)                                        |
| `transition-property`   | Specifies the CSS property to which the transition is applied.                     | `none`, `all`, Specific property names (e.g., `opacity`, `transform`)                                     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property)                               |
| `transition-duration`   | Defines the duration of the transition effect.                                     | `time` (e.g., `0.5s`, `300ms`)                                                                            | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration)                              |
| `transition-timing-function` | Describes how intermediate values are calculated during a transition.         | `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out`, cubic-bezier values                               | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function)                       |
| `transition-delay`      | Specifies a delay before the transition starts.                                    | `time` (e.g., `0.2s`)                                                                                     | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay)                                 |

HTML:

```html
<div id="box">
  <p>I'm the box.</p>
</div>
```

CSS:

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

Additional Insights:

- Transition properties default to applying to **all** properties, but you can specify particular ones for animation, such as `opacity` or `background-color`. Specifying individual properties can help focus the transition effect on just the intended elements.
- The **duration** of a transition defines its length, with longer durations making the effect more noticeable and shorter durations providing a quick, snappy response, which can enhance the feel of user interactions.
- A transition’s **timing function** dictates its acceleration curve, determining how it speeds up or slows down over time. Custom values like `cubic-bezier` allow you to create unique timing curves that suit specific design needs.
- If you need a transition to start after a **delay**, the `transition-delay` property allows you to set a waiting period before the transition begins. This can be particularly useful when animating sequences where multiple elements transition one after another for a cascading effect.

### Responsive Design

Responsive design ensures that websites adapt and render optimally across a variety of devices. It aims to offer a consistent user experience from the smallest mobile device to the largest desktop monitor.

#### Responsive Grid vs. Fluid Grid

- A responsive grid uses a **fixed** grid system, commonly based on a 12-column layout, with specific breakpoints in pixels to accommodate different screen sizes. At these breakpoints, the design may shift to a new column arrangement or selectively hide or show certain elements for optimal display.
- Fluid grids offer **greater flexibility** than responsive grids by using percentages to define element widths. This approach allows elements to continuously adjust in size relative to their parent container, enabling them to expand and contract smoothly as the viewport changes.

Recommended Number of Columns:

| Device Type | Number of Columns |
|-------------|--------------------|
| Desktop     | 12 columns         |
| Tablet      | 8 columns          |
| Mobile      | 4 columns          |

#### Mobile First Design

Adopting a **Mobile First** design strategy means building the initial design for the smallest screens (mobile devices) and then progressively enhancing the design for larger screens. This methodology ensures that mobile users receive only the essential features and content, helping improve performance and user experience on slower networks.

#### Media Queries

Media queries are the backbone of responsive design. They allow developers to apply styles based on the device characteristics. For instance, different styles can be applied depending on the device's screen width, height, orientation, and more.

Let's say we want to create a button that changes its color depending on the screen size.

HTML:

```html
<button id="button">Click me!</button>
```

CSS:

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


| Rule       | Description                                   | Usage Examples                                                                                         | MDN Documentation                                                                                     |
|------------|-----------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `@media`   | The heart of media queries in CSS. It allows for styles to be applied based on specific conditions, such as screen size or orientation. | `screen`, `print`, `all`, `min-width`, `max-width`, `orientation: portrait`, `orientation: landscape` | [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/@media)                                    |

Additional Insights:

- Overlapping styles in CSS are influenced by its **cascading** nature, meaning that when the same selector is used multiple times, styles defined later will override earlier ones. This behavior is especially important to consider when using media queries, as their order in the stylesheet can lead to unintentional style overrides.
- Including the **viewport meta tag** in the HTML head is essential for proper display on mobile devices. This tag, `<meta name="viewport" content="width=device-width, initial-scale=1.0">`, ensures that responsive designs adjust correctly to the device’s screen width, which is crucial for mobile responsiveness.
- Modern layout techniques like **Flexbox** and **Grid** provide enhanced control over responsive designs, allowing for the creation of flexible, adaptive layouts without the need for traditional grid systems. These tools simplify the process of designing layouts that adapt to different screen sizes.
- Regular **testing** across various devices and screen sizes is key to ensuring design consistency. Browser developer tools and other software can simulate different devices, helping you identify and resolve any potential design issues across different viewing environments.

### Units

Units in CSS provide a way to express measurements. Understanding when and how to use different units is crucial for designing responsive and accessible websites.

#### Absolute Units

These are fixed-size units and do not scale with changes in other properties or viewer's settings.

| Unit | Description                                                                                                                        | Conversion Example                             |
|------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `px` | Pixels – A dot on the computer screen. Relative in the sense that it's not consistent across devices, but absolute within a device. | Commonly used for digital screens              |
| `pt` | Points – Traditionally used in print media. 1pt = 1/72 of an inch.                                                                 | `12pt` = 1/6 inch                              |
| `pc` | Picas – A print measure where 1pc = 12 points.                                                                                     | `1pc` = 12pt                                   |
| `cm` | Centimeters.                                                                                                                       | `2.54cm` = 1 inch                              |
| `mm` | Millimeters.                                                                                                                       | `10mm` = 1cm                                   |
| `in` | Inches – 1 inch is equal to 2.54 centimeters.                                                                                      | `1in` = 2.54cm                                 |
| `%`  | Percentage – Relative to the parent element or another reference point.                                                            | `50%` of the parent element's size             |


#### Relative Units

Relative units are responsive and adapt based on the context in which they're used.

| Unit    | Description                                                                                                  | Example Calculation                        |
|---------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| `em`    | Font size of the current element. If the font size is 16px, then "2em" is 32px.                              | `2em` = 32px (assuming base font size is 16px) |
| `rem`   | Font size of the root element (usually `<html>`). Consistent across nested elements.                         | `2rem` = 32px (assuming root font size is 16px) |
| `ch`    | Width of the '0' character of the current font.                                                              | Depends on the font being used             |
| `ex`    | x-height of the current font, roughly the height of lowercase letters in most fonts.                         | Depends on the font being used             |
| `vh`    | 1% of the height of the viewport window.                                                                     | `50vh` = half of the viewport height       |
| `vw`    | 1% of the width of the viewport window.                                                                      | `50vw` = half of the viewport width        |
| `vmin`  | 1% of the viewport's smaller dimension (height or width).                                                    | `10vmin` = 10% of the smaller viewport dimension |
| `vmax`  | 1% of the viewport's larger dimension (height or width).                                                     | `10vmax` = 10% of the larger viewport dimension |

Further Insights:

- The `em` and `rem` units are valuable for **scalability** and accessibility in web design, as they allow the layout to adapt to user preferences, such as increasing the browser's default font size. This flexibility enhances the user experience by catering to individual needs.
- Viewport units like `vh`, `vw`, `vmin`, and `vmax` provide an **adaptive** approach to responsive design, adjusting the layout based on the user’s screen size. These units are especially useful for creating designs that remain consistent across different devices.
- Units like `pt` and `pc`, known as **legacy** units, originate from the print industry and are less prevalent in modern web design. However, they can still be useful when creating designs intended for print or specific use cases requiring precise measurements.
- Selecting the right **unit** is essential in web design. For typography, relative units such as `em` and `rem` are typically preferred, as they adapt well to scaling. For layout elements, units like `px`, `%`, and viewport units are widely used for a more responsive and flexible design structure.

### Best Practices

#### General

* Use external CSS files and place them within the `<head>` tag.
* Organize your CSS into logical sections and use comments to explain complex or important parts.
* Follow a consistent naming convention for class and ID names.
* Use shorthand properties when possible to reduce code length.

#### Formatting

* Don't leave out the last semicolon in a CSS block.
* Maintain consistent casing, preferably lowercase, for selector names.
* Use a single space after the colon in property-value pairs.
* Use a new line for each declaration in a rule set.
* Remove trailing white spaces and keep indentation consistent.

#### Layout and Positioning

* Use the box model consistently throughout the document.
* Avoid breaking the flow by using absolute positioning sparingly.
* Utilize Flexbox and Grid for modern, responsive layouts.
* Avoid using fixed pixel values for layout and spacing; use relative units like `rem`, `em`, and percentages.

#### Selectors and Specificity

* Prefer classes over selectors that are tightly coupled to the DOM.
* Reduce the usage of IDs to avoid high specificity conflicts.
* Minimize the use of overly complex or deeply nested selectors.
* Keep selector specificity low to make styles easier to override and maintain.

#### Inheritance and Efficiency

* Don't duplicate style declarations that can be inherited from parent elements.
* Use unitless values when possible, or `rem` for relative units.
* Use the hexadecimal format for colors, or use CSS variables for consistent theming.
* Minimize the use of vendor prefixes by leveraging tools like Autoprefixer.

#### Responsiveness and Accessibility

* Design your CSS with responsiveness in mind, using media queries to adapt to various screen sizes and devices.
* Prioritize readability and usability in your designs.
* Use appropriate color contrasts to ensure legibility for all users.
* Include alternative text and labels for interactive elements to improve accessibility.

#### Performance and Optimization

* Minify your CSS files to reduce file size and improve load times.
* Use CSS properties like `transform` and `opacity` for animations and transitions that leverage hardware acceleration.
* Optimize images and other assets used as background images or within your styles.
* Utilize browser caching to improve page load times for returning visitors.

### Links

- [Official Website](https://www.w3.org/Style/CSS/)
- [Isobar Front-end Code Standards](http://isobar-idev.github.io/code-standards/)
- [HTML Best Practices](https://github.com/hail2u/html-best-practices)
- [Writing Your Best Code](http://learn.shayhowe.com/html-css/writing-your-best-code/)
- [Web Accessibility Best Practices](https://www.webaccessibility.com/best_practices.php)
- [CleanCSS Formatter](https://www.cleancss.com/css-beautify/)
