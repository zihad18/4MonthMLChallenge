from  functools import reduce

data = [1,2,3,4]

result = reduce(lambda a,b : a*b, data)
print(result)