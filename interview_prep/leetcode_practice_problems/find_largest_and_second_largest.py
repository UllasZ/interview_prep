

def find_largest(arr):

    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    print("largest: ", largest)


def second_largest(arr):
    largest = second = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    for num in arr:
        if num > second and num != largest:
            second = num

    print("second: ", second)




if __name__ == "__main__":
    array = [1,7,9,8]

    find_largest(arr=array)
    second_largest(arr=array)