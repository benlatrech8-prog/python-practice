from ex30 import Task, TaskList

def test_complete():
    tl=TaskList()
    tl.add(Task("A"))
    tl.add(Task("B"))
    tl.complete("B")
    assert tl.find("B").done == True
    assert tl.find("A").done == False
    assert tl.pending() == ["A"]
def test_remove_find():
    tl=TaskList()
    tl.add(Task("A"))
    tl.add(Task("B"))
    tl.add(Task("C"))
    tl.add(Task("D"))
    assert len(tl.tasks) == 4
    tl.remove("D")
    assert len(tl.tasks) == 3
    assert tl.find("D") is None
    assert tl.find("B").done is not None
def test_save_load():
    tl=TaskList()
    tl.add(Task("A"))
    tl.add(Task("B"))
    tl.complete("A")
    tl.save("test_tasks.json")

    tl2=TaskList()
    tl2.load("test_tasks.json")
    assert len(tl2.tasks) == 2
    assert tl2.find("A").done == True
    assert tl2.pending() == ["B"]

test_complete()
test_remove_find()
test_save_load()
print("All remove and find tests passed")
