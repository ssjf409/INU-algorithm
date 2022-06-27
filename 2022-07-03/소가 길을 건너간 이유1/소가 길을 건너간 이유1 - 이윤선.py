N = int(input())

cow = dict()
check = dict()

for i in range(1,11):
    check[i] = 0    

for _ in range(N):
    cow_num, where = map(int, input().split())
    if cow_num in cow:
        if cow[cow_num] != where:
            check[cow_num] += 1
            cow[cow_num] = where
    else:
        cow[cow_num] = where

print(sum(check.values()))