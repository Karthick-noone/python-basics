import os
# r = Read
# a = Append
# w = Write
# x = Create

f = open("names.txt")
print(f.read())
# o/p 
# Karthick
# Full Stack Developer
# 23
# Nagercoil

print(f.read(4)) # o/p  Kart

print(f.readline()) # o/p Karthick
print(f.readline()) # o/p Karthick Full Stack Developer 

for line in f:
    print(line)
f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print(f"The file you want to open doesn't exist")
finally:
    f.close()

# f =open("names.txt","a")
# f.write("\nGenius")
# f.close

# overwrite "w"
# f = open("names.txt", "w")
# f.write("Deleted all details")

if not os.path.exists("name.txt"):
    f = open("name.txt",'x')
    f.close()

# if os.path.exists("name.txt"):
#     os.remove('name.txt')


with open("names.txt") as f:
    content = f.read()

with open("name.txt", "w") as f:
    f.write(content)

