def todo_list():
    tasks = []
    
    while True:
        print("\n-- To do list ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            if tasks:
                print("\n Your tasks: ")
                for i, task in enumerate(tasks, start =1):
                    print("f{1}. {task}")
            else:
                print("\nNo tasks added yet.")
                
        elif  choice == '2':
            task  = input("Enter a new task: ")
            tasks.append(task)
            print("Task added! ")
        elif choice == '3':
            if tasks:
                task_num = int(input("Enter the task number to remove: "))
                if 0 < task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number!")
            else:
                print("NO task to remove")
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again")
            
todo_list()

