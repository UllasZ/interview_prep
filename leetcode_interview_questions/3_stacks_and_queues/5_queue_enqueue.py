"""
# Queue:Enqueue
Implement the enqueue method for the Queue class that adds a new node with a given value to the end of the queue.

The method should perform the following tasks:
- Create a new instance of the Node class using the provided value.
- If the queue is empty (i.e., self.first is None),
  set the first and last attributes of the Queue class to point to the new node.
- If the queue is not empty, perform the following steps:
    - Set the next attribute of the current last node to point to the new node.
    - Update the last attribute of the Queue class to point to the new node.
    - Increment the length attribute of the Queue class by 1.
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
        print(f"{'-' * 100}")
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
        print("Queue: " + " -> ".join(values))
        print(f"{'-' * 100}")

    def enqueue(self, value):

        new_node = Node(value)

        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return self.last


# Instantiate Queue
queue = Queue(1)

# print_queue
print("\nBefore Enqueue")
queue.print_queue()

# enqueue
queue.enqueue(2)

# print_queue
print("\nAfter Enqueue")
queue.print_queue()
