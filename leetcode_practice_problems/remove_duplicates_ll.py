"""
# Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
Return the linked list sorted as well.
"""

from collections import Counter


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

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
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def remove_duplicates_2(self):

        if not self.head or not self.head.next:
            return

        values = []
        curr = self.head

        while curr is not None:
            values.append(curr.value)
            curr = curr.next

        counter = Counter(values)

        dummy = Node(0)
        dummy.next = self.head
        prev, curr = dummy, self.head

        while curr:
            if counter[curr.value] > 1:  # If a value appears more than once, skip it
                prev.next = curr.next
            else:
                prev = curr  # Move prev forward only if current node is unique
            curr = curr.next

        self.head = dummy.next
        self.tail = prev if prev else None

        temp = self.head
        new_length = 0
        while temp:
            new_length += 1
            temp = temp.next
        self.length = new_length


# Instantiate LinkedList
my_linked_list = LinkedList(1)

# append
my_linked_list.append(2)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(4)
my_linked_list.append(5)

# print_list
print("\nBefore removing duplicates: ")
my_linked_list.print_list()

# remove duplicates
my_linked_list.remove_duplicates_2()

# print_list
print("\nAfter removing duplicates: ")
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("length:", my_linked_list.length)
print(f"{'-'*100}")
