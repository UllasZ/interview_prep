array = [1, 4, 2, -2, -9, 10, 2, 12, 2, -4, -4, -4, -4, 2, 6, 7]
peak = array[0]
index = 0
output = []

for x in range(1, len(array) - 1):
    if array[x] * array[x - 1] > 0:
        if peak < 0 and array[x] < peak:
            peak = array[x]
            index = x
            continue

        if peak >= 0 and array[x] > peak:
            peak = array[x]
            index = x
            continue
    else:
        output.insert(index, (index, peak))
        peak = array[x]
        index = x

print(output)
