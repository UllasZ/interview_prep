"""
- The n-queens problem asks how to place n chess queens on an n×n chessboard so that no two queens attack each other.
- This means ensuring no two queens share the same row, column, or diagonal.
- The goal is to find all distinct solutions (permutations of [1, 2, 3...n]) representing the column placement of each queen in a respective row.

Key aspects of the problem:
    Input: An integer n representing the size of the chessboard and the number of queens.
    Output: A list of distinct solutions, where each solution is a representation of the board configuration with Q for queens and None for empty squares.
    Constraints: No two queens can attack each other.
"""
