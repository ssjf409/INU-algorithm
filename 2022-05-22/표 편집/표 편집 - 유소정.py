from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.size = 0

    def size(self):
        return self.size

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        self.size += 1

    # 모든 노드 값
    def print_all(self, n):
        answer = ["X"] * n

        cur = self.head
        while cur is not None:
            answer[cur.data] = "O"
            cur = cur.next

        return answer

    # 인덱스에 맞는 노드 값 찾기
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    # 삽입
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    # 삭제
    def delete_node(self, index):
        self.size -= 1

        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next


def solution(n, k, cmd):
    ll = LinkedList(0)
    trash = deque()  # [idx, data]

    for i in range(1, n):
        ll.append(i)

    for c in cmd:
        c = c.split()

        a = c[0]

        if a == "C":  # 삭제
            val = ll.get_node(k).data  # 값 추출
            ll.delete_node(k)
            trash.append([k, val])

            # 마지막 행 예외처리
            if k == ll.size-1:
                k -= 1

        elif a == "Z":  # 복구
            idx, val = trash.pop()
            ll.add_node(idx, val)

        else:
            b = int(c[1])

            if a == "U":  # 위
                k -= b

            elif a == "D":  # 아래
                k += b

    return "".join(ll.print_all(n))


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))