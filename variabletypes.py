class phone:
    chargertype="C-TYPE"  #Class Variable
    def __init__(self,brand,price):
        self.brand=brand   #Instance Variable
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("ChargerType:",self.chargertype)

samsung=phone("Samsung","30000")
poco=phone("POCO","20000")
moto=phone("MOTO","10000")

samsung.display()
poco.display()
moto.display()
