def running_avg():
    total = 0
    count = 0
    avg = 0
    while True:
        value = yield avg
        count += 1
        if value is not None:
            total += value
            avg = total / count

avg = running_avg()
next(avg)
print(avg.send(2))
print(avg.send(4))
print(avg.send(6))
print(avg.send(8))