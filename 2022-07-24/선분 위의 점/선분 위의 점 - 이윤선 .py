import sys 
input = sys.stdin.readline

N, M = map(int, input().split())


def binary_search1(target, lst):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if target <= lst[mid]:
            right = mid-1
        else:
            left = mid + 1
    
    return right+1


def binary_search2(target, lst):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if target < lst[mid]:
            right = mid-1
        else:
            left = mid + 1
    
    return right

dot_lst = list(map(int, input().split()))

for _ in range(M):
    start , end = map(int, input().split())
    start_dot = binary_search1(start, dot_lst)
    end_dot = binary_search2(end, dot_lst)
    
    print(end_dot-start_dot+1)
       