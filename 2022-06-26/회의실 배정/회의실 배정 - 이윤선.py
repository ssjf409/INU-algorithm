import sys
input = sys.stdin.readline

N = int(input())

max_end, cnt = 0, 0
lst = []
for i in range(N):
    start, end = map(int, input().split())
    lst.append([start,end])

lst.sort(key=lambda x:(x[1],x[0]))

for start, end in lst:
    if start >= max_end:
            max_end = end
            cnt += 1

print(cnt)