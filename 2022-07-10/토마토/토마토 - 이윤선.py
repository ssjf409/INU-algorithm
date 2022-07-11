from collections import deque

M, N = map(int, input().split())
#bfs ㅁㅜㄹㅂㅏㅇㅇㅜㄹ...ㅍㅓㅈㅣㄴㅡㄴㄴㅡㄲㅣㅁ 
#ㅅㅣㄱㅏㄴㅇㅔㄸㅏㄹㅏㅅㅓ ㄴㅡㄹㅇㅓㄴㅏㅁ

board = []
for i in range(N):
    board.append(list(map(int,input().split())))

# print(board)


# N,M = 4, 6
# board = [[1, -1, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, -1, 1]]
queue = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            queue.append([i,j])


dx,dy = [1,-1,0,0], [0,0,1,-1]
max_answer = 0
while queue:
    y, x = queue.popleft()
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0<=xx<M and 0 <= yy < N and board[yy][xx] == 0:
            board[yy][xx] = board[y][x] + 1
            queue.append([yy,xx])


for i in range(N):
    if 0 in board[i]:
        print(-1)
        break

    max_answer = max(max(board[i]),max_answer)
    
    if i == N-1:
        print(max_answer-1)
