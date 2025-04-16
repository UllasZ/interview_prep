from collections import Counter


def check_magazine(magazine, note):
    # Write your code here
    mag_count = Counter(magazine)

    for word in note:
        if mag_count[word] == 0:
            print("No")
            break
        mag_count[word] -= 1
    else:
        print("Yes")


if __name__ == "__main__":

    m = "two times three is not four"
    n = "two times two is four"

    print(check_magazine(m.split(), n.split()))
