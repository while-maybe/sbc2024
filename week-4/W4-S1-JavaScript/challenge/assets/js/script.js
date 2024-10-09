function calculate(n1, n2, op) {
    // check if n1 or n2 is(are) not a number, if so return an error
    if (isNaN(n1) || isNaN(n2)) {
        return "Invalid input: both arguments must be numbers.";
    }

    valid_ops = ["add", "subtract", "multiply", "divide"];
    // convert op variable to String in case user specifies a number for the operation and .toLowerCase() fails (as it cannot convert a number to lowercase...)
    if (!valid_ops.includes(String(op).toLowerCase())) {
        return "Unknown operation. Please use 'add', 'subtract', 'multiply', or 'divide'.";
    };

    switch(op) {
        case "add": {
            return n1 + n2;
            break
        }
        case "subtract": {
            return n1 - n2;
            break
        }
        case "multiply": {
            return n1 * n2;
            break
        }
        case "divide": {
            // if n2 is 0 (a falsy value) negate it and return the error
            if (!n2) {
                // return Error if divide by zero
                return "Divide by zero? :/";
            }
            return n1 / n2;
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
