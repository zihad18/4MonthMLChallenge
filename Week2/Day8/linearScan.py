def contains(list, target=-5):
    index = 0
    length = len(list)

    while index < length:
        current_value = list[index]

        if current_value == target:
            return True
        index = index + 1
        #print(index)

    return False

list = [0] * 10000000
print(contains(list,-5))