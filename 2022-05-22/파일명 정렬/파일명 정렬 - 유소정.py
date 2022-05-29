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