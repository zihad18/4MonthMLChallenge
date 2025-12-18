number = int(input('Enter a number: '))

if number < 0:
    raise ValueError("NO negatives")