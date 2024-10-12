## What is JavaScript?

JavaScript is a programming language that is primarily used for client-side scripting (making web pages interactive). Since NodeJS we can also use JavaScript in server-side scripting (e.g. for APIs). 

Main idea:

- **JavaScript** is a versatile programming language primarily used for adding interactivity to web pages, making it essential for creating dynamic and responsive user experiences.
- JavaScript is considered a **high-level language**, meaning it abstracts away most of the complex details of the computer’s hardware, making it easier to read and write while allowing developers to focus on programming logic rather than intricate details.
- It is a **multi-paradigm language**, supporting different programming styles, including procedural, object-oriented, and functional programming, which gives developers flexibility in how they structure and write code.
- JavaScript is an **interpreted language**, meaning the code is executed line by line by the browser’s JavaScript engine without the need for prior compilation, making it highly suitable for interactive web applications.
- Being a **dynamic language**, JavaScript allows variables to change types at runtime, which makes it flexible but can lead to unexpected behavior if not managed carefully.
- JavaScript is also known as a **weakly-typed language**, which means that it does not enforce strict type constraints on variables, allowing different types to be easily combined. For instance, you can add a string to a number without needing explicit type conversions.

### Skills Every JavaScript Developer Should Have

1. A strong understanding of **basic syntax and concepts** is necessary, including variables, data types, operators, conditionals, and loops, as they form the foundation of JavaScript programming.
2. Familiarity with **functions and scope** is essential, as functions allow for code reuse, and understanding scope ensures that variables are used correctly within different contexts.
3. Knowledge of **asynchronous programming** techniques, including callbacks, promises, and async/await, is crucial for handling operations like API requests and other time-consuming tasks without blocking the main thread.
4. **DOM manipulation** skills are vital for creating interactive web pages, enabling developers to add, remove, and modify HTML elements dynamically in response to user actions.
5. The ability to work with **APIs and JSON** is essential, as it allows JavaScript developers to fetch data from external sources, such as RESTful APIs, and integrate it into web applications.
6. **Debugging and testing** are critical skills for identifying and resolving issues in JavaScript code. Familiarity with browser developer tools and debugging methods improves development efficiency.
7. Regular use of resources like **MDN** (Mozilla Developer Network) is recommended for up-to-date documentation, learning new JavaScript features, and staying informed about best practices.

### Fundamentals

The following are the fundamental concepts of JavaScript:

#### Adding JavaScript to the HTML

You can either inline JavaScript or include refrence to an external JavaScript file:

1. Inline JavaScript is put between `<script>` tags:

```html
<script>
  // JavaScript code goes here
</script>
```

2. External JavaScript file is set in the src attribute of the `<script>` tag:

```html
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
```

#### Null and Undefined

1. Undefined means that a variable has not been assigned a value.
2. Null is a value set to a variable that is supposed to represent the absence of a value.

```javascript
var x;
console.log(x); // undefined

var y = null;
console.log(y); // null

console.log(typeof x); // undefined
console.log(typeof y); // object

console.log(x === y); // false
console.log(x == y); // true
```

#### Useful Built-In Methods

A few useful built-in methods that you can use in JavaScript:

1. `console.log()` - to display messages in the console
1. `alert()` - to display a message in an alert box
1. `prompt()` - to get input from the user
1. `confirm()` - to ask the user a question and get a yes or no answer
1. `parseInt()` - to convert a string to an integer
1. `parseFloat()` - to convert a string to a floating point number
1. `isNaN()` - to check if a value is not a number
1. `isFinite()` - to check if a value is a finite number
1. `Number()` - to convert a string to a number
1. `String()` - to convert a number to a string
1. `Boolean()` - to convert a value to a boolean
1. `Array()` - to convert a value to an array
1. `Object()` - to convert a value to an object
1. `Date()` - to get the current date and time

Let's take a look at some examples:

```javascript	
var name = prompt("Enter your name");
alert("Hello " + name);
```

#### Numbers

Some of the most common number operations:

