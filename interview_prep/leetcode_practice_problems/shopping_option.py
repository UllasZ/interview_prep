"""
# Shopping Options

- You are given the list of costs of pants in an array “pants”, shirts in an array “shirts”,
  shoes in an array “shoes”, and skirts in an array “skirts”.
- You are also given a budget amount ‘X’ to spend. You want to buy exactly 1 item from each list.
- Your task is to determine the total number of possible combinations that you can buy,
  given that the total amount of your purchase does not exceed your budget amount.

Constraints:
1 <= T <= 100
1 <= ‘P’, ‘Q’, ‘R’, ‘S’  <= 10
1 <= ‘X’ <= 10^9
1 <= pants[i], shirts[i], shoes[i], skirts[i] <= 10^9

Time Limit: 1 sec
Sample Input 1:
2
2 2 1 1 10
3 4
2 4
2
1
3 2 2 1 15
3 4 6
1 4
2 3
8
Sample Output 1:
3
3
Explanation For Sample Output 1:
In the first case,
There are a total of four ways to buy. Only valid purchases are [3, 2, 2, 1], [3, 4, 2, 1], [4, 2, 2, 1] because the sum of the cost of each item of each valid purchase is less than the budget amount.

In the second case,
There are a total of four ways to buy. Only valid purchases are [3, 1, 2, 8], [3, 1, 3, 8], [4, 1, 2, 8] because the sum of the cost of each item of each valid purchase is less than the budget amount.
Sample Input 2 :
2
3 3 3 3 14
3 4 7
1 3 5
6 8 10
1 2 3
4 3 2 2 20
2 8 7 10
5 5 5
6 3
4 5
Sample Output 2:
12
21
"""


def shopping_options(pants, shirts, shoes, skirts, budget):
    answer = 0


pant_costs = []
shirt_costs = []
shoe_costs = []
skirt_costs = []

result = shopping_options(pant_costs, shirt_costs, shoe_costs, skirt_costs)
print(result)
