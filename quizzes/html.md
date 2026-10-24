# HTML Quiz

Notes: [HTML](../notes/01_html.md)

Check your understanding of document structure, semantic elements, forms, media and loading behavior.

#### Q. Which element is intended for a page's or section's introductory content and navigational aids?

* [ ] `<aside>`
* [ ] `<section>`
* [x] `<header>`
* [ ] `<footer>`

> **Explanation:** `<header>` groups introductory material such as a logo, heading or navigation. `<aside>` holds tangential content and `<footer>` holds supporting information like copyright or related links.

#### Q. How should you provide a text alternative for a purely decorative image?

* [x] `alt=""`
* [ ] Omit the `alt` attribute
* [ ] `alt="image"`
* [ ] `title="decorative"`

> **Explanation:** An empty `alt=""` tells assistive technology to skip the image. Omitting `alt` makes screen readers fall back to the file name, and "image" adds noise without information.

#### Q. Which attribute pattern lets you store custom data on any HTML element?

* [ ] `data`
* [ ] `custom-*`
* [x] `data-*`
* [ ] `meta-*`

> **Explanation:** Any attribute starting with `data-` (for example `data-user-id`) is valid on any element and is exposed to scripts through `element.dataset`.

#### Q. What is the main semantic difference between `<section>` and `<div>`?

* [ ] `<section>` cannot contain other sections
* [x] `<section>` is a thematic grouping, usually with a heading; `<div>` has no meaning
* [ ] `<div>` is for layout only, while `<section>` is for styling only
* [ ] `<div>` must always have a `class` attribute

> **Explanation:** `<section>` represents a thematic part of a document and normally has its own heading. `<div>` is a generic container used when no semantic element fits.

#### Q. Inside `<picture>`, which child element lists alternative image sources?

* [ ] `<image>`
* [ ] `<media>`
* [ ] `<src>`
* [x] `<source>`

> **Explanation:** Each `<source>` offers a `srcset` with optional `media` or `type` conditions; the required `<img>` inside `<picture>` is the fallback and carries the `alt` text.

#### Q. You build a custom slider from `<div>` elements. Which ARIA role tells assistive technology what it is?

* [ ] `role="application"`
* [ ] `role="region"`
* [x] `role="slider"`
* [ ] `role="presentation"`

> **Explanation:** `slider` (together with `aria-valuenow`, `aria-valuemin` and `aria-valuemax`) describes the widget. Better still, a native `<input type="range">` gets the role and keyboard support for free.

#### Q. What does the `defer` attribute on an external `<script>` do?

* [ ] Prevents the script from running until the user interacts
* [ ] Pauses HTML parsing until the script has downloaded and run
* [x] Downloads during parsing and runs after parsing completes, in document order
* [ ] Runs the script as soon as it downloads, in any order

> **Explanation:** Deferred scripts download in parallel and execute in order just before `DOMContentLoaded`. Running as soon as downloaded, in any order, describes `async`.

#### Q. What does HTML stand for?

* [ ] HyperText Machine Language
* [ ] Hyperlink and Text Markup Language
* [x] HyperText Markup Language
* [ ] HyperText Markdown Language

> **Explanation:** HTML is the HyperText Markup Language: markup that describes the structure and meaning of documents connected by hyperlinks.

#### Q. Which element embeds or references executable JavaScript?

* [ ] `<js>`
* [ ] `<code>`
* [x] `<script>`
* [ ] `<javascript>`

> **Explanation:** `<script>` contains inline code or references a file with `src`. `<code>` only marks up a fragment of computer code for display.

#### Q. How do you write a comment in HTML?

* [ ] `// This is a comment`
* [x] `<!-- This is a comment -->`
* [ ] `/* This is a comment */`
* [ ] `# This is a comment`

> **Explanation:** HTML comments start with `<!--` and end with `-->`. `//` and `/* */` are JavaScript (and CSS for `/* */`) comment syntax.

#### Q. Which attribute gives an `<a>` element its destination?

