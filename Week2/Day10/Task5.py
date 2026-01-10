import time
def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print(f"The total time takes {time.time() - start}")

    return wrapper

@timer
def add(a, b):
    time.sleep(3)
    print(f"{a+b}")
add(3,6)