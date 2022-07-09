#인접한 노드르 탐색하여 문제를 풀어야 함으로 bfs를 써야 함

from collections import deque


def bfs(graph,visited,start,N,M):
    dx = [1,-1,0,0] 
    dy = [0,0,1,-1]

    queue = deque()
    queue.append(start)

    while queue:
        y,x = queue.popleft()
        visited.append([y,x])
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < M and 0 <= yy < N :
                if [yy,xx] not in visited and graph[yy][xx] == 1:
                    queue.append([yy,xx])

    return visited


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]



    # M, N, K = 10, 8, 17
    # graph = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


    for _ in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1


    visit = []
    #visit에 없어야 하고... 1인걸 찾아야 함... visit은 행열 위치가 들어가야 함..
    count = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and [i,j] not in visit:
                start = [i,j]
                visit = bfs(graph, visit, start,N,M)
                #bfs 이용하여 탐색
                count += 1
                #print(visit)

    print(count)