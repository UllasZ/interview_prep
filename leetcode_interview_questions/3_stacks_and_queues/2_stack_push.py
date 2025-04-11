"""
# Stack:Push
Implement the push method for the Stack class that adds a new node with a given value to the top of the stack.

The method should perform the following tasks:
- Create a new instance of the Node class using the provided value.
- Set the next attribute of the new node to point to the current top node.
- Update the top attribute of the Stack class to point to the new node.
- Increment the height attribute of the Stack class by 1.
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

    def push(self, value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1
        return True


# Instantiate Stack
stack = Stack(2)

# push
stack.push(1)

# print_stack
stack.print_stack()
