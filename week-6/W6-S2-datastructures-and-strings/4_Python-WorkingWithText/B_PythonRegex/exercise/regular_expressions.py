import re

pattern = r"\d+"

match = re.search(pattern, 'The price is 100 dollars')
print(match.group())

all_matches = re.findall(pattern, "The price for 2 is 200 dollars")
print(all_matches)

# pattern to reveal only part of the price
pattern = r"(?:\d)\d{2}"
replaced_text = re.sub(pattern, r"\0??", "The price is 100 dollars")
print(replaced_text)
