## Intro

* HyperText Markup Language
* NOT a programming language
* structure of a webpage
* nouns of the web-design language

## What should an HTML developer know?

* Structure simple web pages using HTML.
* Correctly use closing and self-closing tags.
* Write tags with attributes.
* Make use of MDN as a resource.
* Recreate a given webpage using HTML.

## Building blocks of HTML

When learning HTML, there are three fundamental skills to master:
1. Knowing the HTML document's overall structure.
2. Understanding the function of tags and attributes, as well as where to look for them in the documentation.
3. Using containers like span and div to properly divide the document body into logical groupings.

### Document structure

Every HTML document follows a specific structure. 

### Example

Here is an example of a simple HTML document:

```html
<!DOCTYPE html>
<html>

<head>
    <title>Document</title>
</head>

<body>
</body>

</html>
```

More or less every HTML document looks like this. The <code>!DOCTYPE</code> tag is used to specify the type of document, in this case it is HTML. All the metadata goes in the <code>head</code> section, and the actual content goes in the <code>body</code> section.

#### Short summary

The following tags are used to create the document structure:

* <code>html</code> - includes the whole document; it frequently has the language set, for example, 'lang="en"' 
* <code>head</code> - metadata information such as document title, character encoding, link to stylesheets, etc.
* <code>body</code> - everything that is displayed on the page, the actual content.

### Tags and attributes

The whole HTML language is built around tags and their attributes. There really are a multitude of them, yet only a handful are used in practice.

