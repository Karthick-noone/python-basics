
# # list is mutable 
# fruits = [ "apple", "mango", "banana"]
# animals =["Tiger","lion","cheetah"]


# fruits.append("graph") # add items in a list
# fruits.extend(animals) # used to merge 2 lists

# fruits.insert(0,"Elephant") #insert used to place item in position

# fruits.remove("Elephant")
# fruits[2:2] = ["food"]

# # animals =[]
# # del animals
# # print(fruits[2:-1])

# print(fruits)
# print(animals)

# # print(len(fruits))

# fruits.sort(key=str.lower) # it will change the Caps letter to small and will sort 

# fruits.append(25)
# print(fruits)
# /////////////////////////

# num = [1,4,56,3,14]

# num.sort(reverse=True)

# print(num)

# num.reverse()
# print(num)

# ///////////////////sorted - global variable used to get actual value

# num =  [1,4,56,3,14]

# print(sorted(num, reverse=True))

# print(num)


# # //////list copy//

# numscopy = num.copy() #method 1
# numscopy2 = list(num) #method 2
# numscopy3 = num[:] #method 3

# print(numscopy)
# print(numscopy2)
# print(numscopy3)

# mylist =list([1,"karthick", True])

# print(mylist)

# Tuple//////////////// immutable


# my_tuple = ("karthick", 1 ,True)


# print(my_tuple)
# print(type(my_tuple))

# my_list = list(my_tuple)

# my_list.append("23")

# new_tuple = tuple(my_list)

# print(new_tuple)

# # we can unpack tuple
# your_tuple = (1,2,3,4,5,5,6)

# (one, *two, hi) = your_tuple

# print(one)
# print(*two)
# print(hi)

# print(your_tuple.count(5))



# ////dictionary////////// key value pair inside {}

#do not accept duplicate


# student = {

#     "name" : "karthick",
#     "Reg No": 962623405007,
#     "Age"  : 23,
#     "Dept" : "CSE"

# }

# student = dict(name = "Karthick", Age = "21", Dept = "BME")

# print(student)
# print(len(student))

# print(student["name"]) #use [] to access value
# print(student.get("name")) #use get method to access value

# print(student.keys()) # to get keys only
# print(student.values()) # to get values only
# print(student.items()) # to get pair items as tuple
# # o/p dict_items([('name', 'Karthick'), ('Age', '21'), ('Dept', 'BME')])      

# # print(std2)

# print("name" in student)

# student["Age"] =25
# student["Dept"] ="IT"

# student.update({"Salary":50000})

# student.pop("Age")
# print(student.popitem())
# print(student)

# del student["name"]

# del student 
# student.clear()
# print(student)


# copy dictionary



# std2 =student # create a reference, not create a copy of student (do not use this method)
# employee=student.copy()
# employee2=dict(student)


# # employee["Experience"] = 2

# print(student)
# print(employee)
# print(employee2)

# /////////nested dictionaries////////////
# emp1 = {

#     "name":"Karthick",
#     "dept":"Full Stack Developer"    
# }

# emp2 = {

#     "name":"Mareeswaran",
#     "dept":"Designer"
# }

# MindTek = {
#     "Employee 1" :emp1,
#     "Employee 2" :emp2
# }

# print(MindTek)
# print(MindTek["Employee 1"]['name'])


# ////set///////
#do not accept duplicate
# can not refer an element in set using index because its an unorder

# num ={1,2,3,4,5,5,56}

# num2 = set((1,2,4,5,6))



# print(num)
# print(type(num))
# print(len(num))
# print(num2)

# mixed_values = {1, True, False, 0, 5,8,9, "Karthick"}

# print(mixed_values)

# num2.add(3)
# print(num2)

# num.update(num2) # used to add element is a set

# print(num)

# one ={1,2,3}
# two = {5,6,7,3,2}

# newset = one.union(two) # union used to merge 2 sets

# print(newset)

# one.intersection_update(two)

# print(one)

# one.symmetric_difference_update(two)

# print(one)