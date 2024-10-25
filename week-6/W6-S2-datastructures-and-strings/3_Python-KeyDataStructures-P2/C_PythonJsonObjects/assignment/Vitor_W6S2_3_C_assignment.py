import json
import sys

from validator import valid_data

INPUT_FILE = "./input_complex.json"
OUTPUT_FILE = "./output_complex.json"

def get_data(input_file=INPUT_FILE):
    try:
        with open(input_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"[FATAL] {INPUT_FILE} not found")
    except json.JSONDecodeError:
        print(f"[FATAL] Invalid JSON format")
    except Exception as e:
        print(f"[FATAL], {e}")
    return None
    

data = get_data()
# if there is no data read from the file, exit the program
if data is None:
    print("Errors found reading JSON data. Can't continue :(")
    exit(1)
else:
    print(f"Opened \"{INPUT_FILE}\", looking good :)")

# JSON schema data validation happens in this try block
try:
    valid_data(data)
    # if there are json validation problems, terminate the program
except Exception as e:
    print(e)
    exit(1)
else:
    print("JSON schema is valid. JSON data is valid. :)")

# print(data)
