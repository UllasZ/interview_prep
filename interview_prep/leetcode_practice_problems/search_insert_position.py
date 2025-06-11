"""
# Search Insert Position
- Given a sorted array of distinct integers and a target value, return the index if the target is found.
- If not, return the index where it would be if it were inserted in order.
- You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

"""


def search_insert_position(nums, k):

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == k:
            return mid
        elif nums[mid] < k:
            start = mid + 1
        else:
            end = mid - 1

    return start


print(search_insert_position([1, 3, 5, 6], 4))
