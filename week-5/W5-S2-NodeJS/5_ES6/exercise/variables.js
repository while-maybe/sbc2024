/*
// Using var (function-scoped)
var message = "Hello, World!";
if (true) {
  var message = "Hello from block!";
}
console.log(message); // "Hello from block!" (var is not block-scoped)
*/

// Using let (block-scoped)
let message = "Hello, World!";
if (true) {
  let message = "Hello from block!";
}
console.log(message); // "Hello, World!" (let is block-scoped)

// Using const for constants
const PI = 3.14159;

// when using let, a variable defined inside a scope lives until the scope ends so attempting to use it outside of the scope that it was defined in results in the varisable not being accessible (as it has "died"). In our example, the output we get refers to the value of the "message" variable from outer the scope.
