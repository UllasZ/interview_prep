"""
- Quick sort's intuition lies in its efficient partitioning of a list around a pivot element.
- This partitioning places smaller elements to the left and larger elements to the right of the pivot.
- By recursively applying this process to the resulting sub-lists, the entire list is sorted.

"""


def quick_sort(nums):

    i = 0
    n = len(input_array) - 1

    divided_array = divide(nums)
    partitioned_array = divided_array[i]

    while i < n:
        partitioned_array = partition(partitioned_array, divided_array[i + 1])
        i = i + 1

    return partitioned_array


def divide(nums):
    i = 0
    result = []
    n = len(nums)

    while i < n:
        temp_array = [nums[i]]
        result.append(temp_array)
        i = i + 1

    return result


def partition(array1, array2):

    i = 0
    pivot = array2[0]
    result = []

    left_array = []
    right_array = []

    while i < len(array1):
        if array1[i] <= pivot:
            left_array.append(array1[i])
        else:
            right_array.append(array1[i])

        i = i + 1

        result = left_array + [pivot] + right_array
    return result


input_array = [7, 5, 8, 4, 9, 1, 3, 6, 2, 2]
print(f"\nInput Array: {input_array}")

res = quick_sort(input_array)
print(f"\nSorted Array: {res}")
