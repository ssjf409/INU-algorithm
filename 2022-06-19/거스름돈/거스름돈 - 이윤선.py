money = int(input())
cnt = 0
if money < 5 and money % 2:
    cnt = -1
elif money < 5:
    cnt += money // 2
else:
    for i in range(money//5, -1, -1):
        if (money-5*i) % 2 == 0:
            cnt += i
            cnt += ((money-5*i)//2)
            print(i, cnt)
            break
print(cnt)