x=2
try:
    print(x)
except Exception as error:
    print(error)

else:
    print("No errors")

finally:
    print("Finally will print if error or there is no error")