* [ ] `name`
* [ ] `link`
* [x] `href`
* [ ] `src`

> **Explanation:** `href` holds the URL; without it an `<a>` is only a placeholder and is not focusable as a link. `src` is used by embedded resources such as images and scripts.

#### Q. Which markup correctly loads an external stylesheet?

* [ ] `<style src="styles.css">`
* [ ] `<stylesheet href="styles.css">`
* [ ] `<css href="styles.css">`
* [x] `<link rel="stylesheet" href="styles.css">`

> **Explanation:** External CSS uses `<link>` with `rel="stylesheet"` in the `<head>`. `<style>` holds inline CSS and has no `src` attribute.

#### Q. Which element wraps the clickable `<area>` regions of a client-side image map?

* [ ] `<imagemap>`
* [ ] `<mapitem>`
* [x] `<map>`
* [ ] `<imgmap>`

> **Explanation:** A `<map name="...">` contains `<area>` elements and is linked to an image through the image's `usemap="#name"` attribute.

#### Q. How do you declare that a document is written in English?

* [ ] `<html language="en">`
* [ ] `<html locale="en">`
* [x] `<html lang="en">`
* [ ] `<html dir="ltr">`

> **Explanation:** `lang` sets the language for screen-reader pronunciation, hyphenation and translation tools. `dir` controls text direction, not language.

#### Q. Which element holds supporting information such as copyright or related links for a page or section?

* [ ] `<bottom>`
* [ ] `<aside>`
* [ ] `<summary>`
* [x] `<footer>`

> **Explanation:** `<footer>` contains information about its nearest sectioning ancestor or the page. `<aside>` is for tangential content and `<summary>` labels a `<details>` widget.

#### Q. What is the purpose of the `<fieldset>` element?

* [ ] Defines a preformatted text area
* [ ] Creates numbered sections
* [x] Groups related controls in a form, captioned by `<legend>`
* [ ] Embeds an external resource

> **Explanation:** `<fieldset>` groups related controls such as a set of radio buttons, and its `<legend>` gives the group an accessible name. Disabling a fieldset disables every control inside it.

#### Q. Which `<form>` attribute specifies the URL that receives submitted data?

* [ ] `method`
* [x] `action`
* [ ] `target`
* [ ] `enctype`

> **Explanation:** `action` is the destination URL; `method` chooses GET or POST, `enctype` the encoding and `target` where the response is displayed.

#### Q. What does the `placeholder` attribute on an `<input>` do?

* [ ] Marks the field as required
* [x] Shows hint text that disappears when the user types
* [ ] Validates the input against a pattern
* [ ] Sets a default value submitted with the form

> **Explanation:** A placeholder is a visual hint only; it is not submitted and vanishes on input, so it must not replace a visible `<label>`.

#### Q. Which attribute makes a checkbox checked when the page loads?

* [x] `checked`
* [ ] `default`
* [ ] `selected`
* [ ] `active`

> **Explanation:** `checked` is a boolean attribute for checkboxes and radios. `selected` is the equivalent for `<option>` elements.

#### Q. Which element displays a scalar value within a known range, such as disk usage?

* [x] `<meter>`
* [ ] `<range>`
* [ ] `<progress>`
* [ ] `<output>`

> **Explanation:** `<meter>` shows a measurement with `min`, `max` and optional `low`/`high`/`optimum`. `<progress>` shows completion of a task and `<output>` shows a calculation result.

#### Q. Which element represents content that is no longer accurate or relevant, such as an old price?

* [ ] `<del>`
* [x] `<s>`
* [ ] `<strike>`
* [ ] `<mark>`

> **Explanation:** The HTML standard defines `<s>` for content that is no longer accurate or relevant. `<del>` records an edit removed from the document, and `<strike>` is obsolete.

#### Q. Which element marks text with stress emphasis that changes the meaning of a sentence?

* [ ] `<b>`
* [x] `<em>`
* [ ] `<i>`
* [ ] `<mark>`

