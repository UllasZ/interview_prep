"""
# Hidden treasure
Problem:
- Alice, an aspiring cryptographer, recently discovered an ancient scroll containing a sequence of mysterious numbers.
- According to a legend, these numbers hold the key to unlocking a hidden treasure buried centuries ago by an enigmatic mathematician.
- However, deciphering the scroll requires identifying specific pairs of numbers that follow an ancient numerical pattern.
- Alice is given an array of integers nums. She wants to determine how many pairs exist such that:
    - The sum of digits of nums[i] is equal to the sum of digits of nums[j].
    - She believes that the correct count of these pairs will reveal a crucial clue needed to decode the
      next part of the scroll. Your task is to help Alice compute this number so she can continue her quest.

Task:
- Return the number of special pairs to assist Alice in uncovering the hidden secret.

Function description:
- Complete the function solve() provided in the editor.
- This function takes the following two parameters and returns the required answer:
    - N: Represents the number of elements in the array
    - nums: A list of N integers

Input format:
- The first line contains a single integer N(size of the array).
- The second line contains N space-separated integers representing the array nums.

Output format:
- For each test case, print the required answer on a new line.
"""

def solve (n, nums):

    print(n, nums)

    for i in range(n):
        print(i, nums[i])




output = solve(4, [51, 71, 17, 42])
print(output)