class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self,l,b):  #Method Overriding
        return l*b

rec = rectangle()
print(rec.area(5,10))
