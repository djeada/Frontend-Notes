<h1>What html developer should know?</h1>

* Write simple web pages using HTML
* Use both closing and self-closing tags correctly
* Write tags with attributes
* Use MDN as a refrence
* Recreate a given webpage using HTML

<h1>Overview</h1>

* HyperText Markup Language
* NOT a programming language
* structure of a webpage
* nouns of the web-design language

<h1>Tags</h1>
There is crap ton of them, but only few are used in practice.

<h2>What are tags?</h2>

```html
<outerTag>
  <innerTag> Content goes here</innerTag>
</outerTag>
```

<h2>Document structure</h2>

```html
<!DOCTYPE html>
<html>
 <head>
   <!-- Metadata goes here -->
   <title>Document</title>
  </head>
<body>
  <!-- Content goes here -->
  </body>
 </html>

```

## Structure of an HTML document

- `<html>`: contains the entire document; it often has the language set, e.g. `lang="en"`
- `<head>`: contains information like document title, character encoding, ...
- `<body>`: the actual content that is displayed in the browser view


# Head

## Entries in the head

- `title`
- `meta`
- favicon
- stylesheet
- scripts

## title

document title that appears in the window bar:

```html
<title>my website</title>
```

## meta

meta tags are used for including associated meta information

## meta: charset

We should usually include a `<meta charset="UTF-8" />` declaration so we can use any Unicode characters

```html
<button>😊</button>
```

## meta: viewport

We should usually include a _viewport_ declaration to reset browser scaling on small devices

```html
<meta name="viewport" width="device-width" />
```

**Background**: In the early days of mobile web (before responsive design), Websites were scaled down by mobile browsers. The above code disables this behavior.

https://viewportsizes.com/mine

## meta: description

- may be used by search engines to show a page summary
- default title for bookmarks

```html
<meta
  name="description"
  content="Wikipedia is a free online encyclopedia, ..."
/>
```

## meta: keywords

may be used by search engines

```html
<meta name="keywords" content="HTML,javascript" />
```

## meta: http-equiv="X-UA-Compatible"

is relevant for Internet Explorer ≤ 10; causes the use of the most modern version of the rendering engine

## favicon

icon that is displayed in the website tab:

```html
<link
  rel="icon"
  sizes="32x32"
  href="favicon_32.png"
  type="image/png"
/>
```

if no explicit link is present, browsers will look for _facivon.ico_ by default


<h2>Basic tags</h2>

Complete list: https://developer.mozilla.org/de/docs/Web/HTML/Element

<h1>Headers and paragraphs</h1>


## Text formatting

in practice:

- `em` or `i` for making text _italic_
- `strong` or `b` for making text **bold**

## Text formatting

actual meaning according to the HTML 5 standard:

- `em` - emphasis
- `i` - proper names, technical terms, foreign words, ...
- `strong` - importance
- `b` - other highlight

## Text formatting

Examples:

```html
My next phone <em>must</em> be a <i>FooPhone</i>.
```

```html
<strong>The event is cancelled</strong> due to bad weather.
```

<h2>Div and Span</h2>

Used for marking text, images etc.

Div is short for divider. It doesn't change anything in html. Separtaes blocks of connected elements. It will get extremly useful once you get into css.

Spans are pretty much the same, except they are used to mark single elements instead of a whole block.

<h1>Attributes</h1>
There is also crap ton of them. An attribute is a piece of code attached to a tag which supplies additional information.

alt is used by blind people. it tells them what is there.

```html
<img src='example.img' alt='a cute puppy'>
```

This one is valid HTML5 and it is absolutely fine without closing it. It is a so-called void element.
Another example with href link.

<h2>Lists</h2>

## Lists

- `ul` (unordered list)
- `ol` (ordered list - numbered)
- `li` (list item)

## Lists

example:

```html
<h1>tetrapods:</h1>
<ul>
  <li>amphibians</li>
  <li>reptiles</li>
  <li>birds</li>
  <li>mammals</li>
</ul>
```

<h1>Links</h1>

Example:

```html
<a href="https://en.wikipedia.org/wiki/HTML"
  >Wikipedia article</a
>
```

## E-Mail link:

```html
<a href="mailto:foo@bar.com">send e-mail</a>
```

## Links

Download link:

```html
<a href="report.ods" download>report</a>
```

<h1>Tables</h1>

<h1>Radio buttons</h1>

<h1>Text area</h1>

<h1>Forms</h1>

# Forms and buttons

## Forms and buttons

elements:

- `button`
- `form`
- `input`
- `label`
- `select`
- ...

## Form example

```html
<form action="/register" method="post">
  <div>
    <label
      >first name: <input type="text" name="firstname"
    /></label>
  </div>
  <div>
    <label
      >last name: <input type="text" name="lastname"
    /></label>
  </div>
  <button type="submit">register</button>
</form>
```

## Buttons

```html
<button type="submit">press me!</button>
```

## Buttons

button types:

- _submit_: button that submits a form (default type for buttons in a form)
- _button_
- (_reset_)

## Input

```html
<input />
```

```html
<input type="password" />
```

## Input types

default type: `text`

other possibilities:

