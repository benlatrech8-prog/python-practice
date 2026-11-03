import json
class Book():
    def __init__(self, title, author,available=True):
        self.title= title
        self.author=author
        self.available=available

    def borrow(self):
        if self.available== True:
            self.available=False
            return True
        else:
            print("already borrowed")
            return False

    def give_back(self):
        self.available = True

    def to_dict(self):
        return {"title":self.title, "author":self.author, "available":self.available}

class Library():
    def __init__(self):
        self.books=[]
    def add(self, book):
        self.books.append(book)
    def find(self,title):
        for book in self.books:
            if book.title == title:
                return book

        print("book not found")
        return None
    def available_books(self):
        av_b=[]
        for book in self.books:
            if book.available==True:
                av_b.append(book.title)
        return av_b
    def save(self,filename):
        data=[]
        for b in self.books:
            data.append(b.to_dict())
        with open (filename, "w") as f:
            json.dump(data, f, indent =2)
    def load(self,filename):
        try:
            with open (filename, "r") as f:
                data=json.load(f)
        except FileNotFoundError:
            data=[]
        self.books=[]
        for d in data:
            b=Book(d["title"], d["author"], d["available"])
            self.books.append(b)

# ---- Test 1: first run, the file doesn't exist yet ----
empty = Library()
empty.load("no_such_file.json")
print("Test 1:", empty.available_books())        # []

# ---- Test 2: save a library with one borrowed book ----
library = Library()
library.add(Book("Dune", "Herbert"))
library.add(Book("1984", "Orwell"))
library.add(Book("Hobbit", "Tolkien"))
library.find("1984").borrow()
library.save("library.json")
print("Test 2: saved")

# ---- Test 3: load into a NEW library ----
library2 = Library()
library2.load("library.json")
print("Test 3:", library2.available_books())     # ['Dune', 'Hobbit']

# ---- Test 4: the loaded book is a real object ----
book = library2.find("1984")
print("Test 4:", book.author, book.available)    # Orwell False
book.give_back()
print("Test 4:", library2.available_books())     # ['Dune', '1984', 'Hobbit']

# ---- Test 5: load twice, no duplicates ----
library2.load("library.json")
library2.load("library.json")
print("Test 5:", len(library2.books))            # 3
