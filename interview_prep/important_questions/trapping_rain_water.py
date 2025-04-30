"""
# Trapping Rain Water

- Given n non-negative integers representing an elevation map where the width of each bar is 1,
  compute how much water it can trap after raining.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
                 In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
"""


def trap(height):

    if not height:
        print("Total water that can be trapped is 0")
        return 0

    print(f"\nHeight: {height}")

    left_index, right_index = 0, len(height) - 1
    left_max, right_max = height[left_index], height[right_index]
    res = 0

    while left_index < right_index:

        if height[left_index] < height[right_index]:
            left_index +=1
            left_max = max(left_max, height[left_index])
            res += left_max - height[left_index]

        else:
            right_index -= 1
            right_max = max(right_max, height[right_index])
            res += right_max - height[right_index]

    print(f"Total water that can be trapped is {res}")


if __name__ == "__main__":

    h1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    trap(h1)

    h2 = [4,2,0,3,2,5]
    trap(h2)

    a = 7
    print(a.__str__())
