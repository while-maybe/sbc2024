# creating several tuples with different types such as integers, strings, and floats
some_odds = (1, 3, 5, 7, 9, 9, 9, 11, 13)
greet_strings = ("hello", "hey", "hi", "hya", "wassup")
add_to_pi_floats = (3.14, 4.25, 5.36, 6.47, 7.58, 8.69, 9.70)
all_sorts = (4, "hello", 31.4, True)

# Access and unpack elements
first_odd, second_odd, third_odd, *_ = some_odds # *_ means don't care about value the remaining tuple elements
print(first_odd, second_odd, third_odd)

_, greeting, age, wears_watch = all_sorts
print(greeting, age, wears_watch)

# slicing to create sub-tuples
print(greet_strings[-2:]) # returns a slice from the element before last to the end
print(all_sorts[1:3]) # returns a slice of elements with index 1 and 2 
print(add_to_pi_floats[2::2]) # returns every other element starting at index 2 to the end of the tuple

# Concatenate and repeat tuples
print(some_odds + add_to_pi_floats) # concatenates both tuples into one
print(greet_strings * 3) # returns a tuple repeated 3 times

# tuple methods
print(some_odds.count(9)) # returns number of occurrences of the value 9
print(greet_strings.index("hi")) # returns the index of the first value maatch

# returns a 5 element tuple made of random numbers
def create_random_tuple():
    import random
    # create a lambda function to generate an int random number between 1 and 10 - helpful to make the return statement a lot shorted in length
    gen = lambda: random.randrange(1,10)
    return (gen(), gen(), gen(), gen(), gen())

print(create_random_tuple())

