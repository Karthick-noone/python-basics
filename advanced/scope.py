# scope is global variable calls outside the function

name = "Karthick" # global scope(variable)

# def id(dept):
#     age = 23 # variable assigned inside the function is local variable(scope)

#     print(name)
#     print(age)
#     print(dept)

# id("Full Stack Developer")


# def employee():
#     print('')
#     id("AI developer")
# employee()


age = 23

def employee(name):
    global age  # if you want to modify the global variable inside the function then assign that as "global var" inside function 
    age += 1
    firstname =name 
    color = "green"
    print(color) #o/p green

    def id():

        nonlocal color # nonlocal used to modify the gloabal variable inside the function

        color = "red"
        print(age)
        print(firstname)
        print(color) # o/p red
    id()
    print('')
    print(color)  # o/p red
    
employee("Karthick")

