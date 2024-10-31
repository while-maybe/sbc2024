import re

# Define regex patterns
pattern = re.compile(r"\d+")
text = "12345"
print(pattern.search(text).group())

phone_pattern = re.compile(r"\(\d{3}\)\s*\d{3}-\d{4}")
text = "(123) 456-7890"
print(phone_pattern.search(text).group())

email_pattern = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
user_email = "something_here@mail.com"
print(email_pattern.search(user_email).group())

# url pattern
url_pattern = re.compile(r"https?://[^\s]+")
print(url_pattern.search("https://google.com").group())

# dates pattern
date_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")
print(date_pattern.search("01/01/2020").group())

# Search for patterns
pattern = re.compile(r"123")
result = pattern.search("678123789 123")
print(result, f"from pattern \"{result.group(0)}\"")


# Find all matches
pattern = re.compile(r"-?123(?:\.\d{2})?")
text = "this 123 is a sent123ence -123 and one more 123.00 and a last one -123.21"
print(pattern.findall(text))

# Demonstrate re.finditer() to iterate over all matches
for i in re.finditer(pattern, text):
    print(f"Found \"{i.group(0):6}\" -> starts at {i.start():3} ends at {i.end():3}")

# Replace text
redact_pattern = "***"
print(pattern.sub(redact_pattern, text))

# Explore re.subn()...
result = pattern.subn(redact_pattern, text, count=2)
print(f"\n{result[1]} replacements made\n{result[0]}")

# Use re.split() to tokenize a sentence into words
pattern = re.compile(r"\W+")
print(pattern.split(text))

# demonstrate how to clean the tokens
# Tokens are already clean as all-non word characters have already been removed

# Validate user input
# Prompt the user to input a phone number and an email address
user_phone = input("Enter a phone number in the format (123) 456-7890: ")
user_email = input("Enter an Email address: ")

# Quicker way to validate
# user_phone = "(123) 456-7890"
# user_email = "something_here@mail.com"
print("\nvalid phone" if phone_pattern.fullmatch(user_phone) else "INVALID phone number")
print("valid email" if email_pattern.fullmatch(user_email) else "INVALID email")

# Compile patterns
# I have used compile on previous examples

print("")
# Escape special characters
# .escape() is used to escape special chars in a string returning all meta-characters (chars that have a special meaning in regex syntax) backslashed to use in a pattern.
 # 'plain' string:      "-?123(?:\.\d{2})?"
 # 'escaped' version:   "\-\?123\(\?:\\\.\\d\{2\}\)\?"
 
escape_this = "-123."
print(re.search(re.escape(escape_this) + "\d{2}?", text))

# Store validated information
user_name = " ".join(input("Enter your name: ").strip().split()).title()

user_age = 0
while user_age not in range (18, 100):
    try:
        user_age = int(input("Finally your age[18 - 99]: "))
    except ValueError:
        continue

my_dict = {
    "name": user_name,
    "age": user_age,
    "number" : user_phone,
    "email": user_email
}
print(my_dict)

# year last
date_patt1 = r"\d{2}[/-]\d{2}[/-]\d{4}"
# year first
date_patt2 = r"\d{4}[/-]\d{2}[/-]\d{2}"

date_patt3 = re.compile(r"(\d{2}[/-]\d{2}[/-]\d{4})|(\d{4}[/-]\d{2}[/-]\d{2})")

string_with_date = "I'm a string with a date in a format like 15/15/1932 and another with year first 2022/10/22"

for r in date_patt3.finditer(string_with_date):
    print(r)

