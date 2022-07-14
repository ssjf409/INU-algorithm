N = int(input())

lst = list(map(int,input().split()))

lst.sort()
lp, rp = 0,N-1
mc = 2000000001
while lp < rp:
    cc = lst[lp] + lst[rp]

    if mc > abs(cc):
        mc = abs(cc)
        answer = [str(lst[lp]),str(lst[rp])]
        if mc == 0:
            break
    
    if cc < 0:
        lp += 1
    elif cc > 0:
        rp -= 1
    

print(' '.join(answer))