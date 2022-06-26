
'''

'''

N = int(input())
value = list(map(int, input().strip().split(' ')))

max_val = max(value)

answer = 0
found = False

for n in value:
    if n == max_val and found == False:
        found = True
        answer += n
        continue
    answer += (n / 2.0)

print(answer)
