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

## Document Structure

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

- `<!DOCTYPE html>`: This declaration defines the document as an HTML5 document. It's a standard instruction to the web browser about what version of the HTML language the page is written in.

- `<html lang="en">`: The root element of an HTML page. The `lang` attribute specifies the language of the document's content, aiding in accessibility and search engine optimization.

  - `<head>`: This is a container for metadata (data about data). It typically includes:

    - `<meta charset="UTF-8">`: Sets the character set encoding type for the document. "UTF-8" encompasses almost all of the world's writing systems.

    - `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: An essential meta tag for responsive design. It ensures that the page scales and sizes correctly on different devices, especially mobile devices.

    - `<title>`: Represents the title of the document; it's what you see on the browser tab or window. A descriptive title is essential for SEO and usability.

  - `<body>`: The main content container. Everything that's displayed on the page (text, images, videos, etc.) goes here. It represents the content of an HTML document that is rendered in browsers.

## Head

The `<head>` section of an HTML document contains metadata (information about the document) and links to resources like stylesheets, scripts, and favicons. While not directly displayed to users, its contents influence how browsers present the page and how search engines interpret it.

### The Document's Title

The `<title>` tag defines the title of the document, which appears in the browser's title bar or tab. 

Here is an example:

```html
<title>My Awesome Website</title>
```

### Metadata Information

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

If the website does not provide an explicit favicon link in the <head>, browsers default to searching for a file named favicon.ico in the website's root directory.

## Tags and Attributes

At the core of HTML lies the concept of tags and attributes. These elements enable the creation of structured documents and provide a way to describe the content's presentation and semantic meaning.

While a vast number of tags are defined in the HTML specification, only a subset is frequently used in day-to-day web development. For a comprehensive list of all available tags, refer to the [MDN's HTML element reference](https://developer.mozilla.org/de/docs/Web/HTML/Element).

### How Tags Work

HTML tags represent elements and come in pairs: an opening tag and a closing tag. The content of the element resides between these tags. Some tags, called void elements (like `<img>` and `<br>`), don't have a closing tag.

```html
<elementName> Content of the element </elementName>
```

### Nesting Tags

It's common in HTML to nest one tag within another, establishing a parent-child relationship between the elements.

```html
<parentElement>
    <childElement> Content inside child element </childElement>
</parentElement>
```

This hierarchical structure forms the basis for the Document Object Model (DOM), a tree-like representation of the content.

### Attributes

Attributes provide additional information about an element and are always specified in the opening tag. They come in `name/value` pairs like this: `name="value"`.

For instance, the <a> tag often uses the href attribute to specify the link destination:

```html
<a href="https://www.example.com">Visit Example</a>
```

In this example, href is the attribute name, and `https://www.example.com` is its value.

## Void (Self-closing) Elements in HTML

Void elements, also known as self-closing elements, are unique HTML tags that don't require a closing tag. While they don't wrap around content, they can have attributes which give them functionality or provide additional context.

### Characteristics of Void Elements

1. **No Closing Tag**: Unlike regular HTML elements, void elements don't have a corresponding closing tag.

2. **Attributes**: Even though void elements don't contain content between an opening and closing tag, they can (and often do) contain attributes. These attributes provide additional information or specify behavior for the element.

### Examples of Void Elements

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

## Grouping elements

In HTML, `div` and `span` are two of the most versatile elements used to control and group content for various purposes, especially when combined with CSS.

### Understanding `div`

- **Purpose**: The `div` (short for "division") element is a block-level container that is used to group content and structure sections of a webpage.
  
- **Display**: By default, a `div` takes up the full width of its parent container, creating a "block" on the page.

- **Usage**: It doesn't have a semantic meaning by itself. Its primary use is as a generic container, often combined with CSS classes or IDs to apply styles or JavaScript for interactivity.

### Understanding `span`

- **Purpose**: The `span` element is an inline-level container. It's used to single out a specific piece of content within a block, such as highlighting a text portion or wrapping an icon within a paragraph.

- **Display**: Unlike `div`, a `span` doesn't create a new line; it remains inline with other content.

- **Usage**: Similar to `div`, `span` is non-semantic and is primarily used to apply styles or scripts to specific parts of the content.

#### Examples

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

## Best Practices

### General

* Use **version control systems** like Git to maintain a record of code changes, allowing for collaborative work and easier rollbacks when necessary.
* Regularly perform **validation checks** using tools such as the W3C HTML validator to ensure the quality and compliance of your code.
* Design with a **mobile-first** approach, so mobile users experience optimized functionality before scaling up for larger screens.
* Stick to **HTML5 standards**, taking advantage of the latest features and enhanced semantic capabilities it offers.
* Choose the **right tags and attributes** for each element, ensuring that they align with the content’s purpose and enhance readability.
* Include **comments** in the code to explain complex sections and document significant design decisions for future reference.

### Formatting