> **Explanation:** `<em>` conveys stress emphasis. `<i>` and `<b>` are for offset text without extra importance, and `<mark>` highlights relevance.

#### Q. Which element marks text as having strong importance, seriousness or urgency?

* [ ] `<em>`
* [ ] `<highlight>`
* [x] `<strong>`
* [ ] `<important>`

> **Explanation:** `<strong>` represents strong importance, such as a warning. `<em>` is stress emphasis, and `<highlight>`/`<important>` are not HTML elements.

#### Q. What does the `<base>` element define?

* [ ] The background color of the page
* [x] The base URL used to resolve relative URLs in the document
* [ ] The default font size
* [ ] The document's character encoding

> **Explanation:** `<base href="...">` in the `<head>` changes how every relative URL is resolved, and can also set a default link `target`. Only one `<base>` is allowed.

#### Q. A `<div>` acts as a custom control. Which attribute makes it reachable with the Tab key in normal document order?

* [x] `tabindex="0"`
* [ ] `tabindex="-1"`
* [ ] `accesskey="tab"`
* [ ] `focus="true"`

> **Explanation:** `tabindex="0"` adds the element to the tab sequence at its DOM position. `-1` makes it focusable only by script, and positive values reorder tabbing in confusing ways.

#### Q. Which element provides a caption for a `<figure>`?

* [ ] `<description>`
* [x] `<figcaption>`
* [ ] `<caption>`
* [ ] `<label>`

> **Explanation:** `<figcaption>` is the first or last child of `<figure>`. `<caption>` is the table equivalent and must be the first child of `<table>`.

#### Q. Which attribute focuses an input automatically when the page loads?

* [ ] `focus="true"`
* [x] `autofocus`
* [ ] `initial`
* [ ] `ready`

> **Explanation:** `autofocus` is a boolean attribute. Use it sparingly: moving focus on load can disorient screen-reader and keyboard users.

#### Q. Which element embeds inline SVG graphics directly in HTML markup?

* [ ] `<vector>`
* [x] `<svg>`
* [ ] `<graphics>`
* [ ] `<canvas>`

> **Explanation:** Inline `<svg>` creates scalable vector graphics that are part of the DOM and can be styled with CSS. `<canvas>` is a bitmap drawing surface controlled by script.

#### Q. Which attributes implement HTML microdata for machine-readable metadata?

* [ ] `data-*` attributes
* [x] `itemscope`, `itemtype` and `itemprop`
* [ ] `rel` and `rev`
* [ ] `name` and `content`

> **Explanation:** Microdata marks an item with `itemscope`/`itemtype` and its properties with `itemprop`. `name`/`content` belong to `<meta>`, and JSON-LD in a `<script>` is an alternative format.

#### Q. Which tag name can be registered as a custom element with `customElements.define()`?

* [x] `user-card`
* [ ] `usercard`
* [ ] `1-card`
* [ ] `user_card`

> **Explanation:** Custom element names must start with a lowercase ASCII letter, contain a hyphen and have no uppercase letters, which keeps them from clashing with built-in elements.

#### Q. What does `<meta charset="UTF-8">` do?

* [ ] Sets the encoding of the `<title>` only
* [x] Declares the character encoding used to decode the document's bytes
* [ ] Loads a Unicode font
* [ ] Sets the encoding used for form submissions only

> **Explanation:** The charset declaration tells the browser how to turn bytes into characters. It should appear within the first 1024 bytes of the document, early in `<head>`.

#### Q. What does the `novalidate` attribute on a `<form>` do?

* [ ] Enables built-in browser validation
* [x] Disables the browser's constraint validation when the form is submitted
* [ ] Removes the `required` attribute from all fields
* [ ] Turns off server-side validation

> **Explanation:** `novalidate` skips native checks such as `required` and `type="email"` on submit, often because a script shows custom errors. Server-side validation is unaffected and still needed.