- `checkbox`
- `radio`
- `file`
- `password`
- `date` (HTML 5)
- `email`(HTML 5)
- `number` (HTML 5)
- `search` (HTML 5)

## Input attributes

- placeholder
- autofocus
- autocomplete
- size

## Autocomplete

Possible values of the `autocomplete` attribute:

- `name`
- `given-name`
- `email`
- `username`
- ...

## Validation

- `required`
- `minlength`
- `maxlength`

CSS pseudoclasses: `:valid`, `:invalid`

## Validation - example

```html
<input
  type="number"
  min="-5"
  max="5"
  step="0.1"
  value="1"
/>
```

## Input and label

Inputs should have labels that describe them:

```html
<label
  >enter your name:
  <input />
</label>
```

or

```html
<label for="name-input">enter your name:</label>
<input id="name-input" />
```

## Forms

```html
<form action="/register" method="post">
  first name: <input type="text" name="firstname" /><br />
  last name: <input type="text" name="lastname" /><br />
  <button type="submit">register</button>
</form>
```

## Forms

When the form is submitted, a _post_ request with the following content is sent to _/register_:

```txt
firstname=John&lastname=Doe
```

```html
<form action="#" method="GET">
  <label for="id">User id:</label>
  <input id="id" type="number" placeholder="Id" name="id">
  <br>
  <label for="password">Password:</label>
  <input id="password" type="text" placeholder="Password" name="password">
  
  <button>Submit</button>
</form>
```

Name is important because it shows up in the get request and you can easily identify which part of the request is 

Id's are internal to html.

Other types include: password, color, date and email.


## Special characters

the following characters should always be "escaped" in an HTML document:

- `<` becomes `&lt;`
- `>` becomes `&gt;`
- `&` becomes `&amp;`

these characters must be escaped if they occur in attributes:

- `"` becomes `&quot;`
- (`'` becomes `&apos;` if the attribute is delimited by `'`)

## Whitespace

In HTML, any sequence of whitespace characters (space, line break, tab) is interpreted as a single space.


## Media

- `img`
- `video`
- `audio`

## img

attributes:

- `src`: image path
- `alt`: alternative text in case the picture cannot be displayed
- `srcset`: list of image paths for different resolutions

## srcset - example

```html
<img
  alt=""
  src="images/2000x1000.png"
  srcset="
    images/500x250.png   500w,
    images/1000x500.png 1000w
  "
/>
```

Demo: http://srcset.salcode.com/

## video

```html
<video autoplay loop controls width="250">
  <source src="myvideo.webm" type="video/webm" />
  <source src="myvideo.mp4" type="video/mp4" />
  Sorry, your browser doesn't support embedded videos.
</video>
```

Example video: https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm

## audio

```html
<audio src="myaudio.mk" loop volume="0.5"></audio>
```

## Image formats

relevant web image formats:

- _jpg_
- _png_ (lossless compression)
- _webp_ (better compression compared to _jpg_ and _png_)
- _avif_ (future format)
- _gif_ (animated, limited color range)
- _svg_ (vector graphics)

## Video formats

relevant web video formats:

- _MP4_ container, _H.264_ (_AVC_) codec: universally supported, patented, good quality
- _MP4_ container, _H.265_ (_HEVC_) codec: patented, better quality
- _WebM_ container, _AV1_ codec: candidate for new standard, open source, better quality

### Best practices

Short list of HTML best practices. Sources are afer the CSS list. 

* use HTML5
* use the doctype
* Don't use XML Declaration
* validate but not validate!
* define character encoding `<meta charset="utf-8">`
* Semantics
* Use `P` tags for paragraphs over multiple `BR`
* use `BLOCKQUOTE` when  appropriate
* use `LABEL` elements with the `FOR` attribute set
* use CSS where possible; includes `INPUT` size attribute
* **Do not use TABLES for layout**
* user [microformats](http://microformats.org/) where possible and helps
* use `THEAD` `TBODY`
* use `TH` tags for table header elements
* use CSS to transform text; headlines use title case. 
* quote attributes ; double quote is preference
* Don't mix quotation marks
* use UTF-8
* omit type tag for CSS link tag
* define `TITLE`
* define the `BODY` tag ; follows explicit defintion concept
* `FIGCAPTION` first or last child of `FIGURE`
* use `rel` attribute where possible
* omit `type` attribute for `SCRIPT` tag when loading javascript
* use the `download` attribute for `A` tags when possible (IE/Safari does not support )
* Close tags
* **Avoid inline styles**
* Place   External CSS Files Within the Head Tag
* Place Javascript files at bottom
* Do not inline Javascript (production, ok in development)
* Lowercase tag names
* Use h1-h6 to outline the page content
* include page navigation `A` anchors for sections
* Do not hijack the TABORDER
* 


##### HTML Best Practice Sources 

http://isobar-idev.github.io/code-standards/

https://github.com/hail2u/html-best-practices

http://code.tutsplus.com/tutorials/30-html-best-practices-for-beginners--net-4957 -- old 2009 

http://learn.shayhowe.com/html-css/writing-your-best-code/

https://www.webaccessibility.com/best_practices.php


