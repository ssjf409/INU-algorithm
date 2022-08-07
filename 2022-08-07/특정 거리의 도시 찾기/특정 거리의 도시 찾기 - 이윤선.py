import heapq
import sys

input = sys.stdin.readline

def dijkstra(X):
   q = []
   heapq.heappush(q, (0, X))
   distance[X] = 0


   while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = dist+i[1] 
            heapq.heappush(q,(cost,i[0]))

N, M, K, X = map(int,input().split())
INF = int(1e9)
distance = [INF] * (N+1)

graph = [[] for i in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append([B,1])


dijkstra(X)

state = False
for i in range(1,N+1):
    if distance[i] == K:
        print(i)
        state = True

if state == False:
    print(-1)

