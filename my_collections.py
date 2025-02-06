# list []
# # allows duplicate , changeable

# a=[1,2,3,4,5,6,7]
# b=[8,9,10]
# # a.append(45)
# # a.pop()
# # a.pop(6)
# # a.insert(2, 3)
# # a.pop(2)
# # a[2] = 3
# a.extend(b)
# print(a)
# # print(a[3])


# tuple ()
#Allow duplicate, cannot modify, cannot add, remove items
# a =(1,2,3,4)
# b=list(a)
# print (a)
# print (b)


# Set {}
# Do not allow duplicate , automatically remove duplicate , cannot modify but can add or remove and sets are unordered

# a = {1,2,3,4,15 }     
# # a.pop() mostly dont use
# a.remove(15)
# print(a)
# # output is {1, 2, 3, 4}

# Dictionary {}
#  stores key value pairs 
# do not allow duplicate value , duplicate key will overwrite existing value

a={
    "Name:":"Karthick",
    "Age" : 23
    }

a["Age"]=24
a.update({"Age":25})

# a.pop("Age")
# del a["Age"]
a["Location"]="Nagercoil"
a.clear()

print(a)