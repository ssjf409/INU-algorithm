import sys
sys.setrecursionlimit(1010)

def find_winner(cache, remain, isChang):
    if remain == 0:
        return not isChang
    
    if cache[remain][isChang] != -1:
        return cache[remain][isChang]

    if remain < 3:
        return find_winner(cache, remain - 1, not isChang)


    result1 = find_winner(cache, remain - 1, not isChang)
    result2 = False
    if remain >= 3:
        result2 = find_winner(cache, remain - 3, not isChang)

    ret = result1 or result2
    cache[remain][isChang] = ret
    
    return ret
    

    

N = int(input())
cache = [[-1, -1] for _ in range(1001)]


if find_winner(cache, N, False) == 0:
    print('SK')
else:
    print('CY')

