#원래 양의 절반을 흘림
#에너지 드링크가 하나만 남을 때 까지..

N = int(input())

lst = list(map(int, input().split()))

lst.sort(reverse= True)
answer = lst[0] + (sum(lst)-lst[0])/2

print(answer)

