# Set creation and initialization.
set1 = {10, 15, 20, 25, 30}
set2 = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

# Accessing and modifying set elements.

print(set1, set2) # print before transforming elements

# print each element
for item in set1:
    print(item)

set1.add(35)
print(set1, set2)

set2.remove(13) # .remove() throws an exception if element doesn't exist, alternative .discard() won't throw exception
print(set1, set2)

# Common set operations like union, intersection, and difference.
print(set1.union(set2)) # .union() method
print(set1 | set2) # union through | operator

print(set1.intersection(set2)) # .intersection() method
print(set1 & set2) # intersection using & operator

print(set1.difference(set2)) # .difference() method
print(set1 - set2) # difference usin - operator
