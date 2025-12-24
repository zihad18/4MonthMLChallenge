list1 = [i*3 for i in range(1, 10001) ]
list2 = [i*5 for i in range(1, 10001) ]

def findMatches(list1, list2):
    matchers = []

    for i in list1:
        for j in list2:
            if i == j:
                matchers.append(i)
    return matchers

print(f"the commone elements are: {findMatches(list1,list2)}")
