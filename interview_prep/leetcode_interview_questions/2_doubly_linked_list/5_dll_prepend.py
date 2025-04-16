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

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True


# Instantiate DoublyLinkedList
dll = DoublyLinkedList(1)

# append
dll.append(2)
dll.append(3)
dll.append(4)

# prepend
dll.prepend(0)
dll.prepend(-1)

# print_list
dll.print_list()

print(f"\n{'-'*100}")
# print("Head:", dll.head.value)
# print("Tail:", dll.tail.value)
print("Length:", dll.length)
print(f"{'-'*100}")
