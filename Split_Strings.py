def solution(s):
    return [s[i:i+2] for i in range(0, len(s), 2)] if len(s) % 2 == 0 else [(s+'_')[i:i+2] for i in range(0, len(s+'_'), 2)]
