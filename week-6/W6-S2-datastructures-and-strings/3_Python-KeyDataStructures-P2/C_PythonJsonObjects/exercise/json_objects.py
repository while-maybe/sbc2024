# Import the JSON module
import json

# Define a JSON string (from a regular string containing a dict)
json_string = '{"name": "John", "age": 30, "email": "john@mail.com"}'

# Parse JSON data - convert to python dict
data = json.loads(json_string)

# Access JSON elements
print(data["name"]) # prints 'John'

# Note to self: when using the methods json.load() and json.dump(), we intend to to read and write to a file whereas using the method names in the plural: json.loads() and json.dumps() converts data from/to Json strings to python dicts and vice-versa. Think loadS (as load String) or dumpS (as dump String) so S at the end standing for "String".

# Modify dict data (former JSON string)
print(data["email"]) # before modification
data["email"] = "new_email@hotmail.com"
print(data["email"]) # after modification

# Convert Python object to JSON
json_data = json.dumps(data, indent=2)
print(json_data)
