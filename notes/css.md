<h1>What is CSS?</h1>

* Cascading Style Stylesheet
* The "adjectives" of the web
* Takes the boring, ugly HTML and makes it looks like we want.

Stylesheets allow us to include predefined styles and reuse them across HTML documents
they may be included from predefined libraries (e.g. _Bootstrap_) or created manually

## Inclusion

example:

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/picnic"
/>
```

usually in the _head_ of a document

## CSS Libraries

CSS Libraries:

- _Picnic CSS_: simple CSS library, doesn't use JavaScript - [website](https://picnicss.com/), [CDN](https://cdn.jsdelivr.net/npm/picnic)
- _Bootstrap_: widely used CSS library with many themes - [website](https://getbootstrap.com/), [CDN for CSS](https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.css), [CDN for JS](https://cdn.jsdelivr.net/npm/bootstrap/dist/js/bootstrap.js)
- _Semantic UI_ - [website](https://semantic-ui.com), [CDN for CSS](https://cdn.jsdelivr.net/npm/semantic-ui/dist/semantic.css), [CDN for JS](https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.js)
- _Foundation_ - [website](https://get.foundation/sites/docs/), [CDN for CSS](https://cdn.jsdelivr.net/npm/foundation-sites/dist/css/foundation.css), [CDN for JS](https://cdn.jsdelivr.net/npm/foundation-sites/dist/js/foundation.js)
- _Tailwind_ - [website](https://tailwindcss.com/), [CDN](https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css)


<h1>The basic rule</h1>

selector {
 property_a: value;
 property_b: value;
}

<h1>Three ways to add css to html</h1>

<h1>Backgrounds</h1> 

Example with multiple pargraphs grouped by one div. And div has different background to p in css.

You can put image in url.

body{
 background: url(...);
 background-repeat: no-repeat;
 background-size: cover;
}

<h2>background</h2>

* background-image
* background-position
* background-size 
* background-repeat 
* background-attachment 
* background-origin 
* background-clip 
* background-color 

<h2>background-size</h2> 

* length 
* %
* auto | cover | contain

<h2>background-repeat</h2> 

* repeat | repeat-x | repeat-y | no-repeat 

<h2>background-attachment </h2>

* scroll | fixed | local 

<h2>background-image </h2>

* url | Gradients | none 

<h2>background-origin</h2> 

* border-box | padding-box | content-box 

<h2>background-position</h2>

* top left | top center | top right 
* center left | center center | center right 
* bottom left | bottom center | bottom right 
* x-% | y-%
* x-pos | y-pos

<h2>background-clip</h2>

* border-box | padding-box | content-box | no-clip

<h2>background-color</h2>

* color | transparent

<h1>Border </h1>
<h2>border</h2>

* border-width 
* border-style 
* border-color 

<h2>border-width</h2>

* thin | medium | thick | length 

<h2>border-style</h2>

* none | hidden | dotted 
* dashed | solid | double
* groove | ridge | inset | outset 

<h2>border-color</h2>

* color 

<h2>border-left</h2>

* border-left-width 
* border-style 
* border-color 

<h2>border-left-style</h2>

* border-style 

<h2>border-left-color</h2>

* border-color 

<h2>border-left-width</h2>

* this | medium | thick | length 

<h2>border-collapse</h2> 

* collapse | separate 

<h2>border-break</h2>

* border-width 
* border-style 
* color close 

<h2>box-shadow</h2>

* inset || \[ length, length, length, length || <color> ] 
* none 

<h2>border-image</h2>

* image 
* \[ number / border-width stretch | repeat round ] 
* none 

<h2>border-radius</h2> 

* border-radius
* border-bottom-right-radius
* border-bottom-left-radius 
* border-top-left-radius 

<h1>Box Model </h1>

 p {
 
  /* Content Area */
 width: 50%;
 
 /*Padding Area */
 padding: 20;
 
  /*Border Area */
 border: solid red 10px;
 
 /* Margin Area */
 margin: 10px 30px 20px 50px;

 }

<h2>float </h2>

* left 
* right 
* none 

<h2>height</h2> 

* auto | length 

<h2>max-height </h2> 

* none | length 

<h2>min-height</h2> 

* none | length 

<h2> width</h2>

* auto | length 

<h2>max-width </h2> 

* none | length 

<h2>min-width </h2>

* none | length 

<h2>margin</h2>

* margin-top 
* margin-right 
* margin-bottom 
* margin-left 

<h2>margin-top</h2>

* auto | length 

<h2>margin-bottom </h2>
* auto | length 

<h2>margin-left</h2>

* auto | height 

<h2>margin-right</h2>

* auto | height 

<h2>padding</h2>

* padding-top 
* padding-right 
* padding-bottom 
* padding-left 

<h2>display</h2> 

* none | inline | block 
* inline-block | list-item | run-in 
* compact table | inline-table | table-row-group 
* table-header-group | table-footer-group 
* table-row | table-column-group | table-column 
* table-cell | table-caption 
* ruby | ruby-base | ruby-text | ruby-base-group | ruby-text-group
* inline-flex | inline-grid | contents 

<h2>overflow</h2>

* visible | hidden | scroll
* auto | no-display | no-content 
* overflow-x
* overflow-y 

<h2>overflow-style</h2> 

* auto | marquee-line | marqueeblock 

<h2>overflow-x</h2>

* visible | hidden | scroll | auto | no-display | no-content 

<h2>rotation</h2>

* angle 

<h2>rotation-point</h2>

* position (paired value off-set) 

<h2>visibility</h2>

* visible | hidden | collapse 

<h2>clear</h2> 

* left | right | both | none 

 <h1>Flexbox</h1>
 
 Flexbox by defualt will shrink thigns down to make them fit on the screen.
 
 https://css-tricks.com/snippets/css/a-guide-to-flexbox/
 
 
 <body>
  <div class="container">
   <div class="flex-item" id="flex-item-1"></div>
   <div class="flex-item" id="flex-item-2"></div>
   <div class="flex-item" id="flex-item-3"></div>
  </div>
 </body>
 
 .container {
 display: flex;
 flex-direction: row;
 wrap: nowrap;
 justify-content: center;
}
 
 .flex_Item {
  height: 100px;
  width: 100px;
 }
 
<h1>Font </h1>

 List of many fonts:
 
 https://www.cssfontstack.com/
 
 To add your own fonts use:
 
 https://fonts.google.com/
 
 1. Search for font.
 2. Copy generate link to head of your html file.
 3. Use font name in css.
 
 body {
  font-size: 16px;
}
 
 p {
 font-family: Helvetica;
 font-size: 1em;
 line-height: 2;
}
 
 .bigger {
 font-size: 2em;
  font-weight: bold;

}
 
<h2>font</h2> 

* font-style
* font-variant
* font-weight
* font-size/line-height
* font-family
* caption | icon | menu | messagebox
* small-caption | status-bar

<h2>font-style</h2> 

* normal | italic | oblique | inherit

<h2>font-variant</h2>

* normal | small-caps | inherit

<h2>font-size</h2>

* xx-small | x-small | small
* medium | large | x-large | xxlarge 
* smaller | larger
* inherit
* length 
* %

<h2>font-size-adjust</h2>

* none | number

<h2>font-family</h2> 

* serif | sans-serif | monospace | cursive
* fantasy | system-ui | emoji | math | fangsong
* inherit | initial | unset

<h2>font-weight </h2> 

* normal | bold | bolder | lighter 
* 100 | 200 | 300 | 400 | 500 
* 600 | 700 | 800 | 900 | inherit 

<h1>Text</h1>

<h2>direction</h2>

* ltr | rtl | inherit 

<h2>hanging-punctuation</h2>

* none | [ start | end | endedge ] 

<h2>letter-spacing</h2> 

* normal
* length
* %

<h2>text-decoration</h2>  

* none | underline | overline
* line-thorugh | blink 

<h2>text-shadow</h2>

* none
* color
* length 

<h2>word-break</h2>

* normal | keep-all | loose 
* break-strict | break-all

<h2>text-outline</h2>

* none
* color

<h2> word-wrap </h2> 

* normal 
* nowrap 

<h2>unicode-bidi</h2>

* normal | embed | bidi-override 

<h2>text-emphasis</h2>

* none [ [ accent | dot | circle
* disc | [ before | after ]?]

<h2>text-indent</h2>

* length
* %

<h2>white-space-collapse</h2> 

* perserve | collapse | pre-servebreaks | discard 

<h2>text-justify</h2>

* auto | inter-word | interideograph 
* punctuation-trim | inter-cluster 
* distribute | kashida | tibetan

<h2>text-transform</h2>

* none | capitalize | uppercase | lowercase

<h2>text-wrap</h2> 

* normal | unresrricted | none | suppress

<h2>word-spacing</h2>

* normal
* length
* %

<h1>Column </h1>

<h2>column-count</h2>

* auto 
* number 

<h2>columns</h2>

* column-width
* column-count

<h2>column-fill</h2>  

* auto | balance  

<h2>column-gap </h2>

* normal
* length


<h2>column-rule </h2>

* column-rule-width  
* column-rule-style
* column-rule-color 

<h2>column-rule-style</h2>

* border-style </h2>

<h2>column-rule-width  </h2>

* thin | medium | thick | length 

<h2>column-width</h2>

* auto
* length

<h2>column-span </h2>

* 1 | all 

<h1>Colors</h1>

<h2>color</h2>

* inherit  
* color  

<h2>opacity</h2>

* inherit 
* number

<h1>Table</h1>

<h2>table-layout </h2>

* auto | fixed 

<h2>caption-side</h2>

* top | bottom | left | right 

<h2>empty-cells </h2>

* show | hide 

<h2>border-spacing</h2>

* length 

<h2>border-collapse </h2>

* collapse | separate 

<h1>List & Markers </h1>

<h2>list-style</h2> 

* list-style-image 
* list-style-type  
* list-style-position  

<h2>list-style-image</h2>

* none
* url

<h2>marker-offset</h2> 

* auto
* length


<h2>list-style-type</h2>  
 
* none | asterisks | box | check circle | diamond | disc | hyphen
* square decimal | decimalleading-zero | lower-roman | upper-roman
* lower-alpha | upper-alpha I lower-greek | lower-latin 
* upper-latin | hebrew | armenian | georgian | cjk-ideographic 
* hiragana | katakana | hiragana-iroha | katakana-iroha | footnotes 

<h1>Animations</h1> 
<h2>animations</h2>

* animation-name
* animation-duration
* animation-timing-function 
* animation-delay
* animation-direction 
* animation-iteration-count

<h2>animation-delay</h2>

* time

<h2>animation-timing-function</h2>

* ease | linear ease-in | easeout | ease-in-out 
* cubic-Bezier (number, number, number, number) 
  
<h2>animation-name</h2>

* none | IDENT 
  
<h2>animation-iteration-count</h2>

* inherit 
* number 
  
<h2>animation-duration</h2>

* time

<h2>animation-direction</h2> 

* nonrmal | alternate 
  
<h2>animation-play-state</h2>

* running | paused

<h1>Transitions </h1>

<h2>transitions</h2>

* transitions-property 
* transitions-duration
* transitions-timing-function 
* transitions-delay
 
<h2>transitions-property</h2>

* none | all

<h2>transition-timing-function</h2>

* ease linear | ease-in | ease-out | ease-in-out
* cubicBezier(number, number, number, number) 

<h2>transitions-delay</h2> 

* time 

<h2>transitions-duration </h2>

* time 

<h1>UI </h1>

<h2>appearance</h2>

* normal | inherit | \[icon | window | desktop 
* work-space | document | tooltip | dialog
* button | push-button | hyperlink | radio-button
* checkbox | menu-item | tab | menu | menubar 
* pull-down-menu | pop-up-menu | list-menu
* radio-group | checkbox-group | outline-tree
* range | field | combo-box | signature | password]
 
<h2>cursor</h2>

* auto | crosshair | default | pointer | move
* e-resize | neresize | nw-resize | n-resize 
* se-resize | sw-resize | swresize | s-resize 
* w-resize | text | wait | help | url
 
 <h2>icon</h2>
 
 * auto | inherit
 * url
 
 <h2>nav-index</h2>
 
* normal | inherit
* number

<h2>nav-up</h2>

* auto inherit <id> \[current root | <target-name>]
 
<h2>nav-down</h2>
 
* auto inherit <id> \[current root | <target-name>]
 
<h2>nav-right</h2>
 
* auto inherit <id> \[current root | <target-name>]
  
<h2>nav-left</h2>
 
* auto inherit <id> \[current root | <target-name>]
 
<h2>resize </h2>

* none | both | horizontal | vertical | inherit 
 
<h1>Pseudo-class</h1>

* <i>:active</i> an activated element 
* <i>:focus</i> an element while the element has focus 
* <i>:hover</i> an element when you mouse over it 
* <i>:link</i> an unvisited link
* <i>:disabled</i> an element while the element is disabled
* <i>:enabled</i> an element while the element is enabled
* <i>:checked</i> an element that is checked
* <i>:selection</i> an element that is currently selected or highlighted by the user
* <i>:lang</i> allows the author to specify a language to use in a specified element
* <i>:nth-child(n)</i> an element that is the n-th sibling
* <i>:nth-last-child(n)</i> an element that is the n-th sibling counting from the last sibling 
* <i>:first-child</i> an element that is the first sibling
* <i>:last-child</i> an element that is the last sibling
* <i>:only-child</i> an element that is the only child
* <i>:nth-of-type(n)</i> an element that is the n-th sibling of its type
* <i>:nth-last-of-type(n)</i> an element that is the n-th sibling of its type counting from the last sibling 
* <i>:last-of-type</i> an element that is the last sibling of its type
* <i>:first-of-type</i> an element that is the first sibling of its type
* <i>:only-of-type</i> an element that is the only child of its type
* <i>:empty</i> an element that has no children
* <i>:root</i> root element within the document
* <i>:not(x)</i> an element not represented by the argument 'x'
* <i>:target</i> a target element as specified by a target a UR 

<h1>Pseudo-element</h1>
 
* <i>::first-letter</i> Adds special style to the first letter of a text
* <i>::first-line</i> Adds special style to the first line of a text
* <i>::before</i> Inserts some content before the content of an element
* <i>::after</i> Inserts some content after the content of an element 
 
<h1>Absolute Measurement</h1> 

* <i>%</i> percentage 
* <i>cm</i> centimeter 
* <i>in</i> inch 
* <i>mm</i> millimeter 
* <i>pc</i> pica (lp = 12 points) 
* <i>pt</i> point (lpt 1/72 inch) 
* <i>px</i> pixels 

<h1>Relative Measurement</h1>
 
* <i>ch</i> width of the '0' glyph found in the font for the font size used to render
* <i>em</i> 1em = current font size of current element
* <i>ex</i> x-height of the element's font 
* <i>gd</i> the grid defined by 'layout-grid' 
* <i>rem</i> the font size of the root element
* <i>vh</i> the viewport's height 
* <i>vw</i> the viewport's width
 
<h1>Colors</h1> 
 
* <i>color name</i> red, blue, green, dark green 
* <i>rgb(x,y,z)</i> red = rgb(255,0,0) 
* <i>rgb(x%,y%,z%)</i> red = rgb(100%,0,0) 
* <i>rgb(x,y,z,alpha)</i> red = rgb(255,0,0,0) 
* <i>#rrggbb</i> red = #ff0000 (or shorthand - #f00)

<h1>Selector Types </h1>

/* Element */

h1 {
	color: green;
}


/* ID */

#header_1 {
	color: red;
}

#header_2 {
	color: blue;
}


/* Class */

h1 {
	color: green;
}


/* Universal */

* {
	font: 10px Arial;
}


/* Child */

#gallery>p {
	font-weight: bold;
}


/* Descendant */

#gallery p {
	color: white;
}

 
<h1>Inheritance and Specificity</h1>
id's > classes, attributes, pseudo-classe > elements, pseudo-elements

https://specificity.keegan.st/
	

## Media queries

possibility to query the screen size and orientation (amongst others)

## Media queries

```css
.menu {
  display: flex;
  flex-direction: column;
}

