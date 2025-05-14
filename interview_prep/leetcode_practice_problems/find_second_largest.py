def find_largest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


def find_second_largest(nums):

    largest = -1
    second_largest = -1

    for num in nums:

        if num > largest:
            second_largest = largest
            largest = num

        elif largest > num > second_largest:
            second_largest = num

    return second_largest


def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def find_kth_largest(k, nums):
    if 1 < k > len(nums):
        return None

    bubble_sort(nums)
    return nums[k - 1]


array = [4,2,6,86,22,34,43]
print("Largest:", find_largest(nums=array))
print("Second Largest:", find_second_largest(nums=array))
print("Kth Largest:", find_kth_largest(k=4, nums=array))
