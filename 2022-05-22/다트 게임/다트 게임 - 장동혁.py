def solution(dartResult):
    answer = 0
    
    scores = []
    
    num_reading = False
    
    for i, c in enumerate(dartResult):
        if c.isdigit(): # 숫자라면
            if num_reading: # 이미 숫자를 읽고 있는 중이었다.
                scores[-1] = scores[-1] * 10 + int(c)
            else: # 이번에 맨처음 숫자를 읽은 상황이다.
                num_reading = True
                scores.append(int(c))
        else: # 숫자가 아니라면
            num_reading = False
            if c == 'D':
                scores[-1] = scores[-1] ** 2
            elif c == 'T':
                scores[-1] = scores[-1] ** 3
            elif c == '*':
                scores[-1] = scores[-1] * 2
                if len(scores) >= 2:
                    scores[-2] = scores[-2] * 2
            elif c == '#':
                scores[-1] = -scores[-1]
    print(scores)
    answer = sum(scores)
    
    return answer