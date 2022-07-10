import heapq

N, K = map(int, input().strip().split(' '))

max_len = max(N, K)

visited = [False] * (max_len * 2 + 1)

pq = []

heapq.heappush(pq, [0, N])

# step = -1

flag = False

while len(pq) != 0:
    pq_size = len(pq)
    # step += 1

    for _ in range(pq_size):
        step, cur = heapq.heappop(pq)
        # print(step, cur)
        if cur == K:
            flag = True
            print(step)
            break;
        
        if cur * 2 <= max_len * 2 and visited[cur * 2] == False:
            visited[cur * 2] = True
            heapq.heappush(pq, [step, cur * 2])
        
        if cur + 1 <= max_len * 2 and visited[cur + 1] == False:
            visited[cur + 1] = True
            heapq.heappush(pq, [step + 1, cur + 1])

        if cur - 1 >= 0 and visited[cur - 1] == False:
            visited[cur - 1] = True
            heapq.heappush(pq, [step + 1, cur - 1])
    
    if flag:
        break





