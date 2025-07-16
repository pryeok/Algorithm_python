class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # push 기능 구현 (맨 앞에 데이터 넣기)
    def push(self, value):
        new_head = Node(value)             # [3] 을 만들고!
        new_head.next = self.head          # [3] -> [4] 로 만든다음에
        self.head = new_head               # 현재 head의 값을 [3] 으로 바꿔준다.
        return

    # pop 기능 구현 (맨 앞의 데이터 뽑기)
    def pop(self):
        if self.is_empty():  # 만약 비어있다면 에러!
            return "Stack is empty!"
        delete_head = self.head  # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next  # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head  # 그리고 제거할 node 반환

    # peek 기능 구현 (맨 앞의 데이터 보기)
    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.head.data

    # isEmpty 기능 구현 (스택이 비었는지 안 비었는지 여부 반환해주기)
    def is_empty(self):
        return self.head is None

stack = Stack()

stack.push(5)
print(stack.peek())

stack.push(4)
print(stack.peek())

stack.push(3) # 3 -> 4 -> 5
print(stack.peek())

stack.pop() # 4 -> 5
print(stack.peek())

stack.pop() # 5
print(stack.peek())

stack.pop() # stack is empty
print(stack.peek())