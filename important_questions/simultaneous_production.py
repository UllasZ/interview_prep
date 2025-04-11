"""
You are given the number of machines 'N', an array 'M' of length 'N' where 'M[i]' represents
the number of days the i-th machine takes to produce one item, and the total number of items 'O' that need to be ordered.
Return the minimum number of days required for all machines working in parallel to complete the order.

For Example :
    Let 'N' = 2, 'M' = [3, 1], 'O' = 5.
    Day 1: Machine 2 produces an item
    Day 2: Machine 2 produces an item
    Day 3: Both Machine 1 and Machine 2 produce an item
    Day 4: Machine 2 produces an item
    Total items produced = 1 + 1 + 2 + 1 = 5 items.
    Therefore, the answer is 4 days.

Problem approach
    Can be solved using Binary Search

Approach
    1. Sort the machines in ascending order of their production times.
    2. Initialize left and right pointers for binary search.
    3. While the left pointer is less than or equal to the right pointer:
        Calculate the mid-value.
Determine how many items each machine can produce in mid-days.
Sum up the total production from all machines.
Update left or right pointers based on the total production.
"""
