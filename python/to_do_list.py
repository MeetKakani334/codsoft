def todo_list():
    task = []
    while True:
        print("to_do_list.")
        for i,tasks in enumerate(task,start=1):
         print(f"{i}.{tasks}")
        print("Options:")
        print("1.Add Task")
        print("2.Remove Task")
        print("3.Show Your task")
        print("4.Exit To_Do_List)")
        choice = input("Choose An Options :- ")
        if choice == "1":
                tasks = input("Enter A Task :-")
                task.append(tasks)
                print(f"{tasks} has bin add in your to_do_list.")
        elif choice == "2":
                try:
                    task_number = int(input("enter your task number to remove your task:"))
                    remove_task = task.pop(task_number - 1)
                    print(f"{remove_task} has bin remove from your to_do_list")
                except(ValueError,IndexError):
                    print("Error :- Invalid Task Number")
        elif choice == "3":
            print("your task")
            if not task:
                print("444")
            else:
                for i, tasks in enumerate(task, start=1):
                    print(f"{i}. {tasks}")
        elif choice == "4":
                print("Exiting The To_Do_List")
                break
        else:
                print("Invalid Option Please Choose Option 1/2/3/4")

todo_list()