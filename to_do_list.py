my_tasks = []

def addToList(list_item):
    my_tasks.append(list_item)

def viewAllTasks():
    for i ,task in enumerate(my_tasks, start=1):
        print(f"{i}. {task}")

def remove_a_task():
    """Remove a selected task by its number."""
    if not my_tasks:
        print("No tasks to remove.")
        return

    for i, task in enumerate(my_tasks, start=1):
        print(f"{i}. {task}")

    try:
        task_id = int(input("Select the task number to remove: "))
        if 1 <= task_id <= len(my_tasks):
            removed = my_tasks.pop(task_id - 1)
            print(f'"{removed}" was removed.')
        else:
            print("Enter a valid number.")
    except ValueError:
        print("Please enter a number.")


while True:
    manage_tasks = input("To manage your tasks enter V - view tasks, a - add tasks, d delete tasks, c - clear all tasks, q - to quit :")
    if manage_tasks.upper() == "V":
        viewAllTasks()
    elif manage_tasks.upper() == "A":
        new_task = input("Enter a new task:")
        addToList(new_task)
    elif manage_tasks.upper() == "D":
        remove_a_task()
    elif manage_tasks.upper() == "Q":
        break
    else:
        print("Enter a valid response : V - view tasks, a - add tasks, d delete tasks, c - clear all tasks, q - to quit :")



    
    