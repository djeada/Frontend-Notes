# JavaScript Quiz

Notes: [JavaScript](../notes/04_javascript.md)

Check your understanding of types and coercion, scope, functions, arrays and objects, and asynchronous JavaScript.

#### Q. What does `console.log(typeof null)` print?

* [x] `object`
* [ ] `null`
* [ ] `undefined`
* [ ] `number`

> **Explanation:** `typeof null` returns `"object"` because of a bug kept from the first version of JavaScript for compatibility. Test for null with `value === null`.

#### Q. Which keyword declares a block-scoped variable that can be reassigned?

* [ ] `var`
* [ ] `function`
* [x] `let`
* [ ] `static`

> **Explanation:** `let` is scoped to the nearest block and can be reassigned. `var` is function-scoped, and `const` is block-scoped but cannot be reassigned.

#### Q. Inside a regular function called as `obj.method()`, what does `this` refer to?

* [ ] The global object
* [ ] `undefined`
* [x] `obj`, the object the method was called on
* [ ] The function itself

> **Explanation:** For regular functions, `this` is set by how the function is called; `obj.method()` binds it to `obj`. Arrow functions instead take `this` from the surrounding scope.

#### Q. Which method converts a JavaScript object into a JSON string?

* [ ] `JSON.parse()`
* [ ] `Object.stringify()`
* [x] `JSON.stringify()`
* [ ] `Object.toJSON()`

> **Explanation:** `JSON.stringify()` serializes a value to a JSON string, and `JSON.parse()` does the reverse.

#### Q. In what order are the messages logged?

```js
console.log('Start');
setTimeout(() => console.log('Timeout'), 0);
Promise.resolve().then(() => console.log('Promise'));
console.log('End');
```

* [ ] Start, Timeout, Promise, End
* [ ] Start, End, Timeout, Promise
* [ ] Start, Promise, End, Timeout
* [x] Start, End, Promise, Timeout

> **Explanation:** Synchronous code runs first. Promise callbacks are microtasks that run as soon as the current job finishes, while the timer callback is a later task, even with a `0` delay.

#### Q. Which queue do promise `.then()` callbacks run from?

* [ ] The timer (macrotask) queue
* [ ] The rendering queue
* [x] The microtask queue
* [ ] The animation frame queue

> **Explanation:** Promise reactions are queued as microtasks, and the whole microtask queue is drained after each task before the browser handles timers or rendering.

#### Q. What does the `async` keyword before a function do?

* [ ] Runs the function on a separate thread
* [ ] Makes every return value a rejected promise
* [x] Makes the function return a Promise and allows `await` inside it
* [ ] Delays the function until the call stack is empty

> **Explanation:** An `async` function always returns a promise: returned values fulfil it and thrown errors reject it. It still runs on the same thread.

#### Q. How do you handle a rejection from an `await` expression inside an `async` function?

* [ ] It cannot be handled; the program terminates
* [ ] Read the `error` field of the object `await` returns
* [x] Wrap the `await` in a `try { … } catch (e) { … }` block
* [ ] Pass an error callback as a second argument to `await`

> **Explanation:** A rejected awaited promise throws at the `await`, so `try`/`catch` handles it like a synchronous error. Calling `.catch()` on the promise before awaiting also works.

#### Q. Which statement about `Promise.race()` is true?

* [ ] It resolves with an array of all results
* [ ] It rejects only if every promise rejects
* [x] It settles as soon as the first input promise settles, fulfilled or rejected
* [ ] It ignores rejected promises and waits for the first fulfilment

> **Explanation:** `race` adopts the outcome of whichever promise settles first. Waiting for the first fulfilment while ignoring rejections describes `Promise.any()`.

#### Q. What does `Promise.allSettled()` fulfil with?

* [ ] An array with the values of the fulfilled promises only
* [ ] Nothing; it rejects if any input promise rejects
* [x] An array of `{ status, value }` or `{ status, reason }` objects, one per input
* [ ] A count of fulfilled and rejected promises

