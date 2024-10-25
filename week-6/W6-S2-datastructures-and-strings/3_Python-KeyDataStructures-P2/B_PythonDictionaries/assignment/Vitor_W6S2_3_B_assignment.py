# create a nested dictionary
users = {
    "user1": {
        "name": "John",
        "age": 22,
        "email": "john@mail.com"
    },
    "user2": {
        "name": "Anna",
        "age": 44,
        "email": "anna@hotmail.com"
    },
    "user3": {
        "name": "Ricky",
        "age": 30,
        "email": "rickzdaman@yahoo.com"
    }
}

# Dynamically add key-value pairs
import random
from pprint import pprint
for user in users.values():
    user["user_id"] =  f"{random.randint(0, 1_000):04}"
    
print(users)

# Merge dictionaries
bonus_users = {
    "user100": {
        "name": "Jack",
        "age": 11,
        "email": "jackblack@mail.com"
    },
    "user101": {
        "name": "Jan",
        "age": 44,
        "email": "jan_has_a_van@janwithvan.com"
    },
    "user3": {
        "name": "Michael",
        "age": 100,
        "email": "michael100@mail.com"
    }
}

# update the first nested dict, with dict compreehension selecting items from the second nested dict, unless the items are present in the first one
users.update({user: details for user, details in bonus_users.items() if user not in users})
    
pprint(users)
