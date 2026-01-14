import random
list1 = [random.randint(1,10) for _ in range(20)]
print(list1)
list2 = []
set1 = set()
for item1 in list1:
    if item1  not in  set1:
        list2.append(item1)
        set1.add(item1)
    
print(list2)