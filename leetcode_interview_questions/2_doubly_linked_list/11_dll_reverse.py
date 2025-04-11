"""

DLL: Reverse ( ** Interview Question)
Create a new method called reverse that reverses the order of the nodes in the list,
i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.
To do this, you'll need to traverse the list and change the direction of the pointers
between the nodes so that they point in the opposite direction.
Do not change the value of any of the nodes.
Once you've done this for all nodes,
you'll also need to update the head and tail pointers to reflect the new order of the nodes.

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

    def reverse(self):

        current = self.head

        while current.next:

            temp_next = current.next
            current.next = current.next
            current.prev = temp_next
            current = temp_next

        self.head, self.tail = self.tail, self.head


# Instantiate DoublyLinkedList
dll = DoublyLinkedList(1)

# append
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)

# print_list
print("\nBefore reverse")
dll.print_list()

# reverse
dll.reverse()

# print_list
print("\nAfter reverse")
dll.print_list()

print(f"\n{'-'*100}")
print("Head:", dll.head.value)
print("Tail:", dll.tail.value)
print("Length:", dll.length)
print(f"{'-'*100}")
