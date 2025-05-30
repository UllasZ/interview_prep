"""
# 5. Product of Array Except Self
Problem: Return array where each element is product of all others.
Input: [1,2,3,4] → Output: [24,12,8,6]
Constraints: O(n) time and O(1) extra space (excluding output array)
"""

def find_product_of_array(nums):

    print(nums)

    prod, left_prod_array, right_prod_array = [], [1], [1]
    left_prod, right_prod = 1, 1
    n = len(nums)

    for i in range(1, n):
        left_prod *= nums[i -1]
        left_prod_array.append(left_prod)

        right_prod *= nums[n - i]
        right_prod_array.append(right_prod)

    right_prod_array = right_prod_array[::-1]

    for i in range(n):
        prod.append(left_prod_array[i] * right_prod_array[i])

    return prod


print(find_product_of_array(nums=[1,2,3,4]))