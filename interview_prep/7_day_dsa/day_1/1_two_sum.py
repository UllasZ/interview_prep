# 1. Two Sum: Return indices of two numbers that add to target.

def two_sum(n, nums):

    seen = {}
    res = []

    for i in range(len(nums)):

        comp = n - nums[i]
        if comp in seen:
            res.append([seen[comp], i])

        seen[i] = i

    return res


arr = [1,2,3,4,5,6,7,8]
k = 6
print(two_sum(n=k, nums=arr))