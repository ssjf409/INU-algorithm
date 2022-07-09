#수빈이는 걷거나 순간이동 가능
# 위치 x일떄 걸으면 1초뒤에 x+1 아님 x-1
# 순간이동하면 2*x
#lst[N] = 0 이면 N이 0일때 무한루프 발생


import heapq


N, K = map(int,input().split())

lst = [0 for _ in range(1000001)]
heap = []
heapq.heappush(heap, [1,N])
lst[N] = 1

while heap:
    cnt, node = heapq.heappop(heap)
    if node == K:
        print(lst[node]-1)
        break
    plus, minus, twice  = node + 1, node - 1, node * 2
    if 0 <= twice < 1000001 and lst[twice] == 0:
        lst[twice] = lst[node]
        heapq.heappush(heap, [lst[twice],twice])
    if 0 <= plus < 1000001 and lst[plus] == 0:
        lst[plus] = lst[node] + 1
        heapq.heappush(heap, [lst[plus],plus])
    if 0 <= minus < 1000001 and lst[minus] == 0:
        lst[minus] = lst[node] + 1
        heapq.heappush(heap, [lst[minus],minus])
    
    
    
        