"""
# HT: Item In Common ( ** Interview Question)
- Write a function item_in_common(list1, list2) that takes two lists as input
  and returns True if there is at least one common item between the two lists, False otherwise.
- Use a dictionary to solve the problem that creates an O(n) time complexity.
"""


# Solution method 1 - O(n**2)
def items_in_common1(list1, list2):
    for i in list1:
        for j in list2:
            if j in list1:
                if i == j:
                    return True
    return False


# Solution method 2 (Better and preferred way)- O(n)
def items_in_common2(list1, list2):
    my_dict = {i: True for i in list1}

    for i in list2:
        if i in my_dict:
            return True
    return False


l1 = [1, 3, 5]
l2 = [2, 4, 5]
result1 = items_in_common1(l1, l2)
print("\nMethod 1: ", result1)

l1 = [1, 3, 5]
l2 = [2, 4, 6]
result2 = items_in_common2(l1, l2)
print("\nMethod 2: ", result2)
