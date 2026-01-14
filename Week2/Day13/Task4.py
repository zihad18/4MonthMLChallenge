try:
    with open('file.txt', 'r') as f:
        content = f.read()
        print(content)
except UnicodeDecodeError:
    print("the text only accepting utf-8 format text")