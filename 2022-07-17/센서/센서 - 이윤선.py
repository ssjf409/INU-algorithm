N = int(input())
K = int(input())

lst = list(map(int,input().split()))
lst.sort()

diff = []
for i in range(1,len(lst)):
    diff.append(lst[i]-lst[i-1])

answer = 0
diff.sort()

for j in range(N-K):
    answer += diff[j]

print(answer)