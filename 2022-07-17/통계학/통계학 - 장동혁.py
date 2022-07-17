from sys import stdin

N = int(stdin.readline())


arr = [0] * 8001
s = 0.0

input_val = []

for _ in range(N):
    val = int(stdin.readline())
    s += val
    input_val.append(val)
    arr[val + 4000] += 1


avg = s / N
if avg >= 0:
    print(int(avg + 0.5))
else:
    print(int(avg - 0.5))


input_val.sort()
print(input_val[len(input_val) // 2])

result = -1
cur = 0
second = False

for i in range(8001):
    if cur < arr[i]:
        cur = arr[i]
        result = i
        second = False
    elif cur == arr[i] and not second:
        result = i
        second = True


print(result - 4000)
print(input_val[N - 1] - input_val[0])





