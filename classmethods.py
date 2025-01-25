class laptop:
    chargertype="C-TYPE"
    def __init__(self):
        self.brand=""
        self.price=34

    def setprice(self,price):  #instance method
        self.price=price

    def getprice(self):
        print(self.price)

    @classmethod                 #decorators
    def changechargertype(cls):  #class method
        cls.chargertype="B-TYPE"
        print("Charger type changed")

    @staticmethod                #decorators
    def info():                  #static method
        print("This is laptop class")

hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changechargertype()
hp.info()
        
        
