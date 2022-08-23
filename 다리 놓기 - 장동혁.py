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


# remain : 아직 짝 짓지 못한 서쪽의 도시 개수
# cur_index : 동쪽 도시 순서
# 순수 함수
# T = int(input())
# def get_possible_cnt(M, cur_index, remain):
#     if cur_index == M:
#         if remain == 0:
#             return 1
#         else:
#             return 0       
    
#     ret = 0
#     ret += get_possible_cnt(M, cur_index + 1, remain)
#     if remain > 0:
#         ret += get_possible_cnt(M, cur_index + 1, remain - 1)

#     print(cur_index, remain, ret)

#     return ret


# for _ in range(T):
#     N, M = map(int, input().split(' '))
#     print(get_possible_cnt(M, 0, N))
