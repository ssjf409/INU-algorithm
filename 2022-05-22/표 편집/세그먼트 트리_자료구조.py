class SegmentTree:
    def __init__(self, source):
        self.n = len(source)
        self.tree = [0] * (4 * self.n)
        self.first_index = 1
        self.__init(source, 0, self.n - 1, self.first_index)
        
    def __init(self, source, start, end, cur_index):
        if start == end:
            self.tree[cur_index] = source[start]
            return self.tree[cur_index]
        mid = (start + end) // 2
        self.tree[cur_index] = self.__init(source, start, mid, cur_index * 2) + self.__init(source, mid + 1, end, cur_index * 2 + 1)
        return self.tree[cur_index]

    def query(self, left, right):
        return self.__query(0, self.n - 1, self.first_index, left, right)

    def __query(self, start, end, cur_index, left, right):
        if left > end or right < start:
            return 0
        
        if left <= start and end <= right:
            return self.tree[cur_index]
        
        mid = (start + end) // 2
        return self.__query(start, mid, cur_index * 2, left, right) \
            + self.__query(mid + 1, end, cur_index * 2 + 1, left, right)

    def update(self, target_index, diff):
        self.__update(0, self.n - 1, self.first_index, target_index, diff)

    def __update(self, start, end, cur_index, tar_index, diff):
        if tar_index < start or tar_index > end:
            return
        
        self.tree[cur_index] += diff
        
        if start == end:
            return
        mid = (start + end) // 2
        self.__update(start, mid, cur_index * 2, tar_index, diff)
        self.__update(mid + 1, end, cur_index * 2 + 1, tar_index, diff)



# source = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]

# sg_tree = SegmentTree(source)

# print(sg_tree.query(0, 1))
# sg_tree.update(1, 2)
# print(sg_tree.query(4, 5))


deleted_count = [1, 2, 3, 4, 5, 6]

sg_tree = SegmentTree(deleted_count)

# sg_tree.update(2, 1)
print(sg_tree.query(1, 4))



#===================

# class SegmentTree:
#     def __init__(self, source):
#         self.n = len(source)
#         self.tree = [0] * (4 * self.n)
#         self.first_index = 1
#         self.__init(source, 0, self.n - 1, self.first_index)
        
#     def __init(self, source, start, end, cur_index):
#         if start == end:
#             self.tree[cur_index] = source[start]
#             return self.tree[cur_index]
#         mid = (start + end) // 2
#         self.tree[cur_index] = self.__init(source, start, mid, cur_index * 2) + self.__init(source, mid + 1, end, cur_index * 2 + 1)
#         return self.tree[cur_index]

#     def query(self, start, end, cur_index, left, right):
#         if left > end or right < start:
#             return 0
        
#         if left <= start and end <= right:
#             return self.tree[cur_index]
        
#         mid = (start + end) // 2
#         return self.query(start, mid, cur_index * 2, left, right) \
#             + self.query(mid + 1, end, cur_index * 2, left, right)

#     def update(self, start, end, cur_index, tar_index, diff):
#         if tar_index < start or tar_index > end:
#             return
        
#         self.tree[cur_index] += diff
        
#         if start == end:
#             return
#         mid = (start + end) // 2
#         self.update(start, mid, cur_index * 2, tar_index, diff)
#         self.update(mid + 1, end, cur_index * 2 + 1, tar_index, diff)

