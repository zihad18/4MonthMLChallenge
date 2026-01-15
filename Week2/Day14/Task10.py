list1 = [x for x in range(3,25,3)]
list2 = [x for x in range(7,35,7)]
print(f"list1 {list1} and list2 {list2}")

new_list = []

p1 = 0
p2 = 0
while p1 < len(list1) and p2 < len(list2):
    if list1[p1] < list2[p2]:
        new_list.append(list1[p1])
        p1 = p1 + 1
    elif list1[p1] > list2[p2]:
        new_list.append(list2[p2])
        p2 += 1
    else:
        new_list.append(list2[p2])
        p1 += 1
        p2 += 1
while p1 < len(list1):
    new_list.append(list1[p1])
    p1 += 1
while p2 < len(list2):
    new_list.append(list2[p2])
    p2 += 1


print(f"the finalized list is {new_list}")