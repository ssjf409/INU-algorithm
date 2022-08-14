#메모리초과 시간초과 코드

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N , M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [0 for _ in range(N+1)]


def dfs(pre_node,cnt):
    if visited[pre_node] > cnt:
        return
    
    
    visited[pre_node] = cnt
    
    if len(graph[pre_node]) == 0:
        return 

    for node in graph[pre_node]:
        dfs(node, cnt+1)


for i in range(N+1):
    if visited[i] == 0:
        dfs(i, 0)
    
max_val = max(visited)

for i in range(1,N+1):
    if max_val == visited[i]:
        print(i, end =' ')
