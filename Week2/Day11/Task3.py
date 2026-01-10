import random
data = [random.randint(-10,10) for _ in range(10)]

filter = filter(lambda a: a >= 0, data)
print(list(filter))