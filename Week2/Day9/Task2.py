import sys

list_comprehension = [x for x in range(1000000)]
print(f"The list comprehension takes {sys.getsizeof(list_comprehension)// 1024**2} MB")

generator_expresion = (x for x in range(1000000))
print(f"The generator takes {sys.getsizeof(generator_expresion)} Bytes")
