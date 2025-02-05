# # polymorphism is a function name being used for differnt types or different purposes
# def add(a,b,c=0):
#     print(a+b+c)
# add(1,2)  #o/p 3
# add(1,2,3)  # op 6
# # here passing 3 value will overwrite the assigned value c=0


# method overriding (polymorphism)
# class animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(animal):
#     def sound(self):
#         print("Dogs barks")

# class Bird(animal):
#     def sound(self):
#         print("Birds sing")


# a= Dog()
# a.sound()

# b=Bird()
# b.sound()


# class shape():
#     def area(self):
#         return 0
    
# class rectangle(shape):
#     def area(self):
#         l= 10
#         b=20
#         print(l*b)

# r1=rectangle()
# r1.area()


# class person():
#     def __init__(self,name):
#         self.name=name

# class student(person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade =grade
#     def display(self):
#         print(self.name)
#         print(self.grade)

# st1 = student("John","A")
# st1.display()


# class person():
#     def __init__(self,name):
#         self.name =name
    
# class student(person):
#     def __init__(self, name, grade):
#         super().__init__(name)
#         self.grade= grade
    
#     def display(self):
#         print(self.name,self.grade)
# s1=student("karthick","A")
# s1.display()        


# class vehicle():
#     def start(self):
#         print("vehicle started")
    
# class car(vehicle):
#     def start(self):
#         print("Car started")

# v=car()
# v.start()

class Employee():
    def __init__(self,name, salary):
        self.name =name
        self.salary =salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        print(self.name, self.salary, self.department)

nm=input("Enter name: ")
salary=int(input("Enter salary: "))
dep=input("Enter department: ")
emp = Manager(nm,salary,dep)
emp.display()
