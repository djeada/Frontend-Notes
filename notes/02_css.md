## CSS

* Cascading Style Sheets (CSS)
* The "adjectives" of the web
* Takes the basic HTML structure and styles it according to our preferences

### Key Points about CSS:

- **What is CSS?**: CSS stands for Cascading Style Sheets. It's a language used to describe how a document, typically written in HTML, should look.
  
- **Role in Web Development**: Consider CSS as the "adjectives" of the web. While HTML provides the structure, CSS adds the styling to make it visually appealing.
  
- **Predefined Styles**: CSS allows developers to establish predefined styles, ensuring consistency across web pages. You can either manually create these styles or import them from libraries like Bootstrap, TailwindCSS, etc.

- **Capabilities**: Using CSS, developers can control various visual aspects such as colors, positions, dimensions, and even complex animations.

## Skills Every CSS Developer Should Acquire:

1. **Basic Styling**: Understanding how to adjust properties like colors, borders, and fonts.

2. **Layout & Positioning**: Crafting layouts using techniques like Flexbox, Grid, and positioning properties. Making designs responsive for different devices is paramount.

3. **Selectors**: Knowing when and how to use different CSS selectors efficiently.

4. **References**: Regularly using resources like the [Mozilla Developer Network (MDN)](https://developer.mozilla.org/) for documentation and best practices.

5. **Building Components**: Ability to recreate and customize design components using pure CSS.

## Integrating CSS with HTML

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

## Understanding Selectors

CSS Selectors play a pivotal role in defining which HTML elements should receive specific styles. By combining different types of selectors and properties, web developers can create intricate designs and layouts.

### Selectors and Properties

In CSS, a basic rule-set consists of a selector and a declaration block. The declaration block contains properties and their values.

```css
selector {
    property_1: value_1;
    property_2: value_2;
    /* ... and so on */
}
```

- **Selectors**: They specify which HTML elements will be affected by the style rules.
- **Properties and Values**: Within the declaration block, properties define what aspect of the element should be styled, and values determine how they should be styled.

### Different Types of CSS Selectors

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

### Introduction to Pseudo-selectors

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

### Common Pseudo-selectors

Pseudo-selectors, often termed pseudo-classes, allow developers to target and style HTML elements based on specific conditions, states, or positions rather than solely on their tags or attributes.

Below is a list of commonly-used pseudo-selectors, each paired with a brief description and a link to its documentation on MDN for deeper insights:

- **`:active`**: Targets elements that are currently being activated by the user (like when clicking on a link or button). [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:active)
  
- **`:focus`**: Highlights the currently focused element, commonly used with form fields. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus)

- **`:hover`**: Styles an element when a user hovers over it with their cursor. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:hover)

- **`:link`**: Targets hyperlinks that haven't been visited by the user. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:link)

- **`:visited`**: Selects links that have been visited by the user. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:visited)

- **`:checked`**: Targets checked elements like radio buttons or checkboxes. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:checked)

- **`:first-child`**: Targets the first child element inside a parent element. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:first-child)

- **`:last-child`**: Selects the last child element within a parent. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:last-child)

- **`:nth-child(n)`**: Allows for the styling of elements based on their position in a group. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child)

- **`:disabled`** and **`:enabled`**: Respectively target disabled and enabled form controls. [MDN Docs for `:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/:disabled), [MDN Docs for `:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/:enabled)

- **`:not(selector)`**: Targets elements that do not match a specific selector. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:not)


## Inheritance and Specificity in CSS

In the world of CSS, it's crucial to understand how rules cascade and how specificity works. Specificity determines which CSS rule is applied to an element when there are multiple conflicting rules.

### Specificity Hierarchy

When two or more CSS rules target the same element but have conflicting styles, the specificity hierarchy determines which rule is applied:

1. **IDs**
2. **Classes, attributes, and pseudo-classes**
3. **Elements and pseudo-elements**

Visualized:

```
ids > classes, attributes, pseudo-classes > elements, pseudo-elements
```

Useful tools like [Specificity Calculator](https://specificity.keegan.st/) can help understand and calculate the specificity of your selectors.

## Pseudo-elements in CSS

Pseudo-elements are a powerful feature in CSS, allowing you to style certain parts of a document, or to virtually insert content into the document, without altering the actual HTML structure.

### Concept

Pseudo-elements are different from pseudo-classes. While pseudo-classes select elements based on their state or position in relation to others (like `:hover` or `:nth-child`), pseudo-elements target specific parts of an element, like the first line or first letter, or they can virtually insert content before or after an element's content.

### Example

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

### Common Pseudo-elements

Pseudo-elements target specific parts of elements or create virtual content around them. They're instrumental in achieving certain design patterns and effects without altering the actual HTML content.

- **`::before`**: Inserts virtual content before an element's actual content. Typically used with the `content` property to display strings, icons, or images. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/::before)

- **`::after`**: Similarly, it inserts virtual content but after an element's content. Just like `::before`, it's commonly paired with the `content` property. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/::after)

