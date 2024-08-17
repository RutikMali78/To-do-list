todo_list = []

# To add a task
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added.")

# To Display all tasks
def Display_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

# To remove a task
def remove_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Remove task")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        Display_tasks()
    elif choice == '3':
        try:
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Exiting the to-do list.")
        break
    else:
        print("Invalid choice, please choose again.")
