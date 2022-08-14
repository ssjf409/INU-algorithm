
N, M, T = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

answer = []

def dfs():
    stack = [[0,0, 0,False]]
    cnt = 0
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    while stack:
        x,y,cnt,state = stack.pop()        
        if x == M-1 and y == N-1:
            answer.append(cnt)
            continue

        if visited[y][x] != 0 and cnt < visited[y][x]:
            visited[y][x] = cnt
        elif visited[y][x] == 0:
            visited[y][x] = cnt
        else:
            continue

        cnt += 1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx >= M and xx < 0 and yy >= N and yy < 0:
                continue
            if state == True:
                stack.append([xx,yy,cnt,state])
            if state == False:
                if graph[yy][xx] == 1:
                    continue
                elif graph[yy][xx] == 2:
                    state = True
                    stack.append([xx,yy,cnt,state])
                else:
                    stack.append([xx,yy,cnt,state])


dfs()
print(graph)
print(answer)          