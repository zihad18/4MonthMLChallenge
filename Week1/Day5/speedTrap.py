import time 
numbers = range(1000000)
listOfNumber = list(numbers)
setOfNumber = set(numbers)
print(".........")
firsttime = time.time()
result = -1 in listOfNumber

secondtime = time.time()
print(f"list  {result}")
print(f"for list search {secondtime - firsttime:.5f}")

firsttime = time.time()
print(f"set  {-1 in setOfNumber}")
secondtime = time.time()
totaltime = secondtime - firsttime
print(f"for set search  {secondtime - firsttime:.5f}")