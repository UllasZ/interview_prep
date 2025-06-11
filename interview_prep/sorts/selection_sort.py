"""
- Selection Sort works by repeatedly finding the smallest (or largest) element from the unsorted part of an array
  and swapping it with the first element of the unsorted part.
- This process expands the sorted portion of the array with each iteration, ultimately leading to a fully sorted array
"""


def selection_sort(array):

    i = 1

    while i < len(array):
        min_index = 0
        print(f"\ncurrent: {i} | min_index: {min_index}")
        min_index = find_min_index(min_index, array[i + 1 :])

        if i != min_index:
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp
            min_index = 0

        print(array)
        i = i + 1

    return array


def find_min_index(min_index, nums):
    i = 0
    while i < len(nums):
        if nums[i] < nums[min_index]:
            min_index = i
        i = i + 1

    return min_index


# input_array = [9, 5, 8, 4, 7, 1, 3, 2, 2]
input_array = [4, 2, 6, 5, 1, 3]

print(f"Input array: {input_array}")

result = selection_sort(array=input_array)
print(f"Result array: {result}")
