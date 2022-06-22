boards = list(input())
# print(boards)
cnt = 0
answer = ''
for i in range(len(boards)):
    if boards[i] == 'X':
        cnt += 1
    elif boards[i] == '.':
        if cnt == 0:
            answer += '.'
            continue
        if cnt % 2:
            answer = -1
            break
        else:
            a_cnt = cnt // 4
            b_cnt = (cnt % 4) // 2
            answer += ('AAAA' * a_cnt + 'BB' * b_cnt + '.')
            cnt = 0
if cnt % 2:
    answer = -1
else:
    a_cnt = cnt // 4
    b_cnt = (cnt % 4) // 2
    answer += ('AAAA' * a_cnt + 'BB' * b_cnt)

#i == 0 or boards[i-1] == '.'
    
print(answer)

