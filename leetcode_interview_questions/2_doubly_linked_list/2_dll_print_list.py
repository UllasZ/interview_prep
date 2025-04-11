# LL: Constructor
# You are tasked with implementing a basic data structure: a singly linked list.
# To accomplish this, you will create two classes, Node and LinkedList.
# The Node class will represent an individual node within the linked list,
# while the LinkedList class will manage the overall list structure.

# Your implementation should satisfy the following requirements:
# Create a Node class with the following features:
# A constructor that takes a value as an argument and initializes the value attribute of the node.
# A next attribute, initialized to None, which will store a reference to the next node in the list.

# Create a LinkedList class with the following features:
# A constructor that takes a value as an argument, creates a new Node with that value,
# and initializes the head and tail attributes of the linked list to point to the new node.
# A length attribute, initialized to 1, which represents the current number of nodes in the list.


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        values = ["None"]
        temp = self.head

        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print("\nDoublyLinkedList: " + " ⇄ ".join(values))


# Instantiate DoublyLinkedList
dll = DoublyLinkedList(1)

# print_list
dll.print_list()

print(f"\n{'-'*100}")
print("Head:", dll.head.value)
print("Tail:", dll.tail.value)
print("Length:", dll.length)
print(f"{'-'*100}")
