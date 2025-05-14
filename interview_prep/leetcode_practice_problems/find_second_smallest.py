def find_smallest(nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    return smallest

def find_second_smallest(nums):

    smallest = float('inf')
    second_smallest = float('inf')

    for num in nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num


        elif smallest < num < second_smallest:
            second_smallest = num

    return second_smallest


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def find_kth_smallest(k, nums):

    if 1 < k > len(nums):
        return None

    bubble_sort(nums)
    return nums[k - 1]

array = [4,2,6,86,22,34,43]
print("Smallest:", find_smallest(nums=array))
print("Second Smallest:", find_second_smallest(nums=array))
print("Kth Smallest:", find_kth_smallest(k=4, nums=array))
