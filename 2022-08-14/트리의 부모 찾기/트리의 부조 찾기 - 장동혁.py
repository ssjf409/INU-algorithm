import sys
from sys import stdin
sys.setrecursionlimit(100100)


def find_parents(adj_list, visited, parents, cur):
    for next in adj_list[cur]:
        if visited[next]:
            continue
        visited[next] = True
        parents[next] = cur
        find_parents(adj_list, visited, parents, next)



N = int(input())

adj_list = [[] for _ in range(N + 1)]
parents = [-1] * (N + 1)
visited = [False] * (N + 1)



for _ in range(N - 1):
    u, v = map(int, input().split(' '))
    adj_list[u].append(v)
    adj_list[v].append(u)

parents[1] = 1
visited[1] = True

find_parents(adj_list, visited, parents, 1)


for i in range(2, N + 1):
    print(parents[i])