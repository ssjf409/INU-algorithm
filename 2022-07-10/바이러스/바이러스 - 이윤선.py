N = int(input()) 
M = int(input())

node_lst = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    node_lst[a].append(b)
    node_lst[b].append(a)

# N = 7
# M = 6
# node_lst = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]] 
visit = set()
stack = [1]

while stack:
    node = stack.pop()
    visit.add(node)
    # print(visit, stack)
    for node_node in node_lst[node]:
        if node_node not in visit:
            stack.append(node_node)

print(len(visit)-1)


# 끊임없이 이어져 있기 때문에 (최단거리 찾는 문제 x) dfs를 선택하여 풀었다.