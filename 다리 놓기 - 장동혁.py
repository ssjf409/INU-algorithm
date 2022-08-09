T = int(input())

def get_possible_cnt(cache, M, cur_index, remain):
    if cur_index == M:
        if remain == 0:
            return 1
        else:
            return 0
    
    if cache[cur_index][remain] != -1:
        return cache[cur_index][remain]
    
    ret = 0
    ret += get_possible_cnt(cache, M, cur_index + 1, remain)
    if remain > 0:
        ret += get_possible_cnt(cache, M, cur_index + 1, remain - 1)
    cache[cur_index][remain] = ret
    return ret


for _ in range(T):
    N, M = map(int, input().split(' '))
    cache = [[-1 for j in range(N + 1)] for i in range(M)]
    print(get_possible_cnt(cache, M, 0, N))

