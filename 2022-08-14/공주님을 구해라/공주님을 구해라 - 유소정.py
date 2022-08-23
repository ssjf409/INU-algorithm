from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    queue = (deque([[x, y]]))
    count[x][y] = 0
    knife = [-1, -1]

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return count[n-1][m-1]

        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if 0 <= ax < n and 0 <= ay < m and count[ax][ay] == -1 and graph[ax][ay] != 1:
                count[ax][ay] = count[x][y] + 1
                queue.append([ax, ay])

                if graph[ax][ay] == 2:
                    cal = n - ax + m - ay - 2
                    return count[ax][ay] + cal

    return count[n-1][m-1]


n, m, t = map(int, input().split())
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

graph = []
count = [[-1] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
result = bfs(0, 0)

print("Fail" if result == -1 or result > t else result)



a = 10

def test():
    #
    # ...