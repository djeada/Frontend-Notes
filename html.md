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

<h2>Basic tags</h2>
<h2>Lists</h2>
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

<h1>Tables</h1>


<h1>Radio buttons</h1>

<h1>Text area</h1>

<h1>Forms</h1>

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