- **`::first-letter`**: Targets the initial letter of block-level elements. This pseudo-element can be handy for design patterns like drop caps. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/::first-letter)

- **`::first-line`**: Captures the first line of text within block-level elements, allowing you to apply specific styles to the initial line of a paragraph or a container. [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/::first-line)

### Noteworthy Points

1. **Content Requirement**: For `::before` and `::after` to manifest any visual change, the `content` property is essential. It dictates what content (if any) these pseudo-elements should display.

2. **Non-alteration of the DOM**: Pseudo-elements are a styling aspect only. They won't alter the DOM, meaning they're invisible in the source HTML and can't be accessed directly through JavaScript.

3. **CSS Only**: Being CSS constructs, pseudo-elements are inaccessible from JavaScript, which is essential to remember when considering site interactivity and functionality.

These pseudo-elements, while subtle, empower developers with additional control over design and presentation, enriching the user experience without the need for additional HTML elements.

## Box Model

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

### Margins

Margins create space around an element, separating it from other elements.

- **Top Margin**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top">margin-top</a></code>: Defines the space above the element.
    - Values: `auto` | `length` | `percentage`

- **Right Margin**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right">margin-right</a></code>: Defines the space to the right of the element.
    - Values: `auto` | `length` | `percentage`

- **Bottom Margin**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom">margin-bottom</a></code>: Defines the space below the element.
    - Values: `auto` | `length` | `percentage`

- **Left Margin**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left">margin-left</a></code>: Defines the space to the left of the element.
    - Values: `auto` | `length` | `percentage`

### Padding

Padding creates space within an element, between the content and its border.

- **Top Padding**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top">padding-top</a></code>: Defines the space between the content and the top border of the element.
    - Values: `length` | `percentage`

- **Right Padding**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-right">padding-right</a></code>: Defines the space between the content and the right border of the element.
    - Values: `length` | `percentage`

- **Bottom Padding**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-bottom">padding-bottom</a></code>: Defines the space between the content and the bottom border of the element.
    - Values: `length` | `percentage`

- **Left Padding**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/padding-left">padding-left</a></code>: Defines the space between the content and the left border of the element.
    - Values: `length` | `percentage`

### Border

Borders surround an element, giving it structure and sometimes helping it stand out. You can define the width, style, color, and even use images as borders.

- **Width**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-width">border-width</a></code>: Defines the thickness of the border.
    - Values: `auto` | `length`

- **Style**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-style">border-style</a></code>: Determines the pattern or design of the border.
    - Values: `none` | `hidden` | `dotted` | `dashed` | `solid` | `double` | `groove` | `ridge` | `inset` | `outset`

- **Color**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-color">border-color</a></code>: Sets the color of the border.
    - Values: color name, hex, rgba, etc.

- **Radius**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius">border-radius</a></code>: Allows you to create rounded borders.
    - Values: `length` (can set each corner individually)

- **Image**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-image">border-image</a></code>: Uses an image as the border.
    - Values: `none` | image source | slice | width | outset | repeat

### Outline

Outlines are similar to borders but don't take up space. They're often used for focus styles and other UI states.

- **Width**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/outline-width">outline-width</a></code>: Defines the thickness of the outline.
    - Values: `auto` | `length`

- **Style**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/outline-style">outline-style</a></code>: Determines the pattern or design of the outline.
    - Values: `none` | `hidden` | `dotted` | `dashed` | `solid` | `double` | `groove` | `ridge` | `inset` | `outset`

- **Color**:
  - <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/outline-color">outline-color</a></code>: Sets the color of the outline.
    - Values: color name, hex, rgba, etc.

### Advanced Tips

When setting the dimensions of an element, be cautious of extremes. An element that is either too small or too large can disrupt the layout and aesthetics of a page. In these cases, special values such as `max-content`, `min-content`, and `fit-content` are valuable:

- `min-content`: Shrinks the element to its smallest size.
- `max-content`: Expands the element to its largest size based on its content.
- `fit-content`: Scales the element based on available space and its content size.


## Flexbox

Flexbox, short for "Flexible Box Layout", is a design model in CSS that allows you to design complex layout structures with a more efficient and predictable way than traditional models, especially when dealing with different screen sizes and dynamic content.

### Flex Container vs. Flex Items

When an element is defined as a flex container (using `display: flex` or `display: inline-flex`), its children automatically become flex items. Flexbox involves two sets of properties:

1. **Container Properties**: These are set on the flex container.
   - `display`: Initiates the flex context (`flex` or `inline-flex`).
   - `flex-direction`: Defines the main axis direction (`row`, `row-reverse`, `column`, `column-reverse`).
   - `flex-wrap`: Determines if items should wrap (`nowrap`, `wrap`, `wrap-reverse`).
   - ... and others like `justify-content`, `align-items`, `align-content`.

