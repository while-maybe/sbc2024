# File Handling with Error Management
FILENAME = "data.txt"
try:
    with open(FILENAME, "r") as file:
        data = file.read()
except FileNotFoundError:
    print(f"Can't find {FILENAME}")
except Exception as e:
    print(f"Something else has gone wrong...\n{e}")
    
# Multiple Exception Handling
numbers = input("Enter two numbers separated by spaces: ").split()
try:
    n1, n2 = map(lambda a: int(a), numbers)
    print(n1 / n2)
except ValueError:
    print("They're not really numbers...")
except ZeroDivisionError:
    print("Can't divide by zero")
    
# Using Finally and Else Blocks
connection = None
try:
    connection = open("data.txt", "r")
except FileNotFoundError:
    print("Can't open the connection")
else:
    print("Data received")
finally:
    if connection:
        print("Closing connection")
        connection.close()
    else:
        print("Exiting without receiving data")

#  Input Validation and Custom Exception
def validate_positive_number():
    try:
        n = int(input("Enter a positive int"))
        if n < 0:
            raise ValueError("The number is not positive")
    except ValueError as e:
        print(f"Operation failed: {e}")

# Logging Errors
from datetime import datetime as dt

LOG_FILE = "system.log"
def log_message(msg):
    with open(LOG_FILE, "a") as file:
        LOG_FILE.write(f"{dt.now()}: {msg}\n")
        

# Class Definition
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.__year = year
        
    def show_details(self):
        print(f"This car is a {self.make} {self.model} from {self.__year}")
        
    def get_year(self):
        return self.__year
        
    def set_year(self, new_year):
        self.__year = new_year
        
        
# Inheritance
class ElectricCar(Car): # Class to inherit from must be specified here
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
        
    def show_battery_info(self):
        print(f"This a {self.battery_size} kWh")


# added to the in the class definition above, demonstration here
new_car = Car("VW", "Golf", 2010)
print(new_car.get_year())
new_car.set_year(2015)
print(new_car.get_year())


# Test the Classes
new_car = Car("Fiat", "Punto", "1998")
new_car.show_details()

new_electric_car = ElectricCar("Tesla", "X", 2025, 1000)
new_electric_car.show_details()
new_electric_car.show_battery_info()


# Constructor and Destructor
class Car:
    def __init__(self):
        print("A new car has been made!")
        
    def __del__(self):
        print("A car has just been destroyed")

new_car = Car()
del new_car

