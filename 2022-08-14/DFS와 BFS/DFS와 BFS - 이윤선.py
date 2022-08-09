import sys
from collections import deque


input = sys.stdin.readline


def dfs(graph,start,N):
    stack = [start]    
    visited = [0 for _ in range(N+1)]
    visit_num = []
    while stack:
        cur_node = stack.pop()
        if visited[cur_node] == 0:
            visit_num.append(cur_node)

        visited[cur_node] = 1
        for node in graph[cur_node]:
            if visited[node] == 0:
                stack.append(node)
    
    return visit_num


def bfs(graph,start,N):
    q = deque()
    q.append(start)
    visited = [0 for _ in range(N+1)]
    visit_num = []
    while q:
        cur_node = q.popleft()
        if visited[cur_node] == 0:
            visit_num.append(cur_node)
        visited[cur_node] = 1
        for node in graph[cur_node]:
            if visited[node] == 0:
                q.append(node)

    return visit_num
    
N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs_answer = bfs(graph,V,N)

for i in range(len(graph)):
    graph[i].sort(reverse=True)

dfs_answer = dfs(graph,V,N)

for i in range(len(graph)):
    graph[i].sort()

bfs_answer = bfs(graph,V,N)

for ans in dfs_answer:
    print(ans, end= " ")

print()
for ans in bfs_answer:
    print(ans, end= " ")

