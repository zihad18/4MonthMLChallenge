def decorator(func):
    def wrapper():
        print(f"This the wrapper function")
        func()
        print(f"This the end of wrapper function")
    return wrapper
def hello():
    print("Hello World!")

new_func = decorator(hello)

new_func()