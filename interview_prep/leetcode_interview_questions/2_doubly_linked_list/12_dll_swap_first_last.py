"""
DLL: Swap First and Last ( ** Interview Question)
Swap the values of the first and last node

Method name:
swap_first_last

Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.

"""


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

    def swap_first_last(self):

        if self.length == 0:
            return None

        self.head.value, self.tail.value = self.tail.value, self.head.value


# Instantiate DoublyLinkedList
dll = DoublyLinkedList(1)

# append
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)

# print_list
print("\nBefore swap")
dll.print_list()

# swap_first_last
dll.swap_first_last()

# print_list
print("\nAfter swap")
dll.print_list()

print(f"\n{'-'*100}")
print("Head:", dll.head.value)
print("Tail:", dll.tail.value)
print("Length:", dll.length)
print(f"{'-'*100}")
