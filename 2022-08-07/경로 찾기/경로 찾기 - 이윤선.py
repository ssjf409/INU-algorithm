

def wornl(i):
     for j in range(N):
        if check[j] == 0 and graph[i][j] == 1:
            check[j]=1
            wornl(j)

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    check = [0 for _ in range(N)]
    wornl(i)
    for j in range(N):
        print(check[j], end = ' ')
    print()

