# LL: Pop First
# Implement the pop_first method for the LinkedList class.
# The pop_first method should remove the first node (the head) from the linked list,
# update the head attribute and the length attribute accordingly, and return the removed node.

# Keep in mind the following requirements:
# The method should handle the cases where the list is empty and where the list has one or more nodes.
# The method should save a reference to the current head node before updating the head attribute.
# The method should update the head attribute to the second node in the list.
# The method should disconnect the removed node from the list by setting its next attribute to None.
# The method should update the length attribute of the LinkedList to reflect the removal of the node.
# If the list becomes empty after removing the node, the method should set the tail attribute of the LinkedList to None.
# The method should return the removed node, or None if the list is empty.


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

    def pop_first(self):
        if self.length == 0:
            print("\nPop First value:", None)

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        print("\nPop First value:", temp.value)


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

# pop_first
my_linked_list.pop_first()

# print_list
my_linked_list.print_list()

print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)
print(f"{'-'*100}")
