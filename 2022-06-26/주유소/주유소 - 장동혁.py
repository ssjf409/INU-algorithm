

N = int(input())

distances = list(map(int, input().strip().split(' ')))
costs = list(map(int, input().strip().split(' ')))

# [cost, remain, index(sequnce)]
data = [[costs[-1], 0, len(costs) - 1]]

last_idx = len(distances) - 1

for i in range(len(distances)):
    cur_dist = distances[last_idx - i]
    cost = costs[last_idx - i]

    acc_dis = data[-1][1] + cur_dist

    data.append([cost, acc_dis, last_idx - i])

data.sort(key = lambda x : (x[0], -x[1]))

prev_index = float('inf')
prev_dist = 0
total_cost = 0

for cost, remain_dist, cur_index in data:
    if cur_index < prev_index:
        range_distance = remain_dist - prev_dist

        total_cost += range_distance * cost

        prev_index = cur_index
        prev_dist = remain_dist

print(total_cost)