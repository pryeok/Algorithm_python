

class MaxHeap:
    def __init__(self):
        self.items = [None]

    #  0   1 2 3      0   1 2 3
    # None 3 4 2  -> None 4 3 2

    def insert(self, value):

        self.items.append(value)

        cur_index = len(self.items) - 1
        print(cur_index)

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2 # parent index를 잡아주는 것이 포인트!!
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
                print("cur_index : ", cur_index)
            else:
                break

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!