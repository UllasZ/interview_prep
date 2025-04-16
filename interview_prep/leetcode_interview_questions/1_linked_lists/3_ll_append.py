# LL: Append
# Implement the append method for the LinkedList class.
# The append method should add a new node with a given value to the end of the linked list,
# updating the tail attribute and the length attribute accordingly.

# Keep in mind the following requirements:
# The method should handle the cases where the list is empty and where the list already has one or more nodes.
# The method should create a new node with the given value and add it to the end of the list.
# The method should update the tail attribute of the LinkedList correctly.
# The method should update the length attribute of the LinkedList to reflect the addition of the new node.


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


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

# print_list
my_linked_list.print_list()

print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)
print(f"{'-'*100}")
