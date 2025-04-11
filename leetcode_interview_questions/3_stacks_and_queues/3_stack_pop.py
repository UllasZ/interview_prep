"""
# Stack:Pop
Implement the pop method for the Stack class that removes the top node from the stack and returns it.

The method should perform the following tasks:
- If the stack is empty (i.e., the height is 0), return None.
- Store a reference to the current top node in a temporary variable, temp.
- Update the top attribute of the Stack class to point to the next node in the stack.
- Set the next attribute of the removed node (stored in the temporary variable) to None.
- Decrement the height attribute of the Stack class by 1.
- Return the removed node (stored in the temporary variable).
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

    def pop(self):

        if self.height == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None

        self.height -= 1
        return temp


# Instantiate Stack
stack = Stack(1)

# push
stack.push(2)

# print_stack
print("Before pop: ")
stack.print_stack()

# pop
stack.pop()

# print_stack
print("After pop: ")
stack.print_stack()
