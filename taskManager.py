task_storage = []

while True:

    menu = """
    What would you like to do?
    (A)dd a task
    (V)iew tasks
    (D)elete a task
    (Q)uit
    """
    print(menu, flush = True)
    menu_select = input("> ").upper()
    if menu_select == "A":
        task = input("Enter task description: ")
        task_storage.append(task)
    elif menu_select == "V":
        for task in task_storage:
            print(task)
    elif menu_select == "D":
        task = input("Enter the index of the task you would like to delete (Starting with 0): ")
        task_storage.pop(int(task))
    elif menu_select == "Q":
        print("Goodbye!")
        break
    else:
        print("Invalid selection. Please try again.")

        