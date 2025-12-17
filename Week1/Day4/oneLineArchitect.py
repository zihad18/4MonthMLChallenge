previouslist = [i for i in range(1, 11)]
print("previous list ",previouslist)
newlist = [i**2 for i in previouslist if i % 2 == 0]
print("The new list ", newlist)