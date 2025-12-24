from random import randint
list = [randint(1, 100000) for i in range(10000)]
slicedList = list[0:5000]
print(f"the main list {list} \n\n\n the sliced one {slicedList}")