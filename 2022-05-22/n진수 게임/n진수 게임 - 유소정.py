# 진법 n
# 미리 구할 숫자의 갯수 t
# 게임에 참가하는 인원 m
# 튜브의 순서 p
def solution(n, t, m, p):
    li = []

    # n진수 리스트
    for i in range(0, (t * m) + 1):
        if n == 2:
            li += list(bin(i)[2:])
        elif n == 8:
            li += list(oct(i)[2:])
        elif n == 16:
            li += list(hex(i)[2:])
        else:
            li += list(str(i))

    # 튜브
    answer = ""
    count = 0

    for i in range(p-1, len(li) + 1, m):
        answer += li[i].upper()
        count += 1

        if count == t:
            return answer


print(solution(10, 2, 2, 1))