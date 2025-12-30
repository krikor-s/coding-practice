#in this app we will build a task manager

tasks = []

def title():
    print("=====Task Manager=====")

def get_action():
    while True:
        print("What would you like to do?")
        act = input("View, Add, Remove, or Exit: ")
        if act.lower() in ("view", "add", "remove", "exit"):
            return act.lower()

def add_task():
    add_t = input("What would you like to add: ")
    tasks.append(add_t)
    print(f"Task '{add_t}' was added!")

def view_task():
    if not tasks:
        print("You currently have no tasks. ")
    if tasks:
        print(f"Your current tasks are:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task():  
    if not tasks:
            print("No tasks to remove.")

    elif tasks: 
            print("These are your current tasks")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    while True:
        rem = input("Which task would you like to remove? (1, 2, 3...): ")
        try:
            rem_t = int(rem) - 1
            if 0 <= rem_t < len(tasks):
                removed_task = tasks.pop(rem_t)
                print(f"Removed task: {removed_task}")
                print("Your remaining tasks are: ")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                break
            else:
                print("Invalid input!")
                print("Please choose from the following: ")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        except ValueError:
            print("Please enter a number.")

title()

while True:
    action = get_action()
    if action == "view":
        view_task()
    elif action == "add":
        add_task()
    elif action == "remove":
        remove_task()
    elif action == "exit":
        print("Exiting Task Manager...")
        break

