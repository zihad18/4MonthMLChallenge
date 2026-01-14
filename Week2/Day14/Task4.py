def flatten(nestedlist):
    for x in nestedlist:
        if isinstance(x,list):
            yield from flatten(x)
        else:
            yield x

nestedlist = [1,[2,[3,4]]]
print(list(flatten(nestedlist)))