#계단 한번에 하나 또는ㄴ 두개
#연속된 세개의 계단 밟으면 안된다.
# 마지막 도착 계단은 반드시 밟아야 한다.
import sys 
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+2)]

stairs = [0]*2 + [int(input()) for _ in range(N)]
dp[2] = stairs[2]

for i in range(3,N+2):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])


print(dp[-1])