> **Explanation:** `allSettled` waits for every promise and never rejects because of an input, so you can inspect each outcome. `Promise.all` rejects on the first rejection.

#### Q. How can you limit `fetch()` concurrency to three requests at a time for a long list of URLs?

* [ ] Pass a `concurrency: 3` option to `Promise.all`
* [x] Use a small queue that starts three requests and starts the next whenever one finishes
* [ ] Call `fetch(url, { limit: 3 })`
* [ ] Rely on the browser to run only three requests at a time

> **Explanation:** `Promise.all` and `fetch` have no concurrency option, so you need a worker pool or queue (or a library such as `p-limit`). Browser connection limits are not a reliable throttle.

#### Q. When one promise passed to `await Promise.all([...])` rejects, what happens?

* [ ] The result array contains the error in that position
* [ ] The rejection is ignored and the other values are returned
* [x] The `await` throws that rejection immediately; the other operations are not cancelled
* [ ] The rejected promise is retried automatically

> **Explanation:** `Promise.all` rejects with the first rejection reason without waiting for the rest. The other operations keep running; promises have no built-in cancellation.

#### Q. Which call aborts a `fetch()` that takes longer than 5 seconds?

* [ ] `fetch(url, { timeout: 5000 })`
* [x] `fetch(url, { signal: AbortSignal.timeout(5000) })`
* [ ] `fetch(url).timeout(5000)`
* [ ] `setTimeout(fetch(url), 5000)`

> **Explanation:** `fetch` has no `timeout` option; it is cancelled through an `AbortSignal`. `AbortSignal.timeout(ms)` creates a signal that aborts automatically after the delay.

#### Q. A search box sends a request for "ca", then for "cat". The "ca" response arrives last and overwrites the results. What is the most reliable fix?

* [ ] Add `await` before each `fetch()` call
* [ ] Increase the server's response speed
* [x] Abort the obsolete request with an `AbortController`, or ignore responses for an old query
* [ ] Use `Promise.all` for both requests

> **Explanation:** `await` alone doesn't order independent requests; both can succeed in any order. Cancelling stale work, or checking that a response matches the current query, prevents outdated results.

#### Q. What is the result of `[] + []`?

* [ ] `undefined`
* [ ] `NaN`
* [x] `""` (an empty string)
* [ ] `[]`

> **Explanation:** `+` converts both arrays to primitives; an empty array becomes the empty string, and `"" + ""` is `""`.

#### Q. Which loop always executes its body at least once?

* [ ] `for`
* [ ] `while`
* [x] `do…while`
* [ ] `for…of`

> **Explanation:** `do…while` checks its condition after each iteration, so the body runs once before the first check.

#### Q. Which expression creates a promise that is already rejected with an `Error`?

* [x] `Promise.reject(new Error('err'))`
* [ ] `Promise.resolve(new Error('err'))`
* [ ] `new Error('err')`
* [ ] `Promise.error('err')`

> **Explanation:** `Promise.reject()` returns a rejected promise. `Promise.resolve(new Error())` fulfils with an Error object as its value, and `Promise.error` does not exist.

#### Q. What can a regular function do that an arrow function cannot?

* [ ] Return a value implicitly
* [ ] Use default parameters
* [x] Be called with `new` as a constructor
* [ ] Be assigned to a variable

> **Explanation:** Arrow functions have no `prototype`, own `this` or `arguments`, so `new` throws a TypeError. Implicit returns are actually an arrow-function feature.

#### Q. Which statement imports the default export of `./math.js`?

* [x] `import add from './math.js';`
* [ ] `import { add } from './math.js';`
* [ ] `import * from './math.js';`
* [ ] `export add from './math.js';`

> **Explanation:** A default import uses a name without braces. Braces import a named export, and `import *` needs `as name`.

