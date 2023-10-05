#initialise an empty list to store tasks
todo_list=[]

#function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print("Task added:",task)

#function to remove a task from the list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("task removed:",task)
    else:
        print("task not found in the list.")

#function to display the current to do list
def display_task():
    print("to do list:")
    for i, task in enumerate(todo_list,1):
        print(f"{i}.{task}")

#main loop
while True:
    print("\n OPtions:")
    print("1.Add Task")
    print("2.Remove Task")
    print("3.Display Tasks")
    print("4.Quit")

    choice=input("Enter your choice(1/2/3/4):")

    if choice=='1':
        task=input("enter the task to add")
        add_task(task)
    elif choice=='2':
        task=input("Enter the task to remove:")
        remove_task(task)
    elif choice=='3':
        display_task()
    elif choice=='4':
        print("good bye")
        break
    else:
        print("invalid choice.please enter a valid option")