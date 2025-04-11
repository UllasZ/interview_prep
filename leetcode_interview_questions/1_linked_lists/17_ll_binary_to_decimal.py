"""
LL: Binary to Decimal ( ** Interview Question)

- Your task is to implement the binary_to_decimal method for the LinkedList class.
- This method should convert a binary number, represented as a linked list, to its decimal equivalent.
- In this context, a binary number is a sequence of 0s and 1s.
- The LinkedList class represents this binary number such that each node in the linked list
  contains a single digit (0 or 1) of the binary number, and the whole number is formed by traversing the linked list
  from the head to the end.
- The binary_to_decimal method should start from the head of the linked list and
  use each node's value to calculate the corresponding decimal number.

The formula to convert a binary number to decimal is as follows:
    - To put it in simple terms, each digit of the binary number is multiplied by 2 raised to the power
      equivalent to the position of the digit, counting from right to left starting from 0,
      and all the results are summed together to get the decimal number.
    - The binary_to_decimal method should return this calculated decimal number.

Examples:
    - Consider the binary number 101. If this number is represented as a linked list,
      the head of the linked list will contain the digit 1, the next node will contain 0, and the last node will contain 1.
      When we apply the binary_to_decimal method on this linked list, the method should return the number 5,
      which is the decimal equivalent of binary 101.

    - Similarly, for a linked list representing the binary number 1101, the binary_to_decimal method should return the number 13.
"""


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
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def binary_to_decimal(self):
        num = 0
        curr = self.head

        while curr is not None:
            num = num * 2 + curr.value
            curr = curr.next

        print(f"\nThe decimal value is {num}")


# Instantiate LinkedList
my_linked_list = LinkedList(1)

# append
my_linked_list.append(1)
my_linked_list.append(0)
my_linked_list.append(1)

# print_list)
my_linked_list.print_list()

# binary_to_decimal
my_linked_list.binary_to_decimal()

print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("length:", my_linked_list.length)
print(f"{'-'*100}")
