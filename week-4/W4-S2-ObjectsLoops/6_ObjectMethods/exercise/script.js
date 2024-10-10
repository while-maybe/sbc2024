// 1. Object.keys() - TODO: WHat does this method do? What is the output?
// .keys() gets the object property names
// output ['name', 'age', 'city']
const person = {
  name: "Alice",
  age: 30,
  city: "New York",
};
console.log("Keys:", Object.keys(person));

// 2. Object.values() - TODO: WHat does this method do? What is the output?
// .values() gets the values of the object
// output ['Alice', 30, 'New York']
console.log("Values:", Object.values(person));

// 3. Array.push() - TODO: WHat does this method do? What is the output?
// .push() adds a new element to the end of an array
// output ['apple', 'banana', 'orange']
let fruits = ["apple", "banana"];
fruits.push("orange");
console.log("After push:", fruits); // ["apple", "banana", "orange"]

// 4. Array.pop() - TODO: WHat does this method do? What is the output?
// .pop() removes the last element of an array and returns it
// output After pop: (2) ['apple', 'banana'] - Popped fruit: orange
let poppedFruit = fruits.pop();
console.log("After pop:", fruits); // ["apple", "banana"]
console.log("Popped fruit:", poppedFruit); // "orange"

// 5. Array.shift() - TODO: WHat does this method do? What is the output?
// .shift() removes the first element of the array and returns it
// output After shift: ['banana'] - Shifted fruit: apple
let shiftedFruit = fruits.shift();
console.log("After shift:", fruits); // ["banana"]
console.log("Shifted fruit:", shiftedFruit); // "apple"

// 6. Array.concat() - TODO: WHat does this method do? What is the output?
// .concat() concatenates an array to another
// output ['banana', 'carrot', 'potato']
let vegetables = ["carrot", "potato"];
let food = fruits.concat(vegetables);
console.log("After concat:", food); // ["mango", "banana", "carrot", "potato"]

// 7. Array.indexOf() - TODO: WHat does this method do? What is the output?
// .indexOf() looks for an element and returns the index of the first match (if any)
// output - 0
let index = food.indexOf("banana");
console.log("Index of banana:", index); // 1

// 8. Array.includes() - TODO: WHat does this method do? What is the output?
// .includes() looks for an element in an array and it returns true on the first match, returns false if it finds none
// output - false
let hasMango = food.includes("mango");
console.log("Array contains mango:", hasMango); // true

// 9. Array.filter() - Creates a new array with all elements that pass a test
// .filter() iterates through the elements of an array and evaluates each one in a function returning the only the elements where this function evaluates to true. In the example it returns items if the length of the item currently evaluated through the test function has a length longer than 5 characters.
// output - ['banana', 'carrot', 'potato']
let longFoods = food.filter((item) => item.length > 5);
console.log("Foods with more than 5 letters:", longFoods); // ["banana", "carrot", "potato"]
