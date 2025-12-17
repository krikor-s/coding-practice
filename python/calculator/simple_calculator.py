#in this piece of code we are going to create a calculator to work on function capabilities

def print_title():
    print("Simple Calculator")

def get_number():
    while True:
        user_input = input("Enter a number: ")

        try:
            return float(user_input)
        except ValueError:
            print("That is not a valid number")

def get_operation():
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in ("+", "-", "*", "/"):
            return op
        else:
            print("Invalid operation, try again.")

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    return a/b

operations_map = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

print_title()

while True:
    num1 = get_number()
    num2 = get_number()
    operation = get_operation()

    func = operations_map[operation]
    result = func(num1, num2)

    print("You entered number:", num1, num2)
    print("Operation chosen:", operation)

    if result is not None:
        print(f"The result of {num1} {operation} {num2} is {result}")
    
    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Exiting calculator")
        break



