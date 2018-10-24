import math
def solution(number):
    list = []
    for x in range(1, math.ceil(number/3), 1):
        if x*3 not in list:
            list.append(x*3)
    for x in range(1, math.ceil(number/5), 1):
        if x*5 not in list:
            list.append(x*5)
    return sum(list)    
