"""
# Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""


def reverse_integer(x):
    is_negative = x < 0
    x = int(str(abs(x))[::-1])

    if is_negative:
        x = -x

    if x < -2 ** 31 or x > 2 ** 31 - 1:
        return 0
    return x


# Test cases
print(reverse_integer(123))  # 321
print(reverse_integer(-123))  # -321
print(reverse_integer(120))  # 21
print(reverse_integer(1534236469))  # 0 (overflow)
