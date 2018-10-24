def digital_root(n):
    while n >= 10:
        n = sum([int(x) for x in str(n)])
    return n