* Adopt a **consistent naming convention** for classes and IDs, such as BEM or camelCase, to maintain code readability.
* For void elements, use **self-closing tags** like `<img src="..." alt="..." />` to improve readability and ensure the code conforms to modern standards.
* Increase **clarity through spacing** by starting new blocks, lists, or table elements on a new line and consistently indenting nested elements.
* Use **double quotation marks** for attribute values, maintaining consistency throughout your HTML.
* Stick to **lowercase tag names** for uniformity, as it is easier to read and more compatible with XHTML requirements.
* Remove unnecessary **whitespace** at the end of lines and ensure consistent indentation to improve code readability.

### Semantic and Accessibility

* Leverage **semantic tags** like `article`, `time`, `header`, `nav`, and `aside` to structure content effectively, improving both SEO and accessibility.
* Represent **text blocks with paragraphs** using `<p>` tags instead of using `<br>` tags for spacing, maintaining a clean document structure.
* Limit **table usage** to tabular data presentation only, avoiding tables for page layout, which impacts accessibility and flexibility.
* Follow a logical **heading hierarchy** with tags from `<h1>` to `<h6>` to provide clear content structure for users and search engines.
* Always provide **alt descriptions** for images, which improves accessibility for users with visual impairments and aids in SEO.
* Use **genuine interactive controls** such as `<button>` and `<input>` instead of relying on non-semantic elements styled to look interactive.
* Implement **ARIA roles** to enhance accessibility, ensuring that users with disabilities can navigate the content effectively.
* Incorporate **skip navigation links** to allow keyboard and screen reader users to bypass repetitive elements and access the main content quickly.
* Label all **form controls** with the `<label>` tag to create accessible forms that are easier to use for screen reader users.

### HTML Structure

* Include **metadata** tags such as `<meta name="author" content="...">` to provide essential information about the page to search engines and browsers.
* Set the **language attribute** on the `<html>` tag, specifying the primary language of the content, like `<html lang="en">` for English.
* Choose **UTF-8 encoding** in your documents to ensure compatibility with various languages and symbols, enhancing user experience globally.
* **Omit XML declarations** in HTML5 documents, as they are no longer required and can cause unnecessary complexity.
* Craft a **descriptive `<title>` tag** for each page to improve SEO and provide clear navigation information for users.
* Enclose the main content within the **`<body>` tag**, making it easier for browsers to locate and render the core elements of your page.
* Make sure that each **opening tag has a corresponding closing tag**, preserving the integrity of the document structure and avoiding rendering errors.

### CSS and JavaScript Integration

* Maintain **separation of concerns** by keeping HTML for structure, CSS for styling, and JavaScript for behavior, enabling modular code management.
* Utilize **CSS custom properties** (variables) to simplify updates, enhance maintainability, and allow for consistent theming.
* Use **non-blocking JavaScript** techniques like `async` and `defer` attributes to prevent JavaScript from blocking the page's initial render.

### Performance and Optimization

* Implement **lazy loading** for images and iframes to defer off-screen content, reducing initial load times and saving bandwidth.
* Inline **critical CSS** to ensure that above-the-fold content loads as quickly as possible, improving perceived load times.
* Utilize a **Content Delivery Network (CDN)** to distribute static assets, increasing load speed for users worldwide.
* Consider **server-side rendering (SSR)** for frameworks like React or Vue to reduce the time it takes for content to appear on the screen.
* Use **minification tools** to compress CSS and JavaScript, reducing file sizes and optimizing page load times.
* Ensure **responsive design** so the layout adapts smoothly across different devices and screen sizes for a better user experience.
* Optimize images using **compression tools and modern formats** to reduce file sizes without losing visual quality.
* Leverage **browser caching** by setting appropriate cache-control headers, minimizing load times for returning visitors and decreasing server requests.

### Security

* Enforce **HTTPS** to secure data transmission, ensuring user data remains encrypted and protected from interception.
* Implement a **Content Security Policy (CSP)** to help prevent XSS attacks by controlling the sources from which content can be loaded.
* Prioritize **input sanitization** and validation for all user inputs, minimizing the risk of security vulnerabilities like SQL injection or XSS.

### SEO (Search Engine Optimization)

* Structure content with a **clear semantic hierarchy** using heading tags, helping search engines better understand and index your content.
* Use **schema.org markup** to enhance search engines' ability to recognize and display relevant information about your site in search results.
* Generate and submit an **XML sitemap** to major search engines, improving the discoverability and crawlability of your site’s pages.

## Links

* [Isobar Code Standards](http://isobar-idev.github.io/code-standards/)
* [Writing Your Best Code](http://learn.shayhowe.com/html-css/writing-your-best-code/)
* [Web Accessibility Best Practices](https://www.webaccessibility.com/best_practices.php)
* [HTML Best Practices](https://github.com/hail2u/html-best-practices)
* [Formatter](https://duckduckgo.com/?t=ffab&q=html+beautifier&ia=answer)
