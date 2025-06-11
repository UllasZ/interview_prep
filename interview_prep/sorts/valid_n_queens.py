# N queens check validity
def main(array):

    if check_rows(array) is False:
        return False

    if check_columns(array) is False:
        return False

    if check_adjacent_cells(array) is False:
        return False

    return True


def check_row(row):
    current = 0
    flag = False

    while current < len(row):
        if row[current] == "Q" and flag is False:
            flag = True
            current = current + 1
            continue

        if row[current] == "Q" and flag is True:
            flag = False
            break

        if row[current] != "Q":
            current = current + 1
            continue

    return flag


def check_rows(array):
    i = 0
    flag = False
    while i < len(array):
        flag = check_row(array[i])
        if flag is False:
            break
        else:
            i = i + 1
    return flag


def check_columns(array):
    cell = 0
    flag = False

    while cell < len(array):
        current = 0
        flag = False

        while current < len(array):

            if array[current][cell] == "Q" and flag is False:
                flag = True
                current = current + 1
                continue

            if array[current][cell] == "Q" and flag is True:
                flag = False
                break

            if array[current][cell] != "Q":
                current = current + 1
                continue

            current = current + 1

        if flag is False:
            break

        cell = cell + 1

    return flag


def check_adjacent_cells(array):
    current_row = 0
    flag = False

    while current_row < len(array):
        prev_row = current_row - 1
        next_row = current_row + 1

        current_cell = 0
        flag = False

        while current_cell < len(array):
            prev_cell = current_cell - 1
            next_cell = current_cell + 1

            if array[current_row][current_cell] == "Q":

                if 0 < prev_row < len(array):

                    if 0 < prev_cell < len(array):
                        if array[prev_row][prev_cell] is not None:
                            return False

                    if 0 < next_cell < len(array):
                        if array[prev_row][next_cell] is not None:
                            return False

                if 0 < next_row < len(array):
                    if 0 < prev_cell < len(array):
                        if array[next_row][prev_cell] is not None:
                            return False

                    if 0 < next_cell < len(array):
                        if array[next_row][next_cell] is not None:
                            return False

                flag = True

            current_cell = current_cell + 1
        current_row = current_row + 1

    return flag


q_queen = [
    [None, "Q", None, None],
    [None, None, None, "Q"],
    ["Q", None, None, None],
    [None, None, "Q", None],
]


print(f"Is valid N Queen: {main(q_queen)}")
