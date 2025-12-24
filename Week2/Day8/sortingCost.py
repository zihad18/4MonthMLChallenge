from random import randint
list = [randint(1, 100) for i in range(100)]
print(f"list {list}")
list.sort()
print(f"sorted list {list}")