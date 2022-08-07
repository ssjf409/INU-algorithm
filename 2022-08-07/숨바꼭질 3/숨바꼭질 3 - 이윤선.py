import heapq

N, M, = map(int,input().split())
time = [0 for _ in range(100001)]

def dijkstra(X):
   q = []
   time[X] = 1
   heapq.heappush(q, (1, X))
   while q:
    imp, now = heapq.heappop(q)
    plus, minus, twice = now + 1, now - 1, now * 2
    if now == M:
        return time[now]-1
    if 0 <= twice <= 100000 and time[twice]  == 0:
        time[twice] = time[now]
        heapq.heappush(q, [time[twice],twice])
    if 0 <= plus <= 100000 and time[plus]  == 0:
        time[plus] = time[now]+1
        heapq.heappush(q, [time[plus],plus])
    if 0 <= minus <= 100000 and time[minus]  == 0:
        time[minus] = time[now]+1
        heapq.heappush(q, [time[minus],minus])
    

print(dijkstra(N))

