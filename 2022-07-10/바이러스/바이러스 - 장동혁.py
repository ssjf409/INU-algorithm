from collections import deque

N = int(input())
edge_cnt = int(input())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)


for _ in range(edge_cnt):
    u, v = map(int, input().strip().split(' '))
    adj_list[u].append(v)
    adj_list[v].append(u)


cnt = 0

q = deque()
visited[1] = True
q.append(1)

while len(q) != 0:
    cur = q.popleft()

    for ny in adj_list[cur]:
        if visited[ny]:
            continue
        
        visited[ny] = True
        q.append(ny)
        cnt += 1
        
print(cnt)





