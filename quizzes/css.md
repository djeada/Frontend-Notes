# CSS Quiz

Notes: [CSS](../notes/02_css.md), [CSS Frameworks and Preprocessors](../notes/03_css_frameworks.md)

Check your understanding of selectors, the cascade, the box model, layout, modern CSS features, Sass, Less and Bootstrap 5.

#### Q. Which CSS property changes the text color of an element?

* [ ] `font-color`
* [ ] `text-color`
* [x] `color`
* [ ] `foreground`

> **Explanation:** `color` sets the foreground (text) color and is inherited by descendants. `font-color` and `text-color` look plausible but are not CSS properties, so browsers ignore them.

#### Q. Which selector matches every `<p>` anywhere inside an element with class `article`, including deeply nested ones?

* [x] `.article p`
* [ ] `.article > p`
* [ ] `p .article`
* [ ] `#article p`

> **Explanation:** The space is the descendant combinator, matching `<p>` at any depth inside `.article`. `>` matches only direct children, and `p .article` reverses the relationship.

#### Q. Which `display` value makes an element start on a new line and respect `width` and `height`?

* [ ] `inline`
* [ ] `inline-block`
* [x] `block`
* [ ] `contents`

> **Explanation:** A block box starts on a new line and accepts width and height. `inline-block` also accepts dimensions but flows within a line, and `contents` removes the element's own box entirely.

#### Q. What does `box-sizing: border-box;` change?

* [ ] Margin is included in the element's declared width and height
* [ ] Padding is excluded from the element's declared width and height
* [x] Padding and border are included in the element's declared width and height
* [ ] The element always stretches to 100% of its parent's width

> **Explanation:** With `border-box`, the declared width covers content, padding and border, so the content area shrinks to fit. Margins always remain outside the box.

#### Q. What is the rendered border-box width of this element?

```css
.card {
  box-sizing: content-box;
  width: 320px;
  padding: 24px;
  border: 2px solid #64748b;
  margin: 16px;
}
```

* [ ] `320px`
* [ ] `368px`
* [x] `372px`
* [ ] `404px`

> **Explanation:** Under `content-box`, `width` sizes only the content: 320 + 2×24 padding + 2×2 border = 372px. Margins add space outside the border, so they are not part of the border-box width.

#### Q. Which pseudo-class applies a style while the pointer is over an element?

* [ ] `:active`
* [ ] `:focus`
* [x] `:hover`
* [ ] `:target`

> **Explanation:** `:hover` matches while the pointer rests on the element. `:active` matches while it is being pressed, and `:focus` when it has focus, so don't rely on hover alone for interactions keyboard users need.

#### Q. What does `margin: 10px 20px;` set?

* [x] Top and bottom to 10px, left and right to 20px
* [ ] Left and right to 10px, top and bottom to 20px
* [ ] Top to 10px and right to 20px, leaving the others at 0
* [ ] All four sides to the average value of 15px

> **Explanation:** With two values, the first sets top and bottom and the second sets left and right. Four values go clockwise: top, right, bottom, left.

#### Q. Which declarations create a layout with two equal-width columns?

* [x] `display: grid; grid-template-columns: 1fr 1fr;`
* [ ] `display: block; grid-template-columns: 1fr 1fr;`
* [ ] `display: grid; grid-columns: 2;`
* [ ] `display: flex; flex-columns: 2;`

> **Explanation:** Grid track properties only work on a grid container, and `1fr 1fr` splits the free space into two equal columns. `grid-columns` and `flex-columns` are not CSS properties.

#### Q. How do you make text bold using CSS?

* [ ] `font-style: bold;`
* [ ] `text-weight: 700;`
* [x] `font-weight: bold;`
* [ ] `font-variant: bold;`

> **Explanation:** `font-weight` controls boldness (`bold` equals `700`). `font-style` handles italics and `font-variant` handles small caps, so neither accepts `bold`.

#### Q. Which unit is relative to the root element's font size?

* [ ] `em`
* [x] `rem`
* [ ] `%`
* [ ] `vh`

> **Explanation:** `rem` ("root em") is based on the `<html>` element's font size, so it stays consistent at any nesting depth. `em` is relative to the current element's font size and compounds when nested.

#### Q. What is the child's computed padding?

```css
html   { font-size: 16px; }
.parent { font-size: 20px; }
.child  { font-size: 1.5em; padding: 1em; }
```

* [ ] `16px`
* [ ] `20px`
* [ ] `24px`
* [x] `30px`

> **Explanation:** The child's font size is 1.5 × 20px = 30px. For other properties such as `padding`, `em` refers to the element's own computed font size, so `1em` is 30px.

#### Q. What is the initial value of the `position` property?

* [ ] `relative`
* [ ] `absolute`
* [x] `static`
* [ ] `sticky`

> **Explanation:** Elements are `position: static` by default and follow normal flow, so `top`, `left` and `z-index` have no effect. `relative` must be set explicitly.

#### Q. Which property controls the space between lines of text?

* [ ] `letter-spacing`
* [x] `line-height`
* [ ] `word-spacing`
* [ ] `text-indent`

