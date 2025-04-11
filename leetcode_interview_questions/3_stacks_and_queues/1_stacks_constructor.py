"""
# Stack: Constructor
Create a Stack class that represents a last-in, first-out (LIFO) data structure using a linked list implementation.

The Stack class should contain the following components:
- A Node class, which serves as the building block for the linked list.
- The Node class should have an __init__ method that initializes the following attributes:
    - value: The value of the node.
    - next: A reference to the next node in the list, initialized to None.
- The Stack class should have an __init__ method that initializes the stack with a single node, using the given value.

The __init__ method should perform the following tasks:
- Create a new instance of the Node class using the provided value.
- Set the top attribute of the Stack class to point to the new node.
- Initialize a height attribute for the Stack class, which represents the current number of nodes in the stack, and set it to 1.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        print(f"\n{'-' * 100}")
        print("Top:", stack.top.value)
        print("Height:", stack.height)
        print(f"{'-' * 100}")

        temp = self.top
        print("Stack: ")
        while temp is not None:
            print(f"  {str(temp.value)} \n  ↓ ")
            temp = temp.next
        print(" None")
        print(f"{'-' * 100}")


# Instantiate Stack
stack = Stack(4)

# print_stack
stack.print_stack()
