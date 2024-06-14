# Quizzes on Frontend

This series of quizzes covers essential topics in web development, including:

- **HTML**: Test your knowledge of HTML elements, attributes, and best practices.
- **CSS**: Explore questions on styling, layout, and best practices for creating visually appealing web pages.
- **JavaScript**: Assess your understanding of JavaScript fundamentals, including variables, functions, asynchronous programming, and modern features like arrow functions and closures.
- **Protocols**: Learn about key protocols such as HTTP, HTTPS, SSL, and the differences between REST and SOAP.
- **Hosting**: Understand DNS, email setup, web hosting, and the costs associated with maintaining a website.

## HTML
<details>
<summary>What is a doctype?</summary><br>
A doctype declaration tells the web browser what version of HTML (or XML) the document is written in. It goes at the top of the HTML document, before the `html` tag. For HTML5, the doctype is simply: `!DOCTYPE html`.
</details>
<details>
<summary>Should I use HTML or XHTML?</summary><br>
HTML is generally preferred over XHTML for most web development purposes due to its greater flexibility and compatibility with modern web development techniques. XHTML, while stricter in its syntax, requires more effort to maintain and can cause compatibility issues with some web technologies.
</details>
<details>
<summary>How do I build menus?</summary><br>
Menus can be built using HTML unordered lists (`ul`) and list items (`li`). The menu items can be styled using CSS to create a desired visual appearance.
</details>
<details>
<summary>How do I build forms?</summary><br>
Forms can be built using HTML form elements (`form`, `input`, `select`, `textarea`, etc.). Each form element has attributes that define its behavior and appearance, and can be styled with CSS.
</details>
<details>
<summary>What is the purpose of a head tag if only the developers can see the information contained within it?</summary><br>
The `head` tag contains metadata about the document, including the document title, character encoding, CSS stylesheets, JavaScript code, and other information that is used by the web browser to interpret and display the content of the document.
</details>
<details>
<summary>What is the difference between a &lt;header&gt; and &lt;h1&gt; tag?</summary><br>
The `header` tag is used to hold introductory information about the material that will be shown, such as a logo, navigation links, or other site-wide content. The `h1` tag is a typography heading that represents the top-level heading of the page or section.
</details>
<details>
<summary>What is the purpose of the &lt;alt&gt; attribute in &lt;img&gt; tags?</summary><br>
The `alt` attribute provides an alternative text description for an image. It is used by screen readers and other assistive technologies for accessibility purposes, and it also serves as a fallback text in case the image fails to load.
</details>
<details>
<summary>What are semantic HTML elements?</summary><br>
Semantic HTML elements are tags that convey meaning about the structure and content of the document, making it easier for both developers and web browsers to understand the purpose of each element. Examples of semantic elements include `article`, `aside`, `figcaption`, `footer`, `header`, `main`, `mark`, `nav`, and `section`.
</details>
<details>
<summary>How do I create a table in HTML?</summary><br>
A table can be created using the `table` element, along with `tr` (table row), `th` (table header), and `td` (table data) elements. The structure of the table is defined by nesting `tr`, `th`, and `td` elements within the `table` element.
</details>
<details>
<summary>What are the main differences between HTML and CSS?</summary><br>
HTML (Hypertext Markup Language) is a markup language used to structure content on the web, while CSS (Cascading Style Sheets) is a stylesheet language used for describing the look and formatting of a document written in HTML. In other words, HTML is responsible for the content structure, and CSS is responsible for the visual presentation.
</details>
<details>
<summary>What is an &lt;iframe&gt; and when should I use it?</summary><br>
An `iframe` is an inline frame element that allows you to embed another HTML document within the current HTML document. It can be used for embedding content from external sources, such as maps, videos, or other web pages, without requiring the user to navigate away from the current page. However, `iframe` usage should be limited as it can cause accessibility and performance issues.
</details>

## CSS

<details>
<summary>How do I add CSS to a website?</summary><br>
CSS can be added to a website in several ways, including:

* Inline styles - using the `style` attribute on an HTML element.
* Internal styles - using a `style` tag in the `head` section of the HTML document.
* External styles - using a separate CSS file and linking to it from the HTML document using the `link` tag in the `head` section of the HTML document.
</details>
<details>
<summary>How can I have several pages use the same CSS style?</summary><br>
You can create a separate CSS file and link to it from each HTML document using the `link` tag in the `head` section of the HTML document.
</details>
<details>
<summary>How do I change the background color?</summary><br>
You can change the background color of an HTML element using the `background-color` property in CSS. For example: `body { background-color: #f0f0f0; }`
</details>
<details>
<summary>How do I remove blue outline on linked images?</summary><br>
You can remove the blue outline on linked images by setting the `outline` property to `none` in CSS. For example: `a img { outline: none; }`
</details>
<details>
<summary>Should I use px, pt or em?</summary><br>
The choice of measurement units (`px`, `pt`, `em`, etc.) in CSS depends on the specific use case and design requirements. Generally, `px` is a good choice for fixed sizes, such as border widths, while `em` or `rem` is better for scalable sizes, such as font sizes. `pt` is less commonly used in web development and is typically used for print design.
</details>
<details>
<summary>What is the difference between classes and IDs in CSS?</summary><br>
Classes and IDs are both selectors used to target HTML elements and apply styles to them. The main difference is that classes can be applied to multiple elements on a page, while IDs are unique and should only be applied to a single element. Additionally, classes use a period (`.`) prefix in the CSS, while IDs use a hash (`#`) prefix.
</details>
<details>
<summary>How do I center a block element horizontally?</summary><br>
To center a block element horizontally, you can set its `margin-left` and `margin-right` properties to `auto`, and specify a `width`. For example: `.centered { margin-left: auto; margin-right: auto; width: 50%; }`
</details>
<details>
<summary>What is the CSS box model?</summary><br>
The CSS box model is a rectangular layout paradigm used for all HTML elements. It consists of four areas: content, padding, border, and margin. The content area contains the actual content of the element, while the padding, border, and margin areas surround it, defining the space between the content and other elements on the page.
</details>
<details>
<summary>What is a CSS pseudo-class?</summary><br>
A CSS pseudo-class is a keyword added to a selector that specifies a special state of the selected element(s). Pseudo-classes allow you to style elements based on user interaction or the element's state. For example, the `:hover` pseudo-class targets an element when the user hovers over it, and the `:checked` pseudo-class targets a checkbox or radio button when it is selected.
</details>
<details>
<summary>What is the difference between `display: none` and `visibility: hidden` in CSS?</summary><br>
`display: none` completely removes the element from the page layout, causing other elements to fill the space it would have occupied. `visibility: hidden` hides the element visually, but the space it occupies in the layout remains. In other words, `display: none` affects the document flow, while `visibility: hidden` does not.
</details>
  
## JavaScript

