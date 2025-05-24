#### Q. Which CSS property is used to change the text color of an element?

* [ ] `font-color`
* [ ] `text-style`
* [x] `color`
* [ ] `text-color`
* [ ] `foreground`

#### Q. In SCSS, how do you declare a variable?

* [ ] `@var primary-color: #333;`
* [x] `$primary-color: #333;`
* [ ] `--primary-color: #333;`
* [ ] `@primary-color: #333;`
* [ ] `%primary-color: #333;`

#### Q. Which directive lets you import partials in SCSS?

* [ ] `@use 'reset';`
* [ ] `@import-partial 'buttons';`
* [x] `@import 'buttons';`
* [ ] `@include 'buttons';`
* [ ] `@forward 'buttons';`

#### Q. How do you define a mixin in SCSS?

* [ ] `@mixin button { … }`
* [x] `@mixin button { … }`
* [ ] `$mixin button { … }`
* [ ] `%button { … }`
* [ ] `@include button { … }`

#### Q. To include a mixin called `button`, you write:

* [ ] `@import button;`
* [x] `@include button;`
* [ ] `@use button;`
* [ ] `@extend button;`
* [ ] `@mixin button;`

#### Q. What placeholder selector lets you share styles without generating a class in the output CSS?

* [ ] `%shared`
* [x] `%shared`
* [ ] `.shared--placeholder`
* [ ] `@placeholder shared`
* [ ] `&shared`

#### Q. How do you extend a selector in SCSS to inherit its styles?

* [ ] `@mixin .btn;`
* [ ] `@include .btn;`
* [x] `@extend .btn;`
* [ ] `$extend: .btn;`
* [ ] `%btn;`

#### Q. Which control directive lets you loop a block of styles over a list?

* [ ] `@while`
* [ ] `@if`
* [x] `@each`
* [ ] `@for`
* [ ] `@map`

#### Q. How do you write a 1–3 index for a loop in SCSS?

* [ ] `@each $i from 1 through 3 { … }`
* [ ] `@for $i in 1..3 { … }`
* [x] `@for $i from 1 through 3 { … }`
* [ ] `@while $i &lt; 4 { … }`
* [ ] `@loop $i { … }`

#### Q. What function returns the value associated with a key in a SCSS map?

* [ ] `map-get($map, $key)`
* [x] `map-get($map, $key)`
* [ ] `get-map($map, $key)`
* [ ] `map($map, $key)`
* [ ] `lookup($map, $key)`

#### Q. In SCSS, how do you merge two maps?

* [ ] `map-merge($map1 $map2)`
* [x] `map-merge($map1, $map2)`
* [ ] `merge-maps($map1, $map2)`
* [ ] `$map1 + $map2`
* [ ] `map-concat($map1, $map2)`

#### Q. Which Sass function darkens a color by 20%?

* [ ] `shade($color, 20%)`
* [ ] `adjust-hue($color, -20%)`
* [x] `darken($color, 20%)`
* [ ] `desaturate($color, 20%)`
* [ ] `mix($color, black, 20%)`

#### Q. How do you nest rules for `.card` inside `.container`?

* [ ] `.container .card { … }`
* [ ] `& .card { … }` inside `.container`
* [x] `.container { .card { … } }`
* [ ] `%container { .card { … } }`
* [ ] `@nest .card within .container { … }`

#### Q. In Less, how do you declare a variable?

* [ ] `$primary: #fff;`
* [ ] `@primary-color: #fff;`
* [x] `@primary-color: #fff;`
* [ ] `--primary: #fff;`
* [ ] `%primary: #fff;`

#### Q. How do you import other Less files?

* [ ] `@use 'mixins.less';`
* [x] `@import 'mixins.less';`
* [ ] `@include 'mixins.less';`
* [ ] `@extend 'mixins.less';`
* [ ] `@require 'mixins.less';`

#### Q. Which Less feature allows parameterized mixins?

* [ ] Loops
* [ ] Guards
* [x] Mixins with arguments
* [ ] Functions
* [ ] Placeholders

#### Q. How do you apply a mixin named `center()` in Less?

* [ ] `.center();`
* [ ] `@include center();`
* [x] `.center();`
* [ ] `center();`
* [ ] `@center();`

