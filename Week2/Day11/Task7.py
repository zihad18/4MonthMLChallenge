import time
start = time.time()
list_comprehension = [x**4 for x in range(1000000) ]
print(f"list comprehension takes time {time.time() - start}")
data = [x for x in range(1000000) ]
start = time.time()
map_lambda = list(map(lambda x: x**4,data ))
print(f"map + lambda takes {time.time() - start}")