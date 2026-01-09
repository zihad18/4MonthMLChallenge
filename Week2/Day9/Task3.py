def fibbonacci():
    x,y = 0,1
    while True:
        x,y = y, x+y
        yield x



count = 1
for value in fibbonacci():
    if count >= 10:
        break
    print(value)
    count += 1