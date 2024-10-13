## HTML

* Hypertext Markup Language (HTML)
* The "nouns" of the web
* Lays down the basic structure of web pages

### Key Points about HTML

- HTML, or **Hypertext Markup Language**, is a standard markup language used to create and structure web pages on the internet.
- In the context of **web development**, HTML forms the backbone of web pages, providing essential structure, while CSS adds styling, and JavaScript enables interactivity.
- HTML is composed of **elements and tags**, where each element is represented by a tag, such as `<p>` for paragraphs, `<a>` for links, and `<img>` for images.
- **Attributes** in HTML provide additional information about elements. For example, an `<img>` tag uses the `src` attribute to specify the image source, and the `alt` attribute for a textual description.
- **Semantic elements** like `<header>`, `<footer>`, `<article>`, and `<nav>` are used to define the purpose and structure of different content areas, enhancing both accessibility and SEO.
- HTML allows for the use of **containers**, such as `<div>` and `<span>`, to group and organize content, making it easier to apply styles and manage layout.

### Skills Every HTML Developer Should Have

1. A solid grasp of **basic tags** is essential, including tags like `<h1>` for headers, `<p>` for paragraphs, `<ul>` for lists, and others that define page content.
2. Understanding the **document structure** is crucial, as an HTML document is organized with a `<head>` for metadata, a `<body>` for content, and commonly includes `<header>` and `<footer>` sections.
3. Familiarity with **forms and inputs** is important, as they allow user interactions. Tags like `<form>`, `<input>`, `<textarea>`, and `<button>` enable data collection on websites.
4. Knowing how to **embed media** such as images, videos, and audio into web pages enriches the user experience. Tags like `<img>`, `<video>`, and `<audio>` facilitate this process.
5. The ability to **link content** is key to web navigation. The `<a>` tag is used to create hyperlinks to other pages or external resources, providing essential connectivity.
6. **Responsive design** skills are necessary, as HTML developers need to ensure that web content is accessible and looks good across various devices and screen sizes.
7. It’s useful to **reference resources like MDN** (Mozilla Developer Network) for up-to-date documentation, examples, and best practices for writing effective HTML code.
8. A valuable skill is the ability to **recreate web pages** using HTML, ensuring that the developer can accurately mirror design specifications and build functional, accessible content layouts.

### Document Structure

The HTML document structure provides a standardized way to structure content on the web. Adhering to this structure ensures browser compatibility and proper rendering of web pages.

Below is a foundational structure of an HTML document:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Document</title>
</head>

<body>
    <!-- Content goes here -->
</body>

