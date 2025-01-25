class teacher:
    def __init__(self,name,reg_no):
        self.name=name
        self.reg_no=reg_no
    def display(self):
        print("Name:",self.name)
        print("RegisterNumber:",self.reg_no)

t1=teacher("brindha","1")
t2=teacher("smitha","2")

t1.display()
t2.display()


        
