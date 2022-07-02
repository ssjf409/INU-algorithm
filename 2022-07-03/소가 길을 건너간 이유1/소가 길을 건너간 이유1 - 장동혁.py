'''
8
"3 1"
"3 0"
"6 0"
"2 1"
"4 1"
"3 0"
"4 0"
"3 1"

'''

N = int(input())

previous = {}

across_cnt = 0

for _ in range(N):
    cow, loc = list(map(int, input().strip().split(' ')))

    if cow not in previous:
        previous[cow] = loc
        continue

    if previous[cow] != loc:
        previous[cow] = loc
        across_cnt += 1


print(across_cnt)