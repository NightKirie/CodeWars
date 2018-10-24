def getCount(inputStr):
    num_vowels = 0
    # your code here
    for char in inputStr:
        if char is 'a' or char is 'e' or char is 'i' or char is 'o' or char is 'u':
            num_vowels = num_vowels + 1
        
    
    return num_vowels