</html>
```

- The `<!DOCTYPE html>` declaration is an essential **instruction** for web browsers, identifying the document as HTML5. This declaration ensures that browsers interpret the page using the standards of HTML5.
- In the `<html lang="en">` element, the **root** of any HTML page is defined. The `lang` attribute, set to "en" in this example, indicates the primary language of the content, which aids in both accessibility and search engine optimization.
- The `<head>` section of an HTML document is a **container** for metadata. Metadata in this section influences how the page is processed by browsers and understood by search engines.
- With `<meta charset="UTF-8">`, the document’s character encoding is set to UTF-8, which supports nearly all **writing** systems worldwide. This encoding is vital for ensuring proper display of text across different languages and characters.
- The `<meta name="viewport" content="width=device-width, initial-scale=1.0">` tag is a **key** component for responsive design. By setting the viewport width to the device width, it ensures the page adjusts properly on various devices, particularly mobile phones and tablets.
- The `<title>` tag specifies the **name** of the document, which appears in the browser tab. An informative and relevant title is crucial for both user experience and search engine optimization, as it describes the page’s content.
- The `<body>` tag is the **main** container for all visible content on the page. Any text, images, videos, and other elements intended for display to the user are included within this tag, making it the core of the HTML document for content rendering.

### Head

The `<head>` section of an HTML document contains metadata (information about the document) and links to resources like stylesheets, scripts, and favicons. While not directly displayed to users, its contents influence how browsers present the page and how search engines interpret it.

#### The Document's Title

The `<title>` tag defines the title of the document, which appears in the browser's title bar or tab. 

Here is an example:

```html
<title>My Awesome Website</title>
```

#### Metadata Information

`<meta>` tags provide additional details about the document, influencing its behavior on devices and its appearance in search results.

1. **Character Encoding**: The charset attribute defines the character encoding for the webpage. This ensures characters display correctly across all browsers.

``` html
<meta charset="UTF-8">
```

2. **Viewport**: This tag optimizes display settings for mobile devices, ensuring a responsive design. It's essential for modern web development to accommodate varying screen sizes.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

3. **Description**: Provides a brief summary of the page's content. This is often displayed in search engine results, affecting click-through rates.

```html
<meta name="description" content="Discover the latest updates and features of My Awesome Website.">
```

4. **Keywords**: While modern search engines don't heavily rely on this metadata for ranking, it can still be included for potential SEO benefits.

```html
<meta name="keywords" content="innovation, tech, design">
```

5. **Favicon**: The favicon (short for "favorite icon") represents the website in browser tabs, bookmarks, and other UI elements.

```html
<link rel="icon" href="favicon.ico" type="image/x-icon">
```

If the website does not provide an explicit favicon link in the `<head>`, browsers default to searching for a file named favicon.ico in the website's root directory.

### Tags and Attributes

At the core of HTML lies the concept of tags and attributes. These elements enable the creation of structured documents and provide a way to describe the content's presentation and semantic meaning.

While a vast number of tags are defined in the HTML specification, only a subset is frequently used in day-to-day web development. For a comprehensive list of all available tags, refer to the [MDN's HTML element reference](https://developer.mozilla.org/de/docs/Web/HTML/Element).

#### How Tags Work

HTML tags represent elements and come in pairs: an opening tag and a closing tag. The content of the element resides between these tags. Some tags, called void elements (like `<img>` and `<br>`), don't have a closing tag.

```html
<elementName> Content of the element </elementName>
```

#### Nesting Tags

It's common in HTML to nest one tag within another, establishing a parent-child relationship between the elements.

```html
<parentElement>
    <childElement> Content inside child element </childElement>
</parentElement>
```

This hierarchical structure forms the basis for the Document Object Model (DOM), a tree-like representation of the content.

#### Attributes

Attributes provide additional information about an element and are always specified in the opening tag. They come in `name/value` pairs like this: `name="value"`.

For instance, the <a> tag often uses the href attribute to specify the link destination:

```html
<a href="https://www.example.com">Visit Example</a>
```

In this example, href is the attribute name, and `https://www.example.com` is its value.

### Void (Self-closing) Elements in HTML

Void elements, also known as self-closing elements, are unique HTML tags that don't require a closing tag. While they don't wrap around content, they can have attributes which give them functionality or provide additional context.

#### Characteristics

- Void elements are unique among HTML elements because they lack a **closing tag**. Unlike regular elements that enclose content, void elements are self-contained and do not need a separate end tag.
- Although void elements do not have any **content** between an opening and closing tag, they can still include attributes. These attributes offer further details or define specific behaviors for the element, enhancing its functionality within the document.

#### Examples

- `<img>`: This is used to embed images in a document. It often comes with attributes such as `src` (which specifies the URL of the image) and `alt` (which provides an alternate description for the image, aiding accessibility).

```html
<img src='example.jpg' alt='a cute puppy'>
```

- `<br>`: Represents a line break. Useful for creating breaks inside paragraphs or other inline-level content.

```html
This is some text.<br>And this is a new line.
```

- `<input>`: Used within forms to let users input data. It can have a variety of types like text, radio, checkbox, etc.

```html
<input type="text" name="username" placeholder="Enter your username">
```

- `<hr>`: Produces a thematic break or a horizontal rule. It's often used to separate content sections.

```html
<hr>
```

- `<meta>`, `<link>`, and `<area>` are other examples of void elements.

### Grouping elements

In HTML, `div` and `span` are two of the most versatile elements used to control and group content for various purposes, especially when combined with CSS.

