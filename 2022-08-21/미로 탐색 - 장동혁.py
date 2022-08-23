from collections import deque

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

N, M = map(int, input().split(' '))
board = []
visited = [[False for j in range(M)] for i in range(N)]

for _ in range(N):
    board.append(input())

q = deque()
q.append([0, 0])
visited[0][0] = True
cnt = 0
findFlag = False

while len(q) != 0:
    cnt += 1
    q_size = len(q)
    for _ in range(q_size):
        cy, cx = q.popleft()
        if cy == N - 1 and cx == M - 1:
            findFlag = True
            break
        for dir in range(4):
            ny, nx = dy[dir] + cy, dx[dir] + cx
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if visited[ny][nx]:
                continue
            if board[ny][nx] == '0':
                continue
            q.append([ny, nx])
            visited[ny][nx] = True
    if findFlag:
        break

print(cnt)
