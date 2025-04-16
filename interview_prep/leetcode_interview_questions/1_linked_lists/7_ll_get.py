# LL: Get
# Implement the get method for the LinkedList class.
# The get method should take an integer index as a parameter
# and return a pointer to the node at the specified index in the linked list.
# If the index is out of bounds (less than 0 or greater than or equal to the length of the list),
# the method should return None.

# Keep in mind the following requirements:
# The method should handle the cases where the index is out of bounds.
# The method should start at the head of the list and traverse the list using the next attribute of the nodes.
# The method should stop traversing the list when it reaches the specified index and return the node at that position.
# If the index is out of bounds, the method should return None.


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

    def get(self, index):

        if index < 0 or index >= self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp.value


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

# get
get5 = my_linked_list.get(5)
print("\nget5: ", get5)

get1 = my_linked_list.get(1)
print("\nget1: ", get1)

# print_list
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)
print(f"{'-'*100}")