<details>
<summary>Will my React-powered website only work in browsers that support React?</summary><br>
No, React-powered websites will work in any modern web browser, regardless of whether or not it supports React. React code is typically transpiled to standard JavaScript code that can be executed by any JavaScript engine.
</details>
<details>
<summary>Do my clients need to install Angular on their PCs and phones in order to browse an Angular-powered website?</summary><br>
No, clients do not need to install Angular on their PCs or phones in order to browse an Angular-powered website. The Angular code is typically compiled into standard HTML, CSS, and JavaScript that can be executed by any modern web browser.
</details>
<details>
<summary>What is JavaScript and what can it be used for?</summary><br>
JavaScript is a high-level, dynamic, and interpreted programming language that is primarily used for client-side web development. It allows developers to create interactive web pages and user interfaces, manipulate the contents of a web page, and communicate with web servers using asynchronous technology. It can also be used for server-side programming, desktop application development, and game development.
</details>
<details>
<summary>What is the difference between var, let, and const in JavaScript?</summary><br>
`var` is a keyword that declares a variable with function scope, meaning it can be accessed within the function it was declared in. `let` and `const` are newer keywords that declare variables with block scope, meaning they can only be accessed within the block they were declared in. The difference between `let` and `const` is that `let` declares a variable that can be reassigned a new value, while `const` declares a variable that cannot be reassigned after it has been assigned a value.
</details>
<details>
<summary>What is an object in JavaScript?</summary><br>
In JavaScript, an object is a collection of key-value pairs, where the keys are strings and the values can be any JavaScript data type, including other objects. Objects can be used to represent complex data structures, such as arrays, lists, or maps, and can be manipulated using various methods and functions.
</details>
<details>
<summary>What is a closure in JavaScript?</summary><br>
A closure is a function in JavaScript that has access to its own lexical scope, as well as the lexical scope of its outer functions, even after the outer functions have returned. This allows the function to "remember" the values of its variables and parameters, and to maintain state across multiple function calls. Closures are often used in event handlers, callbacks, and asynchronous programming.
</details>
<details>
<summary>What is the difference between synchronous and asynchronous code in JavaScript?</summary><br>
Synchronous code is executed in sequence, with each line of code waiting for the previous line to finish before executing. Asynchronous code, on the other hand, allows multiple lines of code to be executed simultaneously, without waiting for each other to finish. This is accomplished using callbacks, promises, or async/await syntax, which allow the code to continue executing while waiting for long-running tasks to complete.
</details>
<details>
<summary>What is the difference between == and === in JavaScript?</summary><br>
`==` is a loose equality operator that compares two values for equality after performing type coercion, meaning it will attempt to convert the values to a common type before comparing them. `===` is a strict equality operator that compares two values for equality without performing type coercion, meaning it will only return true if the values are of the same type and have the same value.
</details>
<details>
<summary>What is a callback function in JavaScript?</summary><br>
A callback function is a function that is passed as an argument to another function, and is executed when the parent function has completed its task. Callback functions are commonly used in JavaScript for event handling, asynchronous programming, and functional programming. They allow developers to create reusable and modular code that can be easily composed and extended.
</details>
<details>
<summary>What is the difference between a function declaration and a function expression in JavaScript?</summary><br>
A function declaration is a statement that creates a named function that can be called anywhere in the code, even before it is declared. A function expression, on the other hand, is an expression that creates an anonymous function that can only be called after it is assigned to a variable or passed as an argument to another function. Function expressions are often used to create callbacks or to create closures.
</details>
<details>
<summary>What is an arrow function in JavaScript?</summary><br>
An arrow function is a shorthand syntax for creating a function in JavaScript. It uses the `=` operator to separate the function parameters from the function body, and automatically returns the value of the function body without the need for a `return` statement. Arrow functions are often used to create concise and readable code, especially when used as callbacks or in functional programming.
</details>

## Protocols

<details>
<summary>What is SSL?</summary><br>
SSL (Secure Sockets Layer) is a security protocol used to establish a secure encrypted connection between a web server and a web browser. It ensures that data transmitted between the two is private and cannot be intercepted or modified by third parties.
</details>
<details>
<summary>What is HTTP?</summary><br>
HTTP (Hypertext Transfer Protocol) is a protocol used to transfer data over the World Wide Web. It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands and requests.
</details>
<details>
<summary>Why are there so many HTTP codes?</summary><br>
There are many HTTP status codes because they provide a standardized way for web servers and browsers to communicate the outcome of various requests and responses. The codes are grouped into several categories based on their general meaning, such as informational, success, redirection, client error, and server error.
</details>
<details>
<summary>What is an API?</summary><br>
API (Application Programming Interface) is a set of rules, protocols, and tools used for building software applications. APIs define how software components should interact with each other and provide a standardized way for applications to exchange data and services.
</details>
<details>
<summary>Do all APIs work the same way?</summary><br>
No, APIs can vary widely in their design and implementation depending on the specific use case and technology stack being used. However, most APIs follow certain common principles and standards, such as RESTful architecture, JSON or XML data formats, and HTTP or HTTPS protocols.
</details>
<details>
<summary>What is the difference between GET and POST requests in HTTP?</summary><br>
GET and POST are two HTTP methods used to request data from a server. GET requests are used to retrieve data from a specified resource, while POST requests are used to submit data to be processed to a specified resource. GET requests include data in the URL as query parameters, while POST requests send data in the request body.
</details>
<details>
<summary>What is a RESTful API?</summary><br>
A RESTful API (Representational State Transfer) is an API that adheres to the principles of the REST architectural style. It uses HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on resources, which are identified by URLs. RESTful APIs are stateless, meaning each request is treated independently and does not rely on any stored state information from previous requests.
</details>
<details>
<summary>What are the main differences between SOAP and REST?</summary><br>
SOAP (Simple Object Access Protocol) and REST (Representational State Transfer) are both web service communication protocols. The main differences between them are:

