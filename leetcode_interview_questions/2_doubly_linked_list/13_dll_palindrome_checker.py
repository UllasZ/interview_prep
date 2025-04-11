"""
DLL: Palindrome Checker ( ** Interview Question)
Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

For example, if the list contains the values [1, 2, 3, 2, 1],
then the method should return True, since the list is a palindrome.

If the list contains the values [1, 2, 3, 4, 5],
then the method should return False, since the list is not a palindrome.

Method name:
is_palindrome
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

    def is_palindrome(self):

        values = []
        while self.head is not None:
            values.append(self.head.value)
            self.head = self.head.next

        return values == values[::-1]


# Instantiate DoublyLinkedList
dll = DoublyLinkedList(1)

# append
dll.append(2)
dll.append(3)
dll.append(3)
dll.append(2)
dll.append(1)

# print_list
dll.print_list()

# is_palindrome
print("Is palindrome: ", dll.is_palindrome())

print(f"\n{'-'*100}")
# print("Head:", dll.head.value)
# print("Tail:", dll.tail.value)
# print("Length:", dll.length)
print(f"{'-'*100}")
