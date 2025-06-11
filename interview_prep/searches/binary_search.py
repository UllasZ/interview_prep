"""
What Is Binary Search?
- Binary Search is one of the most important algorithms every problem solver must master.
- It's efficient (O(logn)) and super useful for searching in sorted arrays.

Given a sorted list and a target value, binary search:
- Looks at the middle element.
- If it’s the target → done!
- If the target is less, search the left half.
- f the target is greater, search the right half.
- Repeat until found or the search space is empty.
"""


def binary_search(nums, k):
    print(nums)

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == k:
            return mid

        elif nums[mid] > k:
            right = mid - 1
        else:
            left = mid + 1

    return -1


arr = [1, 3, 5, 7, 9, 11]
target = 9
result = binary_search(arr, target)
print("Result: ", result)
