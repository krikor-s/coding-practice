#this will be a banking app that works on the fundamentals of previous projects

import json

try:
    with open("accounts.json", "r") as file:
        accounts = json.load(file)
except FileNotFoundError:
    accounts = {"users": []}



def create_account():
    while True:
        username = input("What would you like your username to be?: ")
        if find_user(username):
            print("Account already exists! ")
            break
        else:
            pin = input("What would you like your pin to be?: ")
            new_user = {"username": username,
                        "balance": 0,
                        "pin": pin
                        }
            accounts["users"].append(new_user)
            with open("accounts.json", "w") as file:
                json.dump(accounts, file)
            break

def find_user(username):
    for user in accounts["users"]:
        if user["username"] == username:
            return user
    return None

def check_pin(pin, cur_user):
    if pin == cur_user["pin"]:
        return True
    else:
        return False
    

def view_account():
    while True:
        username = input("Username: ")
        cur_user = find_user(username)
        if cur_user:
            pin = input("Pin: ")
            if check_pin(pin, cur_user):
                print("Your account balance is: ", cur_user["balance"])
                next_in = input("Would you like to 'deposit', 'withdraw', or 'exit'?: ")
                if next_in == "deposit":
                        deposit(cur_user)
                        break
                elif next_in == "withdraw":
                        withdraw(cur_user)
                        break
                elif next_in == "exit":
                        return "exit"
            else:
                print("Incorrect Pin!")
                break
        else:
            print("Your account doesn't exist! ")
            print("Would you like to open an account or exit? ")
            view_error = input("Reply with 'open' or 'exit': ")
            if view_error.lower() == "open":
                create_account()
            else:
                break

def deposit(cur_user):
    while True:    
        deposit_amount = int(input("How much would you like to deposit?: "))
        if deposit_amount > 0: 
            cur_user["balance"] += deposit_amount
            print("Your new account balance is: ", cur_user["balance"])
            with open("accounts.json", "w") as file:
                json.dump(accounts, file)
                break
        else:
            print("Invalid input! ")
            break
    
def withdraw(cur_user):
    while True:    
        withdraw_amount = int(input("How much would you like to withdraw?: "))
        if withdraw_amount > 0 and withdraw_amount <= cur_user["balance"]:    
            cur_user["balance"] -= withdraw_amount
            print("Your new account balance is: ", cur_user["balance"])
            if cur_user["balance"] == 0:
                print("You have reached an account balance of '$0' and cannot withdraw anymore money!")
            with open("accounts.json", "w") as file:
                json.dump(accounts, file)
                break
        else:
            print("Invalid input! ")
            break

def account_info():
    while True:
        print("Would you like to open or view an account? ")
        action = input("Reply with 'open', 'view', or 'exit': ")
        if action.lower() == "open":
            create_account()
        elif action.lower() == "view":
            act = view_account()
            if act == "exit":
                break
        elif action.lower() == "exit":
            break
    
print(" === Krikor Banking === ")
account_info()


