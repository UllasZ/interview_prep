"""
#  Rearrange Alternatively
Problem statement
Given an array arr of size N containing positive and negative integers. Arrange the array alternatively such that every non-negative integer is followed by a negative integer and vice-versa.

Note:
The number of positive integers and negative integers may not be equal. In such cases, add the extra integers at the end.
For Example:
For array {4, -9, -2, 6, -8}, the output will be {-9, 4, -2, 6, -8}

For array {1, 2, 3, -5}, the output will be {-5, 1, 2, 3}
"""


def rearrange(arr):
    negative, positive, lis, new_arr = [], [], [], []

    for ele in arr:

        if ele < 0:
            negative.append(ele)
        else:
            positive.append(ele)

    l1 = len(positive)
    l2 = len(negative)

    if l2 < l1:
        negative += [0] * (l1 - l2)

    else:
        positive += [0] * (l2 - l1)

    for i in range(len(positive)):
        lis.append(negative[i])
        lis.append(positive[i])

    for ele in lis:
        if ele != 0:
            new_arr.append(ele)

    return new_arr


array1 = [-1, 2, 2, -5]
array2 = [4, -9, -2, 6, -8]
array3 = [1, 2, 3, -5]

result = rearrange(array1)
print(result)

result = rearrange(array2)
print(result)

result = rearrange(array3)
print(result)
