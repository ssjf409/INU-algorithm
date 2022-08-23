from collections import deque
import sys
input = sys.stdin.readline


def bfs(start_node):
    check = [0 for _ in range(n + 1)]
    check[start_node] = 1
    count = 1
    queue = deque([start_node])

    while queue:
        now_node = queue.popleft()
        for next_node in graph[now_node]:
            if check[next_node] == 0:
                check[next_node] = 1
                count += 1
                queue.append(next_node)
    return count


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
candiate = [True] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    candiate[a] = False


print(candiate)

result = []
for i in range(1, n + 1):
    if candiate[i]:
        result.append([bfs(i), i])

max_val = -1


for i in range(1, n + 1):
    if result[i] == max_val:
        print(i, end=" ")