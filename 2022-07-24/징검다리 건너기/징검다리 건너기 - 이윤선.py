
N = int(input())

rock = list(map(int, input().split()))

dp = [0] +[1e12 for _ in range(len(rock)-1)]


left = 0
right = 1
while right < len(rock):
    if left == right:
        right += 1
        left = 0
        continue

    K = (right - left) * (1 + abs(rock[left] - rock[right]))
    dp[right] = min(max(K, dp[left]), dp[right])
    left += 1


print(dp[-1])
