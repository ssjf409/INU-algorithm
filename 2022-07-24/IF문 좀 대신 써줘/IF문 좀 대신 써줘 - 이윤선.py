import sys 
input = sys.stdin.readline

def binary_search(target, data):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > data[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


N, M = map(int,input().split())

name_dic, data = {}, []
for i in range(N):
    name, val = input().split()
    data.append(int(val))
    if val in name_dic:
        continue
    else:
        name_dic[val] = name   


for _ in range(M):
    target = int(input())
    left = binary_search(target, data)
    print(name_dic[str(data[left])])
    