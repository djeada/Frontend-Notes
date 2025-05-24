#### Q. What will the following code log to the console? `console.log(typeof null);`

* [x] `object`
* [ ] `null`
* [ ] `undefined`
* [ ] `number`
* [ ] `NaN`

#### Q. Which keyword creates a block-scoped variable?

* [ ] `var`
* [ ] `function`
* [x] `let`
* [ ] `global`
* [ ] `static`

#### Q. What does the `this` keyword refer to inside a regular function called as a method on an object?

* [ ] The global object
* [ ] `undefined`
* [x] The object the method was called on
* [ ] A new empty object
* [ ] The function itself

#### Q. Which method converts a JavaScript object into a JSON string?

* [ ] `JSON.parse()`
* [ ] `Object.stringify()`
* [x] `JSON.stringify()`
* [ ] `toJSON()`
* [ ] `Stringify()`

#### Q. What will the following code output first? `console.log('Start'); setTimeout(() => console.log('Timeout'), 0); Promise.resolve().then(() => console.log('Promise')); console.log('End');`

* [ ] Start, Timeout, Promise, End
* [ ] Start, End, Timeout, Promise
* [ ] Start, Promise, End, Timeout
* [x] Start, End, Promise, Timeout
* [ ] Start, Promise, Timeout, End

#### Q. Which queue does `.then()` callbacks use under the hood?

* [ ] Macrotask queue
* [ ] Render queue
* [x] Microtask queue
* [ ] Event callback queue
* [ ] Animation frame queue

#### Q. What does `async` before a function declaration do?

* [ ] Executes the function in a separate thread
* [ ] Makes all return values automatically rejected promises
* [x] Ensures the function returns a Promise and allows use of `await` inside
* [ ] Converts callback-based code to promise-based code
* [ ] Delays the function execution until the call stack is clear

#### Q. How do you catch errors from an `await` expression?

* [ ] You can’t catch them; `await` will terminate the program
* [ ] `await` returns an object `{ error, value }`
* [x] Wrap the `await` call in a `try { … } catch (e) { … }` block
* [ ] Use `.catch()` directly on the awaited value
* [ ] Pass a second callback to `await`

#### Q. Which statement about `Promise.race()` is true?

* [ ] It waits for all promises to fulfill or any to reject, then resolves with an array of results
* [ ] It resolves only after all promises in the iterable have resolved
* [ ] It rejects only if all promises reject
* [x] It resolves or rejects as soon as the first promise settles
* [ ] It ignores rejected promises

#### Q. What’s the difference between `setImmediate(fn)` (Node.js) and `setTimeout(fn, 0)`?

* [x] `setImmediate` callbacks run before timers scheduled with `setTimeout(..., 0)` in the same turn
* [ ] There is no difference; they are aliases
* [ ] `setTimeout(..., 0)` runs before `setImmediate` always
* [ ] `setImmediate` uses the microtask queue while `setTimeout` uses the macrotask queue
* [ ] `setImmediate` is deprecated and behaves like `setInterval`

#### Q. Which pattern avoids “callback hell” by chaining asynchronous operations?

* [ ] Nested callbacks
* [x] Promise chaining
* [ ] Using global variables
* [ ] Synchronous loops
* [ ] Event emitters

#### Q. What does `Promise.allSettled()` return when passed an array of promises?

* [ ] A promise resolved with an array of values for fulfilled promises only
* [ ] A promise rejected if any input promise rejects
* [x] A promise resolved with an array of objects describing each promise’s outcome
* [ ] A promise that never settles
* [ ] A promise resolved with `[fulfilled, rejected]` counts

#### Q. How can you limit concurrency (e.g., only 3 at a time) when fetching many URLs with `fetch()`?

* [ ] Use `Promise.all(urls.map(fetch))` with a `concurrency` option
* [x] Implement a pool/queue that starts only 3 `fetch()` calls at once and starts next on each completion
* [ ] Use `fetch.concurrent(urls, 3)`
* [ ] Pass `{ limit: 3 }` as second argument to `fetch`
* [ ] Browsers automatically throttle to 3 at a time

