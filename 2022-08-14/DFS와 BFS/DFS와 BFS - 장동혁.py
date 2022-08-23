from collections import deque


def do_dfs(adj_list, visited, cur):
    
    print(cur, end = " ")

    for ny in adj_list[cur]:
        if visited[ny]:
            continue
        visited[ny] = True
        do_dfs(adj_list, visited, ny)

def do_bfs(adj_list, visited, start):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while len(q) != 0:
        cur = q.popleft()
        print(cur, end = " ")

        for next in adj_list[cur]:
            if visited[next]:
                continue
            q.append(next)
            visited[next] = True


vertex, edge, start = map(int, input().split(' '))

adj_list = [[] for _ in range(vertex + 1)]
visited = [False for _ in range(vertex + 1)]

for _ in range(edge):
    u, v = map(int, input().split(' '))
    adj_list[u].append(v)
    adj_list[v].append(u)

for child_list in adj_list:
    child_list.sort()

visited[start] = True
do_dfs(adj_list, visited, start)
print()


visited = [False for _ in range(vertex + 1)]
do_bfs(adj_list, visited, start)

