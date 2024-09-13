def todo_list():

    tasks = []

    print("To-Do-List:")

    while True:
        for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        choice = input("Choose An Option: ")


        if choice == "1":
            new_task = input("Enter A Task: ")
            tasks.append(new_task)
            print(f"'{new_task}' Has Been Added To Your To-Do-List.")


        elif choice == "2":
            try:
                task_number = int(input("Enter Your Task Number To Remove Your Task:"))
                remove_task = tasks.pop(task_number - 1)
                print(f"{remove_task} Has Bin Remove From Your To-Do-List")
            except(ValueError, IndexError):
                print("Error :- Invalid Task Number")


        elif choice == "3":
            print("Your Tasks:")
            if not tasks:
                print("No Tasks To Show.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")


        elif choice == "4":
            print("Exiting The To-Do-List.")
            break


        else:
            print("Invalid Option. Please Choose Only 1, 2, 3, or 4.")


print("Options To Using Our TO-DO-LIST:")
print("Type 1 To Add A New Task")
print("Type 2 To Remove Old Task")
print("Type 3 To View Your All Task List")
print("Type 4 To Exit  To-Do List")
todo_list()
