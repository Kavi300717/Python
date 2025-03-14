tasks = []

def display_menu():
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    display_menu()

    choice = input("sSelect an opton: ")

    #If the choice is 1 Add new Task
    if choice == '1':
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task added successfully.")

    #If the choice is 2 they edit the task present in the index/list
    elif choice == '2':
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            try:
                task_index = int(input("Enter task index to edit: ")) - 1
                if 0 <= task_index < len(tasks):
                    new_task = input("Enter new task: ")
                    tasks[task_index] = new_task
                    print("Task edited successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No task available to edit.")

    #If choice is 3 then we have to delete the elementfrom the tasks
    elif choice == '3':
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            try:
                task_index = int(input("Enter task index to delete: "))
                if 0 <= task_index < len(tasks):
                    tasks.pop(task_index)
                    print("Task deleted successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valif number.")
        else:
            print("No tasks available to delete.")

    elif choice == '4':
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invaid choice. Please select a valid option")