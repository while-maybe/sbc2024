# Custom Iterator Class
print("\n\nCustom Iterator Class")
class CustomIterator:
    current_index = 0
    def __init__(self, collection):
        self.collection = collection
        self.current = -1
        
    def __iter__(self): # implement __iter__ dunder method
        return self
        
    def __next__(self): # implement __next__ dunder method
        self.current += 1
        if self.current < len(self.collection):
            return self.collection[self.current]
        else:
            raise StopIteration # raise StopIteration if attempted access to out-of-bounds element

for each in CustomIterator([1, 2, 3]):
    print(each, end=" ") # replace the default new line character on print with a space so all elements are printed in the same line
    
# Complex String Iterator
print("\n\nComplex String Iterator")
class ComplexStringIter:
    current_index = 0
    def __init__(self, string):
        self.string = string
        self.current = -1
        
    def __iter__(self): # implement __iter__ dunder method
        return self
        
    def __next__(self): # implement __next__ dunder method
        self.current += 1
        if self.current < len(self.string):
            return self.string[self.current].upper()
        else:
            raise StopIteration # raise StopIteration if attempted access to out-of-bounds element

for each in ComplexStringIter("Hello"):
    print(each, end=" ") # replace the default new line character on print with a space so all elements are printed in the same line
    
# StopIteration Handling
print("\n\nStopIteration Handling")
seq = iter([1, 2, 3, 4, 5])
while True: # infinite loop demonstrates exception being caught
    try:
        print(next(seq), end=" ") # replace the default new line character on print with a space so all elements are printed in the same line
    except:
        print("<- END OF LIST")
        break

# Built-in Functions with Iterators
print("\n\nBuilt-in Functions with Iterators")
list_even = [2, 4, 6, 8, 10]

print("demonstrating .enumerate()")
for index, number in enumerate(list_even, start=10): # start lets us begin from a different number than zero
    print(f"position {index} contains {number:2}")
    
list_odd = [1, 3, 5, 7, 9]
print("\ndemonstrating .zip()")
for joint in zip(list_odd, list_even):
    print(f"list1 - {joint[0]}, list2 - {joint[1]}")
    
# Chained Iterators
print("\n\nChained Iterators")

from itertools import chain, permutations
# prints a list of a repetition of all the permutations resulting from chaining together two iterables
print(list(permutations(chain([0, 1], [2, 3]))))


# Python Comprehensions for Data Manipulation
# Advanced List Comprehension
print("\n\nAdvanced List Comprehension")
print([x ** 2 for x in range(1, 21) if (x % 2)])

# Nested List Comprehension
print("\n\nNested List Comprehension")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([x for row in matrix for x in row])

# Set Comprehension with Conditions
print("\n\nSet Comprehension with Conditions")
print(list(
    map(lambda y: y ** 2, 
        filter(lambda x: not (x % 2),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
    )
)) # chaining these methods in this way looks horrible in Python  :/

# Complex Dictionary Comprehension
print("\n\nComplex Dictionary Comprehension")
source = {
    "one": 10,
    "two": 20,
    "three": 30,
    "four": 40
}
print({key: value for key, value in source.items() if value > 20})

# Real-World Scenario
print("\n\nReal-World Scenario")
fake_log = '''2024-10-28 10:00:01 INFO  User 'john_doe' logged in successfully.
2024-10-28 10:01:45 INFO  File 'report_q3.xlsx' was uploaded by user 'john_doe'.
2024-10-28 10:02:22 ERROR Failed to process payment for order #1234.
2024-10-28 10:05:13 INFO  User 'anna_smith' logged out.
2024-10-28 10:06:47 WARNING Low disk space on server 'server-02'.
2024-10-28 10:10:01 INFO  Scheduled backup completed on server 'server-01'.
2024-10-28 10:11:30 ERROR Database connection timeout on 'db-server'.
2024-10-28 10:12:05 INFO  User 'mike_ross' accessed 'settings' page.
2024-10-28 10:15:20 ERROR Unauthorized access attempt detected from IP '192.168.0.102'.
2024-10-28 10:17:59 INFO  Application version '2.3.1' deployed successfully.
'''
print([entry for entry in fake_log.splitlines() if "ERROR" in entry])


# Mastering Python Loops
# List Manipulation with Loops
print("\n\nList Manipulation with Loops")
listing = [
    {"name": "Jonna", "grade": "F"},
    {"name": "John", "grade": "B"},
    {"name": "Rick", "grade": "C"},
    {"name": "Rachel", "grade": "B"}
]
for student in listing:
    print(f"{student["name"]} landed a {student["grade"]}")


# Nested Loops
print("\n\nNested Loops")
for x in [1, 4, 7]:
    for y in range(1, 11):
        print(f"{x:2} * {y:2} = {x * y:2}   {x + 1:2} * {y:2} = {(x + 1) * y:2}   {x + 2:2} * {y:2} = {(x + 2) * y:2}")
    print()

# Break and Continue Statements
print("\n\nBreak and Continue Statements")
ask_more = True
count = 0
while ask_more:
    answer = input(f"[{count}] your choice ('q' to quit): ")
    try:
        if int(answer) > 0:
            count += 1
            continue
    except ValueError: # if parsing the answer to an int fails
        if answer.lower() == 'q':
            print("goodbye")
            break

# Looping Through a Dictionary:
print("\n\nLooping Through a Dictionary:")
stock_prices = {
    "AAPL": 182.50,
    "MSFT": 319.23,
    "GOOGL": 131.75,
    "AMZN": 141.43,
    "TSLA": 217.44,
    "META": 297.28,
    "NVDA": 412.86,
    "NFLX": 437.50,
    "DIS": 85.94,
    "IBM": 143.32
}
threshold = float(input(f"Enter a threshold [{min(stock_prices.values())}..{max(stock_prices.values())}]: "))
for key, value in stock_prices.items():
    if value >= threshold:
        print(key, end=" ")

# Data Filtering with Loops
print("\n\nData Filtering with Loops")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in numbers:
    if n % 2:
        print(n, end=" ")

print("\n\n")


# Infinite Custom Iterator: Create a custom iterator class that generates an infinite sequence of natural numbers.

class Infinite:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 3
        return self.current

example = Infinite()
for n in range(20):
    print(f"{next(example)}", end=" ")
print("\n")


# Complex Chaining: Extend chained iterators to apply multiple transformations.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sorted(filter(lambda y: y > 10, map(lambda x: x * 3, numbers)), reverse=True)

print(list(result))

