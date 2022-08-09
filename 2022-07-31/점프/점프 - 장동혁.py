import sys
from sys import stdin
sys.setrecursionlimit(10050)

# 현재 위치가 y, x일 때, 목적지까지 갈 수 있는 경우의 수를 반환
def get_possible_path(cache, board, y, x):
    if y == len(board) - 1 and x == len(board) - 1: # 기저 사례 : 탈출 조건
        return 1
    
    if cache[y][x] != -1:
        return cache[y][x]
    
    if board[y][x] == 0:
        return 0

    ret = 0
    if y + board[y][x] < len(board):
        ret += get_possible_path(cache, board, y + board[y][x], x)
    if x + board[y][x] < len(board):
        ret += get_possible_path(cache, board, y, x + board[y][x])
    
    cache[y][x] = ret
    return ret


N = int(stdin.readline())
board = []
cache = [[-1 for j in range(N)] for i in range(N)]

for _ in range(N):
    board.append(list(map(int, stdin.readline().split(' '))))



print(get_possible_path(cache, board, 0, 0))
