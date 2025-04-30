"""
# 4! = 4 * 3 * 2 * 1

Explanation:
    4! = 4 * 3!
            3! = 3 * 2!
                    2! = 2 *  1!
                            1! = 1
"""

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)


res = factorial(4)
print(res)