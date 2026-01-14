from collections import Counter
s1 = 'slient'
s2 = 'listen'
def anagramChecker(s1,s2):
    sorted(s1)
    sorted(s2)
    return Counter(s1) == Counter(s2)
print(anagramChecker(s1,s2))
