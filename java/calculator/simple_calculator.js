// This is a program that I've already written and understand the logic
// The point of this is to learn more about javascript as well as test the macbook for coding

const readline = require('readline-sync');

function print_title() {
    console.log(" === Simple Calculator === ");
}

operations_map = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
};

function get_number(){
    while(true){
        let input = readline.question("Enter a number (or type 'exit' to quit): ");
        let num = parseFloat(input);

        if (input.toLowerCase() === "exit") {
            console.log("Exiting Calculator...")
            return null;
        }

        if (!isNaN(num)) {
            return num;
        } else {
            console.log("That is not a valid number. Try again.");
        }
    }
}

function get_operation(){
    while (true) {
        let op = readline.question("Enter operation (+, -, *, /): ");
        if (op ==="+" || op === "-" || op === "*" || op === "/") {
            return op;
        } else {
            console.log("Invalid operation, try again.");
        }
    }
}

function add(a, b) {
    return a + b;
}

function sub(a, b) {
    return a-b;
}

function mult(a, b) {
    return a * b
}

function div(a, b) {
    if (b === 0) {
        console.log("Error: Cannot divide by zero.")
        return null;
    }
    return a/b;
}

print_title();
while (true) {
    let num1 = get_number();
    if (num1 === null) break;

    let num2 = get_number();
    if (num2 === null) break;

    let operation = get_operation();
    let func = operations_map[operation]
    let result = func(num1, num2);
    console.log("The result of " + num1 + " " + operation + " " + num2 + " = " + result);
}