
N = int(input())
dic, lst = {}, []

def mode(dic,n):
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
    return 0 

ans_sum, min_ans, max_ans = 0, 4001, -4001

for i in range(N):
    num = int(input())
    ans_sum +=num #합
    lst.append(num) #중간
    mode(dic,num) #최빈

    if num < min_ans:
        min_ans = num
    if num > max_ans:
        max_ans = num

lst.sort()
dic_lst = list(dic.items())
dic_lst = sorted(dic_lst, key=lambda x: (-x[1],x[0]))

print(round(ans_sum/N))

print(lst[N//2])

if len(dic_lst) > 1:
    if dic_lst[1][1] == dic_lst[0][1]:
        print(dic_lst[1][0])
    else:
        print(dic_lst[0][0])
else:
    print(dic_lst[0][0])

print(max_ans-min_ans)
