#아래로가거나 오른쪽으로 가는 경우만 존재

import sys 
input = sys.stdin.readline
from collections import deque

N = int(input())

boards = [list(map(int,input().split())) for _ in range(N)]

check = [[0 for _ in range(N)] for _ in range(N)]
check[0][0] = 1


for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break

        if check[i][j]:
            move = boards[i][j]
            if i+ move < N:
                check[i+move][j] += check[i][j]
            if j + move < N:
                check[i][j+move] += check[i][j]
              

print(check[-1][-1])

## dfs는 시간초과 bfs는 메모리 초과 났음
## 왜 안됐냐..... queue나 stack에 중복되는 index값을 계속 넣을 수 밖에 없어서.. 이런 슬픈 경우 발생
