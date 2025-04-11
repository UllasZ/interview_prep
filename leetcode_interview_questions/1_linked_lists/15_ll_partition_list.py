"""
LL: Partition List ( ** Interview Question)
⚠️ CAUTION: Advanced Challenge Ahead!

    - This Linked List problem is significantly more challenging than the ones we've tackled so far.

    - It's common for students at this stage to find this exercise demanding, so don't worry if you're not ready to tackle it yet.

    - It's perfectly okay to set it aside and revisit it later when you feel more confident.

    - If you decide to take on this challenge, I strongly advise using a hands-on approach: grab a piece of paper and visually map out each step.

    - This problem requires a clear understanding of how elements in a Linked List interact and move.

    - By now, you've observed numerous Linked List animations in the course, which have prepared you for this moment.

    - This exercise will be a true test of your ability to apply those concepts practically.

    - Remember, patience and persistence are key here!

Now, here is the exercise:
------------------------------------------------------------------
Implement the partition_list member function for the LinkedList class,
which partitions the list such that all nodes with values less than x come before nodes with
values greater than or equal to x.

Note:
    - This linked list class does NOT have a tail which will make this method easier to implement.
    - The original relative order of the nodes should be preserved.

Details:
    - The function partition_list takes an integer x as a parameter and
      modifies the current linked list in place according to the specified criteria.
    - If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.

------------------------------------------------------------------
Example 1:
    Input:
        Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5

    Process:
        Values less than 5: 3, 2, 1
        Values greater than or equal to 5: 8, 5, 10

    Output:
        Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10
------------------------------------------------------------------

------------------------------------------------------------------
Example 2:

    Input:
        Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3

    Process:
        Values less than 3: 1, 2, 2
        Values greater than or equal to 3: 4, 3, 5

    Output:
        Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5
------------------------------------------------------------------

Tips:
    - While traversing the linked list, maintain two separate chains: one for values less than x and
      one for values greater than or equal to x.

    - Use dummy nodes to simplify the handling of the heads of these chains.

    - After processing the entire list, connect the two chains to get the desired arrangement.

Note:
    - The solution must maintain the relative order of nodes.

    - For instance, in the first example, even though 8 appears before 5 in the original list,
      the partitioned list must still have 8 before 5 as their relative order remains unchanged.

    - You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes
      (i.e., only the nodes' next pointers may be changed.)

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
