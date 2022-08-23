def find_boom_area(state, boom_pos):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    n = len(state)
    m = len(state[0])
    visited = [[False for j in range(len(state[0]))] for i in range(len(state))]

    ret = []
    
    for cy, cx in boom_pos:
        ret.append([cy, cx])
        visited[cy][cx] = True
        
        for dir in range(4):
            ny, nx = dy[dir] + cy, dx[dir] + cx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if state[ny][nx] == -1:
                continue
            ret.append([ny, nx])
            visited[ny][nx] = True

    return ret



R, C, N = map(int, input().split(' '))

board = []


for _ in range(R):
    board.append(input())

state = [[-1 for j in range(C)] for i in range(R)]

# visited = [[False for j in range(M)] for i in range(N)]
# q = deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == 'O':
            state[i][j] = 0

for time in range(2, N + 1):

    boom_pos = []
    for i in range(R):
        for j in range(C):
            if state[i][j] == -1:
                state[i][j] = time
            elif time - state[i][j] == 3:
                boom_pos.append([i, j])


    explosion_pos = find_boom_area(state, boom_pos)
    for y, x in explosion_pos:
        state[y][x] = -1

answer = []
for i in range(R):
    line = ""
    for j in range(C):
        if state[i][j] == -1:
            line += '.'
        else:
            line += 'O'
    answer.append(line)
    print(line)

# print(answer)