1. `number.toFixed(n)` - returns a string with n decimal places for a variable named number
2. `number.toPrecision(n)` - returns a string with n significant digits for a variable named number
3. `number.valueOf()` - returns the number as a primitive value
4. `parseInt(string)` - returns the first number in the string
5. `parseFloat(string)` - returns the first floating point number in the string
6. `Number.MAX_VALUE` - largest possible JS number
7. `Number.MIN_VALUE` - smallest possible JS number
8. `Number.NEGATIVE_INFINITY` - -Infinity
9. `Number.POSITIVE_INFINITY` - Infinity

Let's parse a floating point number from a string and display it with two decimal places:

```javascript
var pi = parseFloat("3.14159");
console.log(pi.toFixed(2));
```

#### Common Math Operations

Some of the most common math functions:

* `Math.round(n)` - rounds a number n to the nearest integer
* `Math.pow(x,y)` - returns x to the power of y
* `Math.sqrt(n)` - returns the square root of n
* `Math.abs(n)` - returns the absolute value of n
* `Math.ceil(n)` - returns the smallest integer greater than or equal to n
* `Math.floor(n)` - returns the largest integer less than or equal to n
* `Math.sin(n)` - returns the sine of n
* `Math.cos(n)` - returns the cosine of n
* `Math.min(n1, n2, ...)` - returns the smallest of the given numbers
* `Math.max(n1, n2, ...)` - returns the largest of the given numbers
* `Math.log(n)` - returns the natural logarithm of n
* `Math.exp(n)` - returns the value of E to the power of n
* `Math.random()` - returns a random number between 0 and 1

In the example below we use the `Math.random()` function to generate a random number between 0 and 1 and then display the value of sine function at that point:

```javascript
var x = Math.random();
var y = Math.sin(x);
console.log(y);
```

#### Comparison Operators

The comparison operators are used to compare two values. 

| Operator | Description |
| -------- | ------ |
| `==` | Equal to |
| `===` | Strictly equal to |
| `!=` | Not equal to |
| `!==` | Strictly not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

In the example below we compare two numbers:

```javascript
var x = 10;
var y = 20;

console.log(x == y); // false
console.log(x < y); // true
```

#### Logical Operators

The logical operators are used to combine two or more conditions.

| Operator | Description |
| -------- | ------ |
| `&&` | Logical AND |
| `&#124;&#124;` | Logical OR |
| `!` | Logical NOT |

In the example below we use logical operators to check if a number is greater than 10 and at the same time less than 20:

```javascript
var x = 15;
var y = 20;

console.log(x > 10 && x < 20); // true
console.log(y > 10 && y < 20); // false
```

#### Conditionals

The conditionals are used to execute different code depending on the value of a variable.

| Operator | Description |
| -------- | ------ |
| `if` | Execute code if a condition is true |
| `else` | Execute code if a condition is false |
| `else if` | Execute code if a condition is false and another condition is true |

In the example below we use conditionals to check if a number is greater than 10 and at the same time less than 20:

```javascript
var x = prompt("Enter a number");

if (x > 10 && x < 20) {
  console.log("The number is between 10 and 20");
} else {
  console.log("The number is not between 10 and 20");
}
```

#### While Loops

The while loops are used to execute a block of code as long as a condition is true.

| Operator | Description |
| -------- | ------ |
| `while` | Execute code as long as a condition is true |

In the example below we use a while loop to count from 1 to 10:

```javascript
var i = 1;

while (i <= 10) {
  console.log(i);
  i++;
} // 1 2 3 4 5 6 7 8 9 10
```

#### For Loops

The for loops are used to execute a block of code a number of times.

| Operator | Description |
| -------- | ------ |
| `for` | Execute code a number of times |

In the example below we use a for loop to count from 1 to 10:

```javascript
for (var i = 1; i <= 10; i++) {
  console.log(i);
}
```

### Functions

A function is a named block of code that performs a specific task. We already used built-in functions like `alert()` and `prompt()` to display messages and get input from the user. Each function has to be first defined and then called. Once defined, the function can be called as many times as needed.

In the example below we create a function that calls the console.log() two times:

```javascript
// Function definition
function sayHello() {
  console.log("Hello");
  console.log("World");
}

sayHello(); // Function call
```

#### Function Arguments

The function arguments are the values that are passed to the function when it is called.

In the example below we create a function that takes two arguments and adds them together:

```javascript
// Function definition
function add(x, y) {
  console.log(x + y);
}

// Function call
add(10, 20); // 30
```

