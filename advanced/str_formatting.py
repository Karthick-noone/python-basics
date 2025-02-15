# f-strings


name = "Karthick"
coins = 6

# method1 string concatenation
print( name + " has " + str(coins) + " coins left")

# %method

mesg = "\n%s has %s coins left." % (name, coins) 

print(mesg)

# string.format() method

message = "\n{} has {} coins left".format(name, coins)

print(message)


message = "\n{1} has {0} coins left".format(coins,name)

print(message)

message = "\n{a} has {b} coins left".format(b =coins,a = name)

print(message)

# dictionary

player = {"name":"Virat",'coins': 5}

message = "\n{name} has {coins} coins left".format(**player)

print(message)

# f- string

message = f"\n{name.lower()} has {coins} ,{coins * 2} coins left"
message = f"\n{player["name"]} has {coins} ,{coins * 2} coins left"

print(message)


num = 10 

print(f"2.25 times {num} is {2.25 * num:.2f}")
# o/p 2.25 times 10 is 22.50    
print(f"2.25 times {num} is {2.25 * num:.3f}")
# o/p 2.25 times 10 is 22.500    


# def greet(a,b):
#     return a + b # return keyword used to send back values

# nm = greet(5,7)
# print(nm)

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, Guest!
greet("Karthick")  # Output: Hello, Karthick!
