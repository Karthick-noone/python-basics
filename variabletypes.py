# instance variable using self 
# class phone:

#     def __init__(self,brand,price,chargertype):
#         self.brand =brand
#         self.price =price
#         self.chargertype =chargertype
#     def display(self):
#         print("Brand: ",self.brand)
#         print("price: ",self.price)
#         print("chargertype: ",self.chargertype)

# realme = phone("Realme",10000, "C-type")
# redmi = phone("Redmi",15000, "C-type")
# vivo = phone("Vivo", 20000,"C-type")

# realme.display()
# redmi.display()
# vivo.display()


# class variable 
class phone:

    # this is class variable
    chargertype = "C-type"
    def __init__(self,brand,price):
        # this is instance variable
        self.brand =brand
        self.price =price
        # self.chargertype =chargertype
    def display(self):
        print("Brand: ",self.brand)
        print("price: ",self.price)
        print("chargertype: ",self.chargertype)
    
phone.chargertype="B-type"
realme = phone("Realme",10000)
redmi = phone("Redmi",15000)
vivo = phone("Vivo", 20000)

realme.display()
redmi.display()
vivo.display()