#### Q. Which event loop phase executes `process.nextTick()` callbacks in Node.js?

* [ ] Timers phase
* [x] Immediately after the current operation, before other microtasks
* [ ] Poll phase
* [ ] Check phase
* [ ] Close callbacks phase

#### Q. What does the `await Promise.all([...])` construct do when one promise rejects?

* [ ] Returns an array with the rejected promise’s error in place
* [ ] Ignores the rejection and resolves with other values
* [x] Throws the rejection immediately and skips waiting for other promises
* [ ] Converts all results to strings
* [ ] Retries the rejected promise

#### Q. How would you implement a timeout for a fetch request using `Promise.race()`?

* [ ] `Promise.race([fetch(url), setTimeout(timeout)])`
* [ ] `Promise.race([fetch(url), rejectAfter(timeout)])`
* [x] `Promise.race([ fetch(url), new Promise((_, rej) => setTimeout(() => rej(new Error('Timeout')), timeout)) ])`
* [ ] `fetch(url, { timeout })`
* [ ] Use `setImmediate` to cancel

#### Q. What is the result of the expression: `[] + [];`

* [ ] `undefined`
* [ ] `NaN`
* [x] `""` (empty string)
* [ ] `0`
* [ ] `[]`

#### Q. Which loop will always execute its body at least once?

* [ ] `for`
* [ ] `while`
* [x] `do…while`
* [ ] `forEach`
* [ ] `for…in`

#### Q. How do you create a promise that immediately rejects with an error?

* [ ] `new Promise((_, reject) => reject("err"))`
* [ ] `Promise.resolve().then(() => { throw "err" })`
* [x] `Promise.reject(new Error("err"))`
* [ ] `Promise.error("err")`
* [ ] `new Error("err")`

#### Q. What feature do arrow functions **not** have compared to regular functions?

* [ ] They cannot return implicitly
* [ ] They bind their own `arguments` object
* [x] They cannot be used as constructors (`new`)
* [ ] They cannot be assigned to variables
* [ ] They don’t support default parameters

#### Q. In JavaScript modules, which keyword is used to import the default export?

* [ ] `require`
* [x] `import`
* [ ] `include`
* [ ] `use`
* [ ] `fetch`

#### Q. What will this code output? `for (var i = 0; i < 3; i++) {  setTimeout(() => console.log(i), 0); }`

* [ ] `0 1 2`
* [ ] `0 0 0`
* [ ] `undefined undefined undefined`
* [x] `3 3 3`
* [ ] `1 2 3`

#### Q. Which method adds one or more elements to the **beginning** of an array?

* [ ] `push()`
* [ ] `concat()`
* [x] `unshift()`
* [ ] `splice()`
* [ ] `shift()`

#### Q. How do you make an object’s property read-only?

* [ ] Using `const` when declaring the object
* [ ] Prefix property name with `_`
* [ ] Seal the object with `Object.seal()`
* [x] Define it with `Object.defineProperty(obj, 'prop', { writable: false })`
* [ ] Freeze the value directly

#### Q. Which of these is **not** a primitive type in JavaScript?

* [ ] `symbol`
* [ ] `bigint`
* [ ] `undefined`
* [x] `object`
* [ ] `boolean`

#### Q. What does the `await` operator do inside an `async` function?

* [ ] Converts the function into a promise
* [ ] Rejects the promise on error
* [x] Pauses execution until the promise settles and returns its value
* [ ] Makes the function synchronous
* [ ] Catches any errors automatically

#### Q. How can you deep-clone an object that contains no functions or symbols?

* [ ] `Object.assign({}, obj)`
* [ ] `_.cloneDeep(obj)`
* [x] `JSON.parse(JSON.stringify(obj))`
* [ ] `structuredClone(obj)`
* [ ] `new Object(obj)`

#### Q. Which event fires when the DOM has been fully parsed, without waiting for stylesheets or images?

