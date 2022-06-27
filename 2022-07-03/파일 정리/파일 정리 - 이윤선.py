# 파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘
# 보기 편하게 확장자들을 사전 순으로 정렬해 줘

#import sys
#input = sys.stdin.readline
#를 하면 출력 형식 잘못..이 나오는데 이유를 모르겠음 ㅠ

N = int(input())

extension_dict = dict()

for _ in range(N):
    name, extension = map(str,input().split('.'))
    if extension in extension_dict:
        extension_dict[extension] += 1
    else:
        extension_dict[extension] = 1

extension_lst = sorted(extension_dict.items())


for ans in extension_lst:
    print(ans)