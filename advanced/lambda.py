# lambda is anonymous function that means namless function used for short operation , typically written in one line

#syntax lambda arguments: expression


squared = lambda num : num * num 
print(squared(5)) 

add_two = lambda num: num +2
print(add_two(5))

# def sum(a,b):
#     return a + b #instead of this method we can use it simply like below
sum_total = lambda a, b: a + b
print(sum_total(3,8))

# one function returns the another function and one function takes another function as input is called higher order function 
print ('')

def funcBuilder(x):
    return lambda num:num + x


add_ten = funcBuilder(5)
print(add_ten(5))

add_twenty = funcBuilder(6)
print(add_twenty(8))



print('')

# map() and filter() are higher order functions

numbers = [1, 2, 3, 4, 5, 6]

squared_numbers = map(lambda num : num * num ,numbers)

odd_numbers = filter(lambda num : num % 2 != 0,numbers) #filter gets True values only so it is faster than map()

print(list(squared_numbers))
print(list(odd_numbers))

print('')

from functools import reduce

nums = [1, 2, 3, 4, 6, 7]

# acc - accumulator , curr -current

# Using reduce() to calculate the sum
sum_nums = reduce(lambda acc, curr: acc + curr, nums)
print(sum_nums)  # Output: 23


# Using built-in sum()
print(sum(nums))  # Output: 23


names = ["Karthick", "sura", "Logesh"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)
