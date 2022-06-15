money = int(input())
cnt = 0
if money < 5:
    cnt = -1
else:
    for i in range(money//5, 0, -1):
        if (money-5*i) % 2 == 0:
            cnt += ((money-5*i)//2)
            break
    cnt += i


print(cnt)