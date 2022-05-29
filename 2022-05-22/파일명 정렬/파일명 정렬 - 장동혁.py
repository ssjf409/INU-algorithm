def solution(files):
    answer = []
    
    # element : [head, number, tail]
    parsed_files = []
    
    for file in files:
        head = ""
        number = ""
        tail = ""

        for i, c in enumerate(file):
            if c.isdigit():
                if len(head) != 0: # number 위치에 해당하는 글자를 읽은 상태다.
                    number += c
            else:
                if len(number) == 0: # head 위치를 읽고 있었음.
                    head += c
                else:
                    tail = file[i:]
                    break
        
        print(head, number, tail)
        
        parsed_files.append([head, number, tail])
        sorted_files = sorted(parsed_files, key=lambda x: (x[0].lower(), int(x[1])))
    
    for file in sorted_files:
        answer.append("".join(file))
    
    
    return answer