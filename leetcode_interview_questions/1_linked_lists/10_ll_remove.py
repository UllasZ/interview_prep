# LL: Remove
# Implement the remove method for the LinkedList class.
# The remove method should take an integer index as a parameter
# and remove the node at the specified index in the linked list, returning the removed node.
# If the index is out of bounds, the method should return None.

# Keep in mind the following requirements:
# The method should handle edge cases, such as removing a node at the beginning or end of the list.
# The method should utilize the pop_first() and pop() methods for handling these edge cases.
# The method should use the get() method to find the node previous to the one to be removed.
# The method should update the next attribute of the previous node to point to the node after the removed one.
# The method should decrement the length attribute of the LinkedList class.
# The method should return the removed node if the removal is successful.
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

    def pop(self):
        if self.length == 0:
            print("Popped value:", None)

        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        print("Popped value:", temp.value)

    def pop_first(self):
        if self.length == 0:
            print("\nPop First value:", None)

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        print("\nPop First value:", temp.value)

    def get(self, index):

        if index < 0 or index >= self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp

    def remove(self, index):

        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return True


# Instantiate LinkedList
my_linked_list = LinkedList(4)

# append
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

# remove
my_linked_list.remove(2)

# print_list
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)
print(f"{'-'*100}")
