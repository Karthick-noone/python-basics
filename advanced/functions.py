# functions start with def keyword and fn_name() 

# def sum(nm1, nm2):
#     return nm1+ nm2

# total = sum(3,6)
# print(total)

# def multiple_values(*args): # inside this function values are parameters and *args means multiple or infinite args
#     print(args)
#     print(type(args))
# multiple_values("karthick",24, "IT") #inside this function values are arguments


# def add(*nums):
#     sum = 0
#     for n in nums:
#         sum = sum + n
#     print(sum)

# add(1,2,3)

# def multiple_named_values(**kwargs): # **kwargs used to get dictionary like values  
#     print(kwargs)
#     print(type(kwargs))

# multiple_named_values(name ="Karthick", age = 23 )

# def add(a,b,*args, option = True, **kwargs):
#     print("")
#     print(a,b)
#     print(args)
#     print(option)
#     print(kwargs)
    

# add(1,2,45,67,name ="Karthick", salary = 150000)

#//////////Recursion/////////
# call the function inside the function is called recursive

def add(num):

    if num >= 9:
        return num + 1
    total = num + 1
    print(total)

    return add(total)

number = add(0)
print(number)





