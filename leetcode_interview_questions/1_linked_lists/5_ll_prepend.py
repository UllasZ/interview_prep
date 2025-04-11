# LL: Prepend
# Implement the prepend method for the LinkedList class.
# The prepend method should add a new node with a given value to the beginning of the linked list,
# updating the head attribute and the length attribute accordingly.

# Keep in mind the following requirements:
# The method should handle the cases where the list is empty and where the list already has one or more nodes.
# The method should create a new node with the given value and add it to the beginning of the list.
# The method should update the head attribute of the LinkedList correctly.
# The method should update the length attribute of the LinkedList to reflect the addition of the new node.
# The method should return True if the operation is successful.


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

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        print("\nPrepend success:", True)


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

# prepend
my_linked_list.prepend(10)

# print_list
my_linked_list.print_list()

print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)
print(f"{'-'*100}")
