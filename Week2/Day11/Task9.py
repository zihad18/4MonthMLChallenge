from functools import partial
def power(base, exp):
    return base**exp

square = partial(power, exp=2)
print(square(7))