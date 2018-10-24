import math
def zeros(n):
    count = 0
    while n > 1:
        n = math.floor(n / 5)
        count = count + n
    return count    
