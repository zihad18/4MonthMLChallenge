from itertools import groupby

data = [
    {"name": "Apple", "category": "Fruit"},
    {"name": "Carrot", "category": "Vegetable"},
    {"name": "Banana", "category": "Fruit"},
]

data.sort(key = lambda x: x['category'])

groupedData = groupby(data, key = lambda x: x["category"])

for category , items in groupedData:
    print(f"--{category}--")
    for item in items:
        print(item["name"])