* [ ] `load`
* [x] `DOMContentLoaded`
* [ ] `readystatechange`
* [ ] `ready`
* [ ] `parsed`

#### Q. What is a **closure** in JavaScript?

* [ ] A loop that captures all variables
* [ ] A function that runs once then destroys itself
* [x] A function bundled with its lexical environment, allowing access to outer scope after execution
* [ ] A special type of promise
* [ ] A method that closes variables

#### Q. Which built-in method returns the call stack leading to where it was called?

* [ ] `Error.stack()`
* [x] `new Error().stack`
* [ ] `console.trace()`
* [ ] `StackTrace()`
* [ ] `Error.callStack()`

#### Q. How do you schedule a function to run **after** the current call stack is clear, but before repaint?

* [ ] `setTimeout(fn, 0)`
* [x] `queueMicrotask(fn)`
* [ ] `requestAnimationFrame(fn)`
* [ ] `setImmediate(fn)`
* [ ] `Promise.resolve().then(fn)`

#### Q. What is a **pure function** in JavaScript?

* [ ] A function that does not return anything
* [ ] A function declared with `function*`
* [x] A function that always returns the same output for the same inputs and has no side effects
* [ ] A function that only uses `const`
* [ ] A function bound to `this`

#### Q. Which method creates a **new** array by applying a function to each element of an existing array?

* [ ] `forEach()`
* [ ] `filter()`
* [x] `map()`
* [ ] `reduce()`
* [ ] `flatMap()`

#### Q. What does **immutability** mean in functional JavaScript?

* [ ] Using only `let` instead of `var`
* [x] Data structures cannot be changed after creation; operations return new copies
* [ ] Objects must be frozen with `Object.freeze()`
* [ ] Variables declared at top‐level only
* [ ] Always using `const`

#### Q. Which array method reduces an array of values to a **single** value?

* [ ] `map()`
* [ ] `filter()`
* [x] `reduce()`
* [ ] `every()`
* [ ] `find()`

#### Q. What is **currying**?

* [ ] Combining two functions into one
* [x] Transforming a function of multiple arguments into a chain of functions each taking a single argument
* [ ] Allowing a function to accept an object instead of separate args
* [ ] Automatically memoizing function calls
* [ ] Executing functions in parallel

#### Q. How do you **compose** two functions `f` and `g` so that the result applies `g` then `f`?

* [ ] `f(g(x))`
* [ ] `g ∘ f`
* [x] `const compose = (f, g) => x => f(g(x));`
* [ ] `const compose = (f, g) => g(f(x));`
* [ ] `pipeline(f, g)`

#### Q. Which characteristic describes a **higher-order function**?

* [ ] A function that uses arrow syntax
* [x] A function that takes one or more functions as arguments or returns a function
* [ ] A function that runs asynchronously
* [ ] A function that mutates its arguments
* [ ] A function that is called only once

#### Q. What is **partial application**?

* [ ] Applying a function to as many arguments as it expects
* [x] Pre-filling some arguments of a function to produce another function of smaller arity
* [ ] Running functions in sequence
* [ ] Memoizing results of a function
* [ ] Splitting a function into two

#### Q. Which of these is **NOT** a benefit of using pure functions?

* [ ] Easier to test
* [ ] Predictable outputs
* [x] Improved performance due to side-effects
* [ ] Referential transparency
* [ ] Better memoization

#### Q. How can you create a **deep clone** of an object in a functional style (no mutation)?

* [ ] `Object.assign({}, obj)`
* [ ] `JSON.parse(JSON.stringify(obj))`
* [x] Use a utility like `structuredClone(obj)` or spread with nested mappings
* [ ] `Object.freeze(obj)`
* [ ] `_.deepFreeze(obj)`

#### Q. What does this log to the console? `console.log(0 == '0');`

* [x] `true`
* [ ] `false`
* [ ] Throws a TypeError
* [ ] `undefined`
* [ ] `NaN`

