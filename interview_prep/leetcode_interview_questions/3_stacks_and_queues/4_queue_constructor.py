"""
# Queue: Constructor
Create a Queue class that represents a first-in, first-out (FIFO) data structure using a linked list implementation.

The Queue class should contain the following components:
- A Node class, which serves as the building block for the linked list.
- The Node class should have an __init__ method that initializes the following attributes:
    - value: The value of the node.
    - next: A reference to the next node in the list, initialized to None
- The Queue class should have an __init__ method that initializes the queue with a single node, using the given value.

The __init__ method should perform the following tasks:
- Create a new instance of the Node class using the provided value.
- Set the first attribute of the Queue class to point to the new node.
- Set the last attribute of the Queue class to point to the new node.
- Initialize a length attribute for the Queue class, which represents the current number of nodes in the queue, and set it to 1.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        print(f"\n{'-' * 100}")
        print("First:", queue.first.value)
        print("Last:", queue.last.value)
        print("Length:", queue.length)
        print(f"{'-' * 100}")

        values = []
        temp = self.first
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print("\nQueue: " + " -> ".join(values))
        print(f"{'-' * 100}")


# Instantiate Queue
queue = Queue(4)

# print_queue
queue.print_queue()
