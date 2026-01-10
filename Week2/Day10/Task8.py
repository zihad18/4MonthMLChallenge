def decorator(func):
    def wrapper():
        print(f"Without giving arguments into wrapper cannot works well")
        func()
        print(f"So use arguments")
    return wrapper

@decorator
def hello_fn():
    print("hello")

#hello_fn()
print(hello_fn.__name__)

import functools
def decorator_name(func):
    @functools.wraps(func)
    def wrapper():
        print(f"Without giving arguments into wrapper cannot works well")
        func()
        print(f"So use arguments")
    return wrapper

@decorator_name
def bye():
    print("good bye")

print(f"now it prints decorator name : {bye.__name__}")