list1 = [x for x in range(1,101) if x != 30 ]
print(list1)
total = 0
for num in list1:
    total += num
result = int((100/2)*101) - total
print(f"The missing value is {result}")