@media (min-width: 800px) {
  .menu {
    flex-direction: row;
  }
}
```

## Media queries

```css
@media (orientation: landscape) {
  .layout {
    flex-direction: row;
  }
}
```

# Transformations

## Transformations

```css
#element1 {
  transform: translsate(100px, 0);
}
```

## Transformations

```css
#element2 {
  transform: translate(100px, 0) rotate(45deg);
  transform-origin: 0 0;
}
```

element will be rotated by 45 degrees first, then translated to the right by 100 pixels

center of rotation: top left corner of the element
	
# Transitions

## Transitions

the change of some CSS properties can be animated:

```css
#animated {
  transition: background-color: 3s, margin-top: 1s;
}
```

## Example: transition on hover

```css
div.box {
  width: 40px;
  height: 40px;
  background-color: blue;
  transform: rotate(0);
  transition: transform 9s, background-color 9s;
}
div.box:hover {
  background-color: red;
  transform: rotate(360deg) scale(2);
  transition: transform 0.5s, background-color 0.5s;
}
```

## Example: game

```css
div {
  width: 40px;
  height: 40px;
  background-color: blue;
  transform: translate(0, 0) rotate(0);
  transition: transform 9s, background-color 9s;
}
div:hover {
  background-color: red;
  transform: translate(200px, 0) rotate(360deg);
  transition: transform 3s, background-color 3s;
}
```

## Task: dropdown

Dropdown that becomes active on button click

HTML template:

```html
<div id="dropdown">dropdown</div>
<button
  id="dropdown-button"
  onclick="dropdown.className = 'active'"
>
  menu
</button>
```

## Task: overlay on hover

## Task: Animating spoon and fork

<figure style="width: 50%; margin: 0 auto">
  <img src="assets/spoon-fork-animated.svg" />
</figure>

Note: we are using CSS transformations, not SVG transformations; we must set `transform-origin` separately

