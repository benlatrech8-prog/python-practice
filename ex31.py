from ex30 import Task, TaskList

tl=TaskList()
tl.load("tasks.json")

while True:
    print("1. Add task \n2. Show pending \n3. Complete task \n4. Remove task \n5. Save and quit")

    task=int(input("choice a task :"))
    if task == 1:
        title=input("Enter a title :").strip()
        t=Task(title)
        tl.add(t)
        tl.save("task.json")
        print("Added")
    elif task == 2:
        print(tl.pending())
    elif task == 3:
        title=input("Enter the title of task you completed :").strip()
        tl.complete(title)
    elif task == 4:
        title=input("Enter the title of task you want to remove it :").strip()
        tl.remove(title)
    elif task == 5:
        tl.save("tasks.json")
        print("Saved, Bye")
        break
    else:
        print("invalid choice")
