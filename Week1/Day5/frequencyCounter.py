fruit = input('Enter banana ')
letter = {}
for alphabet in fruit:
    if alphabet in letter:
        letter[alphabet] += 1
    else:
        letter[alphabet] = 1
print(letter)