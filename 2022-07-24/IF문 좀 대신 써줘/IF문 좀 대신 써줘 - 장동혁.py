from bisect import bisect_left, bisect_right
from sys import stdin

N, M = map(int, stdin.readline().strip().split(' '))

index_title = {} # key : index(int), value : 랭크이름 (str)
title = []

for _ in range(N):
    title_name, value = stdin.readline().strip().split(' ')
    value = int(value)
    index_title[len(title)] = title_name
    title.append(value)


for _ in range(M):
    target = int(stdin.readline())
    index = bisect_left(title, target)
    print(index_title[index])

