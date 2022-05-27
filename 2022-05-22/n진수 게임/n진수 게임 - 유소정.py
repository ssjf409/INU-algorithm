# 진법 n
# 미리 구할 숫자의 갯수 t
# 게임에 참가하는 인원 m
# 튜브의 순서 p

# 진수 변환
def change(n, q):
    check = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)

        if str(mod) in check:
            rev_base +=  check[str(mod)]
        else:
            rev_base += str(mod)

    return rev_base[::-1]  # 역순인 진수를 뒤집어 줘야 원래 변환 base가 출력


def solution(n, t, m, p):
    li = ['0']

    # n진수 리스트
    for i in range(1, (t * m) + 1):
        li += change(i, n)

    # 튜브
    answer = ""
    count = 0

    for i in range(p-1, len(li) + 1, m):
        answer += li[i]
        count += 1

        if count == t:
            return answer


print(solution(2, 4, 2, 1))