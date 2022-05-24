# S: 1제곱, D: 2제곱, T: 3제곱
# *: 해당 점수와 바로 전에 얻은 점수를 각 2배
# #: 해당 점수를 마이너스

def solution(dartResult):
    li = []
    i = -1

    dartResult = dartResult.replace("10", "K")
    for n in dartResult:
        if n == "S":
            continue

        elif n == "D":
            li[i] **= 2

        elif n == "T":
            li[i] **= 3

        elif n == "*":
            if i == 0:
                li[i] *= 2

            else:
                li[i] *= 2
                li[i - 1] *= 2

        elif n == "#":
            li[i] *= -1
        else:
            if n == "K":
                n = 10
            li.append(int(n))
            i += 1
    return sum(li)


print(solution("1D2S#10S"))
