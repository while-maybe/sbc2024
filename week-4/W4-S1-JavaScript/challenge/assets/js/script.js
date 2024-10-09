function calculate(n1, n2, op) {
    // check if n1 or n2 is(are) not a number, if so return an error
    if (isNaN(n1) || isNaN(n2)) {
        return "Invalid input: both arguments must be numbers.";
    }

    // convert op variable to String in case user specifies a number for the operation and .toLowerCase() fails (as it cannot convert a number to lowercase...) - break statement not needed in case blocks as return exits the function
    switch(String(op).toLowerCase()) {
        case "add": {
            return n1 + n2;
        }
        case "subtract": {
            return n1 - n2;
        }
        case "multiply": {
            return n1 * n2;
        }
        case "divide": {
            // if n2 is 0 (a falsy value) negate it and return the error
            if (!n2) {
                // return Error if divide by zero
                return "Divide by zero? :/";
            }
            return n1 / n2;
        }
        default: {
            return "Unknown operation. Please use 'add', 'subtract', 'multiply', or 'divide'.";
        }
    }
}

console.log(calculate(100, 7, "add"));
console.log(calculate(100, 7, "subtract"));
console.log(calculate(100, 7, "multiply"));
console.log(calculate(100, 7, "divide"));

// divide by zero
console.log(calculate(100, 0, "divide"));

// non-existent parameter
console.log(calculate(100, 7, "blabla"));

// bad parameter(s)
console.log(calculate("something", 7, "add"));
console.log(calculate(7, "something", "add"));
console.log(calculate("something", "something", "add"));