> **Explanation:** `line-height` sets the height of each line box; unitless values such as `1.5` scale with the font size. `letter-spacing` and `word-spacing` adjust horizontal spacing.

#### Q. Which media query matches viewports narrower than 600px, but not exactly 600px?

* [x] `@media (width < 600px) { … }`
* [ ] `@media (max-width: 600px) { … }`
* [ ] `@media (width <= 600px) { … }`
* [ ] `@media (min-width: 600px) { … }`

> **Explanation:** Range syntax `width < 600px` excludes 600px and is supported in all modern browsers. `max-width: 600px` is equivalent to `width <= 600px`, so it still matches at exactly 600px.

#### Q. Which property adds space between an element's content and its border?

* [ ] `margin`
* [x] `padding`
* [ ] `outline-offset`
* [ ] `border-spacing`

> **Explanation:** Padding sits inside the border and shows the element's background. Margin is outside the border, and `border-spacing` only applies to table cells.

#### Q. Which declaration rounds the corners of a square element into a full circle?

* [x] `border-radius: 50%;`
* [ ] `border-radius: 25%;`
* [ ] `shape-outside: circle();`
* [ ] `outline-radius: 50%;`

> **Explanation:** A 50% radius on each corner of a square meets in the middle of each side, producing a circle. `shape-outside` only changes how text wraps around a float, and `outline-radius` is not a standard property.

#### Q. Which pseudo-element, written in standard syntax, inserts generated content before an element's content?

* [x] `::before`
* [ ] `::after`
* [ ] `::first-line`
* [ ] `:first-child`

> **Explanation:** `::before` (with the `content` property) creates a first child box. The double colon marks pseudo-elements; browsers also accept legacy `:before`. `:first-child` is a pseudo-class that selects an existing element.

#### Q. How do you let flex items wrap onto multiple lines?

* [ ] `flex-direction: wrap;`
* [ ] `flex-lines: wrap;`
* [x] `flex-wrap: wrap;`
* [ ] `display: flex-wrap;`

> **Explanation:** `flex-wrap: wrap` lets items move to new lines when they run out of space; the default `nowrap` keeps them on one line and may shrink or overflow them. `flex-direction` only accepts row or column values.

#### Q. Which property makes an element semi-transparent, including its children?

* [ ] `visibility`
* [x] `opacity`
* [ ] `transparency`
* [ ] `display`

> **Explanation:** `opacity` takes 0–1 and applies to the element and all its contents. `visibility: hidden` hides the element completely while keeping its space, and `transparency` is not a CSS property.

#### Q. How do you define a global CSS custom property?

* [ ] `@variable --main-color: #333;`
* [ ] `--main-color = #333;`
* [x] `:root { --main-color: #333; }`
* [ ] `:root { $main-color: #333; }`

> **Explanation:** Custom properties are declared like ordinary properties with a `--` prefix, usually on `:root` so every element inherits them, and read with `var(--main-color)`. `$main-color` is Sass syntax.

#### Q. Which property controls whether a background image tiles?

* [ ] `background-position`
* [ ] `background-size`
* [x] `background-repeat`
* [ ] `background-clip`

> **Explanation:** `background-repeat` accepts values such as `repeat`, `no-repeat`, `repeat-x` and `space`. `background-position` sets where the image starts, and `background-size` sets how large it is.

#### Q. What does `justify-content: space-between;` do in a flex container?

* [ ] Centers all items along the cross axis
* [ ] Packs all items at the start of the main axis
* [x] Puts the first item at the start, the last at the end, and spaces the rest evenly
* [ ] Stretches items so they fill the main axis

> **Explanation:** `space-between` distributes free space only between items, with none before the first or after the last. `space-around` and `space-evenly` also add space at the edges.

#### Q. In a flex container with `flex-direction: row`, which declaration centers items vertically?

* [x] `align-items: center;`
* [ ] `justify-content: center;`
* [ ] `vertical-align: middle;`
* [ ] `text-align: center;`

> **Explanation:** In a row, the cross axis is vertical, and `align-items` aligns items on the cross axis. `justify-content` works on the main (horizontal) axis, and `vertical-align` doesn't apply to flex items.

#### Q. A flex container has `flex-direction: column`. Along which direction does `justify-content` now distribute items?

* [ ] Horizontally, because `justify-content` always uses the inline axis
* [x] Vertically, because the main axis now runs top to bottom
* [ ] Neither, because `justify-content` is ignored in column layouts
* [ ] Diagonally, because both axes are swapped

> **Explanation:** `justify-content` always acts on the main axis, and `flex-direction: column` makes the main axis vertical. `align-items` then works horizontally.

#### Q. In Flexbox, which declaration makes items fill the container's cross axis (and is the default)?

* [x] `align-items: stretch;`
* [ ] `justify-content: stretch;`
* [ ] `flex-grow: 1;`
* [ ] `flex-shrink: 0;`

> **Explanation:** `align-items: stretch` is the initial value, so items without a fixed cross size fill the line's height in a row. `flex-grow` distributes extra space along the main axis instead.

#### Q. Which selector has the highest specificity?

