# Initialize strings
single = 'Sentence in single quotes'
double = "Sentence in double quotes"
triple = '''Sentence in triple quotes
which also spans across
multiple lines
'''
print(single)
print(double)
print(triple)

# Concatenate strings
name = "John"
# string concatenation using the + operator
greeting = "Welcome to the program "+ name
# format the string to have width of 40 chars and justify the string content in this space
print(f"{greeting:^40}")

# Slice strings
first_word = greeting[:7] # slice first word
last_char = greeting[-1] # last char
some = greeting[11:19] # slice some characters in a range
print(first_word, last_char, name)

# Use common string methods
# remove the end of the string containing space + name from the greeting string
greeting = greeting.removesuffix(f" {name}")
print(f"removesuffix - \"{name}\" is no longer in \"{greeting}\"")

split_sentence = f"{greeting} {name}".split(" ") # splits the string with given separator and returns an array of strings
print(split_sentence)

print(greeting.title()) # prints the greeting using title case

print(f"{greeting}{name}".endswith(name)) # print True or False if the provided arguments terminates the string

print(" ".join(split_sentence)) # creates a new string by joining the array with the provided separator

print(greeting.find("the")) # returns the index of the found search term

print(greeting.replace("the", "our amazing")) # replaces source substring with destination substring

# Get user input and Manipulate dictionary values
user_data = {"name": input("Enter your name: ").strip().capitalize(), # strips leading and trailing whitespaces from user input and capitalizes
             "age": int(input("Type your age: ")), # parses string with age value to an int
             "color": input("Your favourite color: ").strip().capitalize()  # strips leading and trailing whitespaces from user input and capitalizes
            }

print(user_data)
