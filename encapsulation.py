# private variable can be accessible within the class 
#  a = 10 is variable , __a = 10 is private variable
# cannot access the private variable outside the class
# single _ variable is protected variable

# class company():
#     def __init__(self):
#         self.__company="Queen"
    
# c1=company()
# c1.__company = "King"
# print(c1.__company) #cannot access private var outside the class 



# class company():
#     def __init__(self):
#         self.__company="MS"
#     def companyname(self):
#         print(self.__company)
# c1=company()
# c1.companyname()


# class company():
#     def __init__(self):
#         self.name ="Karthick"
#         print(self.name)

# class employee(company):
#     pass
# nm = employee()