* [ ] `div.item span`
* [ ] `.item span:hover`
* [x] `#container .item > span.active`
* [ ] `body div#container .item span`

> **Explanation:** It scores (1,2,1): one ID, two classes, one type. `body div#container .item span` is (1,1,3). After an equal ID count, the class column decides, so the number of type selectors doesn't matter.

#### Q. What color is the paragraph?

```html
<p class="b a">Hello</p>
```

```css
.a { color: red; }
.b { color: blue; }
```

* [ ] Red, because `a` is listed last in the `class` attribute
* [x] Blue, because `.b` comes later in the stylesheet
* [ ] Red, because `.a` comes first in the stylesheet
* [ ] Purple, because the two colors are mixed

> **Explanation:** Both selectors have equal specificity (0,1,0), so source order decides and the later rule wins. The order of names in the `class` attribute has no effect on the cascade.

#### Q. What does `!important` do to a declaration?

* [ ] Lowers the specificity of the rule
* [x] Makes it beat normal declarations, regardless of their selector specificity
* [ ] Delays it until all other rules have been applied
* [ ] Converts the rule into an inline style

> **Explanation:** Important declarations take precedence over normal ones in the cascade, so specificity only matters between two declarations that are both important. Use it sparingly; it makes later overrides hard.

#### Q. What color is the link?

```html
<nav class="nav"><a class="btn" href="/">Home</a></nav>
```

```css
@layer base, components;

@layer components {
  .btn { color: blue; }
}

@layer base {
  .nav .btn { color: red; }
}
```

* [x] Blue, because `components` is listed later in the `@layer` statement
* [ ] Red, because `.nav .btn` has higher specificity
* [ ] Red, because the `base` block appears last in the file
* [ ] The browser default, because conflicting layers cancel out

> **Explanation:** For normal declarations, layer order is checked before specificity, and the first `@layer base, components;` statement fixes that order. A later layer wins even with a less specific selector.

#### Q. In CSS Grid, what does `grid-template-areas` let you do?

* [ ] Generate grid tracks automatically from the content
* [x] Name regions and place items with an ASCII-art layout
* [ ] Define the breakpoints at which the grid changes
* [ ] Control the stacking order of overlapping grid items

> **Explanation:** You draw rows of named cells as strings, such as `"header header" "sidebar main"`, then put an item into a region with `grid-area: main`.

#### Q. Which CSS function is designed for fluid font sizes with a minimum and a maximum?

* [ ] `calc()`
* [ ] `min()`
* [ ] `max()`
* [x] `clamp()`

> **Explanation:** `clamp(1rem, 2.5vw, 2rem)` uses the preferred middle value but never goes below the minimum or above the maximum. `min()` or `max()` alone only enforce one bound.

#### Q. How do you write a container query that applies when the container is at least 400px wide?

* [x] `@container (min-width: 400px) { … }`
* [ ] `@media container and (min-width: 400px) { … }`
* [ ] `@container-type (min-width: 400px) { … }`
* [ ] `@query (container-width >= 400px) { … }`

> **Explanation:** `@container` queries the nearest ancestor that is a size container. `container-type` is the property that creates that container, not an at-rule.

#### Q. A component's `@container (min-width: 30rem) { … }` rules never apply, although its wrapper is 40rem wide. What is the most likely cause?

* [x] No ancestor declares `container-type: inline-size` (or `size`)
* [ ] Container queries only accept pixel units, not `rem`
* [ ] The wrapper needs `display: grid` to act as a container
* [ ] The rules must be repeated inside a matching `@media` query

> **Explanation:** An element is only queried as a size container when it sets `container-type`, so without it the query finds no container. Any display type and length unit works.

#### Q. Which pseudo-class matches a focused element only when the browser decides focus should be visibly indicated, typically after keyboard navigation?

* [ ] `:focus`
* [ ] `:active`
* [x] `:focus-visible`
* [ ] `:focus-within`

> **Explanation:** `:focus-visible` uses browser heuristics: keyboard focus usually matches, while a mouse click on a button usually doesn't. `:focus` matches any focus, and `:focus-within` matches ancestors of the focused element.

#### Q. What does `contain: layout paint;` do?

* [ ] Prevents child elements from inheriting styles
* [x] Isolates the element's layout and painting from the rest of the page
* [ ] Disables pointer events inside the element
* [ ] Hides the element until all its images have loaded

> **Explanation:** Containment tells the browser that changes inside the element can't affect layout outside it and that its contents are clipped to its box, so less of the page needs recalculating or repainting.

#### Q. Which declaration, on its own, creates a new stacking context?

* [ ] `opacity: 1;`
* [ ] `position: relative;` (with the default `z-index: auto`)
* [x] `transform: translateZ(0);`
* [ ] `display: inline-block;`

> **Explanation:** Any `transform` other than `none` creates a stacking context. `opacity` only does so when below 1, and positioned elements need a `z-index` other than `auto`.

#### Q. How do you read a custom property with a fallback value?

* [ ] `color: var(red, --col);`
* [x] `color: var(--col, red);`
* [ ] `color: fallback(var(--col), red);`
* [ ] `color: var(--col) || red;`

