def decorator(func):
    def wrapper():
        print(f"Without giving arguments into wrapper cannot works well")
        func()
        print(f"So use arguments")
    return wrapper

@decorator
def add(a, b):
    return a + b
add()