#### The "return" Keyword

The "return" keyword is used to return a value from a function.

In the example below we create a function that takes two arguments and adds them together:

```javascript
// Function definition
function add(x, y) {
  return x + y;
}

// Function call
var result = add(10, 20);
console.log(result); // 30
```

#### ES6 Arrow Functions
  
Arrow functions are a new way to define functions in JavaScript. They are a shorter syntax for writing function definitions.

In the example below we create a function that takes two arguments and adds them together:

```javascript
// ES5
function add(x, y) {
  return x + y;
}

// ES6
const add = (x, y) => {
  return x + y;
}
```

#### Scope

The scope of a variable is the part of a program where that variable can be accessed.

| Variable Type | Scope      | Mutability            | Hoisting                     | Description                                                                                   | Best Practices                                   |
|---------------|------------|-----------------------|------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| `var`         | Global or function | Mutable               | Hoisted but initialized as `undefined` | - `var` is function-scoped, meaning it’s accessible throughout the function where it’s declared.<br> - Variables declared with `var` are hoisted to the top of their scope, meaning they are accessible before their declaration (with an `undefined` value).<br> - Can be redeclared within the same scope. | Avoid using `var` due to potential issues with scope and hoisting. Instead, use `let` or `const`. |
| `let`         | Block      | Mutable               | Hoisted but not initialized    | - `let` is block-scoped, meaning it’s only accessible within the block (e.g., inside a loop or conditional statement) where it’s declared.<br> - While `let` variables are hoisted, they are not initialized, so referencing them before declaration results in a `ReferenceError`.<br> - Can’t be redeclared in the same scope. | Use `let` when you expect the variable value to change later in the code.                  |
| `const`       | Block      | Immutable (value cannot be reassigned) | Hoisted but not initialized    | - `const` is also block-scoped and follows the same scoping and hoisting rules as `let`.<br> - Values assigned to `const` cannot be reassigned. However, if the value is an object or array, its properties or elements can still be modified.<br> - Can’t be redeclared in the same scope. | Use `const` by default when you don’t plan to reassign the variable, as it provides more predictable behavior. |

In the example below we create a variable that is accessible from anywhere in the program:

```javascript
var x = 10;

function add(y) {
  return x + y;
}

console.log(add(20)); // 30
```

In the example below we create a variable that is accessible only from within the block:

```javascript
var x = 10;

{
  var a = 20;
  let b = 15;
  console.log(a + b); // 35
}

function add(y) {
  return x + y;
}

console.log(add(a)); // 30
console.log(add(b)); // Uncaught ReferenceError: y is not defined
```

#### Higher-Order Functions

Higher-order functions are functions that take other functions as arguments or return functions.

In the example below we create a function that takes another function as an argument:

```javascript
function add(x, y) {
  return x + y;
}

function multiply(x, y) {
  return x * y;
}

function doMath(x, y, callback) {
  return callback(x, y);
}

console.log(doMath(2, 3, add)); // 5
console.log(doMath(2, 3, multiply)); // 6
```

### Arrays

Arrays are used to hold several values under a single name and to organize them using indexes represented by consecutive integers.

Let's create an array of numbers:

```javascript
var numbers = [1, 2, 3, 4, 5];
console.log(numbers); // [1, 2, 3, 4, 5]
```

Let's let the user enter a number and add it to the array:

```javascript
var numbers = [];

for (var i = 0; i < 5; i++) {
  var number = prompt("Enter a number");
  numbers.push(number);
}

console.log(numbers);
```

#### Copying Arrays

The array can be copied using the `.slice()` method:

```javascript
var numbers = [1, 2, 3, 4, 5];
var numbersCopy = numbers.slice();

console.log(numbers); // [1, 2, 3, 4, 5]
console.log(numbersCopy); // [1, 2, 3, 4, 5]
```

To copy only a part of the array, use the `.slice()` method with two arguments:

```javascript
var numbers = [1, 2, 3, 4, 5];
console.log(numbers.slice(1, 3)); // [2, 3]
```

#### Mutators

The array can be modified using the `.push()` and `.pop()` methods:

```javascript
var numbers = [1, 2, 3, 4, 5];

numbers.push(6);
console.log(numbers); // [1, 2, 3, 4, 5, 6]

numbers.pop();
console.log(numbers); // [1, 2, 3, 4, 5]
```

#### Accessors

Methods that return a new value or representation are known as accessor methods.

1. `.join()` - Joins all elements of an array into a string.
2. `.reverse()` - Reverses the order of the elements in an array.
3. `.sort()` - Sorts the elements of an array.
4. `.concat()` - Combines two or more arrays.
5. `.slice()` - Extracts a part of an array.
6. `.indexOf()` - Searches an array for an element.
7. `.lastIndexOf()` - Searches an array for an element from the end.

In the example below we first use concat() to combine two arrays, then we sort the result and finally we call the join() method to join the elements of the array into a string:

```javascript
var numbersA = [5, 6, 2, 1, 8];
var numbersB = [9, 7, 1, 10, 4];

var numbers = numbersA.concat(numbersB);
numbers.sort();

console.log(numbers.join()); // 1,1,2,4,5,6,7,8,9,10
```

#### Array Methods: Iterators

The array can be iterated using the `.forEach()` method:

```javascript
var numbers = [1, 2, 3, 4, 5];

numbers.forEach(function(number) {
  console.log(number);
});
```

### Strings

Strings are sequences of characters. They are used to represent text. We use single or double quotes to create strings.

An example of a string is:

```javascript
var name = "John";
console.log(name); // John
```

#### Common String Methods

Some of common string methods include:

1. `.indexOf()` - Searches a string for a specified value and returns the position of the match.
2. `.lastIndexOf()` - Searches a string for a specified value and returns the position of the match.
3. `.slice()` - Extracts a part of a string and returns the extracted part in a new string.
4. `.replace()` - Finds a match between a regular expression and a specified string, and returns a new string with the matches replaced.
5. `.toUpperCase()` - Converts a string to upper case.
6. `.toLowerCase()` - Converts a string to lower case.
7. `.concat()` - Combines two or more strings.
8. `.charAt()` - Returns the character at the specified index (position) of a string.
9. `.charCodeAt()` - Returns the Unicode of the character at the specified index (position) of a string.

Lets slice the string "John loves JavaScript" from index 5 to index 10:

```javascript
var text = "John loves JavaScript";
console.log(text.slice(5, 10)); // loves
```

### Classes

Classes are a way to capture under a single name a set of related properties (data) and methods (functions). The class is a blueprint for creating objects.

Lets create a class that represents a person:

```javascript

// Class definition
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  speak() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

var john = new Person("John", 30); // an object john is created
var jane = new Person("Jane", 25); // an object jane is created

john.speak(); // Hello, my name is John and I am 30 years old.
jane.speak(); // Hello, my name is Jane and I am 25 years old.
```

#### Arrays vs Objects

* Arrays are used to hold several values under a single name and to organize them using indexes represented by consecutive integers.
* Objects are used to hold several values under a single name and to organize them using named properties.
* You can store the same data in both arrays and objects. The power of objects comes from the fact that you can access the data using named properties.

Lets create an array and object containing the same data:

```javascript
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}

var point = new Point(5, 8);
var array = [5, 8];

console.log(point.x, point.y); // 5, 8
console.log(array); // [5, 8]
```

### Exceptions

#### Throwing Exceptions

1. `throw` - Throws an exception.

```javascript
throw new Error("An error has occurred.");
```

#### Try/Catch Blocks

The following syntax is used to handle exceptions:

1. `try` - The try block contains the code that might throw an exception.
2. `catch` - The catch block contains the code that executes when an exception occurs.
3. `finally` - The finally block contains the code that executes regardless of whether or not an exception occurred.

```javascript
try {
  // code that might throw an exception
} catch (e) {
  // code that executes when an exception occurs
} finally {
  // code that executes regardless of whether or not an exception occurred
}
```

#### Types of Errors

1. `ReferenceError` - Thrown when a variable or function is not defined.
2. `TypeError` - Thrown when a value is not of the expected type.
3. `SyntaxError` - Thrown when a syntax error is encountered.
4. `URIError` - Thrown when an invalid URI is encountered.

### Dom

The DOM is a programming interface that allows you to access and manipulate the content of the web page.