> **Explanation:** The first argument of `var()` is the property name, and anything after the first comma is the fallback used when the property is not defined.

#### Q. Which selector matches elements with class `a` or `b` while adding zero specificity?

* [ ] `:is(.a, .b)`
* [ ] `:not(.a, .b)`
* [x] `:where(.a, .b)`
* [ ] `.a, .b`

> **Explanation:** `:where()` always has specificity 0, so it is easy to override. `:is()` and `:not()` take the specificity of their most specific argument, and a plain list keeps each class at (0,1,0).

#### Q. What does `will-change: transform;` tell the browser?

* [ ] To skip the element during painting
* [x] That `transform` is about to change, so it can prepare optimizations in advance
* [ ] To remove the element from the layout flow
* [ ] To polyfill transforms in older browsers

> **Explanation:** It is a hint that lets the browser, for example, promote the element to its own layer before an animation starts. Overusing it wastes memory, so apply it only to elements that will actually animate.

#### Q. Which pair of properties can usually be animated without triggering layout recalculation?

* [x] `transform` and `opacity`
* [ ] `width` and `height`
* [ ] `top` and `left`
* [ ] `margin` and `padding`

> **Explanation:** Browsers can apply transform and opacity changes during compositing without reflowing the page. Animating size, offsets or spacing forces layout on every frame and can cause jank and layout shifts.

#### Q. Which CSS function performs arithmetic with mixed units, such as `100% - 2rem`?

* [ ] `math()`
* [x] `calc()`
* [ ] `compute()`
* [ ] `expression()`

> **Explanation:** `calc()` is resolved by the browser, so it can combine units like `%` and `rem` that a preprocessor can't know at build time. `expression()` was an old, non-standard Internet Explorer feature.

#### Q. How does a nested grid item reuse the column tracks of its parent grid?

* [ ] `display: subgrid;`
* [ ] `grid-template-columns: inherit;`
* [x] `display: grid; grid-template-columns: subgrid;`
* [ ] `grid-sub: columns;`

> **Explanation:** The child must itself be a grid, and setting `subgrid` as its column template makes it use the parent's column lines, so nested content stays aligned. `inherit` only copies the parent's track list.

#### Q. Which media feature detects that the user prefers a dark color scheme?

* [ ] `(theme: dark)`
* [x] `(prefers-color-scheme: dark)`
* [ ] `(color-scheme: dark)`
* [ ] `(dark-mode: on)`

> **Explanation:** `prefers-color-scheme` reflects the operating-system or browser setting. `color-scheme` is a property that tells the browser which schemes a page supports, not a media feature.

#### Q. Which at-rule limits styles to a DOM subtree, optionally stopping at an inner boundary?

* [x] `@scope (.card) to (.card-body) { … }`
* [ ] `@layer card { … }`
* [ ] `@container card { … }`
* [ ] `@supports (.card) { … }`

> **Explanation:** `@scope` applies its rules only inside the scoping root and excludes anything inside the `to (…)` limit. `@layer` changes cascade priority and `@container` queries container size; neither limits which elements match.

#### Q. Which declaration makes in-page anchor links scroll smoothly instead of jumping?

* [x] `html { scroll-behavior: smooth; }`
* [ ] `html { scroll-snap-type: smooth; }`
* [ ] `html { overflow: smooth; }`
* [ ] `html { transition: scroll 0.3s; }`

> **Explanation:** `scroll-behavior` on the scrolling container controls navigation and programmatic scrolls. Wrap it in `prefers-reduced-motion: no-preference` for users who reduce motion, as Bootstrap's Reboot does.

#### Q. In native CSS nesting (and Sass), what does this rule match?

```css
.card {
  &.featured { border-color: gold; }
}
```

* [x] An element that has both the `card` and `featured` classes
* [ ] A `.featured` element anywhere inside a `.card`
* [ ] A `.featured` element that directly follows a `.card`
* [ ] Every `.card` and every `.featured` element separately

> **Explanation:** `&` stands for the parent selector, and writing `&.featured` with no space produces `.card.featured`, the same element. `& .featured`, with a space, would match a descendant.

#### Q. Why can setting `--accent` on `.card[data-tone="warning"]` recolor a card in the browser, while changing a Sass `$accent` cannot?

* [ ] Sass variables only work inside media queries
* [x] Sass variables are replaced with values at compile time; custom properties cascade at runtime
* [ ] Custom properties are faster because they skip the cascade
* [ ] Sass variables are scoped to the `:root` element only

> **Explanation:** Compiled CSS contains only the value of `$accent`, not the variable. A custom property remains in the CSS, so an attribute or class on an element can override it through the cascade.

#### Q. In SCSS, how do you declare a variable?

* [ ] `@var primary-color: #333;`
* [x] `$primary-color: #333;`
* [ ] `@primary-color: #333;`
* [ ] `%primary-color: #333;`

> **Explanation:** Sass variables start with `$`. `@primary-color` is Less syntax, and `%name` is a Sass placeholder selector, not a variable.

