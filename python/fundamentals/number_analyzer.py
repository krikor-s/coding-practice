# We're starting off with the very basics of python here
# This should help with user input/loops fundamentals

message = "Number Analyzer starting..."
print(message)

numbers = []

while True:
    user_input = input("Enter a number (or type 'done'): ")
    print("You entered:", user_input)

    if user_input.lower() == "done":
        break

    try:
        number = int(user_input)
        numbers.append(number)
        print("Numbers so far: ", " ".join(str(n) for n in numbers))
    except ValueError:
        print("Invalid input, please enter a number.")


count = len(numbers)
print("Total numbers: ", count)
total = sum(numbers)
print("Sum of numbers: ", total)

if count > 0:
    average = total/count
    print("Average is: ", average)
else:
    print("No numbers were entered.")

for n in numbers:
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

    



