with open('file.txt','w') as f:
    for i in range(1000000):
        f.write(f"line no {i+1}\n")