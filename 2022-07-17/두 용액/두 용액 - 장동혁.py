N = int(input())
inputs = list(map(int, input().strip().split(' ')))

acid = []
alkali = []

for num in inputs:
    if num < 0:
        alkali.append(num)
    else:
        acid.append(num)

acid.sort()
alkali.sort(reverse=True)
inputs.clear()


if len(acid) == 0:
    print(alkali[1], alkali[0])
elif len(alkali) == 0:
    print(acid[0], acid[1])
else:
    min_diff = float('inf')
    min_diff_left = -float('inf')
    min_diff_right = float('inf')
    
    len_acid = len(acid)
    len_alkali = len(alkali)
    index_acid = 0
    index_alkali = 0

    if len_acid >= 2:
        temp_diff = abs(acid[0] + acid[1])
        if temp_diff < min_diff:
            min_diff = temp_diff
            min_diff_left = acid[0]
            min_diff_right = acid[1]

    if len_alkali >= 2:
        temp_diff = abs(alkali[0] + alkali[1])
        if temp_diff < min_diff:
            min_diff = temp_diff
            min_diff_left = alkali[1]
            min_diff_right = alkali[0]


    while index_acid < len_acid and index_alkali < len_alkali:
        cur_acid = acid[index_acid]
        cur_alkali = alkali[index_alkali]

        diff = cur_acid + cur_alkali
        abs_diff = abs(diff)

        if abs_diff < min_diff:
            min_diff = abs_diff
            min_diff_left = cur_alkali
            min_diff_right = cur_acid
            
        
        if diff == 0:
            index_acid += 1
            index_alkali += 1
        elif diff < 0:
            index_acid += 1
        else:
            index_alkali += 1
    
    print(min_diff_left, min_diff_right)


'''
4
7 6 -2 -1
-> -2 -1
'''
    