#### Understanding `div`

- The `div` element, short for "division," is a **block-level** container that serves to group content and organize sections within a webpage. It helps structure different parts of the page visually and functionally.
- By default, a `div` occupies the **entire width** of its parent container, forming a block on the page. This block-level nature distinguishes it from inline elements.
- While the `div` element itself lacks **semantic** meaning, it is widely used as a generic container. It becomes more meaningful when combined with CSS classes or IDs for styling, or with JavaScript for added interactivity.

#### Understanding `span`

- The `span` element functions as an **inline-level** container, making it ideal for isolating specific pieces of content within a larger block. For example, it can be used to highlight text or wrap icons within a paragraph without disrupting the line flow.
- Unlike `div`, a `span` does not create a **new line** but stays inline with other content, making it suitable for small adjustments within text or images.
- Similar to `div`, the `span` element is **non-semantic**, meaning it has no inherent meaning on its own. It is primarily utilized to apply specific styles or scripts to targeted portions of content within a document.

Examples:

- Grouping content with `div`:

```html
<div class="section">
  <p>This is a paragraph within a div.</p>
</div>
```

- Highlighting text with `span`:

``` html
<p>This is a <span class="highlight">highlighted</span> text.</p>
```

- Nesting a span within a div is a common practice:

```html
<div>
    <span>This is a span inside a div.</span>
</div>
```

However, since div is a block-level element and span is an inline-level element, placing a div inside a span is considered incorrect and goes against HTML specifications:

```html
<!-- Incorrect Usage -->
<span> This is a <div>This is a div</div> span.</span>
```

### Readonly elements

Some elements are only used for displaying information and users can't interact with them. We can call them readonly elements.

#### Headers and paragraphs

Basic elements that are used to display text in a document are headers and paragraphs. Headers are used to display titles and paragraphs are used to display large amounts of text. There are many levels of headers, from H1 to H6.

Example:

