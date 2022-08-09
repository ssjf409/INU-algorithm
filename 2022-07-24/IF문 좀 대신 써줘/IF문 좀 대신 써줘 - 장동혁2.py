from sys import stdin

def find_index(source, target):
    left = 0
    right = len(source) - 1
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if source[mid] >= target:
            right = mid - 1
            result = mid
        else:
            left = mid + 1
    return result




N, M = map(int, stdin.readline().strip().split(' '))

index_title = {}
title = []

for _ in range(N):
    title_name, value = stdin.readline().strip().split(' ')
    value = int(value)
    index_title[len(title)] = title_name
    title.append(value)


for _ in range(M):
    target = int(stdin.readline())
    index = find_index(title, target)
    print(index_title[index])

