# Generate two sets

import random
set1 = set(random.randint(1, 10) for _ in range(5)) # randint sometimes generates a number that is already present in the set so it may be that the set length varies
set2 = set(x for x in range(5, 11))
print(set1, set2)

# Use union, intersection, and difference to manipulate the sets
print(f"Union - {set1 | set2}") # union
print(f"Intersection - {set1 & set2}") # intersection
print(f"Difference - {set1 - set2}") # difference

# Add and remove elements
set2.add(11)
set2.remove(5)
print(set2) # number 11 added, 5 removed

# Use set comprehension - Generate a new set containing only even numbers from one of the original sets using set comprehension.
new_set = {x for x in set2 if not (x % 2)} # negating a by two division reminder makes condition True when number is even
print(new_set)
