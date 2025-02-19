# classes are blueprint to create objects
# class Car
# object is an instacnce of class
# example
# car1 = Car("Toyota", "Camry")  # Object 1
# car2 = Car("Honda", "Civic")   # Object 2


# The self keyword represents the current object inside the class.


class Vehicle():
    def __init__(self, color, price):
        self.color = color
        self.price = price
    
    def moves(self):
        print("Moves along ...")

    def display(self):
        print(f"vehicle color is {self.color} and price is {self.price}")

my_car = Vehicle("Blue","5Cr")
my_car.moves()
print(my_car.color)
print(my_car.price)

my_car.display()

friend_car = Vehicle("White", "3Cr")
print("")
friend_car.display()
print("\n\n")

# Inheritance

class Airplane(Vehicle):
    def __init__(self, color, price, id):
        super().__init__(color, price)
        self.id = id

    def moves(self):
        # return super().moves()
        print("Flies along")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along ...")

class Bus(Vehicle):
    pass


airindia = Airplane("Black", "25cr", "ID25")

airindia.moves()

truck = Truck("Grey", "25cr", )

truck.moves()

bus = Bus("Black", "25cr")

bus.moves()
print("\n\n")
# polymorphism
#
for v in (my_car,airindia, truck,bus):
    v.display()
    v.moves()

