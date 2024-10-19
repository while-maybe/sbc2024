"use strict";

const fs = require("fs");
const path = require("path");

const fileName = "./log.txt";
// import all exported definitions from "operations.js"
const calc = require('./operations.js');

// import fs from "fs";
// import path from "path";
// import * as calc from "./operations.js";

const message = process.argv.slice(2);

// Check if a message was provided
if (!message) {
    console.log("Please provide a message as a command-line argument.");
    process.exit(1); // Exit the process if no message is provided
}

// let message = ["5", "+", "10"];
let [n1, op, n2] = message;
n1 = Number(n1);
n2 = Number(n2);

let result;
switch (op) {
    case '+': {
        result = calc.add(n1, n2);
        break;
    }
    case '-': {
        result = calc.subtract(n1, n2);
        break;
    }
    case '*': {
        result = calc.multiply(n1, n2);
        break;
    }
    case '/': {
        result = calc.divide(n1, n2);
        break;
    }
}

const output = `${n1} ${op} ${n2} = ${result}`;

const filePath = path.join(__dirname, fileName);

fs.appendFile(filePath, output.concat("\n"), (err) => {
    if (err) {
        console.error(`${output} [ERROR]`, err);
        return;
    }
    console.log(`${output} [SAVED IN ${fileName}]`);
});