Complete list can be found [here](https://developer.mozilla.org/de/docs/Web/HTML/Element). 

#### Example

Let's take a look at some made up tags:

```html
<outerTag>
    <innerTag> Content goes here</innerTag>
</outerTag>
```

Those tags don't exist in the real world, but they show how every other tag is used. There is an opening tag, then you may add some information, and finally you close the tag. You can put another tag inside the body of a tag. 

### Void elements

Void elements are tags that don't contain any content. They are used to create empty elements.

##### Example

An example of a void element:

```html
<img src='example.img' alt='a cute puppy'>
```

### Div and span

Div and span are used to separate the document's body into logical sections. Div is an abbreviation for divider. It has no effect on the content, but it becomes quite handy if you start using CSS. Spans are similar to divs, except that they are used to denote specific items rather than entire blocks. ck.

#### Example

You can put a span inside a div:

```html
<div>
    <span>This is a span</span>
</div>
```

It is illegal to put a div inside a span. The following is not a valid HTML:

```html
<span> This is a <div>This is a div</div> span.</span>
```

## Head

Here goes all the metadata information. It is important to include the title of the page, the character encoding, and the link to the stylesheet. 

### Title

document title that appears in the window bar:

#### Example

```html
<title>my website</title>
```

### Meta

Meta tags are used to specify metadata information about the document.

1. charset

    In order to specify the character encoding of the document, you can use the <code>charset</code> attribute.

    ```html
    <meta charset="UTF-8">
    ```

1. viewport

    The mobile devices assume that the website is not using media queries for responsive design (it will be discussed in detail in CSS section). The viewport tag is used to tell the browser that media queries were indeed used.

    ```html
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ```

1. description

    Search engines use the description to position the website in the search results.

    ```html
    <meta name="description" content="This is a description">
    ```

1. keywords

    Keywords may also be used to position the website in the search results.

    ```html
    <meta name="keywords" content="keyword1, keyword2, keyword3">
    ```

### Favicon

Favicon is the icon that is displayed in the website tab.

#### Example

Let's take a look at a simple favicon:

```html
<link rel="icon" href="favicon.ico" type="image/x-icon" />
```

#### Additional explanations

* If no explicit link is present, browsers will look for a `favicon.ico` file in the root directory of the website.

## Readonly elements

Some elements are only used for displaying information and users can't interact with them. We can call them readonly elements.

### Headers and paragraphs

Basic elements that are used to display text in a document are headers and paragraphs. Headers are used to display titles and paragraphs are used to display large amounts of text. There are many levels of headers, from H1 to H6.

##### Example

```html
<h1>This is a header</h1>
<p>This is a paragraph</p>
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182040915-c8e8130a-0c6d-49fc-a995-a632ef1404f9.PNG" width=400 />
</p>

### Links

Links are used to link to other pages. When clicked, the user is taken to the linked page.

##### Example

The link below will take the user to the [Wikipedia](https://en.wikipedia.org/) website.

```html
<a href="https://en.wikipedia.org/wiki/HTML">Wikipedia</a>
```

This link will trigger email client to send an email to the address `foo@bar.com`:

```html
<a href="mailto:foo@bar.com">send e-mail</a>
```

You may also connect links to files stored on the server. Users may download the file by clicking on the link: 

```html
<a href="report.txt" download>report</a>
```

### Lists

To display a list of items, we use lists. There are two types of lists: ordered and unordered.

#### Example

An example of unordered list:

```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182040923-f4a11b95-db36-424d-9211-ec4a5210cafa.PNG" width=400 />
</p>

#### Short summary

The following tags are used to create lists:

* <code>ul</code> - unordered list
* <code>ol</code> - ordered list
* <code>li</code> - list item

### Tables
Tables are used to display data using rows and columns of cells.

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
        <td>Cell 4</td>
        <td>Cell 5</td>
        <td>Cell 6</td>
    </tr>
</table>
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182040934-309078e7-21c4-4df2-9507-1df7727e448d.PNG" width=400 />
</p>

#### Short summary

The following tags are used to create tables:

* <code>table</code> - table
* <code>tr</code> - table row
* <code>th</code> - table header
* <code>td</code> - table cell

## Interactive elements

As opposed to readonly elements, there are some elements that users can interact with and trigger actions based on their state.

### Buttons

Buttons are used to trigger actions. They are used to submit forms, to open links, and to trigger media playback.

#### Example

A simple button:

```html
<button type="submit">press me!</button>
```

Whenever the button is clicked, the event handler will be triggered.

#### Short summary

There are following types of buttons:

* <code>button</code> - default button
* <code>submit</code> - used for submitting forms
* <code>reset</code> - used to reset form fields

### Input

Input is used to collect data from the user.

#### Example

A simple example with placeholder text:

```html
<input type="text" placeholder="enter your name" />
```

A more complex example with a label and validation:

```html
<label for="name">Name</label>
<input type="text" id="name" name="name" minlength="3" maxlength="10" required />
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182040948-47409f3a-8c7f-4ea9-af09-f0e5c879c115.gif" width=400 />
</p>

#### Short summary

Input can be one of the many types. The default type is <code>text</code>. Other types include:

* <code>text</code>
* <code>password</code>
* <code>email</code>
* <code>number</code>
* <code>radio</code>
* <code>checkbox</code>
* <code>search</code>

Input attributes include:

* <code>placeholder</code> - text that appears in the input when it is empty
* <code>autofocus</code> - input is focused when the page loads
* <code>disabled</code> - input is disabled
* <code>readonly</code> - input is readonly
* <code>size</code> - size of the input
* <code>list</code> - list of options for the input

Possible values for the <code>validation</code> attribute:

* <code>minlength</code> - minimum length of the input
* <code>maxlength</code> - maximum length of the input
* <code>required</code> - input is required

### Forms

Forms are way of grouping many inputs in a signle structure.

#### Example

Let's create a simple form:

```html
<form>
    <label for="name">Name</label>
    <input type="text" id="name" name="name" />
    <button type="submit">Submit</button>
</form>
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182040111-83eb46cb-e751-43b2-b2a6-30c33968e4f7.gif" width=400 />
</p>

In this example, there is a single input field with a label. The label is used to describe the input. The input is used to collect data from the user. The button is used to submit the form.

#### Short summary

* <code>form</code> - form
* <code>label</code> - label
* <code>input</code> - input
* <code>button</code> - button

### Text area

Inputs are great, but they are displayed as a single line. Sometimes we need to collect more than one line of text and then we use text areas.

#### Example

Let's take a look at the following example:

```html
<textarea name="description" rows="5" cols="50">
  Enter your description here
</textarea>
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182040961-353c0cbd-bb50-4aef-ae24-1187055478c2.gif" width=400 />
</p>

In the example above, we have a text area with a name `description` which consists of 5 rows and 50 columns.

## Style

For styling elements, we generally use CSS. There are however some ways to style text using only HTML.

### Text formatting

Text formatting includes making text bold, italic, underlined, and strikethrough.

#### Example

The following example shows how to make text bold:

```html
<p>This is <b>bold</b> text.</p>
```

#### Short summary

* <code>b</code> or <code>strong</code> - bold text
* <code>i</code> or <code>em</code> - italic text
* <code>u</code> - underline
* <code>s</code> - strikethrough

### Special characters

There are some special characters that should be escaped in HTML in order to be correctly displayed in the browser.

#### Example

```html
<p>This is &lt;b&gt;bold&lt;/b&gt; text.</p>
```

#### Short summary

The following characters should always be escaped:

* <code>&</code> - ampersand is escaped by using <code>&amp;</code>
* <code>&lt;</code> - less than is escaped by using <code>&amp;lt;</code>
* <code>&gt;</code> - greater than is escaped by using <code>&amp;gt;</code>
* <code>&quot;</code> - double quote is escaped by using <code>&amp;quot;</code>

### Whitespace

Any sequence of whitespace characters (space, line break, tab) is treated as a single space in HTML. 

## Media

We may use three types of media:

* Images.
* Videos.
* Audio.

### Image

Images are specified using the <code>img</code> tag.

#### Example

Let's take a look at the following example:

```html
<img src="https://placekitten.com/g/200/300" srcset="https://placekitten.com/g/400/600 400w, https://placekitten.com/g/600/900 600w, https://placekitten.com/g/800/1200 800w" alt="A cute cat">
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182040980-77075cbc-5d7a-4841-95d0-d0dddd68a700.PNG" width=400 />
</p>

We use the `srcset` attribute to specify multiple image paths for different resolutions. The first image path is the one that is displayed by default.

#### Short summary

The following attributes are used to specify images:

* <code>src</code> - path to the image
* <code>srcset</code> - multiple paths to the image
* <code>alt</code> - alternative text in case the image cannot be displayed

Some of the commenly used image formats are:

* <code>jpg</code> - JPEG image
* <code>jpeg</code> - JPEG image
* <code>png</code> - PNG image
* <code>gif</code> - GIF image
* <code>svg</code> - SVG image

### Video

Videos are specified using the <code>video</code> tag.

#### Example

Let's take a look at the following example:

```html
<video controls>
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm" type="video/webm">
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
```

A video can have multiple sources. The first source is the one that is displayed by default. The second source is used if the first source is not supported. Finally, the text `Your browser does not support HTML5 video.` is displayed if the browser does not support any of the formats.

#### Short summary

The following attributes are used to specify videos:

* <code>src</code> - path to the video
* <code>type</code> - type of the video
* <code>controls</code> - video is displayed with controls
* <code>autoplay</code> - video is played automatically
* <code>loop</code> - video is played in a loop

Some of the commenly used video formats are:

* <code>webm</code> - WebM video
* <code>mp4</code> - MP4 video

### Audio

Audio is specified using the <code>audio</code> tag.

#### Example

Let us take a look at the following example:

```html
<audio controls>
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3" type="audio/mpeg">
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.ogg" type="audio/ogg">
  Your browser does not support the audio element.
</audio>
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182039844-a5a417ef-71e7-4329-9483-5e176c20448b.gif" width=400 />
</p>

The first source is the one that is played by default. The second source is used if the first source is not supported. Finally, the text `Your browser does not support the audio element.` is displayed if the browser does not support any of the formats.

#### Short summary

The following attributes are used to specify audio:

* <code>src</code> - path to the audio
* <code>type</code> - type of the audio
* <code>controls</code> - audio is displayed with controls
* <code>autoplay</code> - audio is played automatically
* <code>loop</code> - audio is played in a loop

The following are some of the commonly used audio formats:

* <code>mp3</code> - MP3 audio
* <code>wav</code> - WAV audio

## Best practices

* Use HTML5.
* Use tags and attributes according to their purpose.
* Don't use XML declarations.
* Use UTF-8.
* Use comments to explain code.
* Use semantic tags like: article, time and header.
* For each block, list, or table element, create a new line and indent each such child element.
* When quoting attribute values, use double quotation marks.
* Use `P` tags for paragraphs over multiple `<br>`.
* Do not use tables for layout.
* Omit type tag for CSS/JS link tag.
* Define `title`.
* Define the `body` tag.
* Use h1-h6 to outline the page content.
* Adding `alt` text to your images can improve user experience.
* Close every tag that you open.
* Avoid inline styles.
* Do not inline any JavaScript code.
* Lowercase tag names.
* Explicitly label controls (no `<div class="button">`).
* Stop putting refrences to JavaScript files at the bottom of your document. Use defer attribute (`<script src="app.js" defer \>`).
* Remove trailing white spaces.
* Keep the indentation consistent.

## Links

* http://isobar-idev.github.io/code-standards/
* http://learn.shayhowe.com/html-css/writing-your-best-code/
* https://www.webaccessibility.com/best_practices.php
* https://github.com/hail2u/html-best-practices
* Formatter: https://duckduckgo.com/?t=ffab&q=html+beautifier&ia=answer
