#파티장 크기 서비스 요청 손님 수

import sys

input = sys.stdin.readline


N, M = map(int,input().split())

party = []
for _ in range(N):
    party.append(list(map(int,input().split())))



for k in range(N):
    for i in range(N):
        for j in range(N):
            if party[i][j] > party[i][k] + party[k][j]:
                party[i][j] = party[i][k] + party[k][j]

for _ in range(M):
    A, B, C =  map(int,input().split())
    #파티장 번호 , 다음 파티장, 다음 파티 열리는 시간
    if party[A-1][B-1] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")