```html
<h1>This is a header</h1>
<p>This is a paragraph</p>
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182040915-c8e8130a-0c6d-49fc-a995-a632ef1404f9.PNG" width=400 />
</p>

#### Links

Links are used to link to other pages. When clicked, the user is taken to the linked page.

Example:

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

#### Lists

To display a list of items, we use lists. There are two types of lists: ordered and unordered.

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

Short summary:

The following tags are used to create lists:

| Element | Description                  | Usage                              | Example                        |
|---------|------------------------------|------------------------------------|--------------------------------|
| `<ul>`  | Unordered List               | Creates a bulleted list            | `<ul><li>Item</li></ul>`       |
| `<ol>`  | Ordered List                 | Creates a numbered list            | `<ol><li>Item</li></ol>`       |
| `<li>`  | List Item                    | Represents an item within a list   | `<ul><li>First item</li></ul>` |

#### Tables
Tables are used to display data using rows and columns of cells.

Example:

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

Short summary:

The following tags are used to create tables:

| Element | Description                  | Usage                                   | Example                                 |
|---------|------------------------------|-----------------------------------------|-----------------------------------------|
| `<table>` | Table                      | Defines a table                         | `<table><tr><td>Data</td></tr></table>` |
| `<tr>`  | Table Row                    | Defines a row within a table            | `<tr><td>Data</td></tr>`                |
| `<th>`  | Table Header                 | Defines a header cell in a table row    | `<tr><th>Header</th></tr>`              |
| `<td>`  | Table Cell                   | Defines a standard cell within a row    | `<tr><td>Data</td></tr>`                |


### Interactive elements

As opposed to readonly elements, there are some elements that users can interact with and trigger actions based on their state.

#### Buttons

Buttons are used to trigger actions. They are used to submit forms, to open links, and to trigger media playback.

A simple button:

```html
<button type="submit">press me!</button>
```

Whenever the button is clicked, the event handler will be triggered.

Short summary:

There are following types of buttons:

| Element          | Description                    | Usage                                     | Example                                       |
|------------------|--------------------------------|-------------------------------------------|-----------------------------------------------|
| `<button>`       | Default Button                 | Creates a clickable button                | `<button>Click Me</button>`                   |
| `<input type="submit">` | Submit Button           | Submits form data to a server             | `<input type="submit" value="Submit">`        |
| `<input type="reset">`  | Reset Button            | Resets all fields in a form to default values | `<input type="reset" value="Reset">`      |

#### Input

Input is used to collect data from the user.

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

Short summary:

Input can be one of the many types. The default type is <code>text</code>. Other types include:

| Element                    | Description                        | Usage                                    | Example                                      |
|----------------------------|------------------------------------|------------------------------------------|----------------------------------------------|
| `<input type="text">`      | Text Input                         | Creates a single-line text input field   | `<input type="text" placeholder="Name">`     |
| `<input type="password">`  | Password Input                     | Creates a field for entering passwords   | `<input type="password" placeholder="Password">` |
| `<input type="email">`     | Email Input                        | Creates a field for email addresses      | `<input type="email" placeholder="Email">`   |
| `<input type="number">`    | Number Input                       | Creates a field for numeric input        | `<input type="number" min="0" max="10">`     |
| `<input type="radio">`     | Radio Button                       | Creates a radio button for selection     | `<input type="radio" name="gender" value="male">` |
| `<input type="checkbox">`  | Checkbox                           | Creates a checkbox for selection         | `<input type="checkbox" name="agree">`       |
| `<input type="search">`    | Search Input                       | Creates a search field                   | `<input type="search" placeholder="Search...">` |

Input attributes include:

| Attribute         | Description                              | Usage                                   | Example                                                |
|-------------------|------------------------------------------|-----------------------------------------|--------------------------------------------------------|
| `placeholder`     | Text that appears when input is empty    | Provides a hint inside the input field  | `<input type="text" placeholder="Enter name">`         |
| `autofocus`       | Input is focused when the page loads     | Sets the initial focus to this input    | `<input type="text" autofocus>`                        |
| `disabled`        | Input is disabled                        | Prevents input and makes it non-editable| `<input type="text" disabled>`                         |
| `readonly`        | Input is readonly                        | Makes the input non-editable but selectable | `<input type="text" readonly>`                     |
| `size`            | Size of the input field                  | Defines the width of the input (in characters) | `<input type="text" size="20">`               |
| `list`            | List of options for the input            | Links input to a `<datalist>` for suggested options | `<input type="text" list="options"><datalist id="options"><option value="Option1"><option value="Option2"></datalist>` |

Possible values for the <code>validation</code> attribute:

| Attribute     | Description                              | Usage                                     | Example                                        |
|---------------|------------------------------------------|-------------------------------------------|------------------------------------------------|
| `minlength`   | Minimum length of the input              | Specifies the minimum number of characters | `<input type="text" minlength="5">`            |
| `maxlength`   | Maximum length of the input              | Specifies the maximum number of characters | `<input type="text" maxlength="10">`           |
| `required`    | Input is required                        | Makes the input mandatory before submission| `<input type="text" required>`                 |

#### Forms

Forms are way of grouping many inputs in a signle structure.

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

Short summary:

| Element          | Description                              | Usage                                    | Example                                      |
|------------------|------------------------------------------|------------------------------------------|----------------------------------------------|
| `<form>`         | Form container                           | Wraps form elements and allows data submission | `<form action="/submit" method="post">...</form>` |
| `<label>`        | Label                                    | Provides a label for an input, aiding accessibility | `<label for="username">Username:</label>` |
| `<input>`        | Input field                              | Allows various types of user input, such as text, email, and password | `<input type="text" id="username">`      |
| `<button>`       | Button                                   | Creates a clickable button for form actions, such as submit or reset | `<button type="submit">Submit</button>` |

#### Text area

Inputs are great, but they are displayed as a single line. Sometimes we need to collect more than one line of text and then we use text areas.

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

### Style

For styling elements, we generally use CSS. There are however some ways to style text using only HTML.

#### Text formatting

Text formatting includes making text bold, italic, underlined, and strikethrough.

The following example shows how to make text bold:

```html
<p>This is <b>bold</b> text.</p>
```

Short summary:

| Element           | Description                   | Usage                                    | Example                                      |
|-------------------|-------------------------------|------------------------------------------|----------------------------------------------|
| `b` or `strong`   | Bold Text                     | Emphasizes text by making it bold        | `b Bold Text b`, `strong Bold Text strong`   |
| `i` or `em`       | Italic Text                   | Emphasizes text by making it italicized  | `i Italic Text i`, `em Italic Text em`       |
| `u`               | Underline                     | Underlines the text                      | `u Underlined Text u`                        |
| `s`               | Strikethrough                 | Adds a strikethrough effect to the text  | `s Strikethrough Text s`                     |

#### Special characters

There are some special characters that should be escaped in HTML in order to be correctly displayed in the browser.

Example:

```html
<p>This is &lt;b&gt;bold&lt;/b&gt; text.</p>
```

Short summary:

The following characters should always be escaped:

| Character Entity   | Description                     | Usage                                    | Example                  |
|--------------------|----------------------------------|------------------------------------------|--------------------------|
| `&`                | Ampersand                        | Escaped by using `&amp;`                 | `&amp;`                  |
| `&lt;`             | Less Than                        | Escaped by using `&amp;lt;`              | `&amp;lt;`               |
| `&gt;`             | Greater Than                     | Escaped by using `&amp;gt;`              | `&amp;gt;`               |
| `&quot;`           | Double Quote                     | Escaped by using `&amp;quot;`            | `&amp;quot;`             |

#### Whitespace

Any sequence of whitespace characters (space, line break, tab) is treated as a single space in HTML. 

### Media

We may use three types of media:

* Images.
* Videos.
* Audio.

#### Image

Images are specified using the <code>img</code> tag.

Let's take a look at the following example:

```html
<img src="https://placekitten.com/g/200/300" srcset="https://placekitten.com/g/400/600 400w, https://placekitten.com/g/600/900 600w, https://placekitten.com/g/800/1200 800w" alt="A cute cat">
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/37275728/182040980-77075cbc-5d7a-4841-95d0-d0dddd68a700.PNG" width=400 />
</p>

