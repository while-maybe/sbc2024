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
    
    
def save_data(ouput_file=OUTPUT_FILE):
    # JSON schema data validation happens in this try block
    try:
        valid_data(data, global_schema)
        # if there are json validation problems, terminate the program
    except Exception as e:
        print(e)
        exit(1)
    # file saving happens here
    try:
        with open(ouput_file, "w") as file:
            json.dump(data, file, indent=4)
        print("\n[OK] data saved")
    except PermissionError:
        print(f"\n[ERROR] Can't write to file")


def show_all_employees(data):
    print(f"\n[Staff list]")
    for d in data["company"]["departments"]:
        print(f"{d["name"]:>15} -> {", ".join(get_employees(d["name"]))}")


def get_employees(dept):
    for d in data["company"]["departments"]:
        if d["name"] == dept.title():
            return [employee["name"] for employee in d["employees"]]
    raise ValueError(f"[ERROR] \"{dept}\" not found")


def add_employee(employee, dept):
    dept = dept.title()
    for idx, d in enumerate(data["company"]["departments"]):
        if d["name"] == dept:
            data["company"]["departments"][idx]["employees"].append(employee)
            return
    raise ValueError(f"[ERROR] \"{dept}\" not found")


def remove_employee(employee, dept):
    dept = dept.title()
    for idx, d in enumerate(data["company"]["departments"]):
        if d["name"] == dept:
            for person in data["company"]["departments"][idx]["employees"]:
                if person["name"] == employee.title():
                    data["company"]["departments"][idx]["employees"].remove(person)
                    print(f"[OK] {employee} has been removed from {dept}")
                    return
    raise ValueError(f"[ERROR] \"{employee}\" not found in \"{dept}\"")


def update_employee_role(employee_name, new_role):
    for dept in data["company"]["departments"]:
        for employee in dept["employees"]:
            if employee["name"] == employee_name:
                print(f"[OK] {employee["name"]} was a \"{employee["role"]}\" but is now a \"{new_role}\"")
                employee["role"] = new_role
                return
    raise ValueError(f"[ERROR] \"{employee_name}\" Not found")


def dynamic_interaction(data):
    print("[INFO] type a key path separated with '>' \ncompany > departments > Engineering > employees > Alice > skills")
    path = ""
    while not path:
        path = input("Info path: ").split(">")
    # creates an array with the user query removing "company", "departments", "employees", "skills" from it if these exist and cleans the data
    query_data = [each.strip().title() for each in path if each.lower() not in ["company", "departments", "employees", "skills"]]
    
    # if len(query_data) is 1, user wants dept; if 2 user wants employee; if 3 or more user wants skills
    
    # "company > departments > Engineering > employees > Alice > skills"
    # clean the data
    try:
        dept = path[2].strip().title() # dept name given by user
        employee = path[4].strip().title() # employee name given by user
        skills = path[5].strip() # # employee skills given by user
    except IndexError:
        

    



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

show_all_employees(data)
# Add a new employee under the "Engineering" department
new_emp = {"name": "Ron", "age": 10, "role": "Rocket Scientist"}
try:
    add_employee(new_emp, "engineering")
except ValueError as e:
    print(str(e))


# ask the user for an employee name and update their role
print("\n[Modify Role]")
employee_name, new_role = "", ""
while not (employee_name and new_role):
    employee_name = input("Please enter the employee name: ").title()
    new_role = input(f"{employee_name}'s new role: ").title()
try:
    update_employee_role(employee_name, new_role)
except ValueError as e:
    print(str(e))

show_all_employees()

# Remove an employee from the "Sales" department
print("\n[Remove Employee]")
employee_name, dept = "", ""
while not (employee_name and dept):
    employee_name = input("Please enter the employee name: ").title()
    dept = input(f"{employee_name}'s department: ").title()
try:
    remove_employee(employee_name, dept)
except ValueError as e:
    print(str(e))

show_all_employees()

print("\n[Employees in dept]")
dept = ""
while not dept:
    dept = input(f"Enter a department: ").title()
try:
    print(f"[OK] {get_employees(dept)}")
except ValueError as e:
    print(str(e))







save_data()
