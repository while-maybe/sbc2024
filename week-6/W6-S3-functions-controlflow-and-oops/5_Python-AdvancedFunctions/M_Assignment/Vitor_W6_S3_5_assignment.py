# 1. **Basic Function**:
def greet():
    return "Hey there"

print(greet())

# Function with Parameters
def create_message(name, age):
    return f"Hi {name}, you are {age} years old"

print(create_message("John", 20))

# Function with Default Arguments
def greet(name="Guest"):
    return f"Hello {name}, how are you today?"

print(greet("Anna"))

# Regular Expression Function
def validate_email(email):
    import re
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.search(pattern, email) is not None:
        return "valid :)"
    return "invalid :("

print(f"The E-mail is: {validate_email("some.email@mail.com")}")

# Function Handling a Dictionary
def process_user_info(user_data):
    print("\nStarting process_user_info()")
    import re
    name_pattern = r'[A-Za-z]{2,25}\s[A-Za-z]{2,25}'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    phone_pattern = r'^(07\d{8,12}|447\d{7,11})$'
    if re.search(name_pattern, user_data["name"]) is None:
        return "Invalid name"
    elif re.search(email_pattern, user_data["email"]) is None:
        return "Invalid E-mail"
    elif re.search(phone_pattern, user_data["phone"]) is None:
        return "Invalid phone number"
    else:
        return "data validated"

user1 = {
    "name": "Diane Smith", # needs a name AND a surname
    "email": "diane@mail.com",
    "phone": "07712344657"
}

print(process_user_info(user1))


# Basic Lambda Function
square = lambda x: x ** 2
print(square(3))

numbers = [1, 2, 3, 4, 5, 6]
# Using map()
print(list(map(lambda x: x ** 2, numbers)))

# list(map(lambda x: x ** 2, numbers))
strings = ["hello", "test", "anchor", "whatever", "alcohol"]
print(list(filter(lambda a: "a" in a, strings)))

# Sorting with Lambda
lot = [("John", 6), ("Anna", 55), ("Richard", 30)]
print(list(sorted(lot, key=lambda a: a[1]))) # sort by age, element index 1 in tuples

# Logging Decorator
def logging_decorator(func):
    
    def wrapper(*args):
        print(f"\nCalling \"{func.__name__}\" with {args}")
        func(*args)
        print("Your function is over")
    return wrapper

@logging_decorator
def create_message(name, age):
    # print(name, age)
    print(f"Hi {name}, you are {age} years old")

create_message("John", 20)

# Timing Decorator
def timing_decorator(func):
    
    def wrapper():
        from time import time
        start_time = time()
        print(f"\nRunning {func.__name__}...")
        func()
        total_time = (time() - start_time) * 1000
        print(f"Took {total_time:.2f} ms")
    return wrapper

@timing_decorator
def add_a_lot(limit=1_000_000):
    x = 0
    for i in range(limit):
        x += 1

add_a_lot()

# Parameterized Decorator
def param_logging_decorator(func, level=1):
    
    def wrapper(l = level):
        if l:    
            from time import time
            start_time = time()
            print(f"\n[1 LOG] Running...")
        else:
            print("[0 LOG] Running your function...")
            
        func()
        
        if l:
            total_time = (time() - start_time) * 1000
            print(f"[1 LOG] Took {total_time:.2f}ms")
        else:
            print("[0 LOG] Done")
    return wrapper

# change logging level in the level parameter below
@param_logging_decorator
def add_a_lot_b(limit=1_000_000):
    x = 0
    for i in range(limit):
        x += 1

add_a_lot_b()
