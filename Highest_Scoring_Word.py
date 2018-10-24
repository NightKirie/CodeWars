def high(x):
    charlist = [list(i) for i in x.split(' ')]
    numlist = []
    for word in charlist:
        for i in range(0, len(word), 1):
            word[i] = ord(word[i])-96
        numlist.append(sum(word))    
    return x.split(' ')[numlist.index(max(numlist))]
