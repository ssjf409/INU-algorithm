from collections import deque

def check_area(board, visited, y, x):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    n = len(board)
    m = len(board[0])

    ret = 0

    q = deque()
    q.append([y, x])
    visited[y][x] = True
    ret += 1

    while len(q) != 0:
        cy, cx = q.popleft()
        for dir in range(4):
            ny, nx = dy[dir] + cy, dx[dir] + cx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx]:
                continue
            if board[ny][nx] == '0':
                continue
            q.append([ny, nx])
            visited[ny][nx] = True
            ret += 1
    return ret


N = int(input())
board = []
visited = [[False for j in range(N)] for i in range(N)]
result = []

for _ in range(N):
    board.append(input())

for i in range(N):
    for j in range(N):
        if board[i][j] == '0':
            continue
        if visited[i][j] == True:
            continue
        result.append(check_area(board, visited, i, j))

result.sort()

print(len(result))
for count in result:
    print(count)