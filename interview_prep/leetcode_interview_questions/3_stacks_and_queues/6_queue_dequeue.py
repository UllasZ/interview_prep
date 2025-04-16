"""
# Queue: Dequeue

Implement the dequeue method for the Queue class that removes the first node from the queue and returns it.

The method should perform the following tasks:
- If the queue is empty (i.e., the length is 0), return None.
- Store a reference to the current first node in a temporary variable, temp.
- If the queue has only one node (i.e., the length is 1), set both the first and last attributes of the Queue class to None.
- If the queue has more than one node, perform the following steps:
    - Update the first attribute of the Queue class to point to the next node in the queue.
    - Set the next attribute of the removed node (stored in the temporary variable) to None.
    - Decrement the length attribute of the Queue class by 1.
    - Return the removed node (stored in the temporary variable).
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

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first

        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            temp.next = None
            self.length -= 1

        return temp


# Instantiate Queue
queue = Queue(1)

# enqueue
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

# print_queue
print("\nBefore Dequeue")
queue.print_queue()

#  dequeue
queue.dequeue()
queue.dequeue()

# print_queue
print("\nAfter Dequeue")
queue.print_queue()
