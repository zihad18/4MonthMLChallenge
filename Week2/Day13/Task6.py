import csv
with open('dict.csv',mode='r',newline = '', ) as csvFile:
    dict = csv.DictReader(csvFile)
    
    for row in dict:
        print(row)