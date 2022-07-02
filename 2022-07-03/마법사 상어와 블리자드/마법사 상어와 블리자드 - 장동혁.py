'''
"7 1"
"0 0 0 0 0 0 0"
"3 2 1 3 2 3 0"
"2 1 2 1 2 1 0"
"2 1 1 0 2 1 1"
"3 3 2 3 2 1 2"
"3 3 3 1 3 3 2"
"2 3 2 2 3 2 3"
"2 2"


"7 4"
"0 0 0 2 3 2 3"
"1 2 3 1 2 3 1"
"2 3 1 2 3 1 2"
"1 2 3 0 2 3 1"
"2 3 1 2 3 1 2"
"3 1 2 3 1 2 3"
"1 2 3 1 2 3 1"
"1 3"
"2 2"
"3 1"
"4 3"

"7 4"
"1 1 1 2 2 2 3"
"1 2 2 1 2 2 3"
"1 3 3 2 3 1 2"
"1 2 2 0 3 2 2"
"3 1 2 2 3 2 2"
"3 1 2 1 1 2 1"
"3 1 2 2 2 1 1"
"1 3"
"2 2"
"3 1"
"4 3"


"3 1"
"0 0 0"
"0 0 0"
"0 0 0"
"1 1"


"7 7"
"1 1 1 2 2 2 3"
"1 2 2 1 2 2 3"
"1 3 3 2 3 1 2"
"1 2 2 0 3 2 2"
"3 1 2 2 3 2 2"
"3 1 2 1 1 2 1"
"3 1 2 2 2 1 1"
"1 3"
"2 2"
"3 1"
"4 3"
"1 3"
"1 1"
"1 3"


'''


def act_blizzard(seq_board, balls, dy, dx, length):
    n = len(seq_board)
    cy, cx = n // 2, n // 2

    deleted_area = set()

    # 1, 2, 3
    ret = [0, 0, 0]
    
    for i in range(length):
        cy += dy
        cx += dx
        deleted_area.add(seq_board[cy][cx])
    
    
    #shorten balls & count ball type
    ball_type_cnt = []
    for i, n in enumerate(balls):
        if i in deleted_area:
            continue
        if len(ball_type_cnt) == 0:
            ball_type_cnt.append([n, 1])
            continue
        if ball_type_cnt[-1][0] == n:
            ball_type_cnt[-1][1] += 1
        else:
            ball_type_cnt.append([n, 1])
        
    # boom
    while True:
        boom_cnt = 0
        temp = []
        for type_cnt in ball_type_cnt:
            if type_cnt[1] >= 4:
                boom_cnt += 1
                ret[type_cnt[0] - 1] += type_cnt[1]
                continue
            if len(temp) == 0:
                temp.append(type_cnt)
                continue
            if temp[-1][0] == type_cnt[0]:
                temp[-1][1] += type_cnt[1]
            else:
                temp.append(type_cnt)
        ball_type_cnt = temp

        if boom_cnt == 0:
            break
    
    # lengthen
    temp = [0]

    for i in range(1, len(ball_type_cnt)):
        temp.append(ball_type_cnt[i][1])
        temp.append(ball_type_cnt[i][0])
    
    ret.append(temp)

    # [1, 2, 3, [](balls) ]
    return ret



dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

N, M = list(map(int, input().strip().split(' ')))

half_len = (N - 1) // 2

seq = 0
seq_board = [[-1 for _ in range(N)] for _ in range(N)]
board = []

balls = [0]

for i in range(N):
    board.append(list(map(int, input().strip().split(' '))))


cy, cx = N // 2, N // 2
seq_board[cy][cx] = seq
seq += 1
cx -= 1
for length in range(2, half_len * 2 + 1, 2):
    for dir in range(len(dy)):
        for l in range(length):
            if board[cy][cx] != 0:
                balls.append(board[cy][cx])
            
            seq_board[cy][cx] = seq
            seq += 1
            if l == length - 1 and dir != 3:
                cy += dy[(dir + 1) % 4]
                cx += dx[(dir + 1) % 4]
            else:
                cy += dy[dir]
                cx += dx[dir]


answer = 0

att_dy = [0, -1, 1, 0, 0]
att_dx = [0, 0, 0, -1, 1]

for _ in range(M):
    dir, length = list(map(int, input().strip().split(' ')))
    one, two, three, balls = act_blizzard(seq_board, balls, att_dy[dir], att_dx[dir], length)
    answer += (one + 2 * two + 3 * three)

print(answer)



