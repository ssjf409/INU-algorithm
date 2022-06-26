board = input()

cnt = 0

output = ""
canDivide = True

for c in board:
    if c == 'X':
        cnt += 1
        continue
    
    if cnt == 0:
        output += '.'
        continue

    if cnt % 2 != 0:
        canDivide = False
        break
    
    output += 'A' * (cnt // 4) * 4 + 'B' * (cnt % 4 // 2) * 2
    
    cnt = 0
    output += '.'

if cnt % 2 != 0:
    canDivide = False
else:
    output += 'A' * (cnt // 4) * 4 + 'B' * (cnt % 4 // 2) * 2

if canDivide:
    print(output)
else:
    print(-1)
