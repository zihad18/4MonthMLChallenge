data1 = [1,0,1,-6]
data2 = [1,1,1,9,-1]
print(f"{any(list(map(lambda x: x<0,data1)))}")
print(f"{all(list(map(lambda x: x> 0, data2)))}")