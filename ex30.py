import json
class Task():
    def __init__(self, title, done = False):
        self.title=title
        self.done=done

    def complete(self):
        self.done=True

    def to_dict(self):
        return {"title": self.title, "done": self.done}

class TaskList():
    def __init__(self):
        self.tasks=[]
    def add(self,task):
        self.tasks.append(task)

    def find(self,title):
        for t in self.tasks:
            if t.title== title:
                return t
        return None

    def complete(self,title):
        task=self.find(title)
        if task is None:
            print("Task Not Found")
        else:
            task.complete()

    def remove(self, title):
        task=self.find(title)
        if task is None:
            print("Task Not Found")
        else:
            self.tasks.remove(task)
    def pending(self):
        pen=[]
        for t in self.tasks:
            if t.done== False:
                pen.append(t.title)
        return pen

    def save(self, filename):
        data=[]
        for d in self.tasks:
            data.append(d.to_dict())
        with open (filename, "w") as f:
            json.dump(data, f, indent=2)
    def load(self,filename):
        try:
            with open (filename, "r") as f:
                data=json.load(f)
        except FileNotFoundError:
            data=[]
        self.tasks=[]
        for d in data:
            task=Task(d["title"],d["done"])
            self.tasks.append(task)

if __name__=="main":
    t = Task("Buy bread")
    print("Test 1a:", t.title, t.done)
    t.complete()

    print("Test 1b:", t.done)
    print("Test 1c:", t.to_dict())
    tl = TaskList()
    tl.add(Task("Buy bread"))
    tl.add(Task("Study Python"))
    tl.add(Task("Call mom"))

    print("Test 2a:", len(tl.tasks))
    print("Test 2b:", tl.find("Study Python").title)
    print("Test 2c:", tl.find("Gym"))

    print("Test 3a:", tl.pending())
    tl.complete("Buy bread")
    print("Test 3b:",tl.pending())
    tl.complete("Gym")
    tl.remove("Call mom")
    print("Test 3c:",tl.pending())
    print("Test 3d:",len(tl.tasks))
    tl.remove("Gym")

    empty = TaskList()
    empty.load("no_task.json")
    print("Test 4:",empty.pending())

    tl.save("tasks.json")
    tl2=TaskList()
    tl2.load("tasks.json")

    print("Test 5a:",len(tl2.tasks))
    print("test 5b:",tl2.pending())
    print("test 5c:",tl2.find("Buy bread").done)