#### Q. Which element represents a self-contained composition, such as a blog post or a comment?

* [ ] `<div class="post">`
* [x] `<article>`
* [ ] `<aside>`
* [ ] `<section>`

> **Explanation:** `<article>` is content that makes sense on its own and could be syndicated. `<section>` groups part of a larger whole.

#### Q. What is the role of the `<template>` element?

* [ ] Displays content after a delay
* [x] Holds inert markup that is not rendered until cloned by script
* [ ] Scopes CSS to its children
* [ ] Marks markup that only the server processes

> **Explanation:** Content inside `<template>` is parsed but not rendered, and its scripts and images do not run or load until a script clones `template.content` into the document.

#### Q. Which attribute makes `<audio>` or `<video>` start playing as soon as it can?

* [ ] `autoplayable`
* [x] `autoplay`
* [ ] `playonload`
* [ ] `start`

> **Explanation:** `autoplay` requests automatic playback, but browsers usually block unmuted autoplay, so videos typically also need `muted`.

#### Q. Which input accepts only numbers from 1 to 10 using built-in validation?

* [x] `<input type="number" min="1" max="10">`
* [ ] `<input type="text" pattern="[1-10]">`
* [ ] `<input type="number" from="1" to="10">`
* [ ] `<input type="text" min="1" max="10">`

> **Explanation:** `min` and `max` constrain number inputs. `[1-10]` is a character class matching `1` or `0`, and `min`/`max` have no effect on text inputs.

#### Q. Which element embeds another HTML document as a nested browsing context?

* [ ] `<object>`
* [ ] `<embed>`
* [ ] `<include>`
* [x] `<iframe>`

> **Explanation:** `<iframe>` loads a full document in its own browsing context and supports `sandbox`, `allow` and `loading`. `<embed>` and `<object>` are generic plugin-style embeds; `<include>` doesn't exist.

#### Q. What do the `async` and `defer` attributes on an external classic script have in common?

* [ ] Both execute the script before parsing continues
* [ ] Both guarantee the scripts run in document order
* [x] Both download the script without blocking HTML parsing
* [ ] Both delay execution until the `load` event

> **Explanation:** Both fetch in parallel with parsing. They differ in execution: `defer` runs in order after parsing, while `async` runs as soon as the file arrives, in any order.

#### Q. Which `rel` value stops a link from sending the `Referer` header to the destination?

* [x] `noreferrer`
* [ ] `noopener`
* [ ] `nofollow`
* [ ] `external`

> **Explanation:** `noreferrer` omits the `Referer` header and also implies `noopener`. `noopener` alone only stops the new page from accessing `window.opener`.

#### Q. What does the `hidden` attribute do to an element?

* [ ] Hides it visually but keeps its space in the layout
* [x] Marks it as not currently relevant, so it isn't rendered or announced
* [ ] Hides it only on small screens
* [ ] Hides it visually but keeps it available to screen readers

> **Explanation:** `hidden` acts like `display: none` by default, removing the element from layout and the accessibility tree. Hiding while keeping space is `visibility: hidden`.

#### Q. Which tag tells the browser to fetch a critical font early, before CSS discovers it?

* [ ] `<link rel="prefetch" href="font.woff2">`
* [ ] `<script rel="preload" src="font.woff2">`
* [x] `<link rel="preload" href="font.woff2" as="font" crossorigin>`
* [ ] `<meta rel="preload" content="font.woff2">`

> **Explanation:** `rel="preload"` with the right `as` value fetches a resource needed for the current page at high priority; fonts also need `crossorigin`. `prefetch` is a low-priority hint for future navigations.

#### Q. Which tag creates an ordered (numbered) list?

* [ ] `<ul>`
* [ ] `<li>`
* [x] `<ol>`
* [ ] `<dl>`

> **Explanation:** `<ol>` is for items where order matters, `<ul>` for unordered items and `<dl>` for term–description pairs. `<li>` is a list item inside `<ol>` or `<ul>`.

