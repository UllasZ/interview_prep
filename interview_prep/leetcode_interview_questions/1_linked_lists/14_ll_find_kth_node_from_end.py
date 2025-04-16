"""

LL: Find Kth Node From End ( ** Interview Question)
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

Given this LinkedList:
1 -> 2 -> 3 -> 4

- If k=1 then return the first node from the end (the last node) which contains the value of 4.
- If k=2 then return the second node from the end which contains the value of 3, etc.
- If the index is out of bounds, the program should return None.

The find_kth_from_end function should follow these requirements:

- The function should utilize two pointers, slow and fast, initialized to the head of the linked list.
- The fast pointer should move k nodes ahead in the list.
- If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
- The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
- The function should return the slow pointer, which will be at the k-th position from the end of the list.

This is a separate function that is not a method within the LinkedList class.
This means you need to indent the function all the way to the LEFT.

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
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_node_from_end(linked_list, k):
    slow_pointer = linked_list.head
    fast_pointer = linked_list.head

    for _ in range(k):

        if fast_pointer is None:
            return None

        fast_pointer = fast_pointer.next

    while fast_pointer is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return slow_pointer


# Instantiate LinkedList
my_linked_list = LinkedList(1)

# append
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

# find_kth_node_from_end
k = 3
result = find_kth_node_from_end(my_linked_list, k)

if result is not None:
    result = result.value

print(f"\nkth node from end is: {result}")


# print_list
my_linked_list.print_list()


print(f"\n{'-'*100}")
print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print(f"{'-'*100}")
