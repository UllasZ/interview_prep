# LL: Reverse
# Implement the reverse method for the LinkedList class.
# The reverse method should reverse the order of the nodes in the linked list
# so that the head becomes the tail and the tail becomes the head.
# The method should not create any new nodes or modify the values of the nodes.
# The method should only update the next attribute of each node to point to the previous node in the list.

# Consider the following requirements while implementing the method:
# The method should handle edge cases, such as an empty list or a list with a single node.
# The method should utilize a temporary variable to swap the head and tail attributes of the LinkedList class.
# The method should use a loop to iterate through the nodes in the list and update the next attribute of each node.
# The method should not modify the length attribute of the LinkedList class.


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
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node

        self.length += 1

    def reverse(self):

        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before

            before = temp
            temp = after


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

# print_list
print("\nBefore")
my_linked_list.print_list()

# reverse
my_linked_list.reverse()

# print_list
print("\nAfter")
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)
print(f"{'-'*100}")
