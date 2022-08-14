import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
answer = [ 0 for _ in range(N+1)]
answer[1] = 1

def bfs(tree, start):
    if len(tree[start]) == 0:
        return 

    for node in tree[start]:
        if answer[node] == 0:
            answer[node] = start
            bfs(tree, node)




tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = 0
bfs(tree, 1)


for i in range(2,N+1):
    print(answer[i])