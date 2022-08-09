from sys import stdin

def find_index(source, target):
    left = 0
    right = len(source) - 1
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if source[mid] > target:
            right = mid - 1
            result = mid
        elif source[mid] < target:
            left = mid + 1
            result = mid
        else:
            return mid
    return result
        

N, M = map(int, stdin.readline().strip().split(' '))

dots = list(map(int, stdin.readline().strip().split(' ')))

for _ in range(M):
    start, end = map(int, stdin.readline().strip().split(' '))
    if start > end:
        print(0)
        break

    start_index = find_index(dots, start)
    end_index = find_index(dots, end)

    cnt = end_index - start_index + 1

    if dots[start_index] < start:
        cnt -= 1
    if dots[end_index] > end:
        cnt -= 1
    print(cnt)



'''
5 1
1 3 10 20 30
'''
