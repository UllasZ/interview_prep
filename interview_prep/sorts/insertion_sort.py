# Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list
# into its correct position in a sorted portion of the list.


def insertion_sort(array):

    result_array = []
    for key in array:

        i = len(result_array)
        result_array.append(key)

        while i != 0:
            if result_array[i - 1] > key:
                temp = result_array[i]
                result_array[i] = result_array[i - 1]
                result_array[i - 1] = temp

            i = i - 1

    return result_array


input_array = [9, 5, 8, 4, 7, 1, 3, 2, 2]
print(f"Input array: {input_array}")

result = insertion_sort(array=input_array)
print(f"Result array: {result}")
