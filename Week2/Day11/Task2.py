square = lambda a: a**2
list1 = [x for x in range(1,101)]
x = map(square,list1)
print(list(x))