#### Q. What is the purpose of the `<meta>` element?

* [ ] To add images to a page
* [x] To provide metadata about the document, such as encoding or viewport
* [ ] To create links to other pages
* [ ] To define the page's main heading

> **Explanation:** `<meta>` lives in `<head>` and supplies information like `charset`, `viewport` and `description` that browsers and search engines read but users don't see.

#### Q. Which element embeds a video with native playback controls?

* [ ] `<media>`
* [ ] `<embed>`
* [x] `<video>`
* [ ] `<movie>`

> **Explanation:** `<video controls>` plays video natively; `<source>` children can offer multiple formats and `<track>` adds captions.

#### Q. Which `<img>` attribute specifies the image file to load?

* [ ] `srcset`
* [x] `src`
* [ ] `href`
* [ ] `alt`

> **Explanation:** `src` is the required image URL. `srcset` offers optional alternatives for different resolutions, while `alt` is the text alternative.

#### Q. Which element inserts a line break within text?

* [x] `<br>`
* [ ] `<lb>`
* [ ] `<break>`
* [ ] `<hr>`

> **Explanation:** `<br>` is a void element for meaningful line breaks such as in addresses or poems. `<hr>` is a thematic break between paragraphs.

#### Q. Which tag creates a table row?

* [ ] `<td>`
* [ ] `<th>`
* [x] `<tr>`
* [ ] `<row>`

> **Explanation:** `<tr>` contains the cells of one row: `<td>` for data and `<th>` for headers.

#### Q. Which element marks a major block of navigation links?

* [x] `<nav>`
* [ ] `<navbar>`
* [ ] `<menu>`
* [ ] `<section>`

> **Explanation:** `<nav>` creates a navigation landmark. Give multiple navs distinct names with `aria-label`, such as "Primary" and "Footer".

#### Q. Which attribute makes the browser refuse to submit a form while an input is empty?

* [ ] `mandatory`
* [x] `required`
* [ ] `validate`
* [ ] `checked`

> **Explanation:** `required` triggers native constraint validation on submit. It is a usability aid only; the server must still validate the data.

#### Q. What does `target="_blank"` on a link do?

* [x] Opens the link in a new tab or window
* [ ] Opens the link in the same tab
* [ ] Forces the target to download
* [ ] Opens the link in the parent frame

> **Explanation:** `_blank` creates a new browsing context. Modern browsers apply `noopener` to it implicitly, and users should be told when a new tab opens. `_parent` targets the parent frame.

#### Q. A `<button>` inside a `<form>` has no `type` attribute. What happens when it is clicked?

* [ ] Nothing, until a click handler is added
* [x] It submits the form
* [ ] It resets the form fields
* [ ] It toggles the form's visibility

> **Explanation:** A button's default type is `submit`. Use `type="button"` for buttons that only run JavaScript, so they don't submit the form accidentally.

#### Q. How is a `<label>` explicitly associated with an `<input>`?

* [ ] The label's `name` matches the input's `name`
* [x] The label's `for` matches the input's `id`
* [ ] The label's `id` matches the input's `for`
* [ ] The label's `href` points to the input

> **Explanation:** `for` references the control's `id`, which gives the input an accessible name and makes clicking the label focus it. `name` is the key used when submitting data.

#### Q. A form has an unchecked checkbox `<input type="checkbox" name="news" value="yes">`. What does it contribute to the submitted data?

* [ ] `news=no`
* [ ] `news=`
* [ ] `news=off`
* [x] Nothing at all

> **Explanation:** Only checked checkboxes are submitted, as `news=yes` here. The server must treat a missing field as unchecked.

#### Q. Which value of the `loading` attribute defers an off-screen image until the user scrolls near it?

* [ ] `defer`
* [x] `lazy`
* [ ] `async`
* [ ] `eager`

> **Explanation:** `loading="lazy"` lets the browser postpone off-screen images and iframes. Don't lazy-load the main above-the-fold image, as that delays the largest contentful paint.
