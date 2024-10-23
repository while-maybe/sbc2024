# array initialization
fruits = ["apple", "banana", "cherry", "kiwi"]
print(fruits)

# accessing individual array elements
print(fruits[0], fruits[2])

# updating the first element
fruits[0] = "orange"
print(fruits[0])

# slicing the array by creating a sub array made of elements 1 and 2 - end index not included
print(fruits[1:3])

# adding elements
fruits.append("melon")
print(fruits)

# removing elements with the remove method
# NOTE: throws a ValueError exception if element does not exist in array
fruits.remove("banana")
print(fruits)

# I have been printing and commenting as I go along
