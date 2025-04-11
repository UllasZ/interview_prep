"""

LL: Remove Duplicates ( ** Interview Question)
You are given a singly linked list that contains integer values, where some of these values may be duplicated.

Note: this linked list class does NOT have a tail which will make this method easier to implement.

- Your task is to implement a method called remove_duplicates() within the LinkedList class that removes
  all duplicate values from the list.
- Your method should not create a new list, but rather modify the existing list in-place, preserving the
  relative order of the nodes.
- You can implement the remove_duplicates() method in two different ways:
    - Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list.
                    You are allowed to use the provided Set data structure in your implementation.
    - Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes
      in the linked list. You are not allowed to use any additional data structures for this implementation.

Here is the method signature you need to implement:
def remove_duplicates(self):

Example:
    Input:
        LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5

    Output:
        LinkedList: 1 -> 2 -> 3 -> 4 -> 5
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

    def remove_duplicates(self):

        values = set()

        prev = None
        curr = self.head

        while curr is not None:
            if curr.value in values:
                prev.next = curr.next
                self.length -= 1
            else:
                values.add(curr.value)
                prev = curr

            curr = curr.next


# Instantiate LinkedList
my_linked_list = LinkedList(1)

# append
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(1)
my_linked_list.append(4)
my_linked_list.append(2)
my_linked_list.append(5)

# print_list
print("\nBefore removing duplicates: ")
my_linked_list.print_list()

# remove duplicates
my_linked_list.remove_duplicates()

# print_list
print("\nAfter removing duplicates: ")
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("length:", my_linked_list.length)
print(f"{'-'*100}")