We use the `srcset` attribute to specify multiple image paths for different resolutions. The first image path is the one that is displayed by default.

Short summary:

The following attributes are used to specify images:

| Attribute  | Description                           | Usage                                       | Example                                                    |
|------------|---------------------------------------|---------------------------------------------|------------------------------------------------------------|
| `src`      | Path to the image                     | Specifies the image file location           | `img src="image.jpg" alt="Description"`                     |
| `srcset`   | Multiple paths to the image           | Provides multiple image sources for different resolutions | `img src="image.jpg" srcset="image-2x.jpg 2x" alt="Description"` |
| `alt`      | Alternative text                      | Displays text if the image cannot be loaded | `img src="image.jpg" alt="Description"`                     |

Some of the commenly used image formats are:

| Format  | Description        | Usage                        | Example File Extension               |
|---------|--------------------|------------------------------|---------------------------------------|
| `jpg`   | JPEG image         | Used for photographs and complex images with gradients | `image.jpg`                           |
| `jpeg`  | JPEG image         | Same as `jpg`, often interchangeable | `image.jpeg`                          |
| `png`   | PNG image          | Supports transparency, good for graphics and icons | `image.png`                           |
| `gif`   | GIF image          | Supports animation, limited color palette | `image.gif`                           |
| `svg`   | SVG image          | Vector format, scalable without quality loss | `image.svg`                           |

#### Video

Videos are specified using the <code>video</code> tag.

Let's take a look at the following example:

```html
<video controls>
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm" type="video/webm">
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
```

A video can have multiple sources. The first source is the one that is displayed by default. The second source is used if the first source is not supported. Finally, the text `Your browser does not support HTML5 video.` is displayed if the browser does not support any of the formats.

Short summary:

The following attributes are used to specify videos:

