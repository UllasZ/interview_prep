"""
# Divide Two Integers
- Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
- The integer division should truncate toward zero, which means losing its fractional part.
- For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
- Return the quotient after dividing dividend by divisor.
"""


def divide_two_integers(dividend, divisor):

    counter = 0
    temp_dividend = abs(dividend)
    temp_divisor = abs(divisor)

    i = temp_dividend

    while temp_dividend >= temp_divisor:
        temp_dividend = temp_dividend - temp_divisor
        counter += 1

    if (dividend < 0 and divisor < 0) or (dividend < 0 or divisor < 0):
        counter = -counter

    return counter


print(divide_two_integers(-1, 1))
