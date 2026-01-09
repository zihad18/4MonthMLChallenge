def gen():
    yield 1
    yield 2

try:
    obj = gen()
    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))
except StopIteration:
    print("Your generator is run out of items")