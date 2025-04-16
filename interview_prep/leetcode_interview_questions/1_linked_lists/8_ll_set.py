# LL: Set
# Implement the set_value method for the LinkedList class.
# The set_value method should take an integer index and a value as parameters
# and update the value of the node at the specified index in the linked list.
# If the index is out of bounds, the method should return False.
# If the value is successfully updated, the method should return True.

# Keep in mind the following requirements:
# The method should utilize the get method to find the node at the specified index.
# The method should update the value of the node if the node is found.
# The method should return True if the value is successfully updated.
# If the node is not found (i.e., the index is out of bounds), the method should return False.


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

        return temp

    def set_value(self, index, value):

        if index < 0 or index >= self.length:
            return False

        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

# get
get = my_linked_list.get(1)
print("\nget: ", get.value)

# set5_10
set_value5_10 = my_linked_list.set_value(5, 10)
print("\nset_value5_10: ", set_value5_10)

# set1_10
set_value1_10 = my_linked_list.set_value(3, 10)
print("\nset_value1_10: ", set_value1_10)

# print_list
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)
print(f"{'-'*100}")
