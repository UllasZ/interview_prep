"""
# Diagonal Difference:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:
    1 2 3
    4 5 6
    9 8 9
    The left-to-right diagonal = .
    The right-to-left diagonal = .
    Their absolute difference is .
"""


def diagonal_difference(arr):
    print(arr)

    n = len(arr)
    i = 0
    j = n - 1
    left_array = []
    right_array = []

    while i < n:
        left_array.append(arr[i][i])
        right_array.append(arr[j][i])

        i = i + 1
        j = j - 1

    difference = abs(sum(left_array) - sum(right_array))
    return difference


nums = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
print(diagonal_difference(nums))