* The DOM is a tree of nodes.
* Each node has a tag name, attributes, and child nodes.
* The root node is the `<html>` tag.

Let's look at the following HTML code:

```html
<html>
  <head>
    <title>Hello World!</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>
```

In the example above:

* The `<head>` tag contains the `<title>` tag.
* The `<body>` tag contains the `<h1>` tag.
* The `<h1>` tag contains the text `Hello World!`.

Now let us modify some properties of the `<h1>` tag using JavaScript:

```javascript
var h1 = document.querySelector("h1");
h1.style.color = "red";
h1.style.fontSize = "50px";
h1.style.textAlign = "center";
```

#### DOM Element Selector Methods

The following methods can be used to select elements from the DOM:

* `.querySelector()` - Returns the first element that matches a specified CSS selector(s) in the document.
* `.querySelectorAll()` - Returns a static NodeList containing all elements that match the specified CSS selector(s) in the document.
* `.getElementById()` - Returns the element that has the ID attribute with the specified value.
* `.getElementsByTagName()` - Returns a list of elements with the given tag name.
* `.getElementsByClassName()` - Returns a list of elements with the given class name.

Here is an example of how to use the `.getElementById()` method to change the background color to a gradient from light blue to dark blue.

```javascript
var div = document.getElementById("container");
div.style.background = "linear-gradient(to right, #00ffff, #0000ff)";
```

#### Edit DOM Elements

Once selected, you can edit the content of the element using the following methods:

* `.innerHTML` - Sets or returns the HTML content (inner HTML) of an element.
* `.innerText` - Sets or returns the text content of an element.
* `.outerHTML` - Sets or returns the HTML content of an element, including the element itself.
* `.outerText` - Sets or returns the text content of an element, including the element itself.

Let's append some text to a paragraph with id `paragraph`:

```javascript
var paragraph = document.getElementById("paragraph");
paragraph.innerHTML += "This text was appended using JavaScript.";
```

#### DOM Events

There are two types of events:

* `click` - Triggered when a user clicks on an element.
* `change` - Triggered when a user changes the value of an element.
* `mouseenter` - Triggered when the mouse pointer enters an element.
* `mouseleave` - Triggered when the mouse pointer leaves an element.
* `mousedown` - Triggered when the user presses a mouse button over an element.
* `mouseup` - Triggered when the user releases a mouse button over an element.
* `keydown` - Triggered when a user presses a keyboard key.
* `keyup` - Triggered when a user releases a keyboard key.
  
Let's add an event listener to the button with id `button`:

```javascript
var button = document.getElementById("button");
button.addEventListener("click", function() {
  alert("The button was clicked!");
});
```

### ES6+ Features

ES6+ features are JavaScript features that were added to the language in 2015. Those futures are widely considered to be a great improvement on the language.

#### Spread operator

* `...` - The spread operator is used to expand the elements of an array into a list of arguments.

Let's take a look at a simple example:

```javascript
var numbers = [1, 2, 3, 4, 5];

// Spread operator
var newNumbers = [...numbers, 6, 7, 8, 9, 10];

// Output
console.log(newNumbers); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

#### Destructuring

Destructuring is a JavaScript feature that allows you to extract data from arrays and objects into distinct variables.

Let's take a look at a simple example:

```javascript
var numbers = [1, 2, 3, 4, 5];
var [first, second, third] = numbers;

// Output
console.log(first); // 1
console.log(second); // 2
console.log(third); // 3
```

#### Promises and Async/Await

* `Promise` - A promise is an object that represents the eventual result of an asynchronous operation.
* `async` - The async keyword is used to declare functions that will execute asynchronously.
* `await` - The await keyword is used to pause the execution of a function until a promise is resolved.

Let's take a look at aexample:  

```javascript
async function getData() { // async function declaration
  var response = await fetch("https://jsonplaceholder.typicode.com/users"); // awaitings the response of the fetch call
  var data = await response.json(); // awaitings the response of the json call
  console.log(data);
}
```

#### Template strings

Template strings are a new type of string literal that allows embedded expressions.

In the example below we will use two variables in a template string:

```javascript
var name = "John";
var age = 30;
var sentence = `My name is ${name} and I am ${age} years old.`;
```

#### Object Literals

Object literals are another way (as opposed to the class syntax) to create objects. For a simple examples there is no difference between the two. When we start adding methods however, then each copy of an object created trough literal carries a copy of all the methods which leads to a memory waste.

In the example bleow we create a simple object called `person` and add a method to it:

```javascript
var person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};

