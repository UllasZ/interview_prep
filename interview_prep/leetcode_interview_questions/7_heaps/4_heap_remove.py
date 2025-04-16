class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (
                left_index < len(self.heap)
                and self.heap[left_index] > self.heap[max_index]
            ):
                max_index = left_index

            if (
                right_index < len(self.heap)
                and self.heap[right_index] > self.heap[max_index]
            ):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def print_heap(self):
        print("\n" + "-" * 100)
        print("Heap: ")
        if not self.heap:
            print(None)
        else:
            print(self.heap)
        print("-" * 100)

    def insert(self, value):

        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(index1=current, index2=self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value


# Instantiate heap
my_heap = MaxHeap()

# insert
my_heap.insert(87)
my_heap.insert(21)
my_heap.insert(90)
my_heap.insert(100)
my_heap.insert(54)
my_heap.insert(120)
my_heap.insert(75)

# print heap
print("Before remove: ")
print(my_heap.print_heap())

# remove
my_heap.remove()

# print heap
print("After remove: ")
print(my_heap.print_heap())
