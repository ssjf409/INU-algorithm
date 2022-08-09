from sys import stdin

def get_board_val(board, y, x):
    if board[y][x] == -1:
        return [1, 0, 0]
    elif board[y][x] == 0:
        return [0, 1, 0]
    else:
        return [0, 0, 1]


# -1, 0, 1
def find_clean_paper_count(board, y, x, length):
    if length == 1:
        return get_board_val(board, y, x)
    
    first_cell = board[y][x]
    is_clean_paper = True

    for i in range(length):
        for j in range(length):
            if board[y + i][x + j] != first_cell:
                is_clean_paper = False
                break
        if not is_clean_paper:
            break
    
    if is_clean_paper:
        return get_board_val(board, y, x)
    
    partial_length = length // 3
    minus_cnt = 0
    zero_cnt = 0
    plus_cnt = 0

    for i in range(3):
        for j in range(3):
            temp = find_clean_paper_count(board, y + i * partial_length, x + j * partial_length, partial_length)
            minus_cnt += temp[0]
            zero_cnt += temp[1]
            plus_cnt += temp[2]
    return [minus_cnt, zero_cnt, plus_cnt]





N = int(stdin.readline())


board = [] 

for _ in range(N):
    board.append(list(map(int, stdin.readline().split(' '))))


result = find_clean_paper_count(board, 0, 0, N)
print(result[0])
print(result[1])
print(result[2])



