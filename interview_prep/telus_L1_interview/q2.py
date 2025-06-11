# Given an array containing only 0’s, 1’s, and 2’s, sort it in linear time and using constant space.
# Input:  [ 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0 ]
# Output: [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2 ]


def sort_nums(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


print(sort_nums([0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]))
