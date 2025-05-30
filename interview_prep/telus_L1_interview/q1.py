
# Given an array of numbers, create a function that removes 25% from every number in the array except the smallest number,
# and adds the total amount removed to the smallest number.  O(n) is preferred
# showTheLove([4, 1, 4]) ➞ [3, 3, 3]
# showTheLove([16, 10, 8]) ➞ [12, 7.5, 14.5]
# showTheLove([2, 100]) ➞ [27, 75]


def showTheLove(nums):

    # return if null
    if not nums:
        return []


    # smallest = min(nums)
    smallest = nums[0]
    total_removed = 0
    smallest_index = 0
    res = []


    # iterate nums and reduce
    for idx, num in enumerate(nums):

        if num < smallest:
            smallest = num
            smallest_index = idx

        removed = num * 0.25
        total_removed += removed
        res.append(num - removed)

    res[smallest_index] += total_removed

    print(res)
    return res


showTheLove([16, 10, 8])