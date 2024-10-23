# Start writing code with comments form here

# mutable variable declaration and assignment
fruits = ["mango", "pineapple"]
student = {
    "name": "John",
    "email": "johnsemail@mail.com",
    "grade": "A"
}
print(fruits, student)

# immutable variable declaration and assignment
x = 55
name = "Jonathan"
lucky_numbers = (11, 4, 44, 45, 6) # a tuple
print(x, name, lucky_numbers)

# demonstration of CONSTANT syntax
INSTALLED_OS = "win32"
PI = 3.1415

# list are mutable
first_letters = ["a", "b", "c", "d", "e"]
first_letters[-1] = "z"
print(first_letters)

# integers are immutable
x = 5 # x = 5
address_first = id(x) # stores the memory address of the value
y = x # y = x (at this moment x is 5 so, y = 5)
x = 10
address_second = id(x) # stores the memory address of the value
print(x, y) # y still has a value of 5
print(id(address_first), id(address_second)) # same variables, different values, addresses mismatch (in my case 125194690568528 != 125194690575440).

# a shallow copy of a list - copies point to the same values in memory:
values = [1, 2, 3]
shallow_values = values
shallow_values[0] = 9 
print(values, shallow_values) # both lists show same result so the value was common to both
deep_copy = values[:]
deep_copy[0] = 5 # [9, 2, 3] == [9, 2, 3]
print(values, deep_copy) # [9, 2, 3] != [5, 2, 3]

# all examples are commented. snake_case has been used throughout