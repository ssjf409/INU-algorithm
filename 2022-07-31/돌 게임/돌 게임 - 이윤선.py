#번갈아가면서 1개 또는 3개 가져갈 수 있고 나머지 돌 가져가는 사람이 이김

first = 'SK'
second = 'CY'


N = int(input())

num = N // 3
num += N % 3

if num % 2:
    print(first)
else:
    print(second)
