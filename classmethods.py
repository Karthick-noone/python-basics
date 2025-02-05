# Instance method(function)

# class phone:

#     # this is class variable
#     chargertype = "C-type"
#     def __init__(self,brand,price):
#         # this is instance variable
#         self.brand =brand
#         self.price =price
#         # self.chargertype =chargertype
#     def display(self):
#         print("Brand: ",self.brand)
#         print("price: ",self.price)
#         print("chargertype: ",self.chargertype)
    
# phone.chargertype="B-type"
# realme = phone("Realme",10000)
# redmi = phone("Redmi",15000)
# vivo = phone("Vivo", 20000)

# realme.display()
# redmi.display()
# vivo.display()


# class method(function)

# class variable 
# class phone:

#     # this is class variable
#     chargertype = "C-type"
#     def __init__(self,brand,price):
#         # this is instance variable
#         self.brand =brand
#         self.price =price
#         # self.chargertype =chargertype
#     def display(self):
#         print("Brand: ",self.brand)
#         print("price: ",self.price)
#         # print("chargertype: ",self.chargertype)

#     #  @classmethod is used for class method here self is no need 
#     @classmethod
#     def chrgeType(cls):
#         cls.chargertype="E-type"
#         print("Charger type:", cls.chargertype)
#     @staticmethod
#     def info():
#         print("This is phone")

# @classmethod and @staticmethod are decorators
    
# # phone.chargertype="B-type"
# realme = phone("Realme",10000)
# redmi = phone("Redmi",15000)
# vivo = phone("Vivo", 20000)

# # phone.chrgeType()
# # phone.info()

# # for using a function without class and instance (@classmethod and self) use @ staticmethod
# realme.info()  

# # realme.display()
# # redmi.display()
# # vivo.display()

