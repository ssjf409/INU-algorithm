from collections import deque

T = int(input())


def bfs(board, visited, i, j):
    N = len(board)
    M = len(board[0])

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    q = deque()

    visited[i][j] = True
    q.append([i, j])

    while len(q) != 0:
        cy, cx = q.popleft()

        for dir in range(len(dy)):
            ny, nx = cy + dy[dir], cx + dx[dir]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if board[ny][nx] != 1:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            q.append([ny, nx])
    


for _ in range(T):
    M, N, K = map(int, input().strip().split(' '))

    board = [[0 for j in range(M)] for i in range(N)]

    for x in range(K):
        j, i = map(int, input().strip().split(' '))
        board[i][j] = 1


    cnt = 0
    visited = [[False for j in range(M)] for i in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                bfs(board, visited, i, j)

    
    print(cnt)