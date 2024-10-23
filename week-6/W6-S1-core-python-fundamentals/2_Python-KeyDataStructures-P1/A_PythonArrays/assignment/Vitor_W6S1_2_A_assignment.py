# Start writing code with comments form here

# Array creation and initialization
my_numbers = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]

# Accessing and updating array elements
# accessing second and before last element
print(my_numbers[1], my_numbers[-2])

# modify elements in the array
my_numbers[-1] = 0
print(my_numbers) # last element has been changed from 9 to 0

# get elements from indexes 3 and 4
print(my_numbers[3:5]) # upper limit not included, prints "4 4"

# appending a value to the end
my_numbers.append(9) # appends 9 to the end of the array
print(my_numbers)

my_numbers.remove(6) # remove element with value 6 from list
# my_numbers.remove(6) - attempting to remove non-existing element would throw a ValueError exception
print(my_numbers)

my_numbers.insert(8, 9) # insert an element at position 8 with value 9
print(my_numbers)

more_numbers = [8, 7, 6, 5, 4, 3, 2, 1]
my_numbers.extend(more_numbers) # extendes a list with elements from an iterable - in this case another list
print(my_numbers)

removed = my_numbers.pop(-2) # removes an element at given position returning it
print(removed, my_numbers)

three_numbers = [0, 1, 5]
three_numbers.clear() # empties the list
print(three_numbers)

print(my_numbers.index(9)) # returns the first index of the element specified if it exists - returns 8 meaning value 9 is at position 8

print(sorted(my_numbers)) # sorts the list (in ascending order) - does NOT modify the list
print(my_numbers)

my_numbers.sort() # sorts the list (in ascending order) - modifies the list
print(my_numbers)

my_numbers.reverse() # reverses the order of the elements in the list
print(my_numbers)

print(my_numbers.count(4)) # counts the ocurrences of the value provided as arguments in the list - returns 3, meaning the number 4 is present 3 times in the list

# quick demo of list compreension, new list containing only multiples of 3
by_three = [x for x in my_numbers if not (x % 3)]
print(by_three)

# creates a new list with the numeric double of each element by using a lambda function
print(list(map(lambda x: x * 2, my_numbers)))

# all code has been commented with print statements used as needed to demonstrate
