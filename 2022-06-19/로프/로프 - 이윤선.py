import sys
input = sys.stdin.readline

n = int(input())
weight=[]

for _ in range(n):
  weight.append(int(input()))

weight.sort(reverse=True)

for i in range(n):
  weight[i] *= (i+1) 

weight.sort()

print(weight[-1])