| Attribute  | Description                          | Usage                                      | Example                                                   |
|------------|--------------------------------------|--------------------------------------------|-----------------------------------------------------------|
| `src`      | Path to the video                    | Specifies the video file location          | `video src="video.mp4" controls`                           |
| `type`     | Type of the video                    | Specifies the video format (e.g., `video/mp4`) | `source src="video.mp4" type="video/mp4"`              |
| `controls` | Video with playback controls         | Displays play, pause, and volume controls  | `video src="video.mp4" controls`                           |
| `autoplay` | Automatically plays the video        | Begins playing the video upon page load    | `video src="video.mp4" autoplay`                           |
| `loop`     | Video plays in a loop                | Repeats the video automatically when it ends | `video src="video.mp4" loop`                            |

Some of the commenly used video formats are:

| Format  | Description         | Usage                                    | Example File Extension  |
|---------|---------------------|-------------------------------------------|--------------------------|
| `webm`  | WebM video          | Open, compressed format for web videos    | `video.webm`             |
| `mp4`   | MP4 video           | Widely used video format compatible with most devices | `video.mp4`              |

#### Audio

Audio is specified using the <code>audio</code> tag.

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

Short summary:

The following attributes are used to specify audio:

| Attribute  | Description                          | Usage                                      | Example                                                    |
|------------|--------------------------------------|--------------------------------------------|------------------------------------------------------------|
| `src`      | Path to the audio                    | Specifies the audio file location          | `audio src="audio.mp3" controls`                           |
| `type`     | Type of the audio                    | Specifies the audio format (e.g., `audio/mpeg`) | `source src="audio.mp3" type="audio/mpeg"`            |
| `controls` | Audio with playback controls         | Displays play, pause, and volume controls  | `audio src="audio.mp3" controls`                           |
| `autoplay` | Automatically plays the audio        | Begins playing the audio upon page load    | `audio src="audio.mp3" autoplay`                           |
| `loop`     | Audio plays in a loop                | Repeats the audio automatically when it ends | `audio src="audio.mp3" loop`                          |


The following are some of the commonly used audio formats:

| Format  | Description         | Usage                                  | Example File Extension  |
|---------|---------------------|-----------------------------------------|--------------------------|
| `mp3`   | MP3 audio           | Widely used for compressed audio files  | `audio.mp3`              |
| `wav`   | WAV audio           | Uncompressed, high-quality audio format | `audio.wav`              |

### Best Practices

#### General

* Use **version control systems** like Git to maintain a record of code changes, allowing for collaborative work and easier rollbacks when necessary.
* Regularly perform **validation checks** using tools such as the W3C HTML validator to ensure the quality and compliance of your code.
* Design with a **mobile-first** approach, so mobile users experience optimized functionality before scaling up for larger screens.
* Stick to **HTML5 standards**, taking advantage of the latest features and enhanced semantic capabilities it offers.
* Choose the **right tags and attributes** for each element, ensuring that they align with the content’s purpose and enhance readability.
* Include **comments** in the code to explain complex sections and document significant design decisions for future reference.

#### Formatting

* Adopt a **consistent naming convention** for classes and IDs, such as BEM or camelCase, to maintain code readability.
* For void elements, use **self-closing tags** like `<img src="..." alt="..." />` to improve readability and ensure the code conforms to modern standards.
* Increase **clarity through spacing** by starting new blocks, lists, or table elements on a new line and consistently indenting nested elements.
* Use **double quotation marks** for attribute values, maintaining consistency throughout your HTML.
* Stick to **lowercase tag names** for uniformity, as it is easier to read and more compatible with XHTML requirements.
* Remove unnecessary **whitespace** at the end of lines and ensure consistent indentation to improve code readability.

#### Semantic and Accessibility