person.fullName(); // "John Doe"
```

####  for...of

The for...of statement is used to iterate over iterable objects, arrays, and strings.

In the example below we will iterate over an array:

```javascript
var array = [1, 2, 3, 4, 5];
for (var element of array) {
  console.log(element);
}
```

#### Modules

Modules are a way to organize code into separate files.

In the example below we will create a module called `person_module` and export a function called `getFullName`:

```javascript
module.exports = function getFullName(person) {
  return person.firstName + " " + person.lastName;
};
```

Then we will import the module into another file:

```javascript
var person_module = require("./person_module");
var person = {
  firstName: "John",
  lastName: "Doe"
};
var fullName = person_module.getFullName(person);
console.log(fullName); // "John Doe"
```

#### New Data Structures

The ES6+ standard included new data structures such as Map, WeakMap, Set, and WeakSet.

* `Map` - A Map is a data structure that associates keys with values that will block the garbage collector from removing data it is referencing.
* `WeakMap` - A WeakMap is a data structure that associates keys with values that will allow the garbage collector to remove data it is referencing.
* `Set` - A Set is a data structure that associates unique values with keys that will block the garbage collector from removing data it is referencing.
* `WeakSet` - A WeakSet is a data structure that associates unique values with keys that will allow the garbage collector to remove data it is referencing.

Let's first demonstrate the difference between Map and WeakMap:

```javascript
var map = new Map();
var weakMap = new WeakMap();
// we will now add some data to the map using a function
(function() {
  var key = { extra: 5 }
  var value = 10
  map.set(key, value);
  weakMap.set(key, value);
})();

// now let us see what will happen when we try to read the data
console.log(map); // Map { { extra: 5 } => 10 }
console.log(weakMap); // WeakMap { <items unknown> }
```
  
When iterating over a Map, be cautious. If you use a standard `for` loop, you will get pairs of keys and values, but if you use `forEach`, you will get values first, then keys! 
  
```javascript
const map = new Map([
  ['A', 1],
  ['B', 2],
]);

for (const [k, v] of map) {
  console.log(k, v)
}
  
map.forEach((v, k) => {
  console.log(v, k) 
});
```

#### Subclassing Built-ins

We can now subclass the built-in types such as Array, Date, and RegExp.

Let's take a look at an example where we extend the Array class with a new method:

```javascript
class SpecialArray extends Array {
  constructor(...args) {
    super(...args);
  }
  front() {
    return this[0];
  }
}

arr = new SpecialArray(1, 2, 3);
console.log(arr.front()); // 1
```
  
### TypeScript

TypeScript is a superset of JavaScript that compiles to plain JavaScript. It introduces many new features such as classes, interfaces, generics, and more.

Some of the advantages of using TypeScript are:

* Type-checking - TypeScript will help you catch errors earlier in the development cycle.
* Stronger typing - TypeScript will help you avoid bugs caused by type errors.
* TypeScript always exposes compilation errors during development (pre-compilation). 

#### Compilation

TypeScript has an integrated development environment that allows you to compile your code and see the errors that are generated.

* `tsc` - The TypeScript compiler is used to compile TypeScript code into JavaScript.
* `tsc --init` - This command will create a tsconfig.json file in the current directory.
* `tsc --watch` - This command will watch for changes in the source code and recompile the code when changes are detected.

Let's say we have a TypeScript file called `app.ts` and we want to compile it into a JavaScript file called `app.js`:

```BASH
tsc app.ts --outFile app.js
```

The above command will compile the TypeScript file into JavaScript and output the result into the file `app.js`. You can now include the file in your HTML code since it's a plain old JavaScript.

#### Converting JavaScript projects to TypeScript projects

Let's assume that we already built a JavaScript project and we now decided to convert it to TypeScript.

1. Create tsconfig.json file in the root directory of the project.

This file contains information used by the TypeScript compiler. A small example of the file is shown below:

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "sourceMap": true,
    "declaration": true,
    "declarationMap": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "lib": ["es5", "es6", "es2015.core", "es2015.promise", "es2015.iterable"]
  },
  "include": [
    "src/**/*.ts"
  ]
}
```

