N = int(input())
K = int(input())

lst = list(map(int,input().split()))
diff = []
lst.sort()


for i in range(1, N):
    diff = (lst[i] - lst[i-1])


[1,3,6,6,7,9]
[2,3,0,1,2]

[3,6,7,8,10,12,14,15,18,20]
[3,1,1,2,2,2,1,3,2]
