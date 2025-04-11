# LL: Insert
# Implement the insert method for the LinkedList class.
# Method signature: def insert(self, index, value):
# The insert method should take an integer index
# and a value as parameters and insert a new node with the given value at the specified index in the linked list.
# If the index is out of bounds, the method should return False.
# If the new node is successfully inserted, the method should return True.

# Keep in mind the following requirements:
# The method should handle edge cases, such as inserting a new node at the beginning or end of the list.
# The method should utilize the prepend, append, and get methods for handling these edge cases.
# The method should create a new node with the given value and insert it at the specified index.
# The method should update the next attribute of the previous node to point to the new node.
# The method should increment the length attribute of the LinkedList class.
# The method should return True if the new node is successfully inserted.
# If the index is out of bounds, the method should return False.


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

    def get(self, index):

        if index < 0 or index >= self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp

    def insert(self, index, value):

        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

# insert
my_linked_list.insert(1, 20)

# print_list
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)
print(f"{'-'*100}")
