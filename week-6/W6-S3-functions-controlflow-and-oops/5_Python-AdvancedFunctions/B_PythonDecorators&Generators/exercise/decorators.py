from functools import wraps
from datetime import datetime as dt

def decorator(func):
    @wraps(func)
    def wrapper():
        start = dt.now().timestamp()
        # print(f"Time before: {dt.now().timestamp()}")
        func()
        print(f"it took: {dt.now().timestamp() - start:.4f}")
    return wrapper

@decorator
def count_a_lot():
    x = 0
    print("Adding to 1000000")
    for i in range(1_000_000):
        x += 1
    print(f"done! Result is {x}")
        
count_a_lot()
