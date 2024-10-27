def say_morning():
    return "Hello, good morning"

print(say_morning())

def personalized(name):
    return f"Good morning {name}"
print(personalized("John"))

def is_a_bigger(a, b):
    return "\"a\" is bigger then \"b\"" if a > b else "\"a\" is not bigger"
print(is_a_bigger(11, 10))

def john_by_default(name="John"):
    return f"Good morning {name}"
print(john_by_default()) # notice no name is provided as an argument

def add_everything(*args):
    return sum(args)
print (add_everything(1, 2, 3, 4, 5))

def greet_everybody(**kwargs):
    for each in kwargs.values():
        print(f"Hello {each}", end=" ")
greet_everybody(name1="John", name2="Lara")
