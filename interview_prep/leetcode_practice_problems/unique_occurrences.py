"""
# Find the Difference of Two Arrays
Hint: Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

from collections import Counter


def unique_occurrences(arr):

    counter = dict(Counter(arr))

    print(counter.values())

    if len(counter.values()) == len(set(counter.values())):
        return True
    return False


if __name__ == "__main__":
    array = [1, 2, 2, 1, 1, 3]

    res = unique_occurrences(array)
    print(res)
