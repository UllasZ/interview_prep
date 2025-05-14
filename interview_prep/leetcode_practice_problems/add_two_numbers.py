"""
# Add Two Numbers
- You are given two non-empty linked lists representing two non-negative integers.
- The digits are stored in reverse order, and each of their nodes contains a single digit.
- Add the two numbers and return the sum as a linked list.
- You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional


# Definition for singly-linked list.


def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

class Solution:

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return  dummy.next



list1 = to_linked_list([2, 4, 3])
list2 = to_linked_list([5, 6, 4])
solution = Solution()
result = solution.add_two_numbers(list1, list2)
print_linked_list(result)  # Output: 7 -> 0 -> 8
