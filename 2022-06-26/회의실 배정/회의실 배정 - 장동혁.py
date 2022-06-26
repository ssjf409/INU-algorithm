'''
11
"1 4"
"3 5"
"0 6"
"5 7"
"3 8"
"5 9"
"6 10"
"8 11"
"8 12"
"2 13"
"12 14"
'''

import heapq


# [end, start]
pq = []


N = int(input())
for _ in range(N):
    start, end = map(int, input().strip().split(' '))
    heapq.heappush(pq, [end, start])

cnt = 0
last_end = 0
while len(pq) != 0:
    end, start = heapq.heappop(pq)
    start = start
    # print(start, end)
    if start < last_end:
        continue
    cnt += 1
    last_end = end

print(cnt)