#### Q. What about this one? `console.log(0 === '0');`

* [ ] `true`
* [x] `false`
* [ ] Throws a TypeError
* [ ] `undefined`
* [ ] `NaN`

#### Q. What will be the value of `a` after execution? `var a = 1; function foo() { console.log(a); var a = 2; } foo();`

* [ ] `1`
* [ ] `2`
* [x] `undefined`
* [ ] Throws a ReferenceError
* [ ] `null`

#### Q. Which date is created by this? `new Date('2025-13-01');`

* [ ] January 1, 2025
* [ ] December 1, 2025
* [x] Invalid Date
* [ ] Throws RangeError
* [ ] January 13, 2025

#### Q. What does this push into the array? `const arr = []; arr.push( arr ); console.log(arr);`

* [ ] `[undefined]`
* [ ] `[]`
* [x] A self-referencing array (`[ [Circular] ]`)
* [ ] Throws a TypeError
* [ ] `null`

#### Q. Which values are logged? `for (let i = 0; i < 3; i++) { setTimeout(() => console.log(i), i * 100); }`

* [ ] `0, 1, 2` (after delays)
* [ ] `3, 3, 3`
* [x] `0, 1, 2`
* [ ] `undefined` three times
* [ ] Nothing

#### Q. What is the result of: `typeof NaN;`

* [ ] `NaN`
* [x] `number`
* [ ] `undefined`
* [ ] `object`
* [ ] `error`

#### Q. Given `const sym = Symbol('x');`, which statement is true?

* [ ] `Object.keys({ [sym]: 1 })` returns `['sym']`
* [x] Symbol-keyed properties are skipped by `for…in` and `Object.keys()`
* [ ] Symbols coerce to strings implicitly
* [ ] `sym + ''` yields `'x'`
* [ ] `typeof sym === 'string'`

#### Q. What does this expression evaluate to? `[] == ![];`

* [ ] `false`
* [x] `true`
* [ ] `TypeError`
* [ ] `NaN`
* [ ] `undefined`

#### Q. What gets logged? `let obj = { a: 1 }; let copy = Object.assign({}, obj); console.log(copy === obj);`

* [ ] `true`
* [x] `false`
* [ ] `undefined`
* [ ] `TypeError`
* [ ] `null`

#### Q. What is the value of `bar` after execution? `const obj = { get foo() { return 42; } }; const bar = obj.foo;`

* [ ] The getter function
* [x] `42`
* [ ] `undefined`
* [ ] Throws a ReferenceError
* [ ] `null`

#### Q. What order do these statements execute? `console.log('A'); setTimeout(() => console.log('B'), 0); Promise.resolve().then(() => console.log('C')); console.log('D');`

* [ ] A, B, C, D
* [ ] A, D, B, C
* [ ] A, D, C, B
* [ ] A, C, D, B
* [x] A, D, C, B

#### Q. What is the result of: `function sum(x, y = x) { return x + y; }  sum(2);  `

* [ ] `2`
* [x] `4`
* [ ] `NaN`
* [ ] Throws ReferenceError
* [ ] `undefined`

#### Q. What does `void 0` evaluate to?

* [ ] `0`
* [x] `undefined`
* [ ] `null`
* [ ] `NaN`
* [ ] Throws SyntaxError

#### Q. Which of these is **not** hoisted?

* [ ] Function declarations
* [ ] `var` variables (initialized to `undefined`)
* [x] `let` and `const` declarations
* [ ] Class declarations
* [ ] Function parameters

#### Q. What happens when you delete a non-configurable property? `const o = {}; Object.defineProperty(o, 'x', { value: 1, configurable: false }); delete o.x;`

* [ ] `o.x` becomes `undefined`
* [x] The delete fails silently (or throws in strict mode), property remains
* [ ] Throws TypeError in non-strict mode
* [ ] The property is removed and restored to default
* [ ] Throws ReferenceError

#### Q. What does this output? `console.log(('b' + 'a' + + 'a' + 'a').toLowerCase());`

