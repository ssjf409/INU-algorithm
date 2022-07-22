N = int(input())

inputs = list(map(int, input().strip().split(' ')))

sorted_inputs = sorted(inputs)

cnt = 0
idx = {}

for num in sorted_inputs:
    if num not in idx:
        idx[num] = cnt
        cnt += 1

for num in inputs:
    print(idx[num], end = ' ')

