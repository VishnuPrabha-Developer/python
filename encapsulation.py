class company():
    def __init__(self):
        self.__companyname="GOOGLE" #private variable can be accessed within a class only
        self._companyceo="Sundar Pichai" #protected variable

    def companyname(self):
        print(self.__companyname)

c1=company()
c1.companyname()
print(c1._companyceo)
