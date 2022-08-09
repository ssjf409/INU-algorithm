import sys
from sys import stdin
sys.setrecursionlimit(200000)


def get_max_span(loc, cur_index, remainer):
    if len(loc) - cur_index < remainer:
        return -float('inf')
    if len(loc) == cur_index:
        if remainer == 0:
            return 0
        else:
           return -float('inf')
    
    


N, M = map(int, stdin.readline().strip().split(' '))

loc = []

for _ in range(N):
    loc.append(int(stdin.readline()))


result = 0

for i in range(N - M + 1):
    result = max(result, get_max_span(loc, i, M - 1))