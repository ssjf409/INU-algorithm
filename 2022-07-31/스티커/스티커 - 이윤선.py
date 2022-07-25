
import sys 
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [[0 for _ in range(N+2)] for _ in range(2)]
    stickers = [[0,0] + list(map(int,input().split())) for _ in range(2)]
    for j in range(2,N+2):
        for i in range(-1,1):
            dp[i][j] = max(dp[i+1][j-2], dp[i+1][j-1])+stickers[i][j]

    print(max(dp[0][-1],dp[1][-1]))