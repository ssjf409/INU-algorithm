# 그리디

n = int(input())

quotient_five = n // 5 # 5원으로 거슬러줄 동전의 개수
remainder = n % 5 # 5원짜리 동전으로도 거슬러줄수 없는 금액

# 짝수 -> 그냥 거슬러주면 됨
# 홀수 -> 짝수로 맞춰주고 싶다.
# ex) quotient_five : 1, remainder : 8,


if remainder % 2 == 0:
    print(quotient_five + remainder // 2)
else:
    if quotient_five == 0:
        print(-1)
    else:
        print(quotient_five - 1 + (remainder + 5) // 2)