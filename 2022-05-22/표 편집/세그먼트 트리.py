def init(start, end, cur_index):
    if start == end:
        tree[cur_index] = source[start]
        return tree[cur_index]
    mid = (start + end) // 2
    tree[cur_index] = init(start, mid, cur_index * 2) + init(mid + 1, end, cur_index * 2 + 1)
    return tree[cur_index]

def query(start, end, cur_index, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[cur_index]
    
    mid = (start + end) // 2
    return query(start, mid, cur_index * 2, left, right) \
        + query(mid + 1, end, cur_index * 2 + 1, left, right)

def update(start, end, cur_index, tar_index, diff):
    if tar_index < start or tar_index > end:
        return
    
    tree[cur_index] += diff
    
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, cur_index * 2, tar_index, diff)
    update(mid + 1, end, cur_index * 2 + 1, tar_index, diff)


source = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
len_source = len(source)
tree = [0] * (4 * len_source)


init(0, len_source - 1, 1)
print(query(0, len_source - 1, 1, 0, 12))
print(query(0, len_source - 1, 1, 0, 1))
update(0, len_source - 1, 1, 1, 2)
print(query(0, len_source - 1, 1, 0, 1))