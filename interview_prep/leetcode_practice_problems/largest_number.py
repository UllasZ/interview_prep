"""
# Largest Number
- Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
- Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
    Input: nums = [10,2]
    Output: '210'

Example 2:
    Input: nums = [3,30,34,5,9]
    Output: '9534330'
"""


def largest_number(nums):
    print(f"nums: {nums}")

    res = []
    i = 0
    while i < len(nums):
        j = 0
        string_num = str(nums[i])

        while j < len(string_num):
            res.append(string_num[j])
            j = j + 1
        i = i + 1

    return "".join(sorted(res)[::-1])


print(largest_number(nums=[3, 30, 34, 5, 9]))
