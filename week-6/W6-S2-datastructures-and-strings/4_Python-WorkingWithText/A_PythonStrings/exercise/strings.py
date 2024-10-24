# Create and initialize strings
sentence = "A simple sentence is the start of... "

# Concatenate strings
sentence += str(1_000_000) # convert int to str and concatenate
sentence = " ".join([sentence, "different things"]) # .join() to concatenate
print(sentence)

# Slice strings
print(sentence[7:-7:2]) # returns every other character in the string starting with character at index 7 up to 7th character counting from the end of the string

# Format strings
stop_text = "*STOP*"
print(f"The original string is: {sentence}")

half_sentence_index = int(len(sentence)/2) # determines the index of the middle character position of the "sentence" string
print("Half of the sentence: {var0} {var1}".format(var0=sentence[:half_sentence_index], var1=stop_text))

# use of some string methods
print(sentence.upper()) # Capitalizes the entire string
print(sentence.title()) # Capitalizes the first letter of each word
print(sentence.lower()) # prints the sente using lower case chars
print(sentence.replace("A simple", "     One")) # replaces "A simple" with "     One" - note the extra leading spaces
print(sentence.lstrip()) # removes previously added spaces
