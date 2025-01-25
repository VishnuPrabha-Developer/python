class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
        
    def display(self):
        print(self.name,self.salary,self.department)

Ryan=manager("Ryan","10000","AI")
Ryan.display()
