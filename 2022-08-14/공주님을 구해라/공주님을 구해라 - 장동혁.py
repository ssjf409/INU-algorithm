from collections import deque

def find_princess(board, visited, y, x, T):

    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    n = len(board)
    m = len(board[0])


    # [y, x, has_sword]
    has_sword = False
    if board[y][x] == 2:
        has_sword = True
    q = deque()
    q.append([y, x, has_sword])
    visited[y][x] = 1

    cnt = 0

    while len(q) != 0:
        q_size = len(q)
        for _ in range(q_size):
            cy, cx, has_sword = q.popleft()

            # 시간 내에 못 찾은 경우
            if cnt > T:
                return -1
            # 찾은 경우
            if cy == n - 1 and cx == m - 1:
                return cnt
            
            for dir in range(4):
                ny, nx = cy + dy[dir], cx + dx[dir]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if visited[ny][nx] == 2:
                    continue
                if visited[ny][nx] == 1:
                    if not has_sword:
                        continue
                if not has_sword:
                    if board[ny][nx] == 1:
                        continue
                if board[ny][nx] == 2:
                    cur_has_sword = True
                else:
                    cur_has_sword = has_sword
                q.append([ny, nx, cur_has_sword])
                if has_sword:
                    visited[ny][nx] = 2
                else:
                    visited[ny][nx] = 1
        cnt +=1
    return -1


N, M, T = map(int, input().split(' ' ))
board = []
visited = [[0 for j in range(M)] for i in range(N)] # 검 없이 방문 1, 검 있는 상태로 방문 2

for _ in range(N):
    board.append(list(map(int, input().split(' '))))

result = find_princess(board, visited, 0, 0, T)

if result == -1:
    print("Fail")
else:
    print(result)
