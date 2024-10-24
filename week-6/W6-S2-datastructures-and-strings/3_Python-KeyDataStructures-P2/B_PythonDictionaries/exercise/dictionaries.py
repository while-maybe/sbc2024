#  Initialize a dictionary
details = {'name': 'John', 'age': 24, 'wears_glasses': True}

# Access elements
print(details["name"],details["age"])

# Update elements
details["age"] += 1
print(details["age"])

# Add new key-value pairs
details["email"] = "john@mail.com"
print(details)

# Remove key-value pairs
del details["email"]
print(details)

# Iterate through the dictionary
for each in details.items():
    print(each)
