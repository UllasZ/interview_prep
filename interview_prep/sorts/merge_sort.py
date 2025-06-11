"""
# Merge sort
Steps:
    divide the given array
    merge by sorted the elements
"""


def merge_sort(array):
    divided_array = divide(array)

    merged_array = divided_array[0]
    i = 0

    while i < len(array) - 1:
        merged_array = merge_array(merged_array, divided_array[i + 1])
        i = i + 1

    return merged_array


def divide(array):
    result_array = []
    len_array = len(array)
    idx = 0

    while idx < len_array:
        temp_array = [array[idx]]
        result_array.append(temp_array)
        idx = idx + 1

    return result_array


def merge_array(array_a, array_b):

    i = 0
    j = 0

    len_a = len(array_a)
    len_b = len(array_b)

    result_array = []

    while True:
        if array_a[i] == array_b[j]:
            result_array.append(array_a[i])
            result_array.append(array_b[j])
            i = i + 1
            j = j + 1

        elif array_a[i] < array_b[j]:
            result_array.append(array_a[i])
            i = i + 1

        else:
            result_array.append(array_b[j])
            j = j + 1

        if i == len_a:
            result_array.extend(array_b[j:len_b])
            break

        elif j == len_b:
            result_array.extend(array_a[i:len_a])
            break

    return result_array


input_array = [9, 5, 8, 4, 7, 1, 3, 2, 2]
print(f"\nInput array: {input_array}")

result = merge_sort(input_array)
print(f"\nResult: {result}")
