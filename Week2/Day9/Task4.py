def gen():
    yield 1
    yield 2
    yield 3

try:
   
   initializer1 = gen()

   for _ in range(3):
        print(next(initializer1))

   for _ in range(3):
        print(next(initializer1))
    


except StopIteration:
    print(f"Your generator instance is exhausted")
finally:
    initializer2 = gen()

    for _ in range(3):
        print(next(initializer2))