#### Q. In modern Dart Sass, which rule loads another Sass file as a module whose members are accessed through a namespace?

* [x] `@use 'buttons';`
* [ ] `@import 'buttons';`
* [ ] `@include 'buttons';`
* [ ] `@forward 'buttons';`

> **Explanation:** `@use` loads a module once and exposes its members as `buttons.$var` or `buttons.mixin()`. `@import` puts everything in a global namespace and is deprecated, while `@forward` re-exports members for other files.

#### Q. In Sass, what does `@forward 'src/list';` do?

* [ ] Copies the file's CSS output without exposing its members
* [x] Makes the file's members available to stylesheets that `@use` the current file
* [ ] Loads the file and lets the current file use its members directly
* [ ] Removes unused selectors from the file

> **Explanation:** `@forward` re-exports a module's variables, mixins and functions, which is how an `index` file builds a library's public API. It does not make those members available in the forwarding file itself; that needs `@use`.

#### Q. How do you define a mixin named `button` in SCSS?

* [x] `@mixin button { … }`
* [ ] `@function button { … }`
* [ ] `%button { … }`
* [ ] `@include button { … }`

> **Explanation:** `@mixin` defines a reusable block of declarations. `@function` defines something that returns a value, `%button` is a placeholder selector, and `@include` uses a mixin rather than defining one.

#### Q. How do you include a Sass mixin called `button`?

* [ ] `@import button;`
* [x] `@include button;`
* [ ] `@extend button;`
* [ ] `@mixin button;`

> **Explanation:** `@include` copies the mixin's declarations into the current rule and can pass arguments, as in `@include button(red)`. `@extend` shares selectors instead of copying declarations.

#### Q. What does `@content` do inside this Sass mixin?

```scss
@mixin small-viewport {
  @media (max-width: 30em) {
    @content;
  }
}

.nav {
  @include small-viewport {
    flex-direction: column;
  }
}
```

* [ ] Outputs the mixin's own default styles
* [x] Inserts the block passed to `@include` at that position
* [ ] Includes the contents of a file named `content`
* [ ] Marks where the media query's breakpoint value goes

> **Explanation:** A block written after `@include` is passed to the mixin and placed where `@content` appears, so the output is `@media (max-width: 30em) { .nav { flex-direction: column; } }`.

#### Q. Which Sass selector shares styles through `@extend` but is never output on its own?

* [x] `%shared`
* [ ] `.shared`
* [ ] `$shared`
* [ ] `&shared`

> **Explanation:** Placeholder selectors (`%name`) are only emitted when another selector extends them, so no unused class appears in the CSS. A `.shared` class would be output even if nothing uses it.

#### Q. How do you make a Sass selector inherit the styles of `.btn`?

* [ ] `@mixin .btn;`
* [ ] `@include .btn;`
* [x] `@extend .btn;`
* [ ] `@use .btn;`

> **Explanation:** `@extend .btn;` adds the current selector to every rule that targets `.btn`. `@include` only works with mixins, not with selectors.

#### Q. Which Sass control rule loops over each item in a list or map?

* [ ] `@while`
* [ ] `@if`
* [x] `@each`
* [ ] `@for`

> **Explanation:** `@each $color in red, green, blue { … }` runs once per item, and it can also destructure map key/value pairs. `@for` counts through a numeric range instead.

#### Q. Which classes does this Sass loop generate?

```scss
@for $i from 1 to 3 {
  .item-#{$i} { width: 100px * $i; }
}
```

* [x] `.item-1` and `.item-2`
* [ ] `.item-1`, `.item-2` and `.item-3`
* [ ] `.item-0`, `.item-1` and `.item-2`
* [ ] Only `.item-3`

> **Explanation:** `to` excludes the end value, so `$i` takes 1 and 2. Use `through` to include 3.

#### Q. With `@use 'sass:map';`, which call returns the value stored under a key in a map?

* [x] `map.get($map, $key)`
* [ ] `map.value($map, $key)`
* [ ] `map.lookup($map, $key)`
* [ ] `$map[$key]`

> **Explanation:** `map.get` is the module-system name for the legacy global `map-get()`, which is deprecated. Sass has no bracket indexing for maps.

#### Q. With `@use 'sass:map';`, how do you merge two maps?

* [ ] `map.concat($map1, $map2)`
* [x] `map.merge($map1, $map2)`
* [ ] `map.join($map1, $map2)`
* [ ] `$map1 + $map2`

> **Explanation:** `map.merge` returns a new map in which keys from `$map2` override matching keys in `$map1`. Using `+` on maps is an error because maps aren't valid CSS values.

#### Q. In current Dart Sass, which call darkens `$c` by 20% lightness without using a deprecated function?

* [ ] `darken($c, 20%)`
* [ ] `color.darken($c, 20%)`
* [x] `color.adjust($c, $lightness: -20%)`
* [ ] `color.mix($c, 20%)`

> **Explanation:** The legacy global `darken()` still compiles but triggers deprecation warnings. The `sass:color` module has no `darken`, and its replacement is `color.adjust` (or `color.scale` for relative changes).

