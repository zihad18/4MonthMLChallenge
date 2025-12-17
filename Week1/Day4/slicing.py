data = [10, 20, 30, 40, 50]
print("data", data)

newlist = data[:-3] + data[-3:][::-1]
print("newlist",newlist)