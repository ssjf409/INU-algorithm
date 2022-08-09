import sys
sys.setrecursionlimit(100010)

from sys import stdin



# state, 0 : 위 가능, 1 : 아래 가능, 2 : 둘 다 가능
def get_maximum(cache, sticker, cur_index, state):
    if cur_index == len(sticker):
        return 0
    
    if cache[cur_index][state] != -1:
        return cache[cur_index][state]
    
    ret = get_maximum(cache, sticker, cur_index + 1, 2)
    
    if state == 0:
        ret = max(ret, get_maximum(cache, sticker, cur_index + 1, 1) + sticker[cur_index][0])
        cache[cur_index][state] = ret
        return ret

    if state == 1:
        ret = max(ret, get_maximum(cache, sticker, cur_index + 1, 0) + sticker[cur_index][1])
        cache[cur_index][state] = ret
        return ret
    
    ret = max(ret, get_maximum(cache, sticker, cur_index + 1, 1) + sticker[cur_index][0])
    ret = max(ret, get_maximum(cache, sticker, cur_index + 1, 0) + sticker[cur_index][1])
    cache[cur_index][state] = ret
    return ret




T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    sticker = [[-1, -1] for _ in range(n)]
    cache = [[-1, -1, -1] for _ in range(n)]


    temp = list(map(int, stdin.readline().split(' ')))
    for i, val in enumerate(temp):
        sticker[i][0] = val
    temp = list(map(int, stdin.readline().split(' ')))
    for i, val in enumerate(temp):
        sticker[i][1] = val
    
    print(get_maximum(cache, sticker, 0, 2))





