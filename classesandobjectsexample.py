class student:
    def __init__(self):
        name=""
        register_number=""
    def display(self):
        print("name:",self.name)
        print("register_number:",self.register_number)

student1=student()

student1.name="Ryan"
student1.register_number="1"
student1.display()
