def decorator(func):
    def wrapper(*args):
        print(f"Without returning the result you will got None")
        func(*args)
    return wrapper

@decorator
def add(a, b):
    print(f"Add function calling")
    return a + b
return_value = add(5,7)
print(return_value)