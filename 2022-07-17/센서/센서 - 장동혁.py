N = int(input())
K = int(input())
sensors = list(map(int, input().strip().split(' ')))
sensors.sort()

dist = []
for i, n in enumerate(sensors[0:-1]):
    dist.append(sensors[i + 1] - sensors[i])

dist.sort(reverse = True)

dist = dist[K - 1:]

print(sum(dist))
