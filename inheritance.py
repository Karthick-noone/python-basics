# inheritance is used to connect parent class with child class
# single inheritance
# class dad():
#     def phone(self):
#         print("Dad has phone")

# class son(dad):
#     def laptop(self):
#         print("Son learning python")

# karthick=son()
# karthick.laptop()
# karthick.phone()

# multiple inheritance

# class dad():
#     def phone(self):
#         print("Dad using phone")

# class mom():
#     def food(self):
#         print("Mom preparing food")        

# class son(dad,mom):
#     def laptop(self):
#         print("Son learning python")

# karthick=son()

# karthick.laptop()
# karthick.phone()
# karthick.food()

# multilevel inheritance (parent connect with grandpa and son connect with parent)

# class grandpa():
#     def property(self):
#         print("Granpa is walking")
# class dad(grandpa):
#     def phone(self):
#         print("Dad using phone")

# class mom():
#     def food(self):
#         print("Mom preparing food")        

# class son(dad,mom):
#     def laptop(self):
#         print("Son learning python")

# karthick=son()

# karthick.laptop()
# karthick.phone()
# karthick.food()
# karthick.property()

# hierarchy inheritance

# class vehicle():
#     def fuel(self):
#         print("Every vehicle need fuel")

# class bike(vehicle):
#     def bike(self):
#         print("Bike needs petrol")

# class car(bike):
#     def car(self):
#         print("Car needs fuel")


# c =car()
# c.fuel()        
# c.bike()        
# c.car()        


# # super() method used to call parent class function in child class
# class Animal:
#     def sound(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         super().sound()  # Calls parent class method
#         print("Dog barks")

# dog = Dog()
# dog.speak()


# hybrid inheritance is the combination of single, multiple, multilevel and hierarchy inheritances


# class animal:

#     def dog(self):
#         print("Dog barks")

# class bird(animal):
#     def parrot(self):
#         super().dog()
#         print("Parrot flies")

# a=bird()
# a.parrot()
# # a.dog()

# super()
class parrent():

    def res(self):
        print("Parents are Responsible")

class son(parrent):
    def irres(self):
        super().res()
        print("Sons are irresponsible")

a = son()
a.irres() 