2. Decide on a build tool to use.

Popular build tools include Webpack and Gulp. Webpack for example also uses configuration files to specify how to build the project. The configuration files are called `webpack.config.js` and look something like this:

```javascript
module: {
    loaders: [
        { test: /\.ts$/, loader: 'ts-loader' }
    ]
}
```

3. Change extension of all `.js` files to `.ts`.
4. Refactor till you get rid of compilation errors.

### Package managers

Package managers are used to install and manage dependencies. The chances are you won't be working with Vanilla JavaScript only. In fact you will probably be installing packages, libraries, and frameworks all the time. For that you will need a package manager.

#### NPM

NPM stands for "Node Package Manager," but don't be fooled by the term.
React, SASS, Angular, Vue, and pretty much everything else can very certainly be installed and maintained using NPM. 

To install the npm, download the <a href="https://nodejs.org/en/#home-downloadhead">installer</a> from the official website.
  
To update NPM to the newest version, use:

```BASH
npm install npm@latest -g
```
  
##### Initializing a project

In order to set up a project with NPM, you should use the following command:

```BASH
npm init
```

It will create a `package.json` file in the root directory of your project. This file contains all important information about the project and its dependencies. Immediately after the command is executed, you will be prompted to enter the following information:

* `name` - The name of your project.
* `version` - The version of your project.
* `description` - A short description of your project.
* `author` - The author of your project.
* `license` - The license of your project.
* `main` - The main file of your project.
* `scripts` - A list of scripts that will be executed when you run `npm run <script>`.
* `dependencies` - A list of dependencies that will be installed when you run `npm install`.
* `devDependencies` - A list of devDependencies that will be installed when you run `npm install`.

You can also use the `--yes` flag to skip the prompts.