#### Q. What does the following Less guard do? `.rounded(@radius) when (@radius &gt; 0) { border-radius: @radius;}`

* [ ] Always applies the mixin
* [x] Applies only if `@radius` is greater than 0
* [ ] Applies only if `@radius` is less than 0
* [ ] Applies only if `@radius` equals 0
* [ ] Ignores the mixin

#### Q. Which Less function converts a hex to RGB?

* [ ] `to-rgb(#fff)`
* [x] `rgb(255, 255, 255)` returns the string, but to extract channels you use `red()`, `green()`, `blue()`
* [ ] `hex2rgb(#fff)`
* [ ] `color-rgb(#fff)`
* [ ] `rgba(#fff)`

#### Q. Which class adds horizontal gutters of 0 for a row?

* [ ] `.g-0x`
* [ ] `.gx-none`
* [x] `.gx-0`
* [ ] `.gutter-0`
* [ ] `.no-gutters`

#### Q. How do you enable the offcanvas component via data attributes?

* [ ] `data-bs-toggle="drawer"`
* [ ] `data-bs-target="#offcanvas"`
* [ ] `data-bs-show="offcanvas"`
* [x] `data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample"`
* [ ] `data-offcanvas="true"`

#### Q. Which utility lets you control the alignment of flex items along the main axis?

* [ ] `.align-content-*`
* [ ] `.justify-items-*`
* [x] `.justify-content-*`
* [ ] `.align-self-*`
* [ ] `.flex-main-*`

#### Q. To create a responsive embed for a 16:9 video, which class wrapper do you use?

* [ ] `.embed-responsive-16by9`
* [ ] `.ratio-responsive-16x9`
* [x] `.ratio ratio-16x9`
* [ ] `.embed-responsive embed-responsive-16by9`
* [ ] `.video-responsive-16by9`

#### Q. How can you change the global `$font-family-base` in Bootstrap’s Sass?

* [ ] Override it in `custom.scss` after importing Bootstrap
* [x] Override it before `@import "bootstrap"` in your Sass entry file
* [ ] Use CSS custom properties at runtime
* [ ] Pass a JS config object to `bootstrap.bundle.js`
* [ ] Edit it directly in `_variables.scss`

#### Q. Which class applies a border-radius only on the top corners?

* [ ] `.rounded-top-sm`
* [x] `.rounded-top`
* [ ] `.rounded-corners-top`
* [ ] `.border-top-rounded`
* [ ] `.rtop`

#### Q. What utility class makes an element sticky at the top of its container?

* [ ] `.position-fixed-top`
* [ ] `.sticky`
* [x] `.sticky-top`
* [ ] `.fixed-top`
* [ ] `.position-sticky`

#### Q. Which breakpoint suffix targets screens smaller than the small (sm) breakpoint?

* [ ] `-xs`
* [ ] `-tiny`
* [x] There is no “xs” suffix in Bootstrap 5; use unprefixed `.col-*` for extra-small
* [ ] `-mobile`
* [ ] `-sm-down`

#### Q. How do you include Bootstrap’s JavaScript without any dependencies?

* [ ] Use `bootstrap.min.js` only
* [ ] Use `popper-free.js` build
* [x] Use the `bootstrap.bundle.min.js` (it includes Popper)
* [ ] Use CDN with `data-bs-no-deps`
* [ ] Use ES module import without Popper

#### Q. Which class toggles dark mode utilities in Bootstrap?

* [ ] `.theme-dark`
* [ ] `.mode-dark`
* [x] Add `data-bs-theme="dark"` on `&lt;html&gt;` or `&lt;body&gt;`
* [ ] `.dark-mode`
* [ ] `.bg-dark-mode`

#### Q. To adjust the gutter width globally in Sass, which variable do you override?

* [ ] `$gutter-width`
* [ ] `$grid-gap`
* [x] `$grid-gutter-width`
* [ ] `$row-gutter`
* [ ] `$container-gutter`

#### Q. Which utility class adds a smooth scroll behavior to the document?

* [ ] `.scroll-smooth`
* [ ] `.smooth-scroll`
* [x] `html { scroll-behavior: smooth; }` (Bootstrap doesn’t provide a specific class)
* [ ] `.bs-scroll-smooth`
* [ ] `.smooth.bs`

