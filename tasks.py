tasks = []

def add_tasks():
    description = input("Please enter the description of the task :")
    check = False
    task = {"description":description, "completed": check}

    tasks.append(task)

    print("Task added sucessfully! \n")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found. \n")
    else:
        print("===== Tasks =====")
        for index, t in enumerate(tasks,start =1):
            status = "[✅ Completed]" if t["completed"] else "[❌ Not completed]"

            print(f"{index}.{t['description']} {status}")


def mark_tasks():
    view_tasks()
    mark = int(input("Enter task number to mark (completed or not completed):"))
    if 1<= mark <= len(tasks):
        tasks[mark-1]['completed'] = True
        print("completed")
    else:
        print("Invalid Task number...please choose correct number. \n")

def delete_tasks():
    view_tasks()
    delete = int(input("Enter the task number to delete :"))
    found = False
    # if 1<= delete <= len(tasks):
    #     tasks[delete-1].remove()
    for index,t in enumerate(tasks,start =1):
        if(index == delete):
            tasks.remove(t)
            found = True
            break

while True:
    choice = input("""===== To-Do List Application =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit 
Enter a choice :""")
    if(choice == '1'):
        add_tasks()
    elif(choice == '2'):
        view_tasks()
    elif(choice == '3'):
        mark_tasks()
    elif(choice == '4'):
        delete_tasks()
    elif(choice == '5'):
        print("Exiting the program....")
        break
    else:
        print("Invalid choice.... Please choose correct choice! \n")