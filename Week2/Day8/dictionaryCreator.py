import time
from random import randint
start = time.time()
print(".....")
start = time.time()

list = [randint(1, 100) for i in range(100)]
start = time.perf_counter()
dictionary = {index:value for index, value in enumerate(list)}
end = time.perf_counter()
print(f" dict {dictionary}")
ti = end - start
print(f"time takes {ti:.6f} seconds")