# import sys
# input = sys.stdin.readline

# N = int(input())

# cnt = 0
# lst = []
# for i in range(N):
#     start, end = map(int, input().split())
#     lst.append([start,end])

# max_lst = [0]
# lst.sort()
# 현재 써져있는 if조건을 만족 안할 시 새로운 강의실 배정
# for i in range(len(lst)):
#     if lst[i][0] >= max_lst[0]:
#         max_lst[0] = lst[i][1]
#     else:
#         max_lst.append(lst[i][1])
#     max_lst.sort()

# print(len(max_lst))

#s에 시작 t에 끝나는 n개의 수업 최소의 강의실 사용

import sys, heapq
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
    start, end = map(int, input().split())
    lst.append([start,end])

end_lst = [0]
lst.sort()

#현재 써져있는 if조건을 만족 안할 시 새로운 강의실 배정

for i in range(len(lst)):
    if lst[i][0] >= end_lst[0]:
        heapq.heappop(end_lst)
        heapq.heappush(end_lst, lst[i][1])

    else:
        heapq.heappush(end_lst, lst[i][1])

print(len(end_lst))