2. **Item Properties**: These are set on the flex items.
   - `flex`: A shorthand for setting `flex-grow`, `flex-shrink`, and `flex-basis`.
   - `align-self`: Allows an item to override the container's `align-items` property.
   - ... and others like `order`, `flex-basis`, `flex-grow`, `flex-shrink`.

### Understanding the Axes

Flexbox layout revolves around two axes: the main axis and the cross axis.

1. **Main Axis**: The primary axis along which flex items are laid out. Its direction is determined by the `flex-direction` property.
2. **Cross Axis**: Perpendicular to the main axis. 

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

### Example

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

### Flexbox Properties

Flexbox introduces a set of properties that provide a more efficient and predictable way to layout, align, and distribute space among items in a container, even when their sizes are unknown or dynamic.

#### Flex Containers

To create a flex container, use the `display` property:

1. [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/display): Determines the element's inner and outer display type.
   - **Values**: `flex` (block-level flex container) | `inline-flex` (inline-level flex container)

#### Ordering and Orientation

Control the order in which items appear and their directional flow:

1. [`order`](https://developer.mozilla.org/en-US/docs/Web/CSS/order): Specifies the order of the flex item relative to its siblings.
   - **Values**: `<number>` (default: 0)
2. [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction): Defines the direction of the main axis, determining the orientation of flex items.
   - **Values**: `row` | `row-reverse` | `column` | `column-reverse`
3. [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap): Specifies whether flex items wrap onto multiple lines or columns.
   - **Values**: `nowrap` | `wrap` | `wrap-reverse`
4. [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow): A shorthand property for setting both `flex-direction` and `flex-wrap`.
   - **Values**: `<flex-direction> || <flex-wrap>`

#### Alignment and Justification

Determine how items are aligned and spaced within the flex container:

1. [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items): Describes how flex items are aligned along the cross axis of the flex container.
   - **Values**: `flex-start` | `flex-end` | `center` | `baseline` | `stretch`
2. [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/align-content): Aligns flex lines within the flex container when there's extra space in the cross-axis.
   - **Values**: `flex-start` | `flex-end` | `center` | `space-between` | `space-around` | `stretch`
3. [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content): Defines how flex items are spaced along the main axis.
   - **Values**: `flex-start` | `flex-end` | `center` | `space-between` | `space-around` | `space-evenly`

#### Flexibility of Items

Define how flex items grow and shrink:

1. [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex): A shorthand to set the `flex-grow`, `flex-shrink`, and `flex-basis` properties.
   - **Values**: `<flex-grow> <flex-shrink> <flex-basis>`
2. [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow): Specifies the flex item's ability to grow relative to other items.
   - **Values**: `<number>` (default: 0)
3. [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink): Defines the flex item's ability to shrink relative to other items.
   - **Values**: `<number>` (default: 1)
4. [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis): Defines the default size of a flex item before the available space is distributed.
   - **Values**: `auto` | `<length>` | `<percentage>`

Leveraging these properties allows for sophisticated layout designs that adapt gracefully across different screen sizes and resolutions.

### Noteworthy Points

- Flexbox layouts adapt to the size of the container and the size of the content. This makes it great for creating responsive designs without depending heavily on media queries.

- Flex items will, by default, try to fit onto one line. Use the `flex-wrap` property if you want items to wrap onto multiple lines.

- Flexbox also provides tools for alignment, distribution, and spacing of items, using properties like `align-items`, `justify-content`, and `gap`.

## Special Styling Elements

Certain elements in CSS come with a unique set of styling options. One such element is the list, with its associated markers.

### Lists & Markers

In web design, lists are ubiquitous. CSS provides granular control over the appearance and positioning of list items and their markers.

#### Key Properties

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style">list-style</a></code>**: Defines an element's list style.
   - `none`: No style is applied.
   - Composite value: A combination of `list-style-type`, `list-style-position`, and `list-style-image`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type">list-style-type</a></code>**: Specifies the type of list marker.
   - Common values: `disc`, `circle`, `square`, `decimal`, `decimal-leading-zero`, `lower-roman`, `upper-roman`.
   - More unique values: `lower-greek`, `lower-latin`, `upper-latin`, `armenian`, `georgian`, `none`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-position">list-style-position</a></code>**: Determines the position of the marker relative to the list item content.
   - `inside`: The marker is placed inside the list item box.
   - `outside`: The marker is outside the list item box, creating an indent.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-image">list-style-image</a></code>**: Allows you to use an image as the list item marker.
   - `url("path_to_image")`: Specifies the URL path to the image to be used as the marker.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/marker-offset">marker-offset</a></code>**: (Deprecated) Specifies the distance between a marker and the principal block box's nearest border edges.
   - `auto`: The browser determines the offset.
   - Length values (e.g., `5px`, `1em`): Defines a specific distance.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/marker-start">marker-start</a></code>**: (Deprecated in favor of SVG's `marker` attribute) Specifies a marker to be used at the start of lines.

Understanding these properties allows developers to create more visually appealing lists and enhances the user experience by making content more digestible and organized.

#### Example

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

### Table

Tables in CSS are designed to structure tabular data. They come with a rich set of properties that offer detailed styling options to enhance their appearance and usability.

### Key Styling Properties

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/table-layout">table-layout</a></code>**: Determines the algorithm used to layout the table cells, rows, and columns.
   - `auto`: Uses the content's width to adjust the column widths. This might cause slower rendering for large tables.
   - `fixed`: The horizontal layout only depends on the table's width and the width of columns, not the contents of its cells. It provides faster rendering.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-collapse">border-collapse</a></code>**: Specifies whether cell borders are collapsed into a single border or detached as in standard HTML.
   - `collapse`: Borders are merged into a single border where possible.
   - `separate`: Borders are split; each cell displays its own border.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-spacing">border-spacing</a></code>**: Determines the spacing between the borders of adjacent cells when `border-collapse` is set to `separate`. 
   - Length values (e.g., `2px 4px`): The first value defines horizontal spacing and the second defines vertical spacing.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/caption-side">caption-side</a></code>**: Specifies the position of the table's caption.
   - `top`: The caption is displayed above the table.
   - `bottom`: The caption is displayed below the table.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/empty-cells">empty-cells</a></code>**: Determines the visibility of borders and backgrounds of empty cells.
   - `show`: Show the borders and background, even if the cell is empty.
   - `hide`: No borders or background are shown if the cell is empty.

#### Example

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

### Text

Text is a fundamental aspect of web design, and CSS offers an extensive suite of properties to style text with precision. From basic color settings to intricate shadow effects, text styling can be as simple or as detailed as the design requires.

### Key Text Styling Properties

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/color">color</a></code>**: Specifies the color of the text.
   - Can be defined using HEX, RGB, RGBA, HSL, or named colors.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/direction">direction</a></code>**: Sets the direction in which text is written.
   - `ltr`: Left to Right (default for most languages).
   - `rtl`: Right to Left (common for Arabic, Hebrew).

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing">letter-spacing</a></code>**: Adjusts the space between characters.
   - Can be defined using units like `px`, `em`, `rem`, etc.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/line-height">line-height</a></code>**: Determines the height of a line box.
   - `normal`: Default line height.
   - Number values (e.g., `1.5`), or units like `px`, `em`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-align">text-align</a></code>**: Aligns the inline content like text.
   - Values: `start`, `end`, `left`, `right`, `center`, `justify`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration">text-decoration</a></code>**: Adds decorative lines to text.
   - Values: `none`, `underline`, `overline`, `line-through`. (Note: `blink` is deprecated.)

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-indent">text-indent</a></code>**: Indents the first line of a text block.
   - Can be defined using units like `px`, `em`, `rem`, etc.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform">text-transform</a></code>**: Controls the capitalization of text.
   - Values: `capitalize`, `uppercase`, `lowercase`, `none`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/vertical-align">vertical-align</a></code>**: Sets the vertical positioning of an element relative to its parent or the line height.
   - Values include: `baseline`, `sub`, `super`, `top`, `text-top`, `middle`, `bottom`, `text-bottom`, and units like `px`, `em`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/white-space">white-space</a></code>**: Specifies how whitespace inside an element is handled.
   - Values: `normal`, `pre`, `nowrap`, `pre-wrap`, `pre-line`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/word-spacing">word-spacing</a></code>**: Adjusts the space between words.
   - Can be defined using units like `px`, `em`, `rem`, etc.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-outline">text-outline</a></code>** (Note: not standard): Defines an outline for the text.
   - Values: `none`, `color`, `width`, `style`, or combined as `[ color, width, style ]`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow">text-overflow</a></code>**: Specifies how overflowed content is signaled to the user.
   - Values: `clip`, `ellipsis`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow">text-shadow</a></code>**: Adds shadow effects to the text.
   - Values can include `color`, `offset-x`, `offset-y`, and `blur-radius`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap">text-wrap</a></code>** (Note: not standard): Specifies line breaking rules.
   - Values: `normal`, `none`, `break-word`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/word-break">word-break</a></code>**: Controls how lines should break in case of long words or overflow.
   - Values: `normal`, `break-all`, `keep-all`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/word-wrap">word-wrap</a></code>**: Specifies whether to break words when they overflow the content box.
   - Values: `normal`, `break-word`.

#### Example

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

## Style

CSS provides a suite of generic styling properties that can be applied universally across elements. Two commonly used properties are `font` and `color`. While `font` dictates the appearance and style of text, `color` sets the foreground color for text and other graphical elements.

### Font

Fonts play a pivotal role in establishing the visual identity of a website. With the advent of web fonts, designers are no longer restricted to a few standard system fonts. Today, a vast collection of fonts can be easily integrated into web projects to achieve the desired typography.

There are numerous platforms that offer free and premium web fonts:

* [CSS Font Stack](https://www.cssfontstack.com/)
* [Google Fonts](https://fonts.google.com/)

Steps to Incorporate Custom Fonts:

1. Navigate to a web fonts platform and select a desired font.
2. Obtain the link or `@font-face` code snippet for the chosen font.
3. Insert the link or code snippet into the `<head>` section of your HTML file.
4. Reference the font in your CSS using the `font-family` property.
 
#### Key Font Properties:

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-style">font-style</a></code>**: Dictates the style of a font.
   - Options: `normal`, `italic`, `oblique`.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight">font-weight</a></code>**: Determines the thickness of characters in a font.
   - Options: `normal`, `bold`, `bolder`, `lighter`, ranging from `100` (thinnest) to `900` (thickest).

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-size">font-size</a></code>**: Specifies the size of a font.
   - Can be defined using units like `px`, `em`, `rem`, `%`, etc.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-family">font-family</a></code>**: Defines which font should be used.
   - Typically defined using the font name in quotes (e.g., `"Helvetica, sans-serif"`).

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant">font-variant</a></code>**: Controls font variants, mainly for capitalized text.
   - Options: `normal`, `small-caps`.

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

#### Aditional explanations

Web fonts have reshaped the landscape of web typography. Platforms like Google Fonts and Adobe Fonts host a myriad of fonts, ensuring websites can have unique and tailored typography. When using custom fonts, it's vital to ensure they're web-optimized for performance and that fallback fonts are specified to cater to users with limited font access or slow internet connections.

### Colors

In web design, colors have a profound influence on user experience and branding. CSS provides diverse methods to assign colors to HTML elements. Besides color, you can also control an element's transparency or opacity, impacting how underlying content might be visible through it.

#### Fundamental Color Properties:

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/color">color</a></code>**: Specifies the foreground color of an element.
   - Accepts a variety of color formats.

- **<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/opacity">opacity</a></code>**: Determines the transparency level of an element.
   - Range: `0.0` (fully transparent) to `1.0` (fully opaque).

#### Common Methods to Define Colors:

- **Color Names**: Human-friendly names for colors. Examples include `red`, `blue`, and `goldenrod`.
- **RGB**: Specifies colors using Red, Green, and Blue values. Example: `rgb(255, 0, 0)` yields red.
- **RGBA**: Like RGB, but with an added Alpha channel to indicate transparency. Example: `rgba(255, 0, 0, 0.5)` gives a semi-transparent red.
- **HEX**: Uses hexadecimal values to define colors. Example: `#ff0000` represents red.
- **HSL**: Represents colors using Hue, Saturation, and Lightness. Useful for creating color variations.
- **HSLA**: Combines HSL with an Alpha channel for transparency control.

#### Example

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

#### Additional explanations

The color you choose in design can evoke emotions, deliver messages, and even influence decision-making. Being adept at using various color definitions in CSS can empower designers to create visually striking and user-friendly interfaces. 

While HEX and RGB are ubiquitous methods for setting colors, HSL can be more intuitive when making adjustments or creating color schemes. Furthermore, the inclusion of an alpha channel in RGBA and HSLA allows designers to introduce varying levels of transparency, perfect for layered designs and overlays.

### Background

Backgrounds serve as a foundation for web elements. Whether it's a vivid color, a subtle gradient, or an evocative image, the background can enhance or soften content, guiding users' attention and enriching the visual experience.

#### Core Background Properties

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-color">background-color</a>**: Defines the solid background color of an element.
   - Accepts any valid color value.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-image">background-image</a>**: Sets an image or gradient as the element's background.
   - Value: `none` or `url(path_to_image)`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-position">background-position</a>**: Specifies the starting position of the background image.
   - Examples: `top left`, `center center`, `10px 20px`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-repeat">background-repeat</a>**: Determines if/how the background image will repeat.
   - Options: `repeat`, `repeat-x`, `repeat-y`, `no-repeat`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-attachment">background-attachment</a>**: Specifies if the background image scrolls with the content or remains fixed.
   - Values: `scroll`, `fixed`, `local`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-size">background-size</a>**: Indicates the size of the background images.
   - Examples: `cover`, `contain`, `50% 50%`.

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

#### Additional explanations

CSS offers impressive flexibility with backgrounds. Beyond mere solid colors:

- **Gradients**: These enable smooth transitions between multiple colors. With CSS, you can craft both linear gradients (where colors transition side-by-side) and radial gradients (where colors transition in a circular pattern).

- **Images**: They can serve as decorative patterns, textures, or even immersive full-screen backdrops. By manipulating properties like `background-size`, `background-position`, and `background-repeat`, designers can tailor images to fit various aesthetic and functional needs.

## Positioning

Positioning elements on a web page is a fundamental task in web design. CSS provides multiple methods to achieve desired layouts and presentations.

### Core Positioning Properties

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/position">position</a>**: Determines the positioning method used for an element.
  - Values: `static`, `relative`, `absolute`, `fixed`, `sticky`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/float">float</a>**: Specifies how an element should float.
  - Options: `none`, `left`, `right`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/clear">clear</a>**: Sets which sides of an element will not be adjacent to earlier floating elements.
  - Values: `none`, `left`, `right`, `both`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/display">display</a>**: Dictates the display box type of an element.
  - Options: `inline`, `block`, `inline-block`, `table`, `table-row`, `table-cell`, `none`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/visibility">visibility</a>**: Defines if an element is visible.
  - Choices: `visible`, `hidden`, `collapse`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/overflow">overflow</a>**: Controls what happens to content that overflows its box.
  - Values: `visible`, `hidden`, `scroll`, `auto`.

#### Example

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

### Additional explanations

Position Property:
- **Static**: The default position. Elements are ordered as they appear in the HTML document.
- **Relative**: Elements are positioned relative to their normal position, but don't affect the position of adjacent elements.
- **Absolute**: Elements are positioned relative to their closest positioned ancestor. If none exists, it's relative to the initial container.
- **Fixed**: Positioned relative to the viewport. The element stays fixed even during scrolling.
- **Sticky**: A hybrid of relative and fixed. The element is treated as relative until a given scroll point, after which it acts as fixed.

Display Property:
- **Inline**: Elements are in line with adjacent elements. Respects left/right margins and padding, but not top/bottom. Width and height cannot be set.
- **Block**: Elements form a block, breaking onto a new line. They respect all margins and padding and occupy the full width by default.
- **Inline-block**: Elements are inline, but can have properties like block elements. Useful for buttons or items in a horizontal navigation.

Lastly, always remember that with the evolving nature of CSS and web design, utilizing developer tools in browsers and referencing platforms like MDN can help keep your understanding current and your designs sharp.

![Screenshot from 2022-10-11 20-46-35](https://user-images.githubusercontent.com/37275728/195174303-2330e847-fcb9-4c86-9b38-13130dd010e6.png)

## Animations and Dynamic Effects

In the digital era, motion design plays a pivotal role in enhancing user experience. CSS3, the third level of Cascading Style Sheets, offers a wide variety of animation capabilities to bring life to web elements and improve user interaction.

### Animations

CSS animations allow elements to transition between styles over a set duration and through specified keyframes. This means an element can smoothly shift from one style to another over a given time period.

#### Core Animation Properties

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation">animation</a>**: A shorthand property to set multiple animation properties at once.
  - Values: `animation-name`, `animation-duration`, `animation-timing-function`, `animation-delay`, `animation-iteration-count`, `animation-direction`, `animation-fill-mode`, and `animation-play-state`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-name">animation-name</a>**: Names the animation for reference.
  - Value type: `string` (name of the keyframes)

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-duration">animation-duration</a>**: Specifies how long the animation takes for a single cycle.
  - Value type: `time` (e.g., `2s` or `200ms`)

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function">animation-timing-function</a>**: Describes the pacing of the animation.
  - Common values: `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-delay">animation-delay</a>**: Sets a delay before the animation starts.
  - Value type: `time`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-iteration-count">animation-iteration-count</a>**: Dictates how many times the animation plays.
  - Value type: `number` or `infinite`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-direction">animation-direction</a>**: Determines the direction of the animation.
  - Values: `normal`, `reverse`, `alternate`, `alternate-reverse`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-fill-mode">animation-fill-mode</a>**: Defines what values are applied before/after the animation.
  - Values: `none`, `forwards`, `backwards`, `both`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/animation-play-state">animation-play-state</a>**: Determines whether the animation is running or paused.
  - Values: `running`, `paused`.

#### Example

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

#### Additional Insights

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

### 2D/3D Transform

In modern web design, the ability to animate and transform elements has become a staple. CSS offers a powerful suite of properties to apply 2D and 3D transformations to elements, granting designers and developers the capacity to change an element's position, size, and orientation in creative ways.

### Quick Overview

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transform">transform</a>**: Applies a 2D or 3D transformation to an element.
  - Values: `none`, `matrix`, `translate`, `translateX`, `translateY`, `translateZ`, `scale`, `scaleX`, `scaleY`, `scaleZ`, `rotate`, `rotateX`, `rotateY`, `rotateZ`, `skew`, `skewX`, `skewY`, `matrix3d`, `translate3d`, `translateX3d`, `translateY3d`, `translateZ3d`, `scale3d`, `scaleX3d`, `scaleY3d`, `scaleZ3d`, `rotate3d`, `rotateX3d`, `rotateY3d`, `rotateZ3d`, `perspective`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin">transform-origin</a>**: Defines the point around which a transformation is applied.
  - Values: `origin-x origin-y origin-z` (e.g., `50% 50%` or `center center`).

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style">transform-style</a>**: Specifies how nested elements are rendered in 3D space.
  - Values: `flat`, `preserve-3d`.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/perspective">perspective</a>**: Determines the distance between the viewer and the z=0 plane, affecting the 3D transformation.
  - Value type: `length` (e.g., `1000px`).

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/perspective-origin">perspective-origin</a>**: Establishes the origin for the perspective property.
  - Value type: `length` or percentage (e.g., `50% 50%`).

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility">backface-visibility</a>**: Defines whether the back face of an element is visible when it's turned towards the viewer.
  - Values: `visible`, `hidden`.
    
#### Example

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

#### Additional Insights

1. **Transformations**: These operations include moving (`translate`), scaling (`scale`), rotating (`rotate`), and skewing (`skew`). These can be applied in both 2D and 3D space. For instance, `rotateX` will revolve the element around its X-axis in 3D space.

2. **Origin of Transformation**: By default, transformations occur around the center of an element. However, with `transform-origin`, you can change this pivot point. This is especially useful when you want an element to rotate around its corner or any other specific point.

3. **3D Space**: When dealing with 3D transformations, `transform-style` and `perspective` come into play. The former allows child elements to be positioned in 3D space, and the latter gives a sense of depth.

4. **Visibility**: With `backface-visibility`, you can control the visibility of the reverse side of an element in 3D space. This can be helpful when you don't want the back of a flipped card, for example, to be shown.

### Transition

Transitions in CSS provide a way to control animation speed when changing CSS properties. Instead of having property changes take effect instantly, you can cause the changes to take place over a period of time. This makes for a smoother visual experience and can add a touch of dynamism to web designs.

### Quick Overview

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition">transition</a>**: A shorthand property for setting `transition-property`, `transition-duration`, `transition-timing-function`, and `transition-delay`.
  - Values: `[ transition-property | transition-duration | transition-timing-function | transition-delay ]`

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property">transition-property</a>**: Specifies the name of the CSS property to which the transition is applied.
  - Values: `none`, `all`, or specific property names (e.g., `opacity`, `transform`).

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration">transition-duration</a>**: Defines the duration over which transitions should occur.
  - Value type: `time` (e.g., `0.5s` or `300ms`).

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function">transition-timing-function</a>**: Describes how the intermediate values used during a transition will be calculated.
  - Values: `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out`, cubic-bezier values.

- **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay">transition-delay</a>**: Specifies when the transition will start.
  - Value type: `time` (e.g., `0.2s`).

#### Example

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

#### Additional Insights

1. **Transition Properties**: By default, transitions apply to all properties (`all`). However, in most cases, you'll want to specify which property to animate, like `opacity` or `background-color`.

2. **Duration**: This determines how long the transition will take. Longer durations can make transitions more noticeable, while shorter ones can give a snappy feeling to user interactions.

3. **Timing Function**: This function describes the acceleration curve of the transition, allowing for the effect to speed up, slow down, or smoothly glide into place. The `cubic-bezier` value can be used to create custom timing functions.

4. **Delay**: If you want to start a transition after a certain period, use the `transition-delay` property. This can be useful in sequences where multiple elements animate one after the other.

## Responsive Design

Responsive design ensures that websites adapt and render optimally across a variety of devices. It aims to offer a consistent user experience from the smallest mobile device to the largest desktop monitor.

### Responsive Grid vs. Fluid Grid

- **Responsive Grid**: This approach utilizes a fixed grid system, usually based on a 12-column structure, with specific breakpoints defined in pixels to cater to different screen sizes. Once the viewport reaches a predefined size, the design might switch to a different column arrangement or even hide/show certain elements.

- **Fluid Grid**: Fluid grids are more flexible than responsive grids. They use percentages to define widths, thereby allowing elements to continually adjust in size relative to their parent container. As the viewport size changes, elements stretch and shrink fluidly.

### Recommended Number of Columns:

- **Desktop**: 12 columns
- **Tablet**: 8 columns
- **Mobile**: 4 columns

### Mobile First Design

Adopting a **Mobile First** design strategy means building the initial design for the smallest screens (mobile devices) and then progressively enhancing the design for larger screens. This methodology ensures that mobile users receive only the essential features and content, helping improve performance and user experience on slower networks.

### Media Queries

Media queries are the backbone of responsive design. They allow developers to apply styles based on the device characteristics. For instance, different styles can be applied depending on the device's screen width, height, orientation, and more.

#### Example

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

#### Key Points:

1. **<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/@media">@media</a>**: The heart of media queries in CSS.
   - Examples of common usages: `screen`, `print`, `all`, `min-width`, `max-width`, `orientation: portrait`, `orientation: landscape`.

#### Additional Insights:

- **Overlapping Styles**: It's crucial to be mindful of the cascading nature of CSS. When using the same selector in multiple places within a stylesheet, any styles defined later will override those defined earlier. This can be particularly relevant when using media queries, as styles can unintentionally override one another based on their order in the CSS file.

- **Viewport Meta Tag**: To ensure that responsive designs are displayed correctly, especially on mobile devices, it's essential to include the viewport meta tag in the HTML head. For instance: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.

- **Flexbox & Grid**: Modern CSS techniques like Flexbox and Grid layout provide powerful tools to create responsive layouts with more control and less reliance on traditional grid systems.

- **Testing**: Regularly testing the design on various devices and screen sizes is vital. Tools like browser developer tools and specialized software can simulate different devices and help in identifying any issues in the design.

## Units

Units in CSS provide a way to express measurements. Understanding when and how to use different units is crucial for designing responsive and accessible websites.

### Absolute Units

These are fixed-size units and do not scale with changes in other properties or viewer's settings.

* <code>px</code>: Pixels – A dot on the computer screen. It's a relative measurement in the sense that it's not a consistent size across devices, but within a device, it is absolute.
* <code>pt</code>: Points – Traditionally used in print media (1pt = 1/72 of an inch).
* <code>pc</code>: Picas – Another print measure where 1pc = 12 points.
* <code>cm</code>: Centimeters.
* <code>mm</code>: Millimeters.
* <code>in</code>: Inches – 1 inch is equal to 2.54 centimeters.
* <code>%</code>: Percentage – Relative to the parent element or another reference point.

### Relative Units

Relative units are responsive and adapt based on the context in which they're used.

* <code>em</code>: Font size of the current element. If the font size is 16px, then "2em" is 32px.
* <code>rem</code>: Font size of the root element (usually the `<html>` element). A consistent unit regardless of the nesting level.
* <code>ch</code>: Width of the '0' character of the current font.
* <code>ex</code>: x-height of the current font. Roughly the height of lowercase letters in most fonts.
* <code>vh</code>: 1% of the height of the viewport window.
* <code>vw</code>: 1% of the width of the viewport window.
* <code>vmin</code>: 1% of the viewport's smaller dimension (height or width).
* <code>vmax</code>: 1% of the viewport's larger dimension (height or width).

### Further Insights

- **Using `em` and `rem`**: These units are especially helpful for building scalable and accessible websites. They allow the design to respond to user preferences, like increasing the default font size in a browser.
  
- **Viewport Units**: `vh`, `vw`, `vmin`, and `vmax` are great for creating fully responsive designs that adjust based on the size of the user's screen.

- **Legacy Units**: Units like `pt` and `pc` are derived from the print industry and are less commonly used in modern web design but can still be found in designs intended for print.

- **Choosing Units**: When designing, it's crucial to pick the right unit for the job. For typography, relative units like `em` or `rem` are often recommended. For layout dimensions, `px`, `%`, and viewport units are commonly used.

## Best Practices

### General

* Use external CSS files and place them within the `<head>` tag.
* Organize your CSS into logical sections and use comments to explain complex or important parts.
* Follow a consistent naming convention for class and ID names.
* Use shorthand properties when possible to reduce code length.

### Formatting

* Don't leave out the last semicolon in a CSS block.
* Maintain consistent casing, preferably lowercase, for selector names.
* Use a single space after the colon in property-value pairs.
* Use a new line for each declaration in a rule set.
* Remove trailing white spaces and keep indentation consistent.

### Layout and Positioning

* Use the box model consistently throughout the document.
* Avoid breaking the flow by using absolute positioning sparingly.
* Utilize Flexbox and Grid for modern, responsive layouts.
* Avoid using fixed pixel values for layout and spacing; use relative units like `rem`, `em`, and percentages.

### Selectors and Specificity

* Prefer classes over selectors that are tightly coupled to the DOM.
* Reduce the usage of IDs to avoid high specificity conflicts.
* Minimize the use of overly complex or deeply nested selectors.
* Keep selector specificity low to make styles easier to override and maintain.

### Inheritance and Efficiency

* Don't duplicate style declarations that can be inherited from parent elements.
* Use unitless values when possible, or `rem` for relative units.
* Use the hexadecimal format for colors, or use CSS variables for consistent theming.
* Minimize the use of vendor prefixes by leveraging tools like Autoprefixer.

### Responsiveness and Accessibility

* Design your CSS with responsiveness in mind, using media queries to adapt to various screen sizes and devices.
* Prioritize readability and usability in your designs.
* Use appropriate color contrasts to ensure legibility for all users.
* Include alternative text and labels for interactive elements to improve accessibility.

### Performance and Optimization

* Minify your CSS files to reduce file size and improve load times.
* Use CSS properties like `transform` and `opacity` for animations and transitions that leverage hardware acceleration.
* Optimize images and other assets used as background images or within your styles.
* Utilize browser caching to improve page load times for returning visitors.

## Links

- [Official Website](https://www.w3.org/Style/CSS/)
- [Isobar Front-end Code Standards](http://isobar-idev.github.io/code-standards/)
- [HTML Best Practices](https://github.com/hail2u/html-best-practices)
- [Writing Your Best Code](http://learn.shayhowe.com/html-css/writing-your-best-code/)
- [Web Accessibility Best Practices](https://www.webaccessibility.com/best_practices.php)
- [CleanCSS Formatter](https://www.cleancss.com/css-beautify/)
