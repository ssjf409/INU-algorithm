N = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]
shark = [[]]
students = {}
favor = {}

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#print(board)

#lst = ['4 2 5 1 7', '2 1 9 4 5','5 8 1 4 3',' 1 2 9 3 4','7 2 3 4 8','9 8 4 5 7','6 5 2 3 4','8 4 9 2 1','3 9 2 1 4']

#lst = ['7 9 3 8 2','5 7 3 8 6','3 5 2 4 9', '9 6 8 3 4','8 5 3 1 6', '6 3 8 5 4','2 6 4 8 7', '1 8 3 4 5','4 7 9 3 8']
for _ in range(N**2):
#for input in lst:
    temp = list(map(int,input().split()))
    favor[temp[0]] = temp[1:]
    max_cnt = -1
    max_zero_cnt = 0
    max_tmp = 0
    location = []
    for st in favor[temp[0]] :
        if st in students:
            location.append(students[st])
    if location:
        for i in range(N):
            for j in range(N):
                cnt = 0
                zero_cnt = 0
                if board[i][j] == 0:
                    for k in range(4):
                        xx = i + dx[k]
                        yy = j + dy[k]
                        if 0 <= xx < N and 0 <= yy < N:  
                            if board[xx][yy] in favor[temp[0]]:
                                cnt += 1
                            elif board[xx][yy] == 0:
                                zero_cnt += 1             
                    if cnt > max_cnt:
                        max_cnt = cnt
                        max_zero_cnt = zero_cnt
                        students[temp[0]]  = [i,j]
                    elif cnt == max_cnt and zero_cnt > max_zero_cnt:
                        max_cnt = cnt
                        max_zero_cnt = zero_cnt
                        students[temp[0]]  = [i,j]
                        
    else:   
        for i in range(N):
            for j in range(N):
                cnt = 0
                if board[i][j] == 0:
                    for k in range(4):
                        xx = i + dx[k]
                        yy = j + dy[k]
                        if  0 <= xx < N and 0 <= yy < N and board[xx][yy] == 0:
                            cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt
                        students[temp[0]]  = [i,j]
    x,y = students[temp[0]]
    board[x][y] = temp[0]


print(board)
answer = 0
for i in range(1, N**2+1):
    xx,yy = students[i]
    cnt = 0
    for k in range(4):
        x = xx + dx[k]
        y = yy + dy[k]
        if  0 <= x < N and 0 <= y < N and board[x][y] in favor[i]:
            cnt += 1

    if cnt == 1:
        answer += 1
    elif cnt == 2:
        answer += 10
    elif cnt == 3:
        answer += 100
    elif cnt == 4:
        answer += 1000

print(answer)