* [ ] `baNaNa`
* [x] `banana`
* [ ] `BaNaNa`
* [ ] `undefined`
* [ ] Throws NaN

#### Q. When converting object keys to strings, what key collisions can occur?

* [ ] Symbols collide with strings
* [x] Numeric keys are converted to strings so different numbers can collide (`{1: 'a', '1': 'b'}`)
* [ ] `true` and `'true'` collide
* [ ] `null` and `'null'` collide
* [ ] No collisions occur

#### Q. What does the **`flatMap`** method do?

* [ ] Runs `map` then `reduce`
* [ ] Only flattens one level of nested arrays
* [x] Maps each element then flattens the result by one level
* [ ] Filters and maps simultaneously
* [ ] Creates an infinite lazy sequence

#### Q. Which approach avoids **callback hell** in asynchronous functional code?

* [ ] Nesting callbacks inside callbacks
* [ ] Using global state
* [x] Chaining Promises or using `async`/`await`
* [ ] Blocking the event loop
* [ ] Infinite recursion

#### Q. What is **referential transparency**?

* [ ] When a function can refer to global variables
* [x] Expressions can be replaced with their values without changing program behavior
* [ ] When `this` always refers to the same object
* [ ] Variables declared with `const`
* [ ] Functions declared at top‐level only

#### Q. Which of these utilities helps enforce **immutability**?

* [ ] `Object.assign()`
* [x] Libraries like Immer or Immutable.js
* [ ] `delete` operator
* [ ] `Array.prototype.splice()`
* [ ] Direct property assignment

#### Q. How would you implement **memoization** for a function `slowFib(n)`?

* [ ] Always recompute `slowFib` each call
* [x] Wrap it with a cache: `const memo = {}; return memo[n] ??= slowFib(n-1)+slowFib(n-2);`
* [ ] Use `setTimeout` inside `slowFib`
* [ ] Use `async`/`await`
* [ ] Convert to tail recursion

#### Q. What is a **functor** in functional JavaScript (e.g., `Maybe`, `Array`)?

* [ ] A function that performs side effects
* [x] A container that implements a `map` method to apply a function inside it
* [ ] A function with two arguments
* [ ] An object with no methods
* [ ] A promise that always resolves

#### Q. What does **point-free** style mean?

* [ ] Always naming all function parameters explicitly
* [x] Defining functions without mentioning their arguments, by composing other functions
* [ ] Avoiding arrow functions
* [ ] Declaring functions inside objects
* [ ] Using only higher-order functions

#### Q. Which operator creates a **null-safe** property access in modern JS?

* [ ] `?.` (optional chaining)
* [ ] `&&`
* [x] `?.` (e.g. `obj?.prop`)
* [ ] `|>`
* [ ] `??`

#### Q. How can you implement a **pipeline** operator (proposal) behavior without syntax sugar?

* [ ] `x |> f |> g`
* [ ] `f |> x`
* [ ] `x |> f(g())`
* [x] `const result = [x].map(f).map(g)[0];` or `g(f(x))`
* [ ] `[x] |> f`

#### Q. What are **transducers**?

* [ ] A new array type
* [x] Composable transformation functions that process data without creating intermediate collections
* [ ] A type of Promise
* [ ] A callback pattern
* [ ] A DOM event

#### Q. Which of these is a **tail-call optimized** recursive approach in JS?

* [ ] A recursive function that accumulates on the call stack
* [x] A recursive function that returns the result of calling itself without further work (e.g., `return recurse(...);`)
* [ ] An iterative `for` loop
* [ ] Using `setTimeout` for recursion
* [ ] A generator function

#### Q. Which operator checks both value and type equality?

* [ ] `=`
* [ ] `==`
* [x] `===`
* [ ] `!=`
* [ ] `=>`

#### Q. What will this log? `console.log(0.1 + 0.2 === 0.3);`

* [ ] `true`
* [ ] `undefined`
* [x] `false`
* [ ] `TypeError`
* [ ] `NaN`

