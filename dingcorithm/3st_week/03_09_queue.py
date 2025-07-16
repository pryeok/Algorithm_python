

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # enqueue 기능 구현 (맨 뒤에 데이터 추가하기)
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():  # 만약 비어있다면,
            self.head = new_node  # head 에 new_node를
            self.tail = new_node  # tail 에 new_node를 넣어준다.
            return

        self.tail.next = new_node
        self.tail = new_node

    # dequeue 기능 구현 (맨 앞의 데이터 뽑기)
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"        # 만약 비어있다면 에러!

        delete_head = self.head             # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next          # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.

        return delete_head.data             # 그리고 제거할 node 반환

    # peek 기능 구현 (맨 앞의 데이터 보기)
    def peek(self):
        if self.is_empty():
            return "Queue is empty!"

        return self.head.data

    # isEmpty 기능 구현 (큐가 비었는지 안 비었는지 여부 반환해주기)
    def is_empty(self):
        return self.head is None

queue = Queue()

queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())

queue.dequeue()
print(queue.peek())