function calculateSum(a, b = 0) {
  console.log("The sum of the numbers is: ", a + b);
}

function multiplyNumbers(a, b = 1) {
  return a * b;
}


let sumResult = calculateSum(5, 10);
// console.log("The result is: " + sumResult);


// method 1
let mulResult = multiplyNumbers(5, 4);
console.log("The multiplication result is: " + mulResult);


// method 2
mulResult = multiplyNumbers(5);
console.log("The multiplication result is: " + mulResult);