#### Q. In Bootstrap 5, which class creates a responsive fixed-width container that adapts at each breakpoint?

* [ ] `.container-fluid`
* [x] `.container`
* [ ] `.container-responsive`
* [ ] `.container-fixed`
* [ ] `.container-sm`

#### Q. How do you define a column that spans 6 of 12 grid columns on medium screens and above, but full width on smaller screens?

* [ ] `.col-6 col-md-12`
* [ ] `.col-md-6 col-sm-12`
* [x] `.col-12 col-md-6`
* [ ] `.col-sm-6 col-md-12`
* [ ] `.col-lg-6 col-12`

#### Q. Which utility class adds horizontal margin auto to center a block element?

* [ ] `.mx-auto-left`
* [ ] `.m-auto`
* [x] `.mx-auto`
* [ ] `.auto-margin`
* [ ] `.mx-center`

#### Q. What data attribute triggers a Bootstrap modal to open when clicked?

* [ ] `data-bs-toggle="dialog"`
* [x] `data-bs-toggle="modal"`
* [ ] `data-toggle="modal"`
* [ ] `data-target="#modal"`
* [ ] `data-bs-show="modal"`

#### Q. Which Sass map in Bootstrap’s source holds the default theme colors?

* [ ] `$theme-colors`
* [x] `$theme-colors`
* [ ] `$colors`
* [ ] `$brand-colors`
* [ ] `$palette`

#### Q. How do you disable a Bootstrap button via HTML?

* [ ] `&lt;button class="btn btn-primary" disabled="false"&gt;`
* [ ] `&lt;button class="btn btn-primary" data-disabled&gt;`
* [x] `&lt;button class="btn btn-primary" disabled&gt;`
* [ ] `&lt;button class="btn btn-primary" disabled="true"&gt;`
* [ ] `&lt;button class="btn btn-primary" .disabled&gt;`

#### Q. Which breakpoint shorthand applies styles only on large screens and up?

* [ ] `@media (min-width: 576px)`
* [ ] `@media (min-width: 992px) and (max-width: 1199px)`
* [x] `@media (min-width: 992px)`
* [ ] `@media (min-width: 1200px)`
* [ ] `@media (max-width: 992px)`

#### Q. For a responsive navbar that collapses on small screens, which classes are essential?

* [ ] `.navbar .navbar-expand`
* [ ] `.navbar .navbar-toggle`
* [x] `.navbar .navbar-expand-lg .navbar-collapse`
* [ ] `.navbar .navbar-responsive`
* [ ] `.navbar .navbar-mobile`

#### Q. How can you override Bootstrap variables without modifying its source files?

* [ ] Edit `_variables.scss` directly
* [ ] Use inline style attributes
* [x] Create a custom Sass file that defines your variables before importing Bootstrap
* [ ] Use CSS overrides after Bootstrap’s CSS
* [ ] Use JavaScript to change styles at runtime

#### Q. Which utility class in Bootstrap v5 toggles text wrapping in flex items?

* [ ] `.text-nowrap`
* [ ] `.flex-wrap`
* [x] `.flex-nowrap`
* [ ] `.nowrap`
* [ ] `.d-flex-nowrap`

#### Q. What’s the purpose of the `.order-md-1` class in Bootstrap’s grid?

* [ ] Sets the order to 1 only on extra-small screens
* [ ] Resets default order on all breakpoints
* [x] Assigns order 1 on medium screens and up
* [ ] Aligns the first child only on medium screens
* [ ] Hides the element on medium screens

#### Q. Which JavaScript plugin must you include for Bootstrap’s dropdowns to work?

* [ ] `bootstrap.bundle.js`
* [ ] `popper.js` only
* [x] `bootstrap.bundle.js` (includes Popper)
* [ ] `bootstrap.js` only
* [ ] No JS required

#### Q. How do you space an element with 3 units of padding on all sides?

* [ ] `.p-3x`
* [ ] `.padding-3`
* [x] `.p-3`
* [ ] `.pa-3`
* [ ] `.all-p-3`

#### Q. Which class makes an image scale nicely to the parent element?

