#센서랑 행복유치원이랑 유사한듯보이는데 센서는 모르겠어서 요것을 먼저 푼다아


N, K = map(int, input().split())

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