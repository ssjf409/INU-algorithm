'''
8
"sbrus.txt"
"spc.spc"
"acm.icpc"
"korea.icpc"
"sample.txt"
"hello.world"
"sogang.spc"
"example.txt"
'''
N = int(input())

ext_count = {}


for _ in range(N):
    file_name, ext = input().split('.')
    
    if ext not in ext_count:
        ext_count[ext] = 1
    else:
        ext_count[ext] += 1

ext_list = list(ext_count)
ext_list.sort()

for ext in ext_list:
    print(ext + ' ' + str(ext_count[ext]))



