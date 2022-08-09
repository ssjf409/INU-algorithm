import sys
from sys import stdin
sys.setrecursionlimit(6000)


def get_minimum(cache, costs, cur_index):
    if len(costs) - 1 == cur_index:
        return 0
    
    if cache[cur_index] != -1:
        return cache[cur_index]
    
    # 계산
    ret = float('inf')
    cur_cost = costs[cur_index]
    for j in range(cur_index + 1, len(costs)):
        next_cost = costs[j]
        K = (j - cur_index) * (abs(cur_cost - next_cost) + 1)
        max_val = max(K, get_minimum(cache, costs, j))
        ret = min(ret, max_val)
    
    cache[cur_index] = ret
    return ret



N = int(stdin.readline())

cache = [-1] * (N + 1)
costs = list(map(int, stdin.readline().strip().split(' ')))

print(get_minimum(cache, costs, 0))






'''
# 완전탐색(재귀)
import sys
from sys import stdin
sys.setrecursionlimit(6000)

# cur_index 위치에서 가능한 최대 K 값들 중에서 최소값을 반환하는 함수
def get_minimum(costs, cur_index):
    if len(costs) - 1 == cur_index:
        return 0

    ret = float('inf')
    cur_cost = costs[cur_index]
    for j in range(cur_index + 1, len(costs)):
        next_cost = costs[j]
        K = (j - cur_index) * (abs(cur_cost - next_cost) + 1)
        max_val = max(K, get_minimum(costs, j))
        ret = min(ret, max_val)
    return ret



N = int(stdin.readline())

costs = list(map(int, stdin.readline().strip().split(' ')))

print(get_minimum(costs, 0))
'''