#### Q. In current Dart Sass, which expression is the recommended way to divide `10px` by 2?

* [ ] `10px / 2`
* [x] `math.div(10px, 2)`
* [ ] `div(10px, 2)`
* [ ] `math.divide(10px, 2)`

> **Explanation:** After `@use 'sass:math';`, `math.div()` performs division explicitly. Using `/` for division is deprecated because `/` is also a CSS separator, as in `font: 16px/1.5`.

#### Q. How do you nest a `.card` rule inside `.container` in SCSS?

* [ ] `.card { .container { … } }`
* [ ] `.container { @nest .card { … } }`
* [x] `.container { .card { … } }`
* [ ] `%container { .card { … } }`

> **Explanation:** A rule nested inside another compiles to a descendant selector: `.container .card { … }`. Reversing the nesting would produce `.card .container`.

#### Q. How do you declare a variable in Less?

* [ ] `$primary-color: #fff;`
* [x] `@primary-color: #fff;`
* [ ] `--primary-color: #fff;`
* [ ] `%primary-color: #fff;`

> **Explanation:** Less variables use `@` and are replaced at compile time. `$` is Sass syntax, and `--primary-color` declares a native CSS custom property that the browser resolves.

#### Q. How do you import another Less file?

* [ ] `@use 'mixins.less';`
* [x] `@import 'mixins.less';`
* [ ] `@include 'mixins.less';`
* [ ] `@require 'mixins.less';`

> **Explanation:** Less uses `@import` to pull in other files, and the `.less` extension can be omitted. Unlike Sass, Less has no `@use` module system.

#### Q. What does this Less code define?

```less
.border(@width: 1px) {
  border: @width solid;
}
```

* [x] A parametric mixin with a default argument, not output as a class on its own
* [ ] A variable named `.border` that stores `1px solid`
* [ ] A function that returns the value `1px`
* [ ] A `.border` class that is always written to the CSS output

> **Explanation:** Parentheses in the definition make it a parametric mixin. It is only output where it is called, as `.border();` or `.border(2px);`.

#### Q. How do you call a mixin named `.center()` in Less?

* [x] `.center();`
* [ ] `@include center();`
* [ ] `@center();`
* [ ] `+center();`

> **Explanation:** Less mixins are called by writing the mixin's selector followed by `();` inside a rule. `@include` is Sass syntax.

#### Q. What does this Less guard do?

```less
.rounded(@radius) when (@radius > 0) {
  border-radius: @radius;
}
```

* [ ] Applies the mixin on every call, whatever the value
* [x] Applies the mixin only when `@radius` is greater than 0
* [ ] Applies the mixin only when `@radius` is less than 0
* [ ] Raises a compile error when `@radius` is 0

> **Explanation:** A `when` guard is a condition on the mixin. If it is false, as in `.rounded(0)`, the call outputs nothing and no error is raised.

#### Q. Which Less declaration makes the compiler output `15px`?

* [x] `@sum: 10px + 5px;`
* [ ] `@sum: calc(10px + 5px);`
* [ ] `@sum: 10px plus 5px;`
* [ ] `@sum: sum(10px, 5px);`

> **Explanation:** Less evaluates `+` at compile time. Less 4 leaves `calc()` untouched for the browser, so that option outputs `calc(10px + 5px)` rather than `15px`.

#### Q. In Less 4 with the default math setting, what does `width: 10px / 2;` compile to?

* [x] `width: 10px / 2;` (unchanged)
* [ ] `width: 5px;`
* [ ] `width: 5;`
* [ ] A compile error

> **Explanation:** Since Less 4, division with `/` is only performed inside parentheses because `/` is also a CSS separator. Write `(10px / 2)` to get `5px`.

#### Q. Which Bootstrap 5 class removes the horizontal gutters between columns in a row?

* [ ] `.no-gutters`
* [ ] `.gx-none`
* [x] `.gx-0`
* [ ] `.gutter-0`

> **Explanation:** Bootstrap 5's gutter utilities are `.g-*`, `.gx-*` (horizontal) and `.gy-*` (vertical), so `.gx-0` sets horizontal gutters to zero. `.no-gutters` was the Bootstrap 4 class.

#### Q. Which attributes make a button open a Bootstrap 5 offcanvas panel with `id="menu"`?

* [ ] `data-bs-toggle="drawer" data-bs-target="#menu"`
* [x] `data-bs-toggle="offcanvas" data-bs-target="#menu"`
* [ ] `data-bs-show="offcanvas" data-bs-panel="#menu"`
* [ ] `data-toggle="offcanvas" data-target="#menu"`

> **Explanation:** Bootstrap 5 plugins use the `data-bs-*` prefix: `data-bs-toggle` names the component and `data-bs-target` selects the element. Unprefixed `data-toggle` is Bootstrap 4 syntax.

#### Q. In Bootstrap 5, which wrapper keeps an embedded video at a 16:9 aspect ratio?

* [ ] `<div class="embed-responsive embed-responsive-16by9">`
* [x] `<div class="ratio ratio-16x9">`
* [ ] `<div class="ratio-responsive-16x9">`
* [ ] `<div class="video-responsive video-16by9">`

