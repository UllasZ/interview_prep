class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        values = ["None"]
        temp = self.head

        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")

        if values:
            print("\nDoublyLinkedList: " + " ⇄ ".join(values))
        else:
            print(f"\nDoublyLinkedList: {None}")

    def append(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def get(self, index):

        if index < 0 or index >= self.length:
            return None

        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        print(f"\nValue at index {index} is: {temp.value}")
        return temp

    def pop(self):

        if self.length == 0:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    def pop_first(self):

        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def remove(self, index):

        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = temp.prev = None

        self.length -= 1
        return True


# Instantiate DoublyLinkedList
dll = DoublyLinkedList(1)

# append
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)

# print_list
print("\nBefore Remove")
dll.print_list()

# Remove
dll.remove(3)

# print_list
print("\nAfter Remove")
dll.print_list()

print(f"\n{'-'*100}")
print("Head:", dll.head.value)
print("Tail:", dll.tail.value)
print("Length:", dll.length)
print(f"{'-'*100}")