1. SOAP is a protocol, while REST is an architectural style.
2. SOAP uses XML for message exchange, while REST can use multiple data formats, such as JSON, XML, or plain text.
3. SOAP typically requires more complex processing and has a larger overhead compared to REST, making REST generally faster and more lightweight.
4. SOAP is more rigid in its structure, while REST is more flexible and can be easily scaled.
</details>
<details>
<summary>What is CORS?</summary><br>
CORS (Cross-Origin Resource Sharing) is a mechanism that allows many resources (e.g., fonts, JavaScript, etc.) on a web page to be requested from another domain outside the domain from which the resource originated. This is useful for allowing web pages to access resources from different origins for security and privacy reasons. CORS works by adding HTTP headers to request and response messages, indicating which origins are allowed to access the resources.
</details>
<details>
<summary>What is the purpose of a CDN?</summary><br>
A CDN (Content Delivery Network) is a system of distributed servers that deliver web content to users based on their geographic location, the origin of the content, and the content delivery server. The main purpose of a CDN is to reduce latency, improve load times, and provide a better user experience by serving content from a server that is geographically closer to the user. CDNs can also help to distribute traffic and protect against DDoS attacks.
</details>

## Hosting

<details>
<summary>What is DNS?</summary><br>
DNS (Domain Name System) is a system used to translate human-readable domain names (such as example.com) into IP addresses that can be used by computers to locate and communicate with web servers.
</details>
<details>
<summary>What is a DNS server?</summary><br>
A DNS server is a computer or network device that provides DNS services by translating domain names into IP addresses and vice versa.
</details>
<details>
<summary>How do I set up email for my domain name?</summary><br>
Email can be set up for a domain name by configuring the domain's DNS records to include MX (Mail Exchange) records that specify the mail server(s) responsible for handling incoming mail for that domain.
</details>
<details>
<summary>How do I set up DNS?</summary><br>
DNS can be set up by configuring the domain's DNS records to include various types of records, such as A records (for mapping domain names to IP addresses), MX records (for specifying mail servers), CNAME records (for creating aliases for domain names), and TXT records (for storing arbitrary text data). This can typically be done through a web-based control panel provided by the domain registrar or hosting provider.
</details>
<details>
<summary>What is hosting and how does it differ from a web server?</summary><br>
Hosting is a service provided by a company that allows individuals or organizations to make their website accessible on the internet. Hosting providers typically offer a variety of plans and options that provide varying amounts of storage space, bandwidth, and other features. A web server is a computer program that is responsible for serving web pages to users when they request them. Web servers can be installed on a hosting provider's infrastructure or on a dedicated physical or virtual server.
</details>
<details>
<summary>When do I need secure HTTP webpages?</summary><br>
Secure HTTP webpages (HTTPS) are needed when sensitive information, such as passwords, credit card numbers, or other personal data, is being transmitted between the web server and the user's browser. HTTPS encrypts this data so that it cannot be intercepted or modified by third parties. Additionally, some web browsers and search engines may prioritize secure websites in search results or display warning messages for non-secure websites.
</details>
<details>
<summary>How much does it cost to set up a website?</summary><br>
The cost of setting up a website can vary widely depending on the specific requirements and technologies being used. A simple website built using a content management system (CMS) such as WordPress can be set up for less than $100, while a complex e-commerce website with custom features and integrations can cost tens of thousands of dollars or more.
</details>
<details>
<summary>What are the annual costs for operating a website?</summary><br>
The annual costs of operating a website can include expenses such as domain registration, hosting fees, website maintenance and updates, security and backup services, and marketing and advertising costs. These costs can vary widely depending on the size and complexity of the website, as well as the specific services and vendors being used.
</details>
