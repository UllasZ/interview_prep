"""
# Find the Difference of Two Arrays
Hint: Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""


def find_difference(nums1, nums2):

    return [
        [i for i in sorted(set(nums1)) if i in nums2],
        [i for i in sorted(set(nums2)) if i in nums1],
    ]


if __name__ == "__main__":
    n1 = [1, 2, 3]
    n2 = [2, 4, 6]

    res = find_difference(n1, n2)
    print(res)