The result of this process will look something like this:

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "MIT",
  "dependencies": {
    "react": "16.3.2",
    "react-dom": "16.3.2"
  }
}
```

##### Installing a package

The most common way to install a package is to use the `npm install` command with different flags:

* `npm install <package>` - This will install the package.
* `npm install <package>@<version>` - This will install the package at the specified version.
* `npm install <package>@<version> --save` - This will install the package at the specified version and save it to the `dependencies` section of the `package.json` file.
* `npm install <package>@<version> --save-dev` - This will install the package at the specified version and save it to the `devDependencies` section of the `package.json` file.

##### Using an existing project

If you downloaded a project from the internet and that project already has a `package.json` file, you can use the `npm install` command to install the dependencies.

##### Listing installed packages

In order to list all installed packages, you can use the `npm list` command:

* `npm list` - This will list all installed packages.
* `npm list -g --depth=0` - This will list all global packages.

##### Updating a package

* `npm update <package>` - This will update the package.
* `npm update <package>@<version>` - This will update the package to the specified version.

### Best Practices

#### General Guidelines

- Consider using **TypeScript** to benefit from enhanced type safety and improved tooling support.
- Leverage **modern ECMAScript** features (ES6+) for more concise, efficient, and maintainable code.
- Limit **external dependencies** to reduce code bloat and improve maintainability over time.
- Keep **code organized** with modules and a clear folder structure, which aids in project scalability and readability.
- Use **code documentation** to clarify complex sections and critical logic, enhancing future maintenance and collaboration.

#### Variables and Constants

- Use `const` for **immutable variables** that won't be reassigned, improving clarity and preventing unintentional modifications. For variables that may change, use `let` to clearly indicate their **mutable nature**.
- Avoid `var` because its **function-scoped behavior** can lead to unpredictable results, especially in loops and conditionals. Stick with `let` and `const` for more reliable block-scoped declarations.
- Employ **descriptive naming conventions** for variables to make code self-documenting and readable. Avoid generic names like `data` or `info`; instead, use names that reflect the variable’s purpose, like `userProfile` or `totalAmount`.

#### Functions

- Favor **arrow functions** for concise syntax and lexical scoping of `this`, especially in callback functions and event handlers where you want to maintain the surrounding scope.
- Aim for **pure functions** that produce no side effects and consistently return the same output for given inputs, which simplifies testing, debugging, and reasoning about code.
- Keep **functions small and focused** on a single task to increase modularity, testability, and reusability. Avoid deeply nested logic; instead, break down complex operations into smaller functions.

#### Loops and Iteration

- Use array methods like `forEach`, `map`, `filter`, and `reduce` for a **functional programming style**, providing cleaner and more expressive ways to work with arrays.
- Choose `for...of` for **array iteration** for simplicity and readability, avoiding loop counter management. When iterating over objects, use `Object.keys`, `Object.values`, or `Object.entries` for clear and functional property handling.

#### Conditionals

- Use the **ternary operator** (`? :`) for simple conditional expressions, making code compact and enhancing readability, especially for straightforward assignments or return statements.
- Prefer `switch` statements for **multiple conditions** that depend on a single variable, improving readability. For more complex conditions, use `if...else` statements to maintain clarity.

#### Error Handling

- Implement **graceful error handling** with `try...catch` blocks in strategic places, such as network requests or JSON parsing, to maintain application stability.
- Ensure **error messages are meaningful**, providing descriptive information that aids in debugging by including context, such as function names or variable values.
- Be mindful of **error propagation**, rethrowing errors or using custom error types when necessary to handle specific error scenarios more effectively.

#### Performance and Optimization

- Balance **readability and optimization** by focusing on clean, functional code before optimizing. Use performance metrics to identify areas for improvement rather than prioritizing premature optimization.
- Use tools like **Webpack or Rollup** for bundling and minification, reducing file size and improving load times by minimizing the number of server requests.
- Optimize with **memoization** to cache expensive function results and **debouncing** to control function call frequency in performance-critical areas like scrolling or resizing events.
- Monitor **memory management** to avoid excessive object creation, unnecessary closures, and memory leaks, ensuring efficient memory usage and application stability.

#### Asynchronous Programming

- Utilize **Promises and async/await** for cleaner asynchronous code, simplifying the handling of asynchronous operations compared to traditional callback patterns.
- Manage **asynchronous errors** using `.catch()` for Promises or `try...catch` with async/await, preventing unhandled rejections and handling errors effectively.
- Familiarize yourself with **async patterns** such as `Promise.all` for concurrent operations and the AbortController API for cancellations, choosing synchronous or asynchronous code based on specific needs.

#### Testing and Code Quality

- Implement **unit tests** with frameworks like Jest or Mocha to validate code in isolation, covering critical areas to ensure that individual functions work as intended.
- Complement unit tests with **integration and end-to-end testing** using tools like Cypress or Selenium, verifying that different components interact correctly and simulating real user interactions.
- Consider **Test-Driven Development (TDD)** to write tests before code, which often results in well-structured code and higher test coverage.
- Use **linting and formatting tools** like ESLint and Prettier to enforce code quality and maintain consistent style, integrating these tools into your build process or code editor.
- Set up **CI/CD pipelines** with services like GitHub Actions or Jenkins for automatic testing and deployment, improving feedback loops and reducing integration issues.
- Engage in **code reviews** to ensure quality, catch potential issues, and encourage knowledge sharing within the team, while using **version control** to manage code effectively.
- Prioritize **documentation and readability**, providing clear inline comments and keeping README files updated for future maintainers or new team members.
- Regularly **refactor code** to improve readability, address technical debt, and enhance performance, helping to keep the codebase efficient and maintainable over time.

### Links

- [JavaScript.com](https://www.javascript.com/)
- [JavaScript Info](https://javascript.info/)
- [Eloquent JavaScript](https://eloquentjavascript.net/)
- [TypeScript Official Site](https://www.typescriptlang.org/)
- [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- [OverAPI JavaScript Cheat Sheet](https://overapi.com/javascript)
- [MDN Web Docs - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [You Don't Know JS (book series)](https://github.com/getify/You-Dont-Know-JS)
- [W3Schools JavaScript Tutorial](https://www.w3schools.com/js/)
- [JavaScript Garden](https://bonsaiden.github.io/JavaScript-Garden/)
- [freeCodeCamp JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
- [Codecademy JavaScript Course](https://www.codecademy.com/learn/introduction-to-javascript)
