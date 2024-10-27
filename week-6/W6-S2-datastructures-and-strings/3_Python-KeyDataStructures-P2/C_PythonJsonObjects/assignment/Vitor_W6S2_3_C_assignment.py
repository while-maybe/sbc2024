import json
import sys

from validator import valid_data, global_schema

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
    print("[FATAL] Errors found reading JSON data. Can't continue :(")
    exit(1)
else:
    print(f"Opened \"{INPUT_FILE}\", looking good :)")

# JSON schema data validation happens in this try block
try:
    valid_data(data, global_schema)
    # if there are json validation problems, terminate the program
except Exception as e:
    print(e)
    exit(1)
else:
    print("JSON schema is valid. JSON data is valid. :)")


def show_all_employees(data = data):
    print("\n***Complete employee listing***")
    for d in data["company"]["departments"]:
        print(f"{d["name"]:>15} -> {", ".join(get_employees(d["name"]))}")


def get_employees(dept):
    for d in data["company"]["departments"]:
        if d["name"] == dept.title():
            return [employee["name"] for employee in d["employees"]]
    return None

def add_employee(employee, dept):
    for d in data["company"]["departments"]:
        if d["name"] == dept.title():

    print(data["company"]["departments"].index(dept.title()))
    try:
        data["company"]["departments"].index(dept.title())["employees"].append(employee)
    # data["company"]["departments"][dept.title()]
    except ValueError:
        print(f"\"{dept.title()}\" doesn't exist")


show_all_employees()
new_emp = {"name": "Ron", "age": 10, "role": "Rocket Scientist"}
add_employee(new_emp, "engineering")
show_all_employees()