* Leverage **semantic tags** like `article`, `time`, `header`, `nav`, and `aside` to structure content effectively, improving both SEO and accessibility.
* Represent **text blocks with paragraphs** using `<p>` tags instead of using `<br>` tags for spacing, maintaining a clean document structure.
* Limit **table usage** to tabular data presentation only, avoiding tables for page layout, which impacts accessibility and flexibility.
* Follow a logical **heading hierarchy** with tags from `<h1>` to `<h6>` to provide clear content structure for users and search engines.
* Always provide **alt descriptions** for images, which improves accessibility for users with visual impairments and aids in SEO.
* Use **genuine interactive controls** such as `<button>` and `<input>` instead of relying on non-semantic elements styled to look interactive.
* Implement **ARIA roles** to enhance accessibility, ensuring that users with disabilities can navigate the content effectively.
* Incorporate **skip navigation links** to allow keyboard and screen reader users to bypass repetitive elements and access the main content quickly.
* Label all **form controls** with the `<label>` tag to create accessible forms that are easier to use for screen reader users.

#### HTML Structure

* Include **metadata** tags such as `<meta name="author" content="...">` to provide essential information about the page to search engines and browsers.
* Set the **language attribute** on the `<html>` tag, specifying the primary language of the content, like `<html lang="en">` for English.
* Choose **UTF-8 encoding** in your documents to ensure compatibility with various languages and symbols, enhancing user experience globally.
* **Omit XML declarations** in HTML5 documents, as they are no longer required and can cause unnecessary complexity.
* Craft a **descriptive `<title>` tag** for each page to improve SEO and provide clear navigation information for users.
* Enclose the main content within the **`<body>` tag**, making it easier for browsers to locate and render the core elements of your page.
* Make sure that each **opening tag has a corresponding closing tag**, preserving the integrity of the document structure and avoiding rendering errors.

#### CSS and JavaScript Integration

* Maintain **separation of concerns** by keeping HTML for structure, CSS for styling, and JavaScript for behavior, enabling modular code management.
* Utilize **CSS custom properties** (variables) to simplify updates, enhance maintainability, and allow for consistent theming.
* Use **non-blocking JavaScript** techniques like `async` and `defer` attributes to prevent JavaScript from blocking the page's initial render.

#### Performance and Optimization

* Implement **lazy loading** for images and iframes to defer off-screen content, reducing initial load times and saving bandwidth.
* Inline **critical CSS** to ensure that above-the-fold content loads as quickly as possible, improving perceived load times.
* Utilize a **Content Delivery Network (CDN)** to distribute static assets, increasing load speed for users worldwide.
* Consider **server-side rendering (SSR)** for frameworks like React or Vue to reduce the time it takes for content to appear on the screen.
* Use **minification tools** to compress CSS and JavaScript, reducing file sizes and optimizing page load times.
* Ensure **responsive design** so the layout adapts smoothly across different devices and screen sizes for a better user experience.
* Optimize images using **compression tools and modern formats** to reduce file sizes without losing visual quality.
* Leverage **browser caching** by setting appropriate cache-control headers, minimizing load times for returning visitors and decreasing server requests.

#### Security

* Enforce **HTTPS** to secure data transmission, ensuring user data remains encrypted and protected from interception.
* Implement a **Content Security Policy (CSP)** to help prevent XSS attacks by controlling the sources from which content can be loaded.
* Prioritize **input sanitization** and validation for all user inputs, minimizing the risk of security vulnerabilities like SQL injection or XSS.

#### SEO (Search Engine Optimization)

* Structure content with a **clear semantic hierarchy** using heading tags, helping search engines better understand and index your content.
* Use **schema.org markup** to enhance search engines' ability to recognize and display relevant information about your site in search results.
* Generate and submit an **XML sitemap** to major search engines, improving the discoverability and crawlability of your site’s pages.

### Links

* [Isobar Code Standards](http://isobar-idev.github.io/code-standards/)
* [Writing Your Best Code](http://learn.shayhowe.com/html-css/writing-your-best-code/)
* [Web Accessibility Best Practices](https://www.webaccessibility.com/best_practices.php)
* [HTML Best Practices](https://github.com/hail2u/html-best-practices)
* [Formatter](https://duckduckgo.com/?t=ffab&q=html+beautifier&ia=answer)
