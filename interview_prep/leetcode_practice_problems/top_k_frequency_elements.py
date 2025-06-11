"""
# Top K Frequent Elements
- Given an integer array nums and an integer k, return the k most frequent elements.
- You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]
"""


def find_top_k_elements(nums, k):

    counter = {}
    i = 0

    while i < len(nums):
        if nums[i] in counter:
            counter[nums[i]] = counter[nums[i]] + 1
        else:
            counter[nums[i]] = 1
        i = i + 1

    counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}

    return list(counter.keys())[::-1][:k]


print(find_top_k_elements(nums=[1, 1, 1, 2, 2, 3], k=2))
print(find_top_k_elements(nums=[-1, -1], k=1))
