from collections import deque


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

M, N = map(int, input().strip().split(' '))


board = []


q = deque()
remainer_cnt = 0
step = -1


for i in range(N):
    board.append(list(map(int, input().strip().split(' '))))

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append([i, j])
        elif board[i][j] == 0:
            remainer_cnt += 1



while len(q) != 0:
    step += 1
    q_size = len(q)
    for _ in range(q_size):
        cy, cx = q.popleft()

        for dir in range(len(dy)):
            ny, nx = cy + dy[dir], cx + dx[dir]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if board[ny][nx] == 0:
                board[ny][nx] = 1
                remainer_cnt -= 1
                q.append([ny, nx])



if remainer_cnt == 0:
    print(step)
else:
    print(-1)

