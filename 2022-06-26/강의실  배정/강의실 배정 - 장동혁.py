'''
3
"1 3"
"2 4"
"3 5"
'''

import heapq


# [end, start]
pq = []


N = int(input())
for _ in range(N):
    start, end = map(int, input().strip().split(' '))
    heapq.heappush(pq, [end, start])

cnt = 1
last_end = 0

temp = []

while len(pq) != 0:
    end, start = heapq.heappop(pq)
    start = start
    if start < last_end:
        heapq.heappush(temp, [end, start])
        continue
    last_end = end

    if len(pq) == 0 and len(temp) != 0:
        cnt += 1
        pq = temp.copy()
        temp = []



print(cnt)