> **Explanation:** Bootstrap 5 replaced the v4 `embed-responsive` helpers with `.ratio` plus a modifier such as `.ratio-16x9`. Child iframes or videos are stretched to fill the box.

#### Q. In a Bootstrap 5 Sass build, where should `$primary: #ff6347;` go so Bootstrap uses it?

* [x] Before importing Bootstrap's Sass, because its variables are declared with `!default`
* [ ] After importing Bootstrap's Sass, so it overrides the compiled output
* [ ] Inside `node_modules/bootstrap/scss/_variables.scss`
* [ ] In a JavaScript config object passed to `bootstrap.bundle.js`

> **Explanation:** `!default` assigns a value only when the variable isn't already set, so your value must exist first. Editing files in `node_modules` is lost on reinstall, and Sass variables can't change after compilation.

#### Q. Which Bootstrap class makes an element stick to the top of the viewport once you scroll past it?

* [ ] `.fixed-top`
* [ ] `.sticky`
* [x] `.sticky-top`
* [ ] `.position-top`

> **Explanation:** `.sticky-top` applies `position: sticky; top: 0`, so the element scrolls normally until it reaches the top and then stays there. `.fixed-top` is always fixed and removed from normal flow.

#### Q. In Bootstrap 5, which class makes a column 6 of 12 grid columns wide on every screen size?

* [x] `.col-6`
* [ ] `.col-xs-6`
* [ ] `.col-sm-6`
* [ ] `.col-all-6`

> **Explanation:** Bootstrap 5 has no `xs` infix: unprefixed classes apply from 0px up. `.col-sm-6` applies only from the `sm` breakpoint (576px), and `.col-xs-6` was Bootstrap 3 syntax.

#### Q. Which Bootstrap 5 JavaScript file already includes Popper, so dropdowns and tooltips work without loading Popper separately?

* [x] `bootstrap.bundle.min.js`
* [ ] `bootstrap.min.js`
* [ ] `bootstrap.esm.min.js`
* [ ] `bootstrap.popper.min.js`

> **Explanation:** The bundle build includes Popper, which dropdowns, popovers and tooltips use for positioning. `bootstrap.min.js` and the ESM build expect you to load Popper yourself.

#### Q. Which JavaScript dependency did Bootstrap 5 drop compared with Bootstrap 4?

* [x] jQuery
* [ ] Popper
* [ ] Sass
* [ ] PostCSS

> **Explanation:** Bootstrap 5 plugins are written in plain JavaScript and no longer need jQuery. Popper is still required for positioned components, which is why the bundle build includes it.

#### Q. In Bootstrap 5.3, how do you switch a page or a single component to the built-in dark color mode?

* [ ] Add the `.theme-dark` class to `<body>`
* [ ] Add the `.dark-mode` class to the element
* [x] Add `data-bs-theme="dark"` to `<html>` or the element
* [ ] Add `data-bs-mode="dark"` to the element

> **Explanation:** Color modes, added in 5.3, are driven by the `data-bs-theme` attribute, which switches Bootstrap's CSS variables. Set it on `<html>` for the whole page or on a component for part of it.

#### Q. In Bootstrap 5, which class creates a centered container whose max-width steps up at each breakpoint?

* [ ] `.container-fluid`
* [x] `.container`
* [ ] `.container-responsive`
* [ ] `.container-fixed`

> **Explanation:** `.container` sets a different `max-width` at each breakpoint. `.container-fluid` is always 100% wide, and the other two classes don't exist.

#### Q. Which class combination makes a Bootstrap column full width on small screens and half width from the `md` breakpoint up?

* [x] `.col-12 .col-md-6`
* [ ] `.col-6 .col-md-12`
* [ ] `.col-sm-6 .col-md-12`
* [ ] `.col-12 .col-lg-6`

> **Explanation:** Bootstrap is mobile-first: `.col-12` applies from 0px, and `.col-md-6` overrides it from 768px. The `lg` version stays full width until 992px.

#### Q. Which Bootstrap utility horizontally centers a block element that has a set width?

* [ ] `.text-center`
* [ ] `.ms-auto`
* [x] `.mx-auto`
* [ ] `.mx-center`

> **Explanation:** `.mx-auto` sets left and right margins to `auto`, which splits the free space equally. `.ms-auto` only pushes the element to the end, and `.text-center` centers inline content inside it.

#### Q. In Bootstrap 5, which attribute on a button opens a modal when the button is clicked (together with `data-bs-target`)?

* [ ] `data-bs-toggle="dialog"`
* [x] `data-bs-toggle="modal"`
* [ ] `data-toggle="modal"`
* [ ] `data-bs-show="modal"`

> **Explanation:** `data-bs-toggle="modal"` with `data-bs-target="#id"` opens the matching modal without custom JavaScript. `data-toggle` without the `bs` prefix is the Bootstrap 4 attribute.

#### Q. Which Sass map in Bootstrap's source defines the theme colors such as `primary`, `success` and `danger`?

