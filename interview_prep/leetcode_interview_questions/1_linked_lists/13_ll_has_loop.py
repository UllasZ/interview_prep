"""

LL: Has Loop ( ** Interview Question)
- Write a method called has_loop that is part of the linked list class.
- The method should be able to detect if there is a cycle or loop present in the linked list.
- You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.
- This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time,
while the fast pointer moves two steps at a time. If there is a loop in the linked list, the two pointers will
eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.

The method should follow these guidelines:
- Create two pointers, slow and fast, both initially pointing to the head of the linked list.
- Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.
- If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.
- If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.

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

    def has_loop(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer is not None and fast_pointer.next is not None:

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            print(f"has_loop: {True}")
        else:
            print(f"has_loop: {False}")


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(9)

# has_loop
my_linked_list.has_loop()


# print_list
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
# print("Length:", my_linked_list.length)
print(f"{'-'*100}")
