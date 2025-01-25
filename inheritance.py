class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in class A")

class b(a):
    def __init__(self):
        super().__init__()
        print("B")

    def display(self):
        print("You are in class B")

class c(b):
    def __init__(self):
        super().__init__()
        print("C")

    def display(self):
        print("You are in class C")

obj1 =c()
obj1.display()
