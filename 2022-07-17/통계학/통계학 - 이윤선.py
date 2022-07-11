
N = int(input())
dic, lst = {}, []

def mode(dic,n):
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
    return 0 

for i in range(N):
    num = int(input())
    mode(dic,num)
    lst.append(num)

lst.sort()
dic_lst = list(dic.items())
dic_lst = sorted(dic_lst, key=lambda x: (-x[1],x[0]))
print(dic_lst)

print(round(sum(lst)/N))
print(lst[N//2])
if len(dic_lst) > 1:
    if dic_lst[1][1] == dic_lst[0][1]:
        print(dic_lst[1][0])
    else:
        print(dic_lst[0][0])
else:
    print(dic_lst[0][0])

print(max(lst)-min(lst))