#### Q. What does this `var` loop with `setTimeout` log?

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```

* [ ] `0 1 2`
* [ ] `0 0 0`
* [ ] `undefined undefined undefined`
* [x] `3 3 3`

> **Explanation:** `var` creates one function-scoped `i` shared by all callbacks, and the loop has finished (leaving `i` at 3) before any timer runs.

#### Q. What does this `let` loop with `setTimeout` log?

```js
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), i * 100);
}
```

* [x] `0 1 2`
* [ ] `3 3 3`
* [ ] `undefined undefined undefined`
* [ ] `0 0 0`

> **Explanation:** `let` creates a fresh binding of `i` for each iteration, so each callback closes over its own value.

#### Q. Which method adds elements to the beginning of an array?

* [ ] `push()`
* [ ] `concat()`
* [x] `unshift()`
* [ ] `shift()`

> **Explanation:** `unshift()` inserts at the start and returns the new length. `shift()` removes the first element and `push()` appends to the end.

#### Q. How do you make a single property of an object read-only?

* [ ] Declare the object with `const`
* [ ] Prefix the property name with `_`
* [ ] Call `Object.seal(obj)`
* [x] `Object.defineProperty(obj, 'prop', { writable: false })`

> **Explanation:** A non-writable property ignores assignments (or throws in strict mode). `const` only prevents rebinding the variable, and `seal` prevents adding or deleting properties but still allows changes.

#### Q. Which of these is not a primitive type in JavaScript?

* [ ] `symbol`
* [ ] `bigint`
* [ ] `undefined`
* [x] `object`

> **Explanation:** The primitives are string, number, bigint, boolean, undefined, symbol and null. Objects, including arrays and functions, are reference types.

#### Q. What does `await` do inside an `async` function?

* [ ] Converts the awaited value into a callback
* [ ] Blocks the whole main thread until the promise settles
* [x] Pauses that function until the promise settles, then returns its value or throws its reason
* [ ] Catches any errors automatically

> **Explanation:** Only the async function is suspended; other code, events and rendering continue. A rejected promise makes `await` throw.

#### Q. Which built-in function deep-copies an object, including nested `Date` and `Map` values?

* [ ] `Object.assign({}, obj)`
* [ ] `{ ...obj }`
* [x] `structuredClone(obj)`
* [ ] `Object.create(obj)`

> **Explanation:** `structuredClone` copies nested structures and many built-in types. Spread and `Object.assign` are shallow, and a JSON round trip turns `Date` into strings and drops `Map` contents.

#### Q. Which event fires when the HTML has been fully parsed, without waiting for images to load?

* [ ] `load`
* [x] `DOMContentLoaded`
* [ ] `readystatechange`
* [ ] `ready`

> **Explanation:** `DOMContentLoaded` fires once parsing and deferred scripts are done. `load` waits for images, stylesheets and other subresources; `ready` is a jQuery concept.

#### Q. What is a closure in JavaScript?

* [ ] A loop that captures all variables
* [ ] A function that runs once and then deletes itself
* [x] A function together with the variables of the scope it was created in
* [ ] A special kind of promise

> **Explanation:** A function keeps access to variables from its defining scope even after that outer function has returned, which is how counters, private state and callbacks remember values.

#### Q. Which expression gives you the current call stack as a string?

* [x] `new Error().stack`
* [ ] `Error.stack()`
* [ ] `console.trace()`
* [ ] `Function.caller`

> **Explanation:** All major engines populate `error.stack` with a stack trace string. `console.trace()` prints a trace to the console but returns `undefined`.

#### Q. Which API schedules a callback to run just before the browser's next repaint?

* [ ] `setTimeout(fn, 0)`
* [ ] `queueMicrotask(fn)`
* [x] `requestAnimationFrame(fn)`
* [ ] `Promise.resolve().then(fn)`

> **Explanation:** `requestAnimationFrame` runs once per frame before paint, which suits visual updates. Microtasks run as soon as the current job ends, and timers run as later tasks.

#### Q. What is a pure function?

* [ ] A function that does not return anything
* [ ] A function declared with `function*`
* [x] A function that returns the same output for the same inputs and has no side effects
* [ ] A function that only uses `const`

> **Explanation:** Pure functions don't read or change outside state, so they are easy to test, cache and reason about.

#### Q. Which method returns a new array containing the return value of a callback for each element?

* [ ] `forEach()`
* [ ] `filter()`
* [x] `map()`
* [ ] `find()`

> **Explanation:** `map()` transforms every element into a new array of the same length. `forEach()` returns `undefined`, and `filter()` keeps or drops the original elements.

#### Q. What does immutability mean in functional JavaScript?

* [ ] Using only `let` instead of `var`
* [x] Data is never changed in place; updates create new values instead
* [ ] Every variable is declared at the top level
* [ ] Every object is deep-frozen by the engine

> **Explanation:** Immutable updates return new arrays or objects (for example with spread or `map`) instead of mutating existing ones, which makes changes easy to detect.

#### Q. Which array method combines all elements into a single value?

* [ ] `map()`
* [ ] `filter()`
* [x] `reduce()`
* [ ] `every()`

> **Explanation:** `reduce()` calls a reducer with an accumulator and each element, for example to sum numbers or group items.

#### Q. What is currying?

* [ ] Combining two functions into one
* [x] Turning a function of several arguments into a chain of functions that each take one argument
* [ ] Passing an options object instead of separate arguments
* [ ] Automatically caching function results

> **Explanation:** A curried `add(a, b)` becomes `add(a)(b)`, which makes it easy to create specialized functions such as `add(1)`.

#### Q. What does this function composition log?

```js
const compose = (f, g) => x => f(g(x));
const addOne = x => x + 1;
const double = x => x * 2;
console.log(compose(addOne, double)(5));
```

* [x] `11`
* [ ] `12`
* [ ] `10`
* [ ] `7`

> **Explanation:** `compose` applies the right-hand function first: `double(5)` is 10, then `addOne(10)` is 11. Applying `addOne` first would give 12.

#### Q. Which description fits a higher-order function?

* [ ] A function written with arrow syntax
* [x] A function that takes a function as an argument or returns one
* [ ] A function that always runs asynchronously
* [ ] A function that is called only once

> **Explanation:** `map`, `filter`, `addEventListener` and function factories are higher-order functions because they accept or return functions.

#### Q. What is partial application?

* [ ] Calling a function with every argument it expects
* [x] Fixing some arguments of a function to produce a function that takes the rest
* [ ] Running several functions in sequence
* [ ] Caching the results of a function

> **Explanation:** For example, `const greetHi = greet.bind(null, 'Hi')` fixes the first argument. Unlike currying, the new function may still take several arguments at once.

#### Q. What does `console.log(0 == '0')` print?

* [x] `true`
* [ ] `false`
* [ ] A TypeError
* [ ] `undefined`

> **Explanation:** Loose equality converts the string `'0'` to the number `0` before comparing, so the values are equal.

#### Q. What does `console.log(0 === '0')` print?

* [ ] `true`
* [x] `false`
* [ ] A TypeError
* [ ] `undefined`

> **Explanation:** Strict equality never converts types; a number and a string are always unequal.

#### Q. What does calling `foo()` log?

```js
var a = 1;
function foo() {
  console.log(a);
  var a = 2;
}
foo();
```

* [ ] `1`
* [ ] `2`
* [x] `undefined`
* [ ] A ReferenceError

> **Explanation:** The inner `var a` is hoisted to the top of `foo` and initialized to `undefined`, shadowing the outer `a` before the assignment runs.

#### Q. What happens when a `let` variable is read before its declaration?

```js
console.log(x);
let x = 5;
```

* [ ] `undefined`
* [ ] `5`
* [x] A ReferenceError
* [ ] `null`

> **Explanation:** `let` and `const` are hoisted but not initialized; reading them before the declaration is in the temporal dead zone and throws a ReferenceError.

#### Q. What does `new Date('2025-13-01')` produce?

* [ ] January 1, 2026
* [ ] December 1, 2025
* [x] An Invalid Date object
* [ ] A thrown RangeError

> **Explanation:** Month 13 is not valid in the ISO date format, so the constructor returns a Date whose time value is `NaN`. It does not throw; `toISOString()` on it would.

#### Q. What does the last line log?

```js
const arr = [];
arr.push(arr);
console.log(arr[0] === arr);
```

* [x] `true`
* [ ] `false`
* [ ] A TypeError
* [ ] `undefined`

> **Explanation:** `push` stores a reference to the array inside itself, creating a circular structure; `JSON.stringify(arr)` would throw for that reason.

#### Q. What is the result of `typeof NaN`?

* [ ] `"NaN"`
* [x] `"number"`
* [ ] `"undefined"`
* [ ] `"object"`

> **Explanation:** `NaN` is a special numeric value meaning "not a valid number", but its type is still number.

#### Q. Given `const sym = Symbol('x')`, which statement is true?

* [ ] `Object.keys({ [sym]: 1 })` returns `['x']`
* [x] Symbol-keyed properties are skipped by `for…in` and `Object.keys()`
* [ ] `sym + ''` evaluates to `'x'`
* [ ] `typeof sym === 'string'`

> **Explanation:** Symbol keys are hidden from normal enumeration; use `Object.getOwnPropertySymbols()` to read them. Implicitly converting a symbol to a string throws a TypeError.

#### Q. What does `[] == ![]` evaluate to?

* [ ] `false`
* [x] `true`
* [ ] A TypeError
* [ ] `NaN`

> **Explanation:** `![]` is `false` because arrays are truthy. Then `[] == false` converts both sides to numbers: `""` becomes 0 and `false` becomes 0.

#### Q. After copying with `Object.assign`, what does `copy === obj` log?

```js
const obj = { a: 1 };
const copy = Object.assign({}, obj);
console.log(copy === obj);
```

* [ ] `true`
* [x] `false`
* [ ] `undefined`
* [ ] A TypeError

> **Explanation:** `Object.assign({}, obj)` copies properties into a new object, and `===` compares object identity, not contents.

#### Q. What does `console.log({ x: 1 } === { x: 1 })` print?

* [ ] `true`
* [x] `false`
* [ ] A SyntaxError
* [ ] `undefined`

> **Explanation:** Each literal creates a separate object, and object comparison tests identity rather than structure. Compare specific fields or use a deep-equality helper instead.

#### Q. What is the value of `bar`?

```js
const obj = { get foo() { return 42; } };
const bar = obj.foo;
```

* [ ] The getter function
* [x] `42`
* [ ] `undefined`
* [ ] A ReferenceError

> **Explanation:** Reading a getter property calls the getter, so `bar` receives its return value rather than the function.

#### Q. In what order are the numbers logged?

```js
async function run() {
  console.log(1);
  await null;
  console.log(3);
}
run();
console.log(2);
```

* [ ] 1, 3, 2
* [x] 1, 2, 3
* [ ] 2, 1, 3
* [ ] 3, 1, 2

> **Explanation:** An async function runs synchronously until its first `await`. The rest of the function resumes as a microtask after the current synchronous code logs 2.

#### Q. What does `sum(2)` return?

```js
function sum(x, y = x) {
  return x + y;
}
```

* [ ] `2`
* [x] `4`
* [ ] `NaN`
* [ ] A ReferenceError

> **Explanation:** Default parameters can refer to earlier parameters, so `y` defaults to `x` (2) and the sum is 4.

#### Q. What does `void 0` evaluate to?

* [ ] `0`
* [x] `undefined`
* [ ] `null`
* [ ] `NaN`

> **Explanation:** The `void` operator evaluates its operand and always returns `undefined`.

#### Q. Which of these can be called on a line before it appears in the source?

* [x] `function greet() {}`
* [ ] `var greet = function () {};`
* [ ] `let greet = () => {};`
* [ ] `class Greet {}` (used as `new Greet()`)

> **Explanation:** Function declarations are hoisted with their body. The `var` version is `undefined` early (a TypeError when called), and `let` and class bindings are in the temporal dead zone (a ReferenceError).

#### Q. What happens here in non-strict code?

```js
const o = {};
Object.defineProperty(o, 'x', { value: 1, configurable: false });
delete o.x;
```

* [ ] `o.x` becomes `undefined`
* [x] `delete` returns `false` and `o.x` stays `1`
* [ ] A TypeError is thrown
* [ ] The property is removed

> **Explanation:** Non-configurable properties cannot be deleted. Sloppy mode fails silently with `false`; strict mode throws a TypeError instead.

#### Q. What does this string-concatenation puzzle print?

```js
console.log(('b' + 'a' + + 'a' + 'a').toLowerCase());
```

* [ ] `baNaNa`
* [x] `banana`
* [ ] `baaa`
* [ ] `bananaa`

> **Explanation:** `+ 'a'` is a unary plus producing `NaN`, so the string is `"baNaNa"`, and `toLowerCase()` turns it into `"banana"`.

#### Q. What does this object with keys `1` and `'1'` log?

```js
const o = { 1: 'a', '1': 'b' };
console.log(Object.keys(o).length, o[1]);
```

* [x] `1 b`
* [ ] `2 a`
* [ ] `2 b`
* [ ] `1 a`

> **Explanation:** Plain-object keys are strings (or symbols), so the number `1` becomes `'1'` and the later property overwrites the earlier one. Use a `Map` when keys must keep their type.

#### Q. What does `[1, [2, [3]]].flatMap(x => x)` return?

* [ ] `[1, 2, 3]`
* [x] `[1, 2, [3]]`
* [ ] `[1, [2, [3]]]`
* [ ] `[[1], [2], [3]]`

> **Explanation:** `flatMap` maps each element and then flattens the result by exactly one level, so the innermost array remains. Use `flat(Infinity)` to flatten completely.

#### Q. Which approach avoids "callback hell" in asynchronous code?

* [ ] Nesting callbacks more deeply
* [ ] Sharing results through global variables
* [x] Chaining promises or using `async`/`await`
* [ ] Making the requests synchronous

> **Explanation:** Promises let each step return the next asynchronous operation, and `async`/`await` makes that chain read like sequential code with ordinary `try`/`catch`.

#### Q. What is referential transparency?

* [ ] A function's ability to read global variables
* [x] An expression can be replaced with its value without changing the program's behavior
* [ ] `this` always refers to the same object
* [ ] Every variable is declared with `const`

> **Explanation:** Calls to pure functions are referentially transparent: `add(2, 3)` can be replaced by `5` anywhere. Hidden state or side effects break that guarantee.

#### Q. Which built-in prevents changes to an object's existing top-level properties?

* [x] `Object.freeze(obj)`
* [ ] `Object.assign(obj, {})`
* [ ] `Array.prototype.splice()`
* [ ] `Object.entries(obj)`

> **Explanation:** A frozen object cannot have properties added, removed or changed. Freezing is shallow, so nested objects stay mutable unless frozen too.

#### Q. What is memoization?

* [ ] Recomputing a result every time to save memory
* [x] Caching a function's results by its arguments so repeated calls are fast
* [ ] Delaying a function until input stops, as in debouncing
* [ ] Converting a recursive function into a loop

> **Explanation:** A memoized `fib(n)` stores each computed value in a cache keyed by `n`, so it is computed once. It only suits pure functions whose output depends solely on their arguments.

#### Q. What does `user?.address?.city` evaluate to when `user.address` is `undefined`?

* [ ] A TypeError
* [x] `undefined`
* [ ] `null`
* [ ] An empty string

> **Explanation:** Optional chaining (`?.`) stops and returns `undefined` when the value before it is `null` or `undefined`, instead of throwing.

#### Q. What does `console.log(0 || 10, 0 ?? 10)` print?

* [x] `10 0`
* [ ] `10 10`
* [ ] `0 0`
* [ ] `0 10`

> **Explanation:** `||` falls back for any falsy value, including `0`. `??` falls back only for `null` or `undefined`, so `0` is kept.

#### Q. Which check reliably detects the value `NaN` without coercing its argument?

* [ ] `value === NaN`
* [x] `Number.isNaN(value)`
* [ ] `isNaN(value)`
* [ ] `typeof value === 'NaN'`

> **Explanation:** `NaN` is not equal to itself, so `===` always fails. Global `isNaN()` coerces first, so `isNaN('abc')` is `true`, whereas `Number.isNaN('abc')` is `false`.

#### Q. What happens when this code runs?

```js
const user = { name: 'Ada' };
user.name = 'Grace';
console.log(user.name);
```

* [x] It logs `Grace`
* [ ] It logs `Ada`
* [ ] It throws a TypeError
* [ ] It throws a SyntaxError

> **Explanation:** `const` prevents reassigning the variable `user`, not changing the object it points to. `user = {}` would throw a TypeError.

#### Q. What does this spread-copy example log?

```js
const a = [1, { n: 1 }];
const b = [...a];
b[0] = 9;
b[1].n = 2;
console.log(a[0], a[1].n);
```

* [x] `1 2`
* [ ] `9 2`
* [ ] `1 1`
* [ ] `9 1`

> **Explanation:** Spread makes a shallow copy: the array is new, so `a[0]` stays 1, but both arrays share the same inner object, so the change to `n` is visible through `a`.

#### Q. What does `[10, 1, 2].sort()` return?

* [ ] `[1, 2, 10]`
* [x] `[1, 10, 2]`
* [ ] `[10, 2, 1]`
* [ ] `[2, 1, 10]`

> **Explanation:** Without a comparator, `sort` compares elements as strings, and `"10"` comes before `"2"`. Use `sort((x, y) => x - y)` for numeric order.

#### Q. What does `console.log('5' + 3, '5' - 3)` print?

* [x] `53 2`
* [ ] `8 2`
* [ ] `53 53`
* [ ] `8 NaN`

> **Explanation:** `+` with a string operand concatenates, while `-` only works on numbers, so `'5'` is converted to 5.

#### Q. What is `new Set([1, 1, 2, '2']).size`?

* [ ] `2`
* [x] `3`
* [ ] `4`
* [ ] `1`

> **Explanation:** A Set keeps unique values using SameValueZero comparison: the duplicate `1` is dropped, but the number `2` and the string `'2'` are different values.

#### Q. What is a key advantage of `Map` over a plain object for a lookup table?

* [ ] It is serialized automatically by `JSON.stringify`
* [x] Keys can be any type, including objects, and keep their type
* [ ] It never holds a reference to its keys
* [ ] It sorts its keys alphabetically

> **Explanation:** Object keys are always strings or symbols, while a `Map` can use objects or numbers as keys and keeps insertion order. Weakly held keys describe `WeakMap`.

#### Q. Why might you use a `WeakMap` instead of a `Map` to attach data to DOM elements?

* [ ] It can be iterated faster
* [x] Its entries don't keep the element keys alive, so they can be garbage-collected
* [ ] It accepts strings as keys
* [ ] It copies the keys instead of referencing them

> **Explanation:** A `WeakMap` holds its object keys weakly, so removing an element lets it be collected along with its data. The trade-off is that a `WeakMap` cannot be iterated.

#### Q. Which operator checks equality without type conversion?

* [ ] `=`
* [ ] `==`
* [x] `===`
* [ ] `=>`

> **Explanation:** `===` compares type and value with no coercion. `=` assigns, `==` coerces types first, and `=>` defines an arrow function.

#### Q. What does `console.log(0.1 + 0.2 === 0.3)` print?

* [ ] `true`
* [ ] `undefined`
* [x] `false`
* [ ] `NaN`

> **Explanation:** Numbers are IEEE 754 binary floats, so `0.1 + 0.2` is `0.30000000000000004`. Compare with a tolerance or use integer cents for money.
