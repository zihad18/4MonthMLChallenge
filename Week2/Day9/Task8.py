def even():
    for i in range(0,11,2):
        yield i

def odd():
    for i in range(0,11,2):
        yield i+1

def generator():
    yield "first we will show some odd numbers "
    yield from odd()
    yield "Now we will see some even numbers"
    yield from even()
    yield "The End!"

for value in generator():
    print(value)