

N = int(input())

lst = list(map(int,input().split()))


tmp_lst = lst[:]
dic = {}
lst = sorted(list(set(lst)))
print(lst)
idx = 0

for i in lst:
    dic[i] = idx
    idx += 1


for num in tmp_lst:
    print(dic[num],  end = " ")
