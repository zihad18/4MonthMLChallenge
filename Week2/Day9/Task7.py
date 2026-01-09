def read_in_small_chunck(file_obj, chunck_size = 16):
    while True:
        data = file_obj.read(chunck_size)
        if not data:
            break
        yield data


with open('TaskExplaination.md') as f:
    for chunck in read_in_small_chunck(f):
        print(chunck)