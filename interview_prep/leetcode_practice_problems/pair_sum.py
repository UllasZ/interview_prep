def pair_sum(arr, s):
    temp = sorted(arr)[0]
    res = []
    for i in sorted(arr):
        if i + temp == s:
            res.append([temp, i])
    else:
        arr.remove(temp)

    return res


if __name__ == "__main__":
    array = [2, -3, 3, 3, -2]
    _sum = 0
    res = pair_sum(array, _sum)
    print(res)
