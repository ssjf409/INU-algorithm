'''
3
"4 2 5 1 7"
"3 1 9 4 5"
"9 8 1 2 3"
"8 1 9 3 4"
"7 2 3 4 8"
"1 9 2 5 7"
"6 5 2 3 4"
"5 1 9 2 8"
"2 9 3 1 4"

3
"4 2 5 1 7"
"2 1 9 4 5"
"5 8 1 4 3"
"1 2 9 3 4"
"7 2 3 4 8"
"9 8 4 5 7"
"6 5 2 3 4"
"8 4 9 2 1"
"3 9 2 1 4"


3
"1 2 3 4 5"
"2 3 4 5 6"
"3 4 5 6 7"
"4 5 6 7 8"
"5 6 7 8 9"
"6 7 8 9 1"
"7 8 9 1 2"
"8 9 1 2 3"
"9 1 2 3 4"

'''

def get_favorite_score(board, N, favorites, i, j):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    ret = 0
    empty_seat_cnt = 0

    for dir in range(len(dy)):
        ny, nx = i + dy[dir], j + dx[dir]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if board[ny][nx] == 0:
            empty_seat_cnt += 1
            continue
        if board[ny][nx] in favorites:
            ret += 1
    
    return [ret, empty_seat_cnt]



def take_best_seat(board, N, favorites, cur_student):
    best_y, best_x = -1, -1
    max_favorite = -1
    max_empty_seat = -1

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            favorite_score, empty_seat_cnt = get_favorite_score(board, N, favorites, i, j)

            if favorite_score > max_favorite:
                max_favorite = favorite_score
                best_y, best_x = i, j
                max_empty_seat = empty_seat_cnt
            elif favorite_score == max_favorite:
                if empty_seat_cnt > max_empty_seat:
                    max_empty_seat = empty_seat_cnt
                    best_y, best_x = i, j
        
    board[best_y][best_x] = cur_student



N = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

# [int, set]
favorite = {}
answer = 0


for _ in range(N * N):
    students = list(map(int, input().strip().split(' ')))
    cur_student = students[0]

    
    favorite[cur_student] = set()
    favorite_students = favorite[cur_student]
    

    for i in range(1, len(students)):
        favorite_students.add(students[i])
    
    take_best_seat(board, N, favorite_students, cur_student)


for i in range(N):
    for j in range(N):
        cur_student = board[i][j]
        favorit_students = favorite[cur_student]
        score = get_favorite_score(board, N, favorit_students, i, j)[0]

        if score == 0:
            continue
        elif score == 1:
            answer += 1
        elif score == 2:
            answer += 10
        elif score == 3:
            answer += 100
        else:
            answer += 1000

print(answer)

