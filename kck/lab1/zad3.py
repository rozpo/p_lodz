list = [100, 80, 20, 35, 90, 101, 99]

def substract (list):
    head, tail = list[0], list[1:]
    newlist = [tail[0] - head]
    if (len(tail) > 1):
        newlist.extend(substract(tail))
    return newlist

print([list[0]] + substract(list))