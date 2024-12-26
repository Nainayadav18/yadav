import os

# List to store tasks
tasks = []

# Main loop to run the to-do list program
while True:
    # Display the menu
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    
    # Get user's choice
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        # View tasks
        if not tasks:
            print("\nNo tasks in your to-do list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
                
    elif choice == '2':
        # Add a task
        task = input("\nEnter the task you want to add: ")
        tasks.append(task)
        print(f"Task '{task}' has been added.")
        
    elif choice == '3':
        # Remove a task
        if not tasks:
            print("\nNo tasks to remove.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            
            try:
                task_index = int(input("\nEnter the task number you want to remove: "))
                if task_index < 1 or task_index > len(tasks):
                    print("Invalid task number.")
                else:
                    removed_task = tasks.pop(task_index - 1)
                    print(f"Task '{removed_task}' has been removed.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == '4':
        # Exit the program
        print("Exiting... Goodbye!")
        break
        
    else:
        # Invalid option
        print("Invalid choice. Please try again.")
