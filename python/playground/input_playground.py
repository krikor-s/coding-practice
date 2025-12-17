#in this project we are making something that allows for us to mess with inputs/integers


while True:
    user_input = input("Enter a number (or type quit): ")
    print(user_input)

    if user_input.lower() == "quit":
            print("Exiting program")
            break

    try:
        number = int(user_input)

        if number > 0:
            print("Your number is positive")
        elif number < 0:
            print("Your number is negative")
        elif number == 0:
            print("Your number is 0")
    except ValueError:
        print("That's not a number")




