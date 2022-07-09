#인접한 노드르 탐색하여 문제를 풀어야 함으로 bfs를 써야 한다고 생각했는ㄴ데 시간초과 ㅎ ㅎ ㅎ ㅎ
#내일 다시 풀어야짓..

from collections import deque
import sys

input = sys.stdin.readline


def bfs(graph,visited,start,queue):
    dx = [1,-1,0,0] 
    dy = [0,0,1,-1]

    tmp_queue= deque()
    tmp_queue.append(start)

    while tmp_queue:
        y,x = tmp_queue.popleft()
        visited.append([y,x])
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if [yy,xx] not in visited and [yy,xx] in queue:
                tmp_queue.append([yy,xx])

    return visited


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    
    # M, N, K = 10, 8, 17
    # graph = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    queue = deque()

    for _ in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1
        queue.append([y,x])


    visit = []
    count = 0

    for i,j in queue:
        start = [i,j]
        if start in visit:
            continue
        visit = bfs(graph, visit, start, queue)
        count += 1

    print(count)