* [x] `$theme-colors`
* [ ] `$brand-colors`
* [ ] `$palette`
* [ ] `$color-scheme`

> **Explanation:** Bootstrap loops over `$theme-colors` to generate `.btn-*`, `.text-*`, `.bg-*` and other variants. Adding a key to this map creates a full set of classes for a new color.

#### Q. How do you disable a `<button class="btn btn-primary">` in Bootstrap?

* [x] Add the `disabled` attribute to the button
* [ ] Add the `.btn-disabled` class to the button
* [ ] Add `data-bs-disabled` to the button
* [ ] Add the `.inactive` class to the button

> **Explanation:** `disabled` is a boolean HTML attribute: it blocks clicks and focus, and Bootstrap styles it. The `.disabled` class is meant for link-styled buttons (`<a class="btn">`), which also need `aria-disabled="true"`.

#### Q. Which media query matches Bootstrap 5's `lg` breakpoint and wider?

* [ ] `@media (min-width: 576px)`
* [ ] `@media (min-width: 768px)`
* [x] `@media (min-width: 992px)`
* [ ] `@media (min-width: 1200px)`

> **Explanation:** The defaults are `sm` 576px, `md` 768px, `lg` 992px, `xl` 1200px and `xxl` 1400px. Bootstrap's responsive classes use `min-width`, so they apply from the breakpoint upward.

#### Q. In a Bootstrap 5 navbar, which class sets the breakpoint from which the menu is shown expanded instead of collapsed behind the toggler?

* [x] `.navbar-expand-lg`
* [ ] `.navbar-collapse-lg`
* [ ] `.navbar-toggler-lg`
* [ ] `.navbar-responsive-lg`

> **Explanation:** `.navbar-expand-{breakpoint}` shows the links inline from that breakpoint up. Below it, the `.collapse.navbar-collapse` content is hidden behind a `.navbar-toggler` button.

#### Q. Which Bootstrap 5 utility keeps flex items on a single line instead of wrapping?

* [ ] `.text-nowrap`
* [ ] `.flex-wrap`
* [x] `.flex-nowrap`
* [ ] `.flex-fill`

> **Explanation:** `.flex-nowrap` sets `flex-wrap: nowrap` on the flex container. `.text-nowrap` prevents text inside an element from wrapping, which is a different property (`white-space`).

#### Q. What does Bootstrap's `.order-md-1` class do?

* [ ] Sets `order: 1` only below the `md` breakpoint
* [x] Sets `order: 1` from the `md` breakpoint upward
* [ ] Resets the item's order to source order
* [ ] Hides the item from the `md` breakpoint upward

> **Explanation:** Like other responsive utilities, `.order-md-1` uses a `min-width` media query. It changes visual order only; reading and tab order still follow the DOM.

#### Q. Which Bootstrap 5 class scales an image down to fit its parent's width?

* [ ] `.img-responsive`
* [x] `.img-fluid`
* [ ] `.img-scale`
* [ ] `.responsive-img`

> **Explanation:** `.img-fluid` applies `max-width: 100%; height: auto;`, so the image shrinks with its container without growing beyond its natural size. `.img-responsive` was the Bootstrap 3 name.

#### Q. How do you enable right-to-left (RTL) layout with Bootstrap 5?

* [ ] Set `dir="rtl"` on `<html>` and keep the standard stylesheet
* [ ] Add the `.rtl` utility class to `<body>`
* [x] Set `dir="rtl"` on `<html>` and load the `bootstrap.rtl.min.css` build
* [ ] Set `lang="ar"` on `<html>` so Bootstrap flips the layout

> **Explanation:** The RTL build mirrors directional styles such as margins, floats and `.ms-*`/`.me-*`, and `dir="rtl"` sets the browser's text direction. Both are needed; `lang` alone doesn't change direction.

#### Q. Which Bootstrap helper truncates overflowing text on one line with an ellipsis?

* [x] `.text-truncate`
* [ ] `.text-ellipsis`
* [ ] `.text-overflow`
* [ ] `.truncate`

> **Explanation:** `.text-truncate` combines `overflow: hidden`, `text-overflow: ellipsis` and `white-space: nowrap`. The element must be `display: block` or `inline-block` for it to work.

#### Q. In Bootstrap 5.3, which helper sets a primary background together with a matching, contrasting text color?

* [x] `.text-bg-primary`
* [ ] `.bg-primary-contrast`
* [ ] `.text-primary`
* [ ] `.bg-primary-text`

> **Explanation:** The `.text-bg-{color}` helpers set the background color and pick a readable foreground color automatically. `.text-primary` only changes the text color to primary.

#### Q. How do you change Bootstrap's default breakpoints in Sass?

* [ ] Override the `$breakpoints` map after importing Bootstrap
* [ ] Change the `--bs-breakpoint-md` CSS variable at runtime
* [x] Override the `$grid-breakpoints` map before importing Bootstrap
* [ ] Pass a `breakpoints` option to the Bootstrap JavaScript bundle

> **Explanation:** `$grid-breakpoints` generates every responsive class and media query at compile time. Media queries can't read CSS variables, so a runtime custom property can't move the breakpoints.
