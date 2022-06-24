
N = int(input())

roads = list(map(int,input().split()))
money = list(map(int,input().split()))
min_money = money[0]
cost = 0

for i in range(N-1):
    if money[i] < min_money:
        min_money = money[i]
        cost += min_money * roads[i]
    else:
        cost += min_money * roads[i]

print(cost)
