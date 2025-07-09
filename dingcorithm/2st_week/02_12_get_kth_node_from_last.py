class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_kth_node_from_last(self, k):
        cur = self.head
        prev = 0

        while cur.next is not None:
            prev = cur
            cur = cur.next

        return prev


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(5)
linked_list.print_all()

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!