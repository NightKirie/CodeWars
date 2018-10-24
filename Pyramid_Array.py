def pyramid(n):
    arr = []
    for x in range(0, n, 1):
        list = []
        for i in range(0, x+1, 1):
            list.append(1)
        arr.append(list)
    return arr
