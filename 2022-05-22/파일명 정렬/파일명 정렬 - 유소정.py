# 파일명: 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")
# 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함
# HEAD, NUMBER, TAIL

# HEAD: 숫자가 아닌 문자, 최소한 한 글자 이상
# NUMBER: 한 글자에서 최대 다섯 글자, 0부터 99999 사이 / 예) 99999, 00000, 0101
# TAIL: 나머지 부분, 아무 글자도 없을 수 있다.

# 정렬 기준
# 1. HEAD 사전 순, 대소문자 구분X
# 2. NUMBER 숫자 순 / 예) 9 < 10 < 0011[11] < 012[12] < 13 < 014[14]
# 3. 원래 순서 유지
from collections import defaultdict


def solution(files):
    head = []
    number = defaultdict(list)
    tail = defaultdict(list)

    for file in files:
        check = False
        for idx in range(1, len(file)):
            if not check:
                if 47 < ord(file[idx]) < 58:
                    start = idx
                    check = True
            else:
                if not 47 < ord(file[idx]) < 58:
                    new_start = idx

                    over_idx = 5 - ((idx - start) + 1)
                    if over_idx < 0:
                        new_start -= over_idx
                    break

        head_data = file[:start].lower()
        number_data = int(file[start:new_start])
        tail_data = file[new_start:]

        head.append(head_data)
        number[head_data].append(number_data)
        number[head_data].sort()

        tail[number_data].append(tail_data)
        tail[number_data].sort()

    print(set(head))
    print()
    print(number)
    print()
    print(tail)



solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])