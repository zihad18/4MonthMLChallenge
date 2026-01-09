def special_multiply():
    total = 1
    while True:
        value = yield total
        if value is not None:
            total *= value

mul = special_multiply()
next(mul)
print(mul.send(2))
print(mul.send(5))
print(mul.send(7))