import json

data = {
    'name': "zihad",
    'age': 23,
    'roll': 104
}

dataDump = json.dumps(data)
print(dataDump)
with open('file.txt', 'w') as f:
    f.write(dataDump)