def spin_words(sentence):
    list = sentence.split(' ')
    for x in range(0, len(list), 1):
        if len(list[x]) >= 5:
            list[x] = list[x][::-1]
    return ' '.join(list)    
