# Simple To-Do List Application

todo_list = []  # List to store tasks

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    todo_list.append(task)
    print(f"✅ Task '{task}' added successfully!")

def update_task():
    view_tasks()
    if todo_list:
        try:
            task_no = int(input("Enter task number to update: "))
            if 1 <= task_no <= len(todo_list):
                new_task = input("Enter updated task: ")
                todo_list[task_no - 1] = new_task
                print("✏️ Task updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_task():
    view_tasks()
    if todo_list:
        try:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(todo_list):
                removed_task = todo_list.pop(task_no - 1)
                print(f"🗑️ Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting... Have a productive day!")
        break
    else:
        print("❌ Invalid choice! Please try again.")