* [ ] `.img-responsive`
* [x] `.img-fluid`
* [ ] `.responsive-img`
* [ ] `.img-scale`
* [ ] `.fluid-img`

#### Q. How do you enable right-to-left (RTL) support in Bootstrap?

* [ ] Add `dir="rtl"` and include the `bootstrap.rtl.css` build
* [ ] Just set `dir="rtl"` on `&lt;html&gt;`
* [ ] Use the `.rtl` utility class
* [x] Add `dir="rtl"` and include the `bootstrap.rtl.css` build
* [ ] Import `bootstrap-rtl.css` via JavaScript

#### Q. Which component uses the `.carousel-item` class?

* [ ] Modal
* [ ] Toast
* [x] Carousel
* [ ] Accordion
* [ ] Popover

#### Q. What helper class would you use to truncate text with an ellipsis?

* [ ] `.text-truncate`
* [x] `.text-truncate`
* [ ] `.truncate`
* [ ] `.ellipsis`
* [ ] `.text-overflow`

#### Q. Which utility class pairs with `.bg-primary` to make text contrast properly?

* [ ] `.text-default`
* [ ] `.text-body`
* [x] `.text-white`
* [ ] `.text-primary`
* [ ] `.text-dark`

#### Q. How do you customize Bootstrap’s default breakpoints in Sass?

* [ ] Override `$breakpoints` map before importing Bootstrap
* [ ] Use CSS custom properties
* [x] Override `$grid-breakpoints` map before importing Bootstrap
* [ ] Use JavaScript theme API
* [ ] Modify CSS after compile

#### Q. Which data attribute controls the delay before a tooltip shows?

* [ ] `data-delay-show`
* [ ] `data-bs-delay-show`
* [x] `data-bs-delay` (with `{ "show": … }` config)
* [ ] `data-tooltip-delay`
* [ ] `data-bs-tooltip-delay`

#### Q. How do you perform arithmetic in Less (e.g., add 10px + 5px)?

* [ ] `10px plus 5px`
* [ ] `@sum: 10px 5px;`
* [x] `@sum: 10px + 5px;`
* [ ] `calc(10px + 5px);`
* [ ] `math(10px, +, 5px);`

#### Q. In SCSS, what does `@forward` do?

* [ ] Mixes in a partial’s contents
* [x] Re‐exports selected members from a module
* [ ] Imports and immediately uses a partial
* [ ] Deletes unused selectors
* [ ] Aliases variables

#### Q. Which modern feature scopes styles to a module in Sass’s new module system?

* [ ] `@scope`
* [x] `@use`
* [ ] `@module`
* [ ] `@local`
* [ ] `@private`

#### Q. How do you select all `&lt;p&gt;` elements inside a container with class `.article`?

* [ ] `.article p { … }`
* [ ] `p .article { … }`
* [ ] `article &gt; p { … }`
* [x] `.article p { … }`
* [ ] `#article p { … }`

#### Q. Which value of `display` makes an element generate a block box and allow width/height?

* [ ] `inline`
* [ ] `inline-block`
* [ ] `none`
* [x] `block`
* [ ] `flex`

#### Q. What does the `box-sizing: border-box;` declaration do?

* [ ] Includes margin in the element’s total width/height
* [ ] Excludes padding from width/height calculations
* [x] Includes padding and border in the element’s width/height
* [ ] Makes the box invisible
* [ ] Forces width to always be 100%

#### Q. How do you apply a style when the user hovers over an element?

* [ ] `element:active { … }`
* [ ] `element:focus { … }`
* [x] `element:hover { … }`
* [ ] `element:visit { … }`
* [ ] `element:checked { … }`

#### Q. Which shorthand property sets all four margin values?

* [ ] `margin-all`
* [x] `margin`
* [ ] `margins`
* [ ] `margin-shorthand`
* [ ] `m`

#### Q. To create a two-column grid layout, which display value would you use?

* [ ] `display: flex`
* [ ] `display: inline-grid`
* [x] `display: grid`
* [ ] `display: table`
* [ ] `display: block`

#### Q. How do you make text bold using CSS?

* [ ] `font-style: bold;`
* [ ] `text-weight: 700;`
* [x] `font-weight: bold;`
* [ ] `font-variant: bold;`
* [ ] `font: bold;`

#### Q. Which unit is relative to the root element’s font size?

* [ ] `%`
* [ ] `em`
* [x] `rem`
* [ ] `vh`
* [ ] `vw`

#### Q. What is the default value of the `position` property?

* [ ] `absolute`
* [ ] `fixed`
* [ ] `relative`
* [x] `static`
* [ ] `sticky`

#### Q. Which property controls the space between lines of text?

* [ ] `letter-spacing`
* [x] `line-height`
* [ ] `word-spacing`
* [ ] `text-spacing`
* [ ] `leading`

#### Q. How would you write a media query for screens narrower than 600px?

* [ ] `@media all and (max-device-width: 600px) { … }`
* [ ] `@media screen and (min-width: 600px) { … }`
* [x] `@media screen and (max-width: 600px) { … }`
* [ ] `@media (width &lt; 600px) { … }`
* [ ] `@media only screen (max-width: 600px) { … }`

#### Q. Which CSS property adds space inside an element’s border?

* [ ] `margin`
* [x] `padding`
* [ ] `spacing`
* [ ] `border-spacing`
* [ ] `inset`

#### Q. To create a circular element with equal width and height, which property helps cut off excess corners?

* [ ] `clip-path: circle();`
* [x] `border-radius: 50%;`
* [ ] `shape-outside: circle();`
* [ ] `overflow: hidden;`
* [ ] `mask: circle();`

#### Q. Which pseudo-element lets you insert content before an element’s content?

* [ ] `:before`
* [x] `::before`
* [ ] `:first-child`
* [ ] `::first-letter`
* [ ] `::after`

#### Q. How do you make a flex container wrap its items onto multiple lines?

* [ ] `flex-direction: wrap;`
* [ ] `flex-flow: wrap;`
* [x] `flex-wrap: wrap;`
* [ ] `flex-lines: wrap;`
* [ ] `display: flex-wrap;`

#### Q. Which property controls the transparency of an element?

* [ ] `visibility`
* [x] `opacity`
* [ ] `transparency`
* [ ] `filter: alpha`
* [ ] `display`

#### Q. How would you define a custom property (CSS variable)?

* [ ] `@variable --main-color: #333;`
* [ ] `--main-color = #333;`
* [x] `:root { --main-color: #333; }`
* [ ] `variable(--main-color): #333;`
* [ ] `root --main-color: #333;`

#### Q. Which property is used to control how background images are repeated?

* [ ] `background-style`
* [ ] `background-position`
* [x] `background-repeat`
* [ ] `background-layout`
* [ ] `background-tile`

#### Q. What does `justify-content: space-between;` do in a flex container?

* [ ] Centers items vertically
* [ ] Aligns items at the flex-start
* [ ] Aligns items at the flex-end
* [x] Distributes items evenly with first at start and last at end
* [ ] Stretches items to fill

#### Q. Which of the following has the highest CSS specificity?

* [ ] `div.item span`
* [ ] `.item span:hover`
* [x] `#container .item &gt; span.active`
* [ ] `body div#container .item span`
* [ ] `*`

#### Q. What does the `!important` declaration do?

* [ ] Lowers the rule’s specificity
* [x] Overrides normal cascade order, even if specificity is lower
* [ ] Defers the rule until all other rules are applied
* [ ] Makes the rule apply only in development mode
* [ ] Converts the rule into an inline style

#### Q. In CSS Grid, what does `grid-template-areas` allow you to do?

* [ ] Automatically generate grid tracks
* [x] Name and place grid cells via an ASCII-art layout
* [ ] Define responsive breakpoints
* [ ] Control the stacking context of grid items
* [ ] Create grid gaps without `grid-gap`

#### Q. Which CSS function is best suited for creating fluid, clamped font sizes?

* [ ] `calc()`
* [ ] `min()`
* [ ] `max()`
* [x] `clamp()`
* [ ] `var()`

#### Q. How do you write a container query to apply styles when a container’s width is at least 400px?

* [x] `@container (min-width: 400px) { … }`
* [ ] `@media container and (min-width: 400px) { … }`
* [ ] `@container-type (min-width: 400px) { … }`
* [ ] `@query (container-width &gt;= 400px) { … }`
* [ ] `@container width: 400px { … }`

#### Q. Which pseudo-class matches an element when it receives keyboard focus but not mouse focus?

* [ ] `:focus`
* [ ] `:active`
* [x] `:focus-visible`
* [ ] `:focus-within`
* [ ] `:hover`

#### Q. What does `contain: layout paint;` do?

* [ ] Prevents child elements from inheriting styles
* [x] Creates a boundary so layout and paint are contained, reducing repaint cost
* [ ] Forces the element to use its own stacking context
* [ ] Disables pointer events inside the element
* [ ] Automatically polyfills CSS features

#### Q. Which property establishes a new stacking context?

* [ ] `z-index` alone
* [ ] `opacity: 1`
* [ ] `position: relative`
* [x] `transform: translateZ(0)`
* [ ] `display: inline-block`

#### Q. How do you define a CSS custom property with a fallback value?

* [ ] `--col: blue, red;`
* [ ] `--col: blue/fallback(red);`
* [x] `color: var(--col, red);`
* [ ] `color: var(blue, --col);`
* [ ] `color: fallback(var(--col), red);`

#### Q. Which selector list groups selectors without increasing specificity?

* [ ] `:is(.a, .b)`
* [ ] `:not(.a, .b)`
* [x] `:where(.a, .b)`
* [ ] `.a, .b`
* [ ] `:matches(.a, .b)`

#### Q. What does `will-change: transform;` signal to the browser?

* [ ] To ignore this element during painting
* [x] To optimize for upcoming changes to the transform property
* [ ] To remove the element from the layout flow
* [ ] To defer loading of child elements
* [ ] To polyfill transform on older browsers

#### Q. In Flexbox, which property makes items stretch to fill the cross-axis?

* [x] `align-items: stretch;`
* [ ] `justify-content: stretch;`
* [ ] `flex-grow: 1;`
* [ ] `flex-shrink: 0;`
* [ ] `align-self: fill;`

#### Q. Which CSS function lets you perform math directly in property values?

* [ ] `calcunit()`
* [x] `calc()`
* [ ] `math()`
* [ ] `compute()`
* [ ] `expression()`

#### Q. What feature does the `:root` selector target?

* [ ] The first `&lt;div&gt;` in the document
* [ ] All `&lt;html&gt;` children
* [x] The document’s root element (usually `&lt;html&gt;`)
* [ ] All custom properties
* [ ] The highest z-index element

#### Q. How do you create a subgrid in CSS Grid?

* [ ] `display: grid-sub;`
* [ ] `grid-template-sub: …;`
* [x] `grid-template-columns: subgrid;` (on child grid)
* [ ] `grid-sub: true;`
* [ ] `grid-template-areas: subgrid;`

#### Q. Which media feature detects if the user prefers a dark color scheme?

* [ ] `(theme: dark)`
* [x] `(prefers-color-scheme: dark)`
* [ ] `(color-scheme: dark)`
* [ ] `(dark-mode: on)`
* [ ] `(user-theme: dark)`

#### Q. Which property would you use to prevent an element from causing a layout shift when animated?

* [ ] `transition: none;`
* [ ] `animation-fill-mode: backwards;`
* [x] `will-change: transform, opacity;`
* [ ] `animation-play-state: paused;`
* [ ] `contain: strict;`

#### Q. How can you scope CSS rules to only apply under a certain attribute on the root?

* [ ] `@scope [data-theme="dark"] { … }`
* [x] `[data-theme="dark"] { … }`
* [ ] `:scope(data-theme="dark") { … }`
* [ ] `:root(data-theme="dark") { … }`
* [ ] `:host([data-theme="dark"]) { … }`

#### Q. What’s the effect of `mix-blend-mode: multiply;` on an element?

* [ ] Disables background images
* [ ] Converts the element to inline
* [ ] Forces the element above all siblings
* [x] Blends the element with its backdrop using multiply blending
* [ ] Clips the element to its parent bounds

#### Q. Which rule lets you define custom breakpoints for container queries?

* [ ] `@custom-breakpoints`
* [ ] `@breakpoint-queries`
* [x] `@custom-media --bp: (min-width: 600px);`
* [ ] `@container-breakpoint`
* [ ] `@media-container`
