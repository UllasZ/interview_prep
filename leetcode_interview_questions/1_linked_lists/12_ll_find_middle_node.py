"""
LL: Find Middle Node ( ** Interview Question)

Implement the find_middle_node method for the LinkedList class.

Note: this LinkedList implementation does not have a length member variable.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

- The method should use a two-pointer approach, where one pointer (slow) moves one node at a time
and the other pointer (fast) moves two nodes at a time.
- When the fast pointer reaches the end of the list or has no next node,
the slow pointer should be at the middle node of the list.
- The method should return the middle node when the number of nodes is odd or
the first node of the second half of the list if the list has an even number of nodes.
- The method should only traverse the linked list once.  In other words, you can only use one loop

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print("\nLinkedList: " + " -> ".join(values))

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node

    def find_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        print(f"\nMiddle Node: {slow_pointer.value}")


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(9)

# find_middle_node
my_linked_list.find_middle_node()


# print_list
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
# print("Length:", my_linked_list.length